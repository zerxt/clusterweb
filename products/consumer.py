# products/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Product
from residents.models import Resident

class ProductMessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the product ID from the URL
        self.product_id = self.scope['url_route']['kwargs']['product_id']
        self.room_group_name = f'product_{self.product_id}_messages'

        # Get the product and user (resident)
        self.product = await Product.objects.aget(id=self.product_id)
        self.user = self.scope['user']
        self.resident = await Resident.objects.aget(user=self.user)

        # Check if the user is the seller of the product
        self.is_seller = self.product.added_by == self.resident

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.resident.user.username,
                'is_seller': self.is_seller
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        is_seller = event['is_seller']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'is_seller': is_seller
        }))
