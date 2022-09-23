# SQL INNER JOIN Keyword
## SQL INNER JOIN Keyword
두 테이블에서 교집합이 있는 레코드를 선택한다. 

```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```


## SQL INNER JOIN Example
```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

- CustomerID가 일치하는 모든 OrderID, CustomerName을 리턴한다. 

## JOIN Three Tables
```sql
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);
```
세 개의 테이블을 JOIN하고 싶을 땐
두 개씩 묶어서 INNER JOIN을 한다. 
