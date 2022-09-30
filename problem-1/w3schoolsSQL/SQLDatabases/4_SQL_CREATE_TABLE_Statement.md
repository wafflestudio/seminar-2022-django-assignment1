# SQL CREATE TABLE Statement
## The SQL CREATE TABLE Statement
데이터베이스에 새 테이블 생성하기

```sql
CREATE TABLE table_name (
    column1 datatype, 
    column2 datatype, 
    column3 datatype, 
    ...
);
```

## SQL CREATE TABLE Example
```sql
CREATE TABLE Persons (
    PersonID int, 
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```

## Create Table Using Another Table
동일한 열 정의를 가져오는 테이블
```sql
CREATE TABLE new_table_name AS
    SELECT column1, column2, ...
    FROM existing_table_name
    WHERE ...;
```

```sql
CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;
```
