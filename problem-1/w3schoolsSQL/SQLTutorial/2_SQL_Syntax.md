# SQL Syntax
## Database Tables
- 데이터베이스에는 하나 이상의 테이블이 있다. 


| CustomerID	| CustomerName	| ContactName	| Address	| City | 	PostalCode	| Country| 
|---|---|----|----|----|----|---|
|1|Alfreds Futterkiste|	Maria Anders|	Obere Str. 57|	Berlin	|12209|	Germany|
|2|	Ana Trujillo| Emparedados y| helados	Ana Trujillo|	Avda. de la Constitución 2222|	México D.F.|	05021	|Mexico|


## SQL Statements
데이터베이스에서는 SQL문을 이용해서 작업을 수행한다. 
``` sql
SELECT * FROM Customers;
```

## Keep in mind that
참고로 SQL은 대소문자를 구분하지 않는다(키워드 한정)

## Semicolon after SQL statements
어떤 데이터베이스에서는 SQL 문장마다 세미콜론을 사용해야 한다. 

## Some of the most important SQL commands
- SELECT : 데이터 추출
- UPDATE : 데이터 업데이트
- DELETE : 데이터 삭제
- INSERT INTO : 데이터 삽입
- CREATE DATABASE : 데이터베이스 생성
- ALTER DATABASE : 데이터베이스 수정
- CREATE TABLE : 테이블 생성
- ALTER TABLE : 테이블 수정
- DROP TABLE : 테이블 삭제
- CREATE INDEX : 인덱스 생성
- DROP INDEX : 인덱스 삭제
