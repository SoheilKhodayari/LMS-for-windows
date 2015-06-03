
CREATE TABLE  "author" (
	"author_id" integer NOT NULL PRIMARY KEY,
    "fname" varchar(50), 
    "lname" varchar(50) 
)
;
CREATE TABLE "author_email" (
    "email_address" varchar(200) NOT NULL ,
    "author_id" integer NOT NULL  REFERENCES "author" ("author_id")
	PRIMARY KEY("author_id","email_address")
)
;
CREATE TABLE "author_phone" (
	"author_id" integer NOT NULL REFERENCES "author" ("author_id"),
    "phone_number" varchar(13) NOT NULL ,

	PRIMARY KEY("author_id","phone_number")
)
;
CREATE TABLE "publisher" (
    "pub_id" integer NOT NULL PRIMARY KEY,
    "name" varchar(200) ,
    "country" varchar(50),
    "city" varchar(50),
    "district" varchar(50),
    "street" varchar(50),
    "alley" varchar(50),
    "building_no" integer ,
    "postal_code" varchar(50)
)
;
CREATE TABLE "publisher_phone" (
	"publisher_id" integer NOT NULL REFERENCES "publisher" ("pub_id"),
    "phone_number" varchar(13) ,
    
	 PRIMARY KEY("publisher_id","phone_number")
)
;
CREATE TABLE "publisher_email" (
	"publisher_id" integer NOT NULL REFERENCES "publisher" ("pub_id"),
    "email_address" varchar(200) NOT NULL ,

	PRIMARY KEY("publisher_id","email_address")
)
;

;
CREATE TABLE "social_security_card" (
    "ssn" integer NOT NULL PRIMARY KEY,
    "serial" integer ,
    "issuance_location" varchar(50),
	"birthdate" datetime,
)
; 
CREATE TABLE "granter" (
    "granter_id" integer NOT NULL PRIMARY KEY,
    "firstname" varchar(50) ,
    "lastname" varchar(50) ,
    "ssn" integer UNIQUE REFERENCES "social_security_card" ("ssn"),
    "country" varchar(50),
    "city" varchar(50),
    "district" varchar(50),
    "street" varchar(50),
    "alley" varchar(50),
    "building_no" integer,
    "postal_code" varchar(50),

)
;
CREATE TABLE "granter_phone" (
    "granter_id" integer NOT NULL REFERENCES "granter" ("granter_id"),
    "phone_number" varchar(13) NOT NULL,
	PRIMARY KEY("granter_id","phone_number")
)
;
CREATE TABLE "granter_email" (
    "granter_id" integer NOT NULL REFERENCES "granter" ("granter_id"),
    "email_address" varchar(200) NOT NULL,
	PRIMARY KEY("granter_id","email_address")
)
;
--ALTER TABLE Employee ADD CONSTRAINT DF_SomeName DEFAULT N'SANDNES' FOR CityBorn;
CREATE TABLE "member" (
    "mem_id" integer NOT NULL PRIMARY KEY,
    "firstname" varchar(50),
    "lastname" varchar(50),
    "membership_type" Char(1) NOT NULL,
    "membership_date" datetime,
    "expiry_date" datetime NOT NULL,
    "has_penalty" Char(1) NOT NULL,
    "ssn" integer UNIQUE REFERENCES "social_security_card" ("ssn"),
    "country" varchar(50),
    "city" varchar(50),
    "district" varchar(50),
    "street" varchar(50),
    "alley" varchar(50),
    "building_no" integer,
    "postal_code" varchar(50),
)
;
CREATE TABLE "member_phone" (
    "phone_number" varchar(13) NOT NULL,
    "member_id" integer NOT NULL REFERENCES "member" ("mem_id")
	PRIMARY KEY("member_id","phone_number")
)
;
CREATE TABLE "member_email" (
    "email_address" varchar(200) NOT NULL,
    "member_id" integer NOT NULL REFERENCES "member" ("mem_id")
	PRIMARY KEY("member_id","email_address")
)
;
CREATE TABLE "Branch" (

    "branch_id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100),
	"head_id" integer ,
	"city" varchar(50),
    "district" varchar(50),
    "street" varchar(50),
    "alley" varchar(50),
    "building_no" integer,
    "postal_code" varchar(50)

)
;
CREATE TABLE "Branch_phone" (
	"branch_id" integer NOT NULL REFERENCES "Branch" ("branch_id"),
    "phone_number" varchar(13) NOT NULL,
	PRIMARY KEY("branch_id","phone_number")
)
;
CREATE TABLE "Branch_email" (
	"branch_id" integer NOT NULL REFERENCES "Branch" ("branch_id"),
    "email_address" varchar(200) NOT NULL,

	PRIMARY KEY("branch_id","email_address")
)
;
CREATE TABLE "Branch_website" (
	"branch_id" integer NOT NULL REFERENCES "Branch" ("branch_id"),
    "website" varchar(200) NOT NULL,

	PRIMARY KEY("branch_id","website")
)
;
CREATE TABLE "Branch_fax" (
	"branch_id" integer NOT NULL REFERENCES "Branch" ("branch_id"),
    "fax_number" varchar(50) NOT NULL,

	PRIMARY KEY("branch_id","fax_number")
);

