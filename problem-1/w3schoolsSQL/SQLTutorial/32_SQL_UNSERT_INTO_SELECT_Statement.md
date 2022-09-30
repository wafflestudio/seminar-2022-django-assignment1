# SQL INSERT INTO SELECT
## The SQL INSERT INTO SELECT Statement
한 테이블의 데이터를 복사해서 다른 테이블에 삽입한다. 
단, 이 명령문을 이용하려면 원본 테이블과 대상 테이블의 타입이 일치해야 한다. 

### INSERT INTO SELECT Syntax
```sql
INSERT INTO table2
SELECT * FROM table1
WHERE condition;
```

```sql
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;
```

## SQL INSERT INTO SELECT Examples
```sql
INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers;
```

```sql
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
SELECT SupplierName, ContactName, Address, City, PostalCode, Country FROM Suppliers;
```
