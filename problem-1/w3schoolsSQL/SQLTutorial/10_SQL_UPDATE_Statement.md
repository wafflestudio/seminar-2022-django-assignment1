# The SQL UPDATE Statement
- 테이블의 기존 레코드를 업데이트하는 기능

## UPDATE Syntax
``` sql
UPDATE table_name
SET column1=value1, column2=value2, ...
WHERE condition;
```

## UPDATE Table
```sql
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City='Frankfurt'
WHERE CustomerID = 1;
```
CustomerID=1인 row의 contactName과 City를 업데이트하는 구문

## UPDATE Multiple Records
```sql
UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico';
```

국가가 'Mexico'인 모든 row의 ContactName을 'Juan'으로 업데이트해주는 구문

## Update Warning!
WHERE으로 조건을 설정해주지 않으면, 
모든 레코드가 업데이트되므로 주의해야 한다. 

```sql
UPDATE Customers
SET ContactName='Juan';
```