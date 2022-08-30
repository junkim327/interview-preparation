/*
    1084. Sales Analysis III

    Table: Product
    +--------------+---------+
    | Column Name  | Type    |
    +--------------+---------+
    | product_id   | int     |
    | product_name | varchar |
    | unit_price   | int     |
    +--------------+---------+
    product_id is the primary key of this table.
    Each row of this table indicates the name and the price of each product.

    Table: Sales
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | seller_id   | int     |
    | product_id  | int     |
    | buyer_id    | int     |
    | sale_date   | date    |
    | quantity    | int     |
    | price       | int     |
    +-------------+---------+
    This table has no primary key, it can have repeated rows.
    product_id is a foreign key to the Product table.
    Each row of this table contains some information about one sale.
*/


-- 517ms
select product_id,'store1' as store, store1 as price
from products
where store1 is not null
union
select product_id, 'store2' as store, store2 as price
from products
where store2 is not null
union
select product_id, 'store3' as store, store3 as price
from products
where store3 is not null;