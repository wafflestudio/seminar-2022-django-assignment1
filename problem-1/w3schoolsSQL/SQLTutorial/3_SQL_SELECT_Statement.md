# SQL SELECT Statement
데이터베이스에서 데이터를 선택하는 구문

## SELECT Syntax
``` sql
SELECT column1, column2
FROM table_name;
```
고르고 싶은 field name(column name)을 SELECT 뒤에, 
탐색 대상인 테이블의 이름을 FROM 뒤에 적는다. 

## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|
사용할 예시 데이터베이스는 위와 같다. 

## SELECT Column Example
``` sql
SELECT CustomerName, City FROM Customers;
```

## SELECT * Example
SELECT * 는 모든 columns를 불러오는 구문이다. 

``` sql
SELECT * FROM Customers;
```