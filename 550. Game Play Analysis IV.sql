# Write your MySQL query statement below
select ifnull(round(count(distinct Result.player_id) / count(distinct Activity.player_id), 2), 0) as fraction
from Activity, (
    select Activity.player_id as player_id
    from Activity, (
        select player_id, date_add(min(event_date), interval 1 day) as second_date
        from Activity
        group by player_id
    ) as Second
    where Activity.player_id = Second.player_id and Activity.event_date = Second.second_date
) as Result

