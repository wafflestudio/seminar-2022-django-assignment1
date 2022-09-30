# SQL GROUP BY Statement
## The SQL GROUP BY Statement
그룹 짓는 함수
주로 aggregate function과 함께 사용된다. 
COUNT(), MAX(), MIN(), SUM(), AVG() 등등

### GROUP BY Syntax
```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```

## SQL GROUP BY Examples
```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;
```

```sql
SELECT City, Country, COUNT(CustomerID)
FROM Customers
GROUP BY City
ORDER BY Country;
```

## GROUP BY With JOIN Example
```sql
SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;
```