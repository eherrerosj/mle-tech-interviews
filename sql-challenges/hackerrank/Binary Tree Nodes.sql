-- You are given a table, BST, containing two columns: N and P,
--   where N represents the value of a node in Binary Tree, and P is the parent of N.
-- Write a query to find the node type of Binary Tree ordered by
--   the value of the node. Output one of the following for each node:
--     Root: If node is root node.
--     Leaf: If node is leaf node.
--     Inner: If node is neither root nor leaf node.
select
     b.n,
     case
          when b.p is null then 'Root'
          when (
               select
                    count(*)
               from
                    bst
               where
                    b.n in (
                         select
                              t.p
                         from
                              bst t
                    )
          ) = 0 then 'Leaf' -- leaf nodes are not parents
          else 'Inner'
     end
from
     bst as b
order by
     n;