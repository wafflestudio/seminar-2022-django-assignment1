# SQL UNION Operator
## The SQL UNION Operator
두 개 이상의 result set을 결합하는 데 사용하는 연산자
- 조건 1. column 개수가 같아야 한다. 
- 조건 2. 각 columns는 비슷한 data type이어야 한다. 
- 조건 3. SELECT에서 같은 order로 명령되어야 한다. 

### UNION Syntax
```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

### UNION ALL Syntax
원래 UNION은 distinct value만 return한다. 
만약 duplicate value도 허용하고 싶다면, UNION ALL을 이용할 것
```sql
SELECT column_name(s) FROM table1
UNION ALL 
SELECT column_name(s) FROM table2;
```

## SQL UNION Example
```sql
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
```
결과에서는 City column에 Customer의 결과와 Suppliers의 결과가 합쳐져서 나온다. 

## SQL UNION ALL Example
```sql
SELECT CIty FROM Customers
UNION ALL 
SELECT City FROM Suppliers
ORDER BY City;
```

## SQL UNION With WHERE
```sql
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
```

## SQL UNION ALL With WHERE 
```sql
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;
```

## Another UNION Example
```sql
SELECT 'Customer' AS Type, CountactName, City, Country
FROM Customers
UNION
SELECT 'Supplier', ContactName, City, Country
FROM Suppliers;
```
![result](https://user-images.githubusercontent.com/81140673/192079668-c2a32ddf-8db4-411c-81c9-f444834f5531.PNG)

결과는 이렇게 나온다. 
즉, Type이라는 column을 새로 만들고, Customer에서 추출하는 내용을 'Customer'라는 값으로 저장해주는 것
