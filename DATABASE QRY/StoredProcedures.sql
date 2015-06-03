/* --------------------STORED PROCEDURES for forms------------------------ */

/* Branch Registeration form 

Create Procedure BranchInsert
( @BranchID int ,
  @name varchar(100),
  @head_id int,
  @city varchar(50),
  @district varchar(50),
  @street varchar(50),
  @alley varchar(50),
  @building_no int,
  @Postal_code varchar(50)
  )
 AS
	begin 
		insert into Branch(branch_id,name,head_id,city,district,street,alley,building_no,postal_code) 
		values(@BranchID,@name,@head_id,@city,@district,@street,@alley,@building_no,@Postal_code);
	end;
 GO

 Create Procedure BranchEmailInsert
 ( @BranchID int ,
   @EmailAdr varchar(200)
)
AS
	begin
		insert into Branch_email(branch_id,email_address)
		values(@BranchID,@EmailAdr);
	end;
GO

 Create Procedure BranchFaxInsert
 ( @BranchID int ,
   @Fax varchar(50)
)
AS
	begin
		insert into Branch_fax(branch_id,fax_number)
		values(@BranchID,@Fax);
	end;
GO

 Create Procedure BranchPhoneInsert
 ( @BranchID int ,
   @Phone varchar(200)
)
AS
	begin
		insert into Branch_phone(branch_id,phone_number)
		values(@BranchID,@Phone);
	end;
GO

 Create Procedure BranchWebsiteInsert
 ( @BranchID int ,
   @Website varchar(200)
)
AS
	begin
		insert into Branch_website(branch_id,website)
		values(@BranchID,@Website);
	end;
GO

*/

/* Publisher Registration Form 

Create Procedure PublisherInsert
( @PubID int ,
  @name varchar(200),
  @country varchar(50),
  @city varchar(50),
  @district varchar(50),
  @street varchar(50),
  @alley varchar(50),
  @building_no int,
  @Postal_code varchar(50)
  )
 AS
	begin 
		insert into publisher(pub_id,name,country,city,district,street,alley,building_no,postal_code) 
		values(@PubID,@name,@country,@city,@district,@street,@alley,@building_no,@Postal_code);
	end;
 GO

 Create Procedure PublihserEmailInsert
 ( @PubID int ,
   @EmailAdr varchar(200)
)
AS
	begin
		insert into publisher_email(publisher_id,email_address)
		values(@PubID,@EmailAdr);
	end;
GO



 Create Procedure PublisherPhoneInsert
 ( @PubID int ,
   @Phone varchar(200)
)
AS
	begin
		insert into publisher_phone(publisher_id,phone_number)
		values(@PubID,@Phone);
	end;
GO */

/*
Create Procedure sscInsert
( @SSN int,
  @serial varchar(50),
  @Issuance_loc varchar(50),
  @birthdate date
)
AS 
	begin 
		insert into social_security_card
		values(@SSN,@serial,@Issuance_loc,@birthdate)
	end;
GO */

/* member Registration Form 

Create procedure MemberInsert
(@MemID int,
 @Fname varchar(50),
 @Lname varchar(50),
 @MemShipDate date,
 @ExpDate date,
 @ssn int,
 @serial varchar(50),
 @ISL varchar(50),
 @BirthDate date,
 @country varchar(50),
 @city varchar(50),
 @district varchar(50),
 @street varchar(50),
 @alley varchar(50),
 @building_no int,
 @Postal_code varchar(50),
 @branch_id int,
 @MemShipType char(1),
 @HasPenalty char(1)
 )
 AS
	begin 
		Execute sscInsert @ssn ,@serial, @ISL, @BirthDate;
		Insert into member values
		(@MemID,@Fname,@Lname,@MemShipDate,@ExpDate,@ssn,
		 @country,@city,@district,@street,@alley,@building_no,@Postal_code,
		 @branch_id,@MemShipType,@HasPenalty);
	end;
GO

 Create Procedure MemberEmailInsert
 ( @MemID int ,
   @EmailAdr varchar(200)
)
AS
	begin
		insert into member_email(email_address,member_id)
		values(@EmailAdr,@MemID);
	end;
GO



 Create Procedure MemberPhoneInsert
 ( @MemID int ,
   @Phone varchar(200)
)
AS
	begin
		insert into member_phone(phone_number,member_id)
		values(@Phone,@MemID);
	end;
GO 
*/
