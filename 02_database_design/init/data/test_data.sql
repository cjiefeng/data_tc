insert into manufacture_tab(name) values ('a brand'), ('b brand'), ('c brand'), ('d brand'), ('e brand');

insert into car_tab(serial_number, model_name, weight, price, manufacture_id) values
('a1', 'a.1', 999, 1999.99, 1),
('a2', 'a.2', 999, 2999.99, 1),
('a3', 'a.3', 999, 3999.99, 1),
('a4', 'a.4', 999, 4999.99, 1),
('b1', 'b.1', 888, 1888.99, 2),
('b2', 'b.2', 888, 2888.99, 2),
('b3', 'b.3', 888, 3888.99, 2),
('c1', 'c.1', 777, 1777.99, 3),
('c2', 'c.2', 777, 2777.99, 3),
('c3', 'c.3', 777, 3777.99, 3),
('d1', 'd.1', 666, 1666.99, 4),
('d2', 'd.2', 666, 2666.99, 4),
('d3', 'd.3', 666, 3666.99, 4),
('e1', 'e.1', 555, 1555.99, 5),
('e2', 'e.2', 555, 2555.99, 5);
insert into sales_person_tab (name) values('john'), ('lisa'), ('adam'), ('peter');

insert into customer_tab (name, phone) values('jane', '111'), ('max', '222'), ('andy', '333'), ('paul', '444');

insert into sales_tab (datetime, sales_person_id, customer_id) values
(extract(epoch from now() - INTERVAL '1 second'), 1, 1),
(extract(epoch from now() - INTERVAL '1 second'), 2, 2),
(extract(epoch from now() - INTERVAL '1 second'), 3, 3),
(extract(epoch from now() - INTERVAL '2 second'), 1, 1),
(extract(epoch from now() - INTERVAL '2 second'), 2, 1),
(extract(epoch from now() - INTERVAL '2 second'), 3, 1),
(extract(epoch from now()), 1, 1),
(extract(epoch from now()), 4, 1),
(extract(epoch from now() - INTERVAL '2 month'), 1, 1),
(extract(epoch from now() - INTERVAL '2 month'), 1, 1);

insert into sale_item_tab (sales_id, car_id) values
(1, 1),
(2, 2),
(3, 4),
(4, 5),
(5, 13),
(6, 12),
(7, 4),
(2, 10),
(2, 4),
(2, 3),
(2, 7),
(2, 10),
(2, 10),
(2, 8),
(2, 4),
(2, 1),
(8, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15),
(9, 15);