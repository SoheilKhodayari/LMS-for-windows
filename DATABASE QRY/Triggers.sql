/* CREATE TRIGGER trgAfterDelete ON [dbo].[Employee_Test] 
AFTER DELETE
AS
	declare @empid int;
	declare @empname varchar(100);
	declare @empsal decimal(10,2);
	declare @audit_action varchar(100);

	select @empid=d.Emp_ID from deleted d;	
	select @empname=d.Emp_Name from deleted d;	
	select @empsal=d.Emp_Sal from deleted d;	
	set @audit_action='Deleted -- After Delete Trigger.';

	insert into Employee_Test_Audit
(Emp_ID,Emp_Name,Emp_Sal,Audit_Action,Audit_Timestamp) 
	values(@empid,@empname,@empsal,@audit_action,getdate());

	PRINT 'AFTER DELETE TRIGGER fired.'
GO */

/*
Create trigger member_afterDel_trigger On [dbo].[member]
After DELETE 
AS
	declare @memID int;
	declare @ssn int;
	select @memID=d.mem_id from deleted d;
	select @ssn=d.ssn from deleted d;

	begin 
		delete from member_email where member_id=@memID;
		COMMIT;
		delete from member_phone where member_id=@memID;
		COMMIT;
		delete from social_security_card where ssn=@ssn;
		COMMIT
		PRINT 'AFTER DELETE member TRIGGER fired.'
	end;
GO 


Create trigger staff_afterDel_trigger On [dbo].[staff]
After DELETE 
AS
	declare @StaffID int;
	declare @ssn int;
	select @ssn=d.ssn from deleted d;
	select @StaffID=d.staff_id from deleted d;

	begin 
		delete from Staff_email where staff_id=@StaffID;
		COMMIT;
		delete from Staff_phone where staff_id=@StaffID;
		COMMIT;
		delete from Absences where staff_id=@StaffID;
		COMMIT;
		delete from social_security_card where ssn=@ssn;
		COMMIT
		PRINT 'AFTER DELETE staff TRIGGER fired.'
	end;
GO


Create trigger pub_afterDel_trigger On [dbo].[publisher]
After DELETE 
AS
	declare @PubID int;
	select @PubID=d.pub_id from deleted d;

	begin 
		delete from publisher_email where publisher_id=@PubID;
		COMMIT;
		delete from publisher_phone where publisher_id=@PubID;
		COMMIT;
	
		PRINT 'AFTER DELETE publisher TRIGGER fired.'
	end;
GO



Create trigger granter_afterDel_trigger On [dbo].[granter]
After DELETE 
AS
	declare @GID int;
	declare @ssn int;
	select @GID=d.granter_id from deleted d;
	select @ssn=d.ssn from deleted d;
	begin 
		delete from granter_email where granter_id=@GID;
		COMMIT;
		delete from granter_phone where granter_id=@GID;
		COMMIT;
		delete from social_security_card where ssn=@ssn;
		COMMIT
	
		PRINT 'AFTER DELETE granter TRIGGER fired.'
	end;
GO



Create trigger branch_afterDel_trigger On [dbo].[branch]
After DELETE 
AS
	declare @BranchID int;
	select @BranchID=d.branch_id from deleted d;
	begin 
		delete from Branch_email where branch_id=@BranchID;
		COMMIT;
		delete from Branch_phone where branch_id=@BranchID;
		COMMIT;
		delete from Branch_website where branch_id=@BranchID;
		COMMIT;
		delete from Branch_fax where branch_id=@BranchID;
		COMMIT;
		-- DELETE ALL BOOKS ASSOCIATED WITH THIS Branch
		delete from book where branch_id=@BranchID;
		COMMIT;
		--DELETE ALL STAFF ASSOCIATED WITH THIS Branch
		delete from staff where branch_id=@BranchID;
		COMMIT;
	
		PRINT 'AFTER DELETE branch TRIGGER fired.'
	end;
GO



Create trigger member_afterDel_trigger On [dbo].[member]
After DELETE 
AS
	declare @memID int;
	declare @ssn int;
	select @memID=d.mem_id from deleted d;
	select @ssn=d.ssn from deleted d;

	begin 
		delete from member_email where member_id=@memID;
		COMMIT;
		delete from member_phone where member_id=@memID;
		COMMIT;
		delete from social_security_card where ssn=@ssn;
		COMMIT
		if exists(select distinct Bid from book where borrow_mem_id=@memID)
			begin
				update book set borrow_mem_id=null where borrow_mem_id=@memID;
				COMMIT; 
			end;
		PRINT 'AFTER DELETE member TRIGGER fired.'
	end;
GO 



Create trigger author_afterDel_trigger On [dbo].[author]
After DELETE 
AS
	declare @AID int;

	select @AID=d.author_id from deleted d;

	begin 
		delete from author_email where author_id=@AID;
		COMMIT;
		delete from author_phone where author_id=@AID;
		COMMIT;
		delete from Compile where author_id=@AID;
		COMMIT;
		PRINT 'AFTER DELETE author TRIGGER fired.'
	end;
GO



Create trigger branch_afterDel_trigger On [dbo].[branch]
After DELETE 
AS
	declare @BranchID int;
	select @BranchID=d.branch_id from deleted d;
	begin 
		delete from Branch_email where branch_id=@BranchID;
		COMMIT;
		delete from Branch_phone where branch_id=@BranchID;
		COMMIT;
		delete from Branch_website where branch_id=@BranchID;
		COMMIT;
		delete from Branch_fax where branch_id=@BranchID;
		COMMIT;
		--DELETE BOOKS IN COMPILE
		delete from Compile where Bid in (select distinct Bid from book where branch_id=@BranchID);
		COMMIT;
		-- DELETE ALL BOOKS ASSOCIATED WITH THIS Branch
		delete from book where branch_id=@BranchID;
		COMMIT;
				
		--DELETE ALL STAFF ASSOCIATED WITH THIS Branch
		delete from staff where branch_id=@BranchID;
		COMMIT;
	
		PRINT 'AFTER DELETE branch TRIGGER fired.'
	end;
GO




CREATE TRIGGER staff_afterInsert_trigger ON [dbo].[staff] 
FOR INSERT
AS
	declare @SID int;
	declare @SSN int;
	select @SID=i.staff_id from inserted i;	
	select @SSN=i.ssn from inserted i;
	
	insert into login_tb(username,pass)
	select staff_id as username,ssn as pass 
	from staff
	where staff.staff_type=0 OR staff.staff_type=1 ;  
	--secretary or head
	PRINT 'AFTER INSERT Staff trigger fired.'
GO

*/

--insert into social_security_card values (311183521,'14547874','Tehran','1990-10-16');
--insert into staff values(1,null,'soheil','khodayari','20140618 10:34:09 AM',311183521,'tehran','narmak','farjam','bagheri',185,'62362332','550.87',0)
