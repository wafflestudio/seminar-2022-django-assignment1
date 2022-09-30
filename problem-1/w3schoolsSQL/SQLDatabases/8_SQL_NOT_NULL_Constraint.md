# SQL NOT NULL Constraint
## SQL NOT NULL Constraint
디폴트 설정으로는 열이 null value가 될 수 있다
NOT NULL은 null 값을 허용하지 않도록 하는 것이다. 

## SQL NOT NULL on CREATE TABLE
```sql
CREATE TABLE Persons (
    ID int NOT NULL, 
    LastName varchar(255) NOT NULL, 
    FirstName varchar(255) NOT NULL, 
    Age int
);
```

## SQL NOT NULL on ALTER TABLE
```sql
ALTER TABLE Persons
ALTER COLUMN Age int NOT NULL;
```
