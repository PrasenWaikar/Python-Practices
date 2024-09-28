show databases;
use my_shop;

create table items3(
item_id int auto_increment primary key,
item_name varchar(50),
item_price int,
item_stock int NOT NULL
);

insert into items3(item_name,item_price,item_stock)values('pajamas','700',8);
desc items3;
select * from items;
select * from items where item_name='hoddie';
select item_price as 'cost of item' from items;
update items set item_price=500 where item_name='t-shirt';
delete from items where item_price=900;
#STRING FUNCTIONS:
select concat(item_name,' ',item_price)  from items;
select concat(item_name,' ',item_price) as item_info  from items;