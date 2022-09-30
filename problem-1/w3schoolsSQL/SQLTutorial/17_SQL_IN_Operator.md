# SQL IN Operator
## The SQL IN Operator
WHERE에서 여러 값을 지정해줄 수 있다. 

### IN Syntax
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

이때, IN 뒤에 sql statement를 넣는 것도 가능하다. 
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT);
```


## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|

사용할 예시 데이터베이스는 위와 같다.


## IN Operator Examples
```sql
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');
```

``` sql
SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');
```

```sql
SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);
```