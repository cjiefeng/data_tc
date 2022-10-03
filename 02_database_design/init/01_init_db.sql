create table manufacture_tab(
    id bigserial primary key,
    name varchar(255) not null
);

create table car_tab(
    id bigserial primary key,
    serial_number varchar(255) not null unique,
    model_name varchar(255) not null,
    weight decimal not null,
    price decimal not null,
    manufacture_id bigint not null references manufacture_tab(id)
);

create table sales_person_tab(
    id bigserial primary key,
    name varchar(255) not null
);

create table customer_tab(
    id bigserial primary key,
    name varchar(255) not null,
    phone varchar(255) not null
);

create table sales_tab(
    id bigserial primary key,
    datetime bigint not null,
    sales_person_id bigint not null references sales_person_tab(id),
    customer_id bigint not null references customer_tab(id)
);

create table sale_item_tab(
    id bigserial primary key,
    sales_id bigint not null references sales_tab(id),
    car_id bigint not null references car_tab(id)
);