# SQL PRIMARY KEY Constraint
## SQL PRIMARY KEY Constraint
레코드를 식별하는 역할을 하는 column을 정하는 명령어

## SQL PRIMARY KEY on CREATE TABLE
```sql
CREATE TABLE Persons (
    ID int NOT NULL PRIMARY KEY, 
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);
```

## SQL PRIMARY KEY on ALTER TABLE
```sql
ALTER TABLE Persons
ADD PRIMARY KEY (ID);
```

## DROP a PRIMARY KEY Constraint
```sql
ALTER TABLE Persons
DROP PRIMARY KEY;
```