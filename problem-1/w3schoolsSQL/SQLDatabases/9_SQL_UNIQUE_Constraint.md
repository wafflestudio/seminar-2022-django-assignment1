# SQL UNIQUE Constraint
## SQL UNIQUE Constraint
열의 모든 값이 다르도록

## SQL UNIQUE Constraint on CREATE TABLE
```sql
CREATE TABLE Persons (
    ID int NOT NULL UNIQUE, 
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);
```

## SQL UNIQUE Constraint on ALTER TABLE
```sql
ALTER TABLE Persons
ADD UNIQUE (ID);
```

## DROP a UNIQUE Constraint
```sql
ALTER TABLE Persons
DROP CONSTRAINT UC_Persons;
```
