# SQL Joins
## SQL JOIN
두 개 이상의 테이블을 연결하는 데 사용되는 명령어

```sql
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate 
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
```

Orders 테이블의 CustomerID와 Customers 테이블의 CustomerID를 일치시켜 INNER JOIN하고 있다. 
이때 그 중에 Orders 테이블의 OrderID, Customer 테이블의 CustomerName, Orders 테이블의 OrderDate 칼럼을 반환한다. 


## Different Types of SQL JOINs
![1517283484](https://user-images.githubusercontent.com/81140673/191939356-6dc5ef7f-9062-45ee-a3d0-4a141557591c.png)
[이미지 출처](https://yenaworldblog.wordpress.com/2018/01/30/sql-join-%ec%a2%85%eb%a5%98-%eb%b0%8f-%ec%82%ac%ec%9a%a9%eb%b2%95/)

- INNER JOIN : 교집합
- OUTER JOIN 
  - LEFT JOIN : 왼쪽 테이블 + 오른쪽에서 일치하는 레코드
  - RIGHT JOIN : 오른쪽 테이블 + 왼쪽에서 일치하는 레코드
  - FULL JOIN : 합집합


