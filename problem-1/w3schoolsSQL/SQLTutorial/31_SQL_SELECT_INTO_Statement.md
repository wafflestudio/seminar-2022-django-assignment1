# SQL SELECT INTO Statement
## The SQL SELECT INTO Statement
한 테이블의 데이터를 다른 테이블로 복사한다. 

### SELECT INTO Syntax
```sql
SELECT *
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;
```
모든 column을 다른 테이블에 복사하고 싶은 경우

```sql
SELECT column1, column2, ...
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;
```
일부 column만 다른 테이블에 복사하고 싶은 경우

## SQL SELECT INTO Examples
```sql
SELECT * INTO CustomersBackup2017
FROM Customers;
```

```sql
SELECT * INTO CustomersBackup2017 IN 'Backup.mdb'
FROM Customers;
```

```sql
SELECT CustomerName, ContactName INTO CustomersBackup2017
FROM Customers;
```

```sql
SELECT * INTO CustomersGermany
FROM Customers
WHERE Country = 'Germany';
```

```sql
SELECT Customers.CustomerName, Orders.OrderID
INTO CustomersOrderBackup2017
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
```

```sql
SELECT * INTO newtable
FROM oldtable
WHERE 1 = 0;
```
