# SQL ANY and ALL Operators
## The SQL ANY and ALL Operators
ANY, ALL 연산자를 이용하면, single column value와 다른 value와 비교를 할 수 있다. 

## The SQL ANY Operator
범위 값 중 하나에 대해 조건이 참인지를 검토하는 연산자
만약 하위 쿼리 중 하나라도 조건을 만족하면, TRUE를 반환한다. 

### ANY Syntax
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY(
    SELECT column_name
    FROM table_name
    WHERE condition
);
```
- 참고) operator는 =, <>, >, >=, <=와 같은 std 비교 연산자여야 한다. 

## The SQL ALL Operator
결과로 bool을 반환한다. 
모든 하위 쿼리를 만족하면 TRUE를 반환한다. 

### ALL Syntax With SELECT
```sql
SELECT ALL column_name(s)
FROM table_name
WHERE condition;
```

### ALL Syntax With WHERE or HAVING
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ALL (
    SELECT column_name
    FROM table_name
    WHERE condition
);
```

## SQL ANY Examples
```sql
SELECT ProductName
FROM Products
WHERE ProductID = ANY (
    SELECT ProductID
    FROM OrderDetails
    WHERE Quantity = 10
);
```

``` sql
SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity > 99);
```

```sql
SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity > 1000);
```


## SQL ALL Examples
```sql
SELECT ALL ProductName
FROM Products
WHERE TRUE;
```

```sql
SELECT ProductName
FROM Products
WHERE ProductID = ALL
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
```
