# SQL FOREIGN KEY Constraint
## SQL FOREIGN KEY Constraint
Foreign key - 테이블 간의 관계를 생성한다. 

child table - foreign key 있는 테이블
parent table - primary key 있는 테이블

## SQL FOREIGN KEY on CREATE TABLE
```sql
CREATE TABLE Orders (
    OrderID int NOT NULL, 
    OrderNumber int NOT NULL, 
    PersonID int, 
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
```

## SQL FOREIGN KEY on ALTER TABLE
```sql
ALTER TABLE Orders
ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);
```

## DROP a FOREIGN KEY Constraint
```sql
ALTER TABLE Orders
DROP FOREIGN KEY FK_PersonOrder;
```
