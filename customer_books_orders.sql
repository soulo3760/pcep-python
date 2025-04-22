create schema luxsql;
SET search_path TO luxsql;
create table customer(
customer_id SERIAL primary key,
first_name VARCHAR(50) not null,
second_name VARCHAR(50) not null,
email VARCHAR(100) unique not null,
phone_number CHAR(10)
);
insert into customer (first_name, second_name, email, phone_number)
values
('John', 'Doe', 'john.doe@gmail.com', '0712345678'),
('Jane', 'Smith', 'janesmith@gmail.com', '0778654239'),
('Paul', 'Otieno', 'paulotis@gmail.com', '0722567981'),
('Mary', 'Okello', 'okellomary@gmail.com', '0798723865');

commit;

CREATE TABLE books (
book_id INT PRIMARY KEY,
title VARCHAR(150) NOT NULL,
author VARCHAR(100),
price NUMERIC(8, 2) NOT NULL,
published_date DATE
);
commit;

INSERT INTO books (book_id, title, author, price, published_date)
VALUES
(101, 'Understanding SQL', 'David Kimani', 1500.00, '2023-01-15'),
(102, 'Advanced PostgreSQL', 'Grace Achieng', 2500.00, '2023-02-20'),
(103, 'Learning Python', 'James Mwangi', 3000.00, '2022-11-10'),
(104, 'Data Analytics Basics', 'Susan Njeri', 2200.00, '2023-03-05');
commit;

CREATE TABLE orders (
order_id SERIAL PRIMARY KEY,
customer_id INT REFERENCES customer(customer_id),
book_id INT REFERENCES books(book_id),
order_date DATE DEFAULT CURRENT_DATE
);
commit;
INSERT INTO orders (customer_id, book_id, order_date)
VALUES
(1, 103, '2023-04-01'), -- John ordered Learning Python
(2, 101, '2023-04-02'), -- Jane ordered Understanding SQL
(3, 102, '2023-04-03'), -- Paul ordered Advanced PostgreSQL
(4, 104, '2023-04-04'), -- Mary ordered Data Analytics Basics
(1, 102, '2023-04-05'); -- John ordered Advanced PostgreSQL again
commit;


alter table customer
add column city VARCHAR(100);

update customer
set city = case customer_id
when 1 then 'Nairobi'
when 2 then 'Mombasa'
when 3 then 'Kisumu'
when 4 then 'Nairobi'
end;

select * from customers;

select * from information_schema.tables;
alter table orders
add column quantity int;
commit;
select * from orders;
update orders
 set quantity = case order_Id
when 1 then 2
when 2 then 1
when 3 then 3
when 4 then 2
when 5 then 1
end;

select count(*) as total_customers
from customer;

select count(*) as total_author
from books
where author LIKE '%James%';

select count(*) as total_orders
from orders
where order_date = '2023-04-01';


===TOTAL PRICE of all BOOKS
 select sum (price) as total_prices
 from books;

===total quantity of orders from customer_id 1

select sum(quantity) as total_customer1_quantity
from orders
where customer_id = 1;

=== what is the total price of books authored by david kimani
select sum(price) as kimani_worthy
from books
where author = 'David Kimani'; 
 = 1500

=== what is the total quantity of books for book_id 102
select sum(quantity) as quantityfrombook1
from orders
where book_id = 102;
=4