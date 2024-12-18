PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2024-12-04 12:13:39.730555');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2024-12-04 12:13:39.751844');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2024-12-04 12:13:39.765893');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2024-12-04 12:13:39.793210');
INSERT INTO django_migrations VALUES(5,'admin','0003_logentry_add_action_flag_choices','2024-12-04 12:13:39.804676');
INSERT INTO django_migrations VALUES(6,'announcements','0001_initial','2024-12-04 12:13:39.809886');
INSERT INTO django_migrations VALUES(7,'contenttypes','0002_remove_content_type_name','2024-12-04 12:13:39.832056');
INSERT INTO django_migrations VALUES(8,'auth','0002_alter_permission_name_max_length','2024-12-04 12:13:39.845279');
INSERT INTO django_migrations VALUES(9,'auth','0003_alter_user_email_max_length','2024-12-04 12:13:39.863603');
INSERT INTO django_migrations VALUES(10,'auth','0004_alter_user_username_opts','2024-12-04 12:13:39.874888');
INSERT INTO django_migrations VALUES(11,'auth','0005_alter_user_last_login_null','2024-12-04 12:13:39.887295');
INSERT INTO django_migrations VALUES(12,'auth','0006_require_contenttypes_0002','2024-12-04 12:13:39.891074');
INSERT INTO django_migrations VALUES(13,'auth','0007_alter_validators_add_error_messages','2024-12-04 12:13:39.902609');
INSERT INTO django_migrations VALUES(14,'auth','0008_alter_user_username_max_length','2024-12-04 12:13:39.914897');
INSERT INTO django_migrations VALUES(15,'auth','0009_alter_user_last_name_max_length','2024-12-04 12:13:39.926859');
INSERT INTO django_migrations VALUES(16,'auth','0010_alter_group_name_max_length','2024-12-04 12:13:39.938736');
INSERT INTO django_migrations VALUES(17,'auth','0011_update_proxy_permissions','2024-12-04 12:13:39.948356');
INSERT INTO django_migrations VALUES(18,'auth','0012_alter_user_first_name_max_length','2024-12-04 12:13:39.961518');
INSERT INTO django_migrations VALUES(19,'informations','0001_initial','2024-12-04 12:13:39.966543');
INSERT INTO django_migrations VALUES(20,'products','0001_initial','2024-12-04 12:13:39.971752');
INSERT INTO django_migrations VALUES(21,'sessions','0001_initial','2024-12-04 12:13:39.981514');
INSERT INTO django_migrations VALUES(22,'residents','0001_initial','2024-12-04 12:39:37.560162');
INSERT INTO django_migrations VALUES(23,'products','0002_product_added_by','2024-12-04 12:39:37.590535');
INSERT INTO django_migrations VALUES(24,'informations','0002_information_added_by','2024-12-05 01:46:08.162811');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO django_admin_log VALUES(1,'3','there is more for you',3,'',9,4,'2024-12-06 02:09:53.572996');
INSERT INTO django_admin_log VALUES(2,'2','i like this food',3,'',9,4,'2024-12-06 02:09:53.573069');
INSERT INTO django_admin_log VALUES(3,'1','aku suka kamy',3,'',9,4,'2024-12-06 02:09:53.573109');
INSERT INTO django_admin_log VALUES(4,'1','Selamat hari halloween',1,'[{"added": {}}]',8,4,'2024-12-06 03:21:16.148654');
INSERT INTO django_admin_log VALUES(5,'11','asdf;lakdsf',1,'[{"added": {}}]',7,4,'2024-12-06 03:45:37.771915');
CREATE TABLE IF NOT EXISTS "announcements_announcement" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "announcementTitle" varchar(255) NOT NULL, "message" text NOT NULL, "photo" varchar(100) NULL, "writer" varchar(100) NOT NULL, "date" datetime NOT NULL);
INSERT INTO announcements_announcement VALUES(1,'Selamat hari halloween','kita akan menikmati hallowen','announcements/halloween-gettyimages-1424736925.jpg','buddy','2024-12-06 03:21:16.147913');
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'auth','user');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'products','product');
INSERT INTO django_content_type VALUES(8,'announcements','announcement');
INSERT INTO django_content_type VALUES(9,'informations','information');
INSERT INTO django_content_type VALUES(10,'residents','resident');
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_user','Can add user');
INSERT INTO auth_permission VALUES(14,4,'change_user','Can change user');
INSERT INTO auth_permission VALUES(15,4,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(16,4,'view_user','Can view user');
INSERT INTO auth_permission VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(21,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(22,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(23,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(24,6,'view_session','Can view session');
INSERT INTO auth_permission VALUES(25,7,'add_product','Can add product');
INSERT INTO auth_permission VALUES(26,7,'change_product','Can change product');
INSERT INTO auth_permission VALUES(27,7,'delete_product','Can delete product');
INSERT INTO auth_permission VALUES(28,7,'view_product','Can view product');
INSERT INTO auth_permission VALUES(29,8,'add_announcement','Can add announcement');
INSERT INTO auth_permission VALUES(30,8,'change_announcement','Can change announcement');
INSERT INTO auth_permission VALUES(31,8,'delete_announcement','Can delete announcement');
INSERT INTO auth_permission VALUES(32,8,'view_announcement','Can view announcement');
INSERT INTO auth_permission VALUES(33,9,'add_information','Can add information');
INSERT INTO auth_permission VALUES(34,9,'change_information','Can change information');
INSERT INTO auth_permission VALUES(35,9,'delete_information','Can delete information');
INSERT INTO auth_permission VALUES(36,9,'view_information','Can view information');
INSERT INTO auth_permission VALUES(37,10,'add_resident','Can add resident');
INSERT INTO auth_permission VALUES(38,10,'change_resident','Can change resident');
INSERT INTO auth_permission VALUES(39,10,'delete_resident','Can delete resident');
INSERT INTO auth_permission VALUES(40,10,'view_resident','Can view resident');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$870000$fx2AmEQkvSTY4R90z6Rs6P$+f/9FnP7fuXy5Pzo9zeF3UumzLhH0K68rRg+c8fHxOM=',NULL,0,'default_user','','',0,1,'2024-12-04 12:36:14.952542','');
INSERT INTO auth_user VALUES(2,'pbkdf2_sha256$870000$a7Ficg56nO00iOFjMAVDlN$GowIN0yhEX5iisjwNyfSS+XZExTrPcioCU2Fso01VZg=','2024-12-06 04:47:45.392206',0,'matteo','','',0,1,'2024-12-04 13:29:20.624697','');
INSERT INTO auth_user VALUES(3,'pbkdf2_sha256$870000$1UcB25qtu7OJZNSfJCeHNI$LXACFzVOXlRwuAEEm+q/OVnmUQj+soW3RchDxvs2GFQ=',NULL,0,'zeronohero','','darmawangsahutagaol@gmail.com',0,1,'2024-12-05 14:48:00.857075','');
INSERT INTO auth_user VALUES(4,'pbkdf2_sha256$870000$LN0T3p26Wf0m7Ejz9feUBj$WY2oxMtTel5MW1KGNEJ4VbN2CHwRj9QgMExlNk8uojU=','2024-12-06 15:18:56.235033',1,'zenux','','darmawangsahutagaol@gmail.com',1,1,'2024-12-05 16:35:22.108524','');
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE TABLE IF NOT EXISTS "residents_resident" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "phone_number" varchar(15) NOT NULL, "address" text NOT NULL, "status_ownership" varchar(50) NOT NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO residents_resident VALUES(1,'11','adf;aljdf;ajdf;lkajdsf','helllow',2);
INSERT INTO residents_resident VALUES(2,'1234','1234','ok',3);
CREATE TABLE IF NOT EXISTS "products_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "product_name" varchar(255) NOT NULL, "product_photo" varchar(100) NULL, "product_type" varchar(100) NOT NULL, "product_price" decimal NOT NULL, "product_weight" decimal NOT NULL, "date_added" datetime NOT NULL, "added_by_id" bigint NOT NULL REFERENCES "residents_resident" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO products_product VALUES(7,'test','','1',1,1,'2024-12-06 02:55:55.384496',1);
INSERT INTO products_product VALUES(8,'sendok sup abad 17','products/img-20231212-114357-6577f43012d50f741a0530f2.jpg','sendok',1,1,'2024-12-06 03:12:17.038055',1);
INSERT INTO products_product VALUES(9,'dadar gulung i show speed','products/Screenshot_9-45903534.webp','makanan',1,1,'2024-12-06 03:13:21.066160',1);
INSERT INTO products_product VALUES(10,'Baso','products/baksobangben.jpg','baso',1,1,'2024-12-06 03:44:05.924992',1);
INSERT INTO products_product VALUES(11,'asdf;lakdsf','','11',1,1,'2024-12-06 03:45:37.771317',1);
CREATE TABLE IF NOT EXISTS "informations_information" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subject" varchar(255) NOT NULL, "aspiration_message" text NOT NULL, "photo" varchar(100) NULL, "date_posted" datetime NOT NULL, "added_by_id" bigint NOT NULL REFERENCES "residents_resident" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO informations_information VALUES(4,'hello world','aku suka ice cream','information_center_photos/Untitled.jpg','2024-12-06 03:16:35.119683',1);
INSERT INTO informations_information VALUES(5,'balablab','blablabla','','2024-12-06 03:44:29.027418',1);
INSERT INTO informations_information VALUES(6,'cara membuat bob','pertama kita akan membuat','','2024-12-06 15:06:46.789689',1);
INSERT INTO sqlite_sequence VALUES('django_migrations',24);
INSERT INTO sqlite_sequence VALUES('django_admin_log',5);
INSERT INTO sqlite_sequence VALUES('django_content_type',10);
INSERT INTO sqlite_sequence VALUES('auth_permission',40);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('auth_user',4);
INSERT INTO sqlite_sequence VALUES('products_product',11);
INSERT INTO sqlite_sequence VALUES('residents_resident',2);
INSERT INTO sqlite_sequence VALUES('informations_information',6);
INSERT INTO sqlite_sequence VALUES('announcements_announcement',1);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "products_product_added_by_id_476916d6" ON "products_product" ("added_by_id");
CREATE INDEX "informations_information_added_by_id_30afcd0e" ON "informations_information" ("added_by_id");
COMMIT;
