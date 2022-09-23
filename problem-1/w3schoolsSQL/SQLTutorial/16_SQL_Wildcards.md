# SQL Wildcards
## SQL Wildcard Characters
Wildcard Characters는 문자열에서 하나 이상의 문자를 대체하는 데 사용한다. 
이때 Wildcard Characters는 LIKE, WHERE 등 열에서 패턴을 검색할 때 사용한다. 

### Wildcard Characters in SQL Server
|Symbol|Desciption|Example|
|-|-|-|
|%|문자 n개 대체|bl% -> black, blue, blob|
|_|문자 1개 대체|h_t -> hot, hat, hit|
|[]|문자 안에 있는 1개 문자 대체|h[oa]t -> hot, hat, hit(X)|
|^|brackets 안에 없는 문자 1개 대체|h[^oa]t -> hit, hot(X), hat(X)|
| - |어떤 범위에 있는 문자 1개 대체|c[a-b]t -> cat, cbt|


## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|

사용할 예시 데이터베이스는 위와 같다.

## Using the % wildcard
```sql
SELECT * FROM Customers
WHERE City LIKE 'ber%';
```
ber로 시작하는 City

```sql
SELECT * FROM Customers
WHERE City LIKE '%es%';
```
중간에 es이 들어가는 City

## Using the _ wildcard
```sql
SELECT * FROM Customers
WHERE City LIKE '_ondon';
```
ondon으로 끝나는 City

```sql
SELECT * FROM Customers
WHERE City LIKE 'L_n_on';
```

## Using the [charlist] Wildcard
```sql
SELECT * FROM Customers
WHERE City LIKE '[bsp]%';
```
b로 시작하거나, s로 시작하거나, p로 시작하는 City

```sql
SELECT * FROM Customers
WHERE City LIKE '[a-c]%';
```

## Using the [!charlist] Wildcard
```sql
SELECT * FROM Customers
WHERE City LIKE '[!bsp]%';
```
b, s, p로 시작하지 않는 City

```sql
SELECT * FROM Customers
WHERE City NOT LIKE '[bsp]%';
```
b, s, p로 시작하지 않는 City
