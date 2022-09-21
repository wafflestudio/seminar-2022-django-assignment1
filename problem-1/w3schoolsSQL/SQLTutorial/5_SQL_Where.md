# SQL Where Clause
- record를 필터링하는 데 사용되는 구문이다. 
- 조건을 만족하는 record만 걸러내는 기능을 한다. 

## WHERE Syntax
``` sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```


## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|
사용할 예시 데이터베이스는 위와 같다. 


## WHERE Clause Example
```sql
SELECT * FROM Customers
WHERE Country='Germany';
```
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1	|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin|	12209|	Germany|
|6|	Blauer See Delikatessen|	Hanna Moos|	Forsterstr. 57|	Mannheim|	68306|	Germany|

```sql
SELECT * FROM Customers
WHERE city='Aachen';
```
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|17	|Drachenblut Delikatessend|	Sven Ottlieb|	Walserweg 21|	Aachen|	52066|	Germany|


## Text Fields vs. Numeric Fields

- Text Field를 찾을 때는 '' 작은 따옴표를 이용한다. 
- Numberic Field를 찾는 경우, 바로 숫자만 나타내면 된다. 


```sql
SELECT * FROM Customers
WHERE CustomerID=1;
```

```sql
SELECT * FROM Customers
WHERE Country='France';
```

## Operators in the WHERE Clause
- '='
- '>'
- '>'
- '>='
- '<='
- <> (!=과 같은 의미)
- BETWEEN
- LIKE
- IN