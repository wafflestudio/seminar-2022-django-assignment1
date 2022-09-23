# SQL COUNT(), AVG() and SUM() Functions
## The SQL COUNT(), AVG() and SUM() Functions
### COUNT() Syntax
- 설정한 조건과 일치하는 행 수를 리턴한다. 
```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

### AVG() Syntax
- 설정한 조건에 맞는 행 개수를 리턴한다. 
```sql
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```

### SUM() Syntax
- 설정한 조건에 맞는 행들의 지정한 열의 합 리턴
```sql
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

## DEMO Database
| ProductID | ProductName | SupplierID | CategoryID | Unit | Price | 
|-|-|-|-|-|-|
|1|Chais|1|1|10 boxes * 20 bags | 18 | 
|2|Chang|1|1|24-12 oz bottles | 19|
|3|Aniseed Syrup|1|2|12-550 ml bottles|10|


## COUNT() Example
```sql
SELECT COUNT(ProductID)
FROM Products;
```

## AVG() Example
```sql
SELECT AVG(Price)
FROM Products;
```

## SUM() Example
```sql
SELECT SUM(Quantity)
FROM OrderDetails;
```
