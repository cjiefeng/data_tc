# Database design
Schema can be found in `init/01_init_db.sql`.    
Using docker: `init/*.sql` files are added to image `/docker-entrypoint-initdb.d/` dir so that it will run when docker image initialize.

Testing data can be found in `init/data/test_data.sql`.   
Data will need to be manually inserted.  
Added a convenience docker-compose.yml to test locally.  
```
$ docker compose up
```

## Customers spending list 
```
SELECT cust.id as cust_id, sum(COALESCE(car.price, 0)) as spending 
FROM customer_tab AS cust 
LEFT JOIN sales_tab AS s ON cust.id = s.customer_id
LEFT JOIN sale_item_tab AS si ON si.sales_id = s.id
LEFT JOIN car_tab as car ON si.car_id = car.id
GROUP BY cust.id;

 cust_id | spending 
---------+----------
       4 |        0
       2 | 36000.90
       3 |  4999.99
       1 | 48450.82
(4 rows)
```
*Customer `4` has yet to make any purchases.


## Top 3 manufacturer by number of sale in current month
```
SELECT manufacture_id, sold FROM (
    SELECT car.manufacture_id, count(car.id) sold, rank() over (order by count(car.id) desc) as r  
    FROM customer_tab AS cust 
    JOIN sales_tab AS s ON cust.id = s.customer_id
    JOIN sale_item_tab AS si ON si.sales_id = s.id
    JOIN car_tab as car ON si.car_id = car.id 
    WHERE to_timestamp(s.datetime) >= date_trunc('month', CURRENT_DATE)
    GROUP BY car.manufacture_id
) b
WHERE b.r <= 3;

 manufacture_id | sold 
----------------+------
              1 |    8
              3 |    4
              4 |    2
              2 |    2
(4 rows)
```
*4 rows are returned because manufacture `2` & `4` has equal amount of sale for the month.
