# SQL Self Join
## SQL Self Join
같은 테이블에서 Join을 하는 케이스
alias를 만들어서 동일한 테이블을 다른 테이블인 것처럼 작업한다. 

```sql
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```

## SQL Self Join Example
```sql
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.customerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;
```
아항!
Customers 테이블에서 CustomerID가 같지 않으면서, City는 같은
Customer Name을 리턴하기 (단, A.City를 기준으로 정렬)

## Self Join이 필요한 이유
- 같은 값을 공유하는 instance를 찾고 싶을 때
- 같은 값을 공유하면서 관계가 있는 instance를 보고 싶을 때
- instance 간의 간접 연결을 확인하고 싶을 때
  
[셀프 조인 사용하는 이유](https://minor-research.tistory.com/24)