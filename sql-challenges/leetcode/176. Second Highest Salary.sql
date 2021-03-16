/*
 Create table If Not Exists Employee (Id int, Salary int)
 Truncate table Employee
 insert into Employee (Id, Salary) values ('1', '100')
 insert into Employee (Id, Salary) values ('2', '200')
 insert into Employee (Id, Salary) values ('3', '300')
 
 Write a SQL query to get the second highest salary from the Employee table.
 
 +----+--------+
 | Id | Salary |
 +----+--------+
 | 1  | 100    |
 | 2  | 200    |
 | 3  | 300    |
 +----+--------+
 
 For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
 
 +---------------------+
 | SecondHighestSalary |
 +---------------------+
 | 200                 |
 +---------------------+
 
 Learnings:
 - OFFSET can be used together with LIMIT to achieve the expected result here, with an inner select to
 avoid problems when there wan't a second non-null salary
 - I used ROW_NUMBER() (RANK() is also valid) plus filtering. The gotcha in this case was the
 corner case in which there wasn't a second non-null salary. That's why the ifnull() was needed
 */
SELECT
    IFNULL(
        (
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
            where
                ranks = 2
        ),
        NULL
    ) as SecondHighestSalary;