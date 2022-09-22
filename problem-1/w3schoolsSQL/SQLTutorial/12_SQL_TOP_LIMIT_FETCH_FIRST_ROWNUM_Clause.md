# SQL TOP, LIMIT, FETCH FIRST or ROWNUM Clause
## THE SQL SELECT TOP Clause
SELECT TOP 구문으로 반환할 레코드 수를 지정해줄 수 있다. 

``` sql
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;
```


## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|

사용할 예시 데이터베이스는 위와 같다.


## SQL TOP, LIMIT, FETCH FIRST
## SQL TOP PERCENT Example
## ADD a WHERE CLAUSE
