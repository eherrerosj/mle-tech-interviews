-- Julia asked her students to create some coding challenges.
-- Write a query to print the hacker_id, name, and the total
-- number of challenges created by each student. Sort your
-- results by the total number of challenges in descending order.
-- If more than one student created the same number of challenges,
-- then sort the result by hacker_id. If more than one student
-- created the same number of challenges and the count is less
-- than the maximum number of challenges created, then exclude
-- those students from the result.
-- Input Format
-- The following tables contain challenge data:
--     Hackers: The hacker_id is the id of the hacker,
--     and name is the name of the hacker.
--     Challenges: The challenge_id is the id of the challenge,
--     and hacker_id is the id of the student who created the challenge. 
-- Key learning: use HAVING because it's computed after the group by
select
     c.hacker_id,
     h.name,
     count(c.hacker_id) as c_count
from
     Hackers as h
     /* this is the join we want to output them from */
     inner join Challenges as c on c.hacker_id = h.hacker_id
     /* after they have been grouped by hacker */
group by
     c.hacker_id,
     h.name
having
     c_count = (
          select
               max(t1.total_challenges)
          from
               (
                    select
                         count(hacker_id) as total_challenges
                    from
                         challenges
                    group by
                         hacker_id
                    order by
                         hacker_id
               ) t1
     )
     or c_count in (
          select
               t2.c_cnt
          from
               (
                    select
                         count(*) as c_cnt
                    from
                         Challenges
                    group by
                         hacker_id
               ) t2
          group by
               t2.c_cnt
          having
               count(t2.c_cnt) = 1
     )
order by
     c_count DESC,
     c.hacker_id;