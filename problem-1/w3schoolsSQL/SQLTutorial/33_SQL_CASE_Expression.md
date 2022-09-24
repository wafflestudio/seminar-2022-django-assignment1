# SQL CASE Expression
## The SQL CASE Expression
C언어의 case와 동일한 기능

### CASE Syntax
```sql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```

## SQL CASE Examples
```sql
SELECT OrderID, Quantity, 
CASE
    WHEN Quantity > 30 THEN 'The qunatity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;
```

```sql
SELECT CustomerName, City, Country
FROM Customers
ORDER BY (
    CASE 
        WHEN City IS NULL THEN Country
        ELSE City
    END
);
```