/*
 Write a SQL query to get the nth highest salary from the Employee table.
 
 +----+--------+
 | Id | Salary |
 +----+--------+
 | 1  | 100    |
 | 2  | 200    |
 | 3  | 300    |
 +----+--------+
 
 For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.
 
 +------------------------+
 | getNthHighestSalary(2) |
 +------------------------+
 | 200                    |
 +------------------------+
 
 
 Learnings:
 - Using where rank = N wouldn't work in certain cases. Better to declare a
 variable which is N - 1 and where use the limit function
 */
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN DECLARE IND INT;

SET
    IND = N - 1;

RETURN (
    select
        DISTINCT salary
    from
        (
            select
                salary,
                RANK() OVER(
                    order by
                        salary desc
                ) ranks
            from
                Employee
        ) b
    limit
        IND, 1
);

END