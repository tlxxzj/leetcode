# Write your MySQL query statement below
select st.student_id, st.student_name, su.subject_name, count(ex.subject_name) as attended_exams
from Students st
cross join Subjects su
left join Examinations ex
on st.student_id = ex.student_id and su.subject_name = ex.subject_name
group by st.student_id, su.subject_name
order by st.student_id, su.subject_name
