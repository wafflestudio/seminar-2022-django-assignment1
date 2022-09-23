# SQL BETWEEN Operator
## THE SQL BETWEEN Operator
- 지정된 범위 내의 값을 선택한다. 
- 숫자, 텍스트, 날짜 등


### BETWEEN Syntax
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

## BETWEEN Example
``` sql
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
```

## NOT BETWEEN Example
``` sql
SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;
```

## BETWEEN with IN Example
```sql
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID NOT IN (1, 2, 3);
```

## BETWEEN Text Values Example
```sql
SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni' 
ORDER BY ProductName;
```

``` sql
SELECT * FROM Products
WHERE ProductName BETWEEN "Carnarvon Tigers" AND "Chef Anton's Cajun Seasoning"
ORDER BY ProductName;
```

## NOT BETWEEN Text Values Example
```sql
SELECT * FROM Products
WHERE ProductName NOT BETWEEN 'Carnarvon Tigers' AND 'Mozzerella di Giovanni'
ORDER BY ProductName;
```

## BETWEEN Dates Example
``` sql
SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;
```


```sql
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
```

