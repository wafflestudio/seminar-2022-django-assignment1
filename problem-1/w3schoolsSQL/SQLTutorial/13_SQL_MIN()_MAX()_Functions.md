# SQL MIN() and MAX() Functions
## The SQL MIN() and MAX() 
- MIN() function
  - 지정한 칼럼의 가장 작은 value를 리턴한다. 
- MAX() function
  - 지정한 칼럼의 가장 큰 value를 리턴한다. 
  
### MIN() Syntax
```sql
SELECT MIN(column_name)
FROM table_name
WHERE condition;
```

### MAX() Syntax
```sql
SELECT MAX(column_name)
FROM table_name
WHERE condition;
```



## MIN() Example
```sql
SELECT MIN(Price) AS SmallestPrice
FROM Products;
```

## MAX() Example
```sql
SELECT MAX(Price) AS LargestPrice
FROM Products;
```
