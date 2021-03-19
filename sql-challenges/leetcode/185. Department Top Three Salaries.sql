/*
 Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int)
 Create table If Not Exists Department (Id int, Name varchar(255))
 Truncate table Employee
 insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '85000', '1')
 insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2')
 insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2')
 insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1')
 insert into Employee (Id, Name, Salary, DepartmentId) values ('5', 'Janet', '69000', '1')
 insert into Employee (Id, Name, Salary, DepartmentId) values ('6', 'Randy', '85000', '1')
 insert into Employee (Id, Name, Salary, DepartmentId) values ('7', 'Will', '70000', '1')
 Truncate table Department
 insert into Department (Id, Name) values ('1', 'IT')
 insert into Department (Id, Name) values ('2', 'Sales')
 
 The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.
 
 +----+-------+--------+--------------+
 | Id | Name  | Salary | DepartmentId |
 +----+-------+--------+--------------+
 | 1  | Joe   | 85000  | 1            |
 | 2  | Henry | 80000  | 2            |
 | 3  | Sam   | 60000  | 2            |
 | 4  | Max   | 90000  | 1            |
 | 5  | Janet | 69000  | 1            |
 | 6  | Randy | 85000  | 1            |
 | 7  | Will  | 70000  | 1            |
 +----+-------+--------+--------------+
 
 The Department table holds all departments of the company.
 
 +----+----------+
 | Id | Name     |
 +----+----------+
 | 1  | IT       |
 | 2  | Sales    |
 +----+----------+
 
 Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows (order of rows does not matter).
 
 +------------+----------+--------+
 | Department | Employee | Salary |
 +------------+----------+--------+
 | IT         | Max      | 90000  |
 | IT         | Randy    | 85000  |
 | IT         | Joe      | 85000  |
 | IT         | Will     | 70000  |
 | Sales      | Henry    | 80000  |
 | Sales      | Sam      | 60000  |
 +------------+----------+--------+
 
 Explanation:
 
 In IT department, Max earns the highest salary, both Randy and Joe earn the second highest salary, and Will earns the third highest salary. There are only two employees in the Sales department, Henry earns the highest salary while Sam earns the second highest salary.
 
 
 Learnings:
 - Corner case of a department with no name, had to check
 - Dense_Rank() function must be used because in case of tie, all with same value must be accepted
 */
select
    d.Name as Department,
    Employee,
    Salary
from
    (
        select
            Name as Employee,
            DepartmentId,
            Salary,
            dense_rank() over (
                partition by DepartmentId
                order by
                    salary desc
            ) as rn
        from
            Employee
    ) tmp
    inner join Department d on d.Id = tmp.DepartmentId
where
    rn < 4
order by
    Salary desc;