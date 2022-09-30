# SQL CHECK Constraint
## SQL CHECK Constraint
값의 범위를 제한하는 Constraint

## SQL CHECK on CREATE TABLE
```sql
CREATE TABLE Persons (
    ID int NOT NULL.
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int, 
    CHECK (Age >= 18)
);
```

## SQL CHECK on ALTER TABLE
```sql
ALTER TABLE Persons
ADD CHECK (Age >= 18);
```

## DROP a CHECK Constraint
```sql
ALTER TABLE Persons
DROP CONSTRAINT CHK_PersonAge;
```
