# SQL NULL Values
## What is a NULL Value?
- 값이 없는 필드
- NULL과 Blank는 다른 것이다. 
  
## How to Test for NULL Values?
비교 연산자(=, <, <> 등)을 이용해서 NULL 값을 체크하는 것이 불가능하다. 
대신, IS NULL, IS NOT NULL 연산자를 이용한다. 

### IS NULL Syntax
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```

### IS NOT NULL Syntax
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```


## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|

사용할 예시 데이터베이스는 위와 같다.


## The IS NULL Operator
- NULL 값을 테스트하는 데 사용된다. 
```sql
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;
```

## The IS NOT NULL Operator
```sql
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NOT NULL;
```