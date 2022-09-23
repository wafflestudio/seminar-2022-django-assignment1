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


## SQL TOP, LIMIT, FETCH FIRST Example
``` sql
SELECT TOP 3 * FROM Customers;
```
이 구문이랑

```sql
SELECT * FROM Customers
LIMIT 3;
```
이 구문은 같은 동작을 한다. 

## SQL TOP PERCENT Example
TOP을 row 개수 말고 퍼센트로 반환한다. 
```sql
SELECT TOP 50 PERCENT * FROM Customers;
```

## ADD a WHERE CLAUSE
```sql
SELECT TOP 3 * FROM Customers
WHERE Country='Germany';
```
