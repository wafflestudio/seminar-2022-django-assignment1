# SQL CREATE INDEX Statement
## SQL CREATE INDEX Statement
인덱스를 생성하기

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

## CREATE INDEX Example
```sql
CREATE INDEX idx_lastname
ON Persons (LastName);
```

## DROP INDEX Statement
```sql
DROP INDEX index_name ON table_name;
```
