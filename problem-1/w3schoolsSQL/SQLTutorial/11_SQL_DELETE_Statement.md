# THE SQL DELETE Statement
DELETE로 테이블의 기존 레코드를 삭제한다. 

## DELETE Syntax
```sql
DELETE FROM table_name WHERE condition;
```


## Demo Database
| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|

사용할 예시 데이터베이스는 위와 같다.


## SQL DELETE Example
```sql
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
```

## Delete All Records
테이블 자체, 테이블 구조/속성/인덱스는 그대로 유지하면서
테이블의 모든 행을 삭제할 수 있다. 

```sql
DELETE FROM table_name;
```
