create index author_id_index on author(author_id);
create index Bid_index on book(Bid);
create index branch_id_index on Branch(branch_id);
create index compile_index on Compile(Bid,author_id);
create index granter_id_index on granter(granter_id);
create index mem_id_index on member(mem_id);
create index pub_id_index on publisher(pub_id);
create index ssn_num_index on social_security_card(ssn);
create index staff_id_index on staff(staff_id);