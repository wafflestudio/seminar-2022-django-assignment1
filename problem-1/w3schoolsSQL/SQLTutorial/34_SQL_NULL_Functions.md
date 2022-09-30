# SQL NULL Functions
## SQL IFNULL(), ISNULL(), COALESCE(), NVL() Functions
null 값을 허용하고 싶을 때

- MySQL
  - IFNULL() 이용
```sql
SELECT ProductName, UnitPrice * (UnitsInStock + IFNULL(UnitsOnOrder, 0))
FROM Products;
```

- SQL server
    - ISNULL()

```sql
SELECT ProductName, UnitPrice * (UnitsInSTock + ISNULL(UnitsOnOrder, 0))
FROM Products;
```

- MS 엑세스
  - IsNULL()


- Oracle
  - NVL()