# SQL DEFAULT Constraint
## SQL DEFAULT Constraint
column 값의 디폴트 값을 설정한다. 

## SQL DEFAULT on CREATE TABLE
```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int, 
    City varchar(255) DEFAULT 'Sandnes'
);
```

## SQL DEFAULT on ALTER TABLE
```sql
ALTER TABLE Persons
ALTER City SET DEFAULT 'Sandnes';
```

## DROP a DEFAULT Constraint
```sql
ALTER TABLE Persons
ALTER City DROP DEFAULT;
```
