# SQL ALTER TABLE Statement
## SQL ALTER TABLE Statement
기존 테이블의 구조를 변경할 때 사용하는 명령어
ALTER - ADD, DROP, ALTER, MODIFY로 세분화된다. 

## ALTER TABLE - ADD COLUMN
```sql
ALTER TABLE table_name
ADD column_name datatype;
```

```sql
ALTER TABLE Customers
ADD Email varchar(255);
```

## ALTER TABLE - DROP COLUMN
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

```sql
ALTER TABLE Customers
DROP COLUMN Email;
```

## ALTER TABLE - ALTER/MODIFY COLUMN
```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype;
```

## SQL ALTER TABLE Example
```sql
ALTER TABLE Persons
ADD DateOfBirth date;
```

## Change Data Type Example
```sql
ALTER TABLE Persons
ALTER COLUMN dateOfBirth year;
```

## DROP COLUMN Example
```sql
ALTER TABLE Persons
DROP COLUMN DateOfBirth;
```
