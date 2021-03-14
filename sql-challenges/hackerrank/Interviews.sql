-- Samantha interviews many candidates from different colleges using coding challenges
-- and contests. Write a query to print the contest_id, hacker_id, name, and the sums
-- of total_submissions, total_accepted_submissions, total_views, and total_unique_views
-- for each contest sorted by contest_id. Exclude the contest from the result if all four
-- sums are
-- Note: A specific contest can be used to screen candidates at more than one college, 
-- but each college only holds screening contest.
-- Input Format
-- The following tables hold interview data:
--     Contests: The contest_id is the id of the contest, hacker_id is the id of the
--     hacker who created the contest, and name is the name of the hacker.
--     Colleges: The college_id is the id of the college, and contest_id is the id of the
--     contest that Samantha used to screen the candidates.
--     Challenges: The challenge_id is the id of the challenge that belongs to one of the
--     contests whose contest_id Samantha forgot, and college_id is the id of the college
--     where the challenge was given to candidates.
--     View_Stats: The challenge_id is the id of the challenge, total_views is the number
--     of times the challenge was viewed by candidates, and total_unique_views is the number
--     of times the challenge was viewed by unique candidates.
--     Submission_Stats: The challenge_id is the id of the challenge, total_submissions is
--     the number of submissions for the challenge, and total_accepted_submission is the
--     number of submissions that achieved full scores. 
select
     a.contest_id,
     a.hacker_id,
     a.name,
     a.sum_total_submissions,
     a.sum_total_accepted_submissions,
     a.sum_total_views,
     a.sum_total_unique_views
from
     (
          select
               con.contest_id,
               con.hacker_id,
               con.name,
               sum(vs.sum_total_views) as sum_total_views,
               sum(vs.sum_total_unique_views) as sum_total_unique_views,
               sum(ss.sum_total_submissions) as sum_total_submissions,
               sum(ss.sum_total_accepted_submissions) as sum_total_accepted_submissions
          from
               contests con
               left join colleges col on con.contest_id = col.contest_id
               left join challenges cha on col.college_id = cha.college_id
               left join (
                    select
                         challenge_id,
                         sum(total_views) as sum_total_views,
                         sum(total_unique_views) as sum_total_unique_views
                    from
                         View_Stats
                    group by
                         challenge_id
               ) vs on cha.challenge_id = vs.challenge_id
               left join (
                    select
                         challenge_id,
                         sum(total_submissions) as sum_total_submissions,
                         sum(total_accepted_submissions) as sum_total_accepted_submissions
                    from
                         Submission_Stats
                    group by
                         challenge_id
               ) ss on cha.challenge_id = ss.challenge_id
          group by
               con.contest_id,
               con.hacker_id,
               con.name
     ) a
where
     a.sum_total_views is not null
order by
     a.contest_id