CREATE TABLE "Staff" (
	"staff_id" integer NOT NULL PRIMARY KEY,
	"branch_id" integer REFERENCES "Branch" ("branch_id"),
	"firstname" varchar(50),
    "lastname" varchar(50),
    "employed_date" datetime,
	"salary" money NOT NULL,
	"staff_type" integer not null,
    "ssn" integer UNIQUE REFERENCES "social_security_card" ("ssn"),

	--home address
	"city" varchar(50),
    "district" varchar(50),
    "street" varchar(50),
    "alley" varchar(50),
    "building_no" integer,
    "postal_code" varchar(50)
)
CREATE TABLE "Staff_phone" (
	"staff_id" integer NOT NULL REFERENCES "Staff" ("staff_id"),
    "phone_number" varchar(13) NOT NULL,
	PRIMARY KEY("staff_id","phone_number")
)
;
CREATE TABLE "Staff_email" (
	"staff_id" integer NOT NULL REFERENCES "Staff" ("staff_id"),
    "email_address" varchar(200) NOT NULL,

	PRIMARY KEY("staff_id","email_address")
)
;
CREATE TABLE "Absences" (
	"ID" integer NOT NULL PRIMARY KEY,
	"staff_id" integer NOT NULL REFERENCES "Staff" ("staff_id"),
	"absence_date" datetime NOT NULL )
;
CREATE TABLE "book" (
    "Bid" bigint NOT NULL PRIMARY KEY,
    "ISBN" integer NOT NULL,
    "Title" varchar(200) NOT NULL,
	"Subject" TinyInt NOT NULL ,
    "Available" char(1) NOT NULL,
    "pub_date" datetime,
    "price" Money,
	"branch_id" integer REFERENCES "Branch" ("branch_id"),
    "publisher_id" integer REFERENCES "publisher" ("pub_id"),
    "num_published" integer,
    "granter_id" integer REFERENCES "granter" ("granter_id"),
    "granted_date" datetime,
    "borrow_mem_id" integer REFERENCES "member" ("mem_id"),
    "borrow_due_date" datetime,
    "borrow_return_date" datetime,
	--CONSTRAINT Subject_check
		--CHECK("Subject" BETWEEN 1 and 10) 
	
)
CREATE TABLE "Compile" (

    "Bid" bigint NOT NULL REFERENCES "book" ("Bid"),
    "author_id" integer NOT NULL REFERENCES "author" ("author_id"),
    UNIQUE ("Bid", "author_id"),
	PRIMARY KEY("Bid","author_id")
)
;
create table login_tb(
	"username" integer NOT NULL PRIMARY KEY ,
	"pass" integer NOT NULL); 
GO


;

