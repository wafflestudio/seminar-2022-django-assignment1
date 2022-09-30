# SQL FULL OUTER JOIN Keyword
## SQL FULL OUTER JOIN Keyword
일단 왼쪽 테이블, 오른쪽 테이블을 모두 리턴하되, 
일치하는 값이 없으면 null인 그대로 둔다. 

```sql
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;
```

## SQL FULL OUTER JOIN Example
```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName;
```
