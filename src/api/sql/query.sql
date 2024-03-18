drop table if exists my_table;
create table my_table as
select
    col1,
    col2
from other_table;
