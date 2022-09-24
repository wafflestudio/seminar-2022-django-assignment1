# SQL Stored Procedures for SQL Server
## What is a Stored Procedure? 
반복해서 사용할 수 있는 프로세저

### Stored Procedure Syntax
- procedure 생성
```sql
CREATE PROCEDURE procedure_name
AS
sql_statement
GO;
```
- procedure 실행
```sql
EXEC procedure_name;
```

## Stored Procedure Example
```sql
CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;
```

```sql
EXEC SelectAllCustomers;
```

## Stored Procedure with One Parameter
```sql
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30)
AS
SELECT * FROM Customers WHERE City = @City
GO;
```

```sql
EXEC SelectAllCustomers @City = 'London';
```

## Stored Procedure with Multiple Parameters
```sql
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode
GO;
```

```sql
EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';
```