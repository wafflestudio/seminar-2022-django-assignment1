# SQL SELECT DISTINCT Statement
## The SQL SELECT DISTINCT Statement
- distinct values만 리턴하는 구문

``` sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|
사용할 예시 데이터베이스는 위와 같다. 

## SELECT Example Without DISTINCT
``` sql
SELECT Country FROM Customers;
```
와 같이 DISTINCT 키워드 없이 구문을 실행한 결과는 다음과 같다. 

| Country | 
|--|
| Germany|
|Mexico|
|Mexico|
|UK|
|Sweden|
|Germany|
|France|
|Spain|
|France|

Mexico처럼 2 개 이상의 값을 가진 경우, 
중복되어 나타나는 것을 알 수 있다. 

## SELECT DISTINCT Examples

이제 같은 구문을 DISTINCT 키워드와 함께 실행해보자. 

```sql
SELECT DISTINCT Country FROM Customers;
```

| Country | 
|--|
| Germany|
|Mexico|
|UK|
|Sweden|
|France|
|Spain|

이제 Mexico, Germany, France라는 중복된 값이 하나로 정리되어 나오는 것을 확인할 수 있다. 

## examples
```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```
이 구문은 distinct country의 개수를 리턴한다. 

|COUNT(DISTINCT Country)|
|--|
|21|

