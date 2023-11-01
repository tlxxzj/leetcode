# Write your MySQL query statement below
select p1.product_id, ifnull(p2.new_price, 10) as price
from (
    select distinct product_id
    from Products
) p1
left join (
    select product_id, new_price
    from Products
    where (product_id, change_date) in (
        select product_id, max(change_date)
        from Products
        where change_date <= '2019-08-16'
        group by product_id
    )
) p2
on p1.product_id = p2.product_id
