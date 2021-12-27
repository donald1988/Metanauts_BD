select distinct day1.* 
from 
stadium_table day1, stadium_table day2, stadium_table day3
where 
day1.people >= 100 and day2.people >= 100 
and day3.people >= 100 and
((day1.id + 1 =  day2.id and day1.id + 2 = day3.id) or 
(day1.id - 1 = day2.id and day1.id + 1 = day3.id) or 
(day1.id - 2 = day2.id and day1.id - 1 = day3.id)) 
order by day1.id; 