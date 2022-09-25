# SQL AUTO INCREMENT Field
## AUTO INCREMENT Field
새로운 record에 대해 unique numer를 부여하는 field

## Syntax for SQL SERVER
```sql
CREATE TABLE Persons (
    Personid int IDENTITY(1, 1) PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);
```
```sql
INSERT INTO Persons (FirstName, LastName)
VALUES ('Lars', 'Monsen');
```