# SQL Aliases
## SQL Aliases
테이블, 테이블 명의 임시 이름을 지정한다. 
AS

### Alias Column Syntax
```sql
SELECT column_name AS alis_name
FROM table_name;
```

### Alias Table Syntax
```sql
SELECT column_name(s)
FROM table_name AS alis_name;
```

## Alias for Columns Example
```sql
SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;
```

``` sql
SELECT CustomerName AS Customer, ContactName AS [Contact Person]
FROM Customers;
```
```sql
SELECT CustomerName, Address+', '+PostalCode+' ' + City+', '+ Country AS Address
FROM Customers;
```

## Alias for Tables Example
```sql
SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;
```

```sql
SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerName='Around the Horn' AND Customers.CustomerID=Orders.CustomerID;
```