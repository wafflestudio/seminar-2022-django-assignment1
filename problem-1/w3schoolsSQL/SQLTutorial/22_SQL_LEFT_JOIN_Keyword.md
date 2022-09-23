# SQL LEFT JOIN Keyword
## SQL LEFT JOIN Keyword
왼쪽 테이블의 모든 레코드와, 오른쪽 테이블에도 일치하는 레코드를 반환한다. 
일치하지 않는 경우 null을 반환한다? 

```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

## SQL LEFT JOIN Example
```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
```
오른족 테이블과 일치하는 레코드가 없더라도 왼쪽 테이블의 모든 CustomerName 값을 반환한다. 
이 예제에서는 null로 채워서 반환한다. 
