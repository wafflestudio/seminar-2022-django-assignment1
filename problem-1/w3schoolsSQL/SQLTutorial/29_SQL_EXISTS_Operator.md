# SQL EXISTS Operator
## The SQL EXISTS Operator
하위 쿼리를 만족하는 레코드가 있는지 테스트
if랑 비슷한 역할
만약 하위 쿼리가 1개 이상의 레코드를 반환하는 경우 
EXISTS 연산자는 TRUE를 반환한다 .

### EXISTS Syntax
```sql
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
```

## SQL EXISTS Examples
```sql
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);
```

``` sql
SELECT SupplierName
FROM suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price = 22);
```