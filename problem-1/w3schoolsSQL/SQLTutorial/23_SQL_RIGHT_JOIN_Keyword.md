# SQL RIGHT JOIN Keyword
## SQL RIGHT JOIN Keyword
오른쪽 테이블의 모든 레코드와 왼쪽 테이블의 일치하는 레코드를 반환한다. 

```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

## SQL RIGHT JOIN Example
```sql
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;
```
모든 Employees.LastName, Employees.FirstName을 반환하되, Orders.OrderID도 있으면, 이걸 리턴한다. 
