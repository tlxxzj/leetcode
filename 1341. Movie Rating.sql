# Write your MySQL query statement below
select t1.name as results from (
select u.name
from Users u, MovieRating mr
where u.user_id = mr.user_id
group by u.user_id
order by count(mr.movie_id) desc, u.name
limit 1
) t1

union all

select t2.title as results from (
    select m.title, avg(mr.rating) as rating
    from Movies m, MovieRating mr
    where m.movie_id = mr.movie_id and mr.created_at >= '2020-02-01' and mr.created_at <= '2020-02-28'
    group by m.movie_id
    order by rating desc, m.title
    limit 1
) t2



