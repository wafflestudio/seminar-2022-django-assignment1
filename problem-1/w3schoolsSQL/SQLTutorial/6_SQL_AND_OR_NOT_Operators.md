## The SQL AND, OR and NOT Operators

- WHERE 구문은 AND, OR, NOT 연산자와 함께 사용할 수 있다. 
- 사용법은 굉장히 간단하다. 
  
## AND Syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```

## OR Syntax
```sql
SELECT column1, column2, ... 
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

## NOT Syntax
```sql
SELECT column1, column2, ... 
FROM table_name
WHERE NOT condition1;
```


## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|
사용할 예시 데이터베이스는 위와 같다. 

## AND Example
``` sql
SELECT * FROM Customers
WHERE Country='Germany' AND City='Berlin';
```


## OR Example
```sql
SELECT * FROM Customers
WHERE City='Berlin' OR City='Munchen';
```

## NOT Example
```sql
SELECT * FROM Customers
WHERE NOT Country='Germany';
```

## Combining AND, OR, and NOT
```sql
SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='Munchen');
```