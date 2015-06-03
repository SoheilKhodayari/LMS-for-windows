
Alter Table staff_email Add Constraint CONS_Email_Staff Check (email_address Like '_%@_%._%');
Alter Table publisher_email Add Constraint CONS_Email_Publisher Check (email_address Like '_%@_%._%');
Alter Table member_email Add Constraint CONS_Email_Member Check (email_address Like '_%@_%._%');
Alter Table granter_email Add Constraint CONS_Email_Granter Check (email_address Like '_%@_%._%');
Alter Table Branch_email Add Constraint CONS_Email_Branch Check (email_address Like '_%@_%._%');
Alter Table author_email Add Constraint CONS_Email_Author Check (email_address Like '_%@_%._%'); 

Alter Table staff_phone Add Constraint CONS_PHONE_Staff Check (phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
															 OR phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');
Alter Table publisher_phone Add Constraint CONS_PHONE_Publisher Check (phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
															 OR phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');
Alter Table member_phone Add Constraint CONS_PHONE_Membor Check (phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
															 OR phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');
Alter Table granter_phone Add Constraint CONS_PHONE_Granter Check (phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
															 OR phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');
Alter Table branch_phone Add Constraint CONS_PHONE_Branch Check (phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
															 OR phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
															 OR phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9]'); --4 digits as well
Alter Table author_phone Add Constraint CONS_PHONE_Author Check (phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
															 OR phone_number Like '+98[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');
															 
 -- NOT LIKE '%[^0-9]%'  -->> contains only numbers

ALTER TABLE Branch_fax Add Constraint CONS_FAX_Branch Check( fax_number NOT LIKE '%[^0-9]%');

ALTER TABLE Branch_website Add Constraint CONS_WEBSITE_Branch Check( website Like 'https://www._%._%)' OR
																	 website Like 'http://www._%._%)' OR
																	 website Like 'www._%._%)' OR
																	 website Like '_%._%)' ); 


ALTER TABLE staff Add Constraint CONS_PostalCode_Staff Check ( postal_code NOT LIKE '%[^0-9]%');
ALTER TABLE staff Add Constraint CONS_BuildingNo_Staff Check ( building_no>0);
ALTER TABLE Branch Add Constraint CONS_BuildingNo_Branch Check ( building_no>0 );
ALTER TABLE Branch Add Constraint CONS_PostalCode_Branch Check ( postal_code NOT LIKE '%[^0-9]%');

AlTER TABLE member Add Constraint CONS_MemType_Member check (membership_type in('0','1'));
AlTER TABLE member Add Constraint CONS_HasPenalty_Member check (has_penalty in('0','1'));
ALTER TABLE member Add Constraint CONS_PostalCode_Member Check ( postal_code NOT LIKE '%[^0-9]%');
ALTER TABLE member ADD CONSTRAINT CONS_COUNTRY_DEFAULT_Member DEFAULT 'Iran' FOR country;
ALTER TABLE member Add Constraint CONS_BuildingNo_Member Check ( building_no>0);

AlTER TABLE book Add Constraint CONS_Available_book check (Available in('0','1')); 
AlTER TABLE book Add Constraint CONS_NumPublished_book check (num_published >=0 ); 


ALTER TABLE granter Add Constraint CONS_PostalCode_Granter Check ( postal_code NOT LIKE '%[^0-9]%');
ALTER TABLE granter ADD CONSTRAINT CONS_COUNTRY_DEFAULT_Granter DEFAULT 'Iran' FOR country;
ALTER TABLE granter Add Constraint CONS_BuildingNo_Granter Check ( building_no>0);  

ALTER TABLE publisher Add Constraint CONS_PostalCode_Publisher Check ( postal_code NOT LIKE '%[^0-9]%');
ALTER TABLE publisher ADD CONSTRAINT CONS_COUNTRY_DEFAULT_Publisher DEFAULT 'Iran' FOR country;
ALTER TABLE publisher Add Constraint CONS_BuildingNo_Publisher Check ( building_no>0);  


