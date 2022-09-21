# SQL ORDER BY Keyword
## The SQL ORDER BY Keyword
- 오름차순, 내림차순으로 정렬하는 데 사용되는 키워드
- 디폴트는 오름차순 정렬
- ORDER BY DESC 키워드를 이용해서 내림차순 정렬 가능함
  
## ORDER BY Syntax
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|
사용할 예시 데이터베이스는 위와 같다. 

## ORDER BY Example
```sql
SELECT * FROM Customers
ORDER BY Country;
```

## ORDER BY DESC Example
```sql
SELECT * FROM Customers
ORDER BY Country DESC;
```

## ORDER BY Several Columns Example
```sql
SELECT * FROM Customers
ORDER BY Country, CustomerName;
```
- 이런 구문에서는
- 일단 Country를 기준으로 오름차순 정렬을 한다. 
- 그러다 동일한 Country 명이 등장하는 경우, CustomerName을 기준으로 정렬한다. 
  
```sql
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;
```
모든 Customers를 Country를 기준으로 오름차순 정렬을 하다가, 
동일한 Country를 가진 행에 대해서는 CustomerName으로 내림차순 정렬을 해준다. 


