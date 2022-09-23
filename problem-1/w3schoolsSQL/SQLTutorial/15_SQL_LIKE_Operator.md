# SQL LIKE Operator

## The SQL LIKE Operator
비슷한 패턴을 가진 행을 찾는 연산자
%, _ 를 이용해서 LIKE 연산자를 사용한다. 

### LIKE Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

| LIKE Operator | Description | 
|-|-|
| WHERE CustomerName LIKE 'a%' | a로 시작|
| WHERE CustomerName LIKE '%a' | a로 끝남|
| WHERE CustomerName LIKE '%or%'| 아무데나 or이 있음|
| WHERE CustomerName LIKE '_r%'| 2번째 문자가 r|
| WHERE CustomerName LIKE 'a_%'| a로 시작하고 최소 2글자 |
| WHERE CustomerName LIKE 'a__%'| a로 시작하고 최소 3글자 |
| WHERE ContactName LIKE 'a%o' | a로 시작하고 o로 끝남 |

## Demo Database
|CustomerID|CustomerName|ContactName|Address|City|
|-|-|-|-|
|1|Alfreds Futterkiste|Maria Anders|Obere Str. 57|Berlin|


## SQL LIKE Examples
```sql
SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';
```
a로 시작하는 모든 Customers 리턴하기

```sql
SELECT * FROM Customers
WHERE CustomerName LIKE '%a';
```
CustomerName이 a로 끝나는 모든 Customers

```sql
SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';
```
가운데 or 문자가 등장하는 모든 Customers

```sql
SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';
```
두번째 위치가 r인 모든 Customers

```sql
SELECT * FROM Customers
WHERE CustomerName LIKE 'a__%';
a로 시작하고 길이가 3자 이상인 모든 Customers
```

```sql
SELECT * FROM Customers
WHERE ContactName LIKE 'a%o';
```
a로 시작하고 o로 끝나는 모든 Customers

```sql
SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'a%';
```
a로 시작하지 않는 모든 Customers
