# SQL Views
# SQL Views
결과를 기반으로 하는 가상 테이블

## SQL CREATE VIEW Statement
```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

## SQL CREATE VIEW Examples
```sql
CREATE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName
FROM Customers
WHERE Country='Brazil';
```

## SQL Updating a View
```sql
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

## SQL Dropping a View
```sql
DROP VIEW view_name;
```
