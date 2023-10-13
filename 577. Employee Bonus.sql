# Write your MySQL query statement below
select e.name, sum(b.bonus) as bonus
from Employee e
left join Bonus b
on e.empId = b.empId
group by e.empId
having sum(b.bonus) < 1000 or count(b.bonus) = 0
