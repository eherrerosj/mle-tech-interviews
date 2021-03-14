-- Generate the following two result sets:
--     Query an alphabetically ordered list of all names in OCCUPATIONS,
--     immediately followed by the first letter of each profession as a
--     parenthetical (i.e.: enclosed in parentheses). For example:
--     AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
--     Query the number of ocurrences of each occupation in OCCUPATIONS.
--     Sort the occurrences in ascending order, and output them in the following format:
--     There are a total of [occupation_count] [occupation]s.
--     where [occupation_count] is the number of occurrences of an
--     occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.
-- Note: There will be at least two entries in the table for each
-- type of occupation.
-- Input Format
-- The OCCUPATIONS table is described as follows: Occupation will
-- only contain one of the following values: Doctor, Professor, Singer or Actor.
select
     concat(
          o.name,
          "(",
          substr(o.occupation, 1, 1),
          ")"
     ) as concated_str
from
     OCCUPATIONS o
order by
     o.name;

SELECT
     "There are a total of ",
     count(OCCUPATION),
     concat(lower(occupation), "s.")
FROM
     OCCUPATIONS
GROUP BY
     OCCUPATION
ORDER BY
     count(OCCUPATION),
     OCCUPATION ASC;