# SQL BACKUP DATABASE for SQL Server
## The SQL BACKUP DATABASE Statement
SQL 데이터베이스에서 전체 백업을 만드는 명령어

### Syntax
```sql
BACKUP DATABASE databasename
TO DISK = 'filepath';
```

## The SQL BACKUP WITH DIFFERENTIAL Statement
변경된 부분만 백업하는 명령어
```sql
BACKUP DATABASE databasename
TO DISK = 'filepath'
WITH DIFFERENTIAL;
```

## BACKUP DATABASE example
```SQL
BACKUP DATABASE testDB
TO DIST = 'D:\backups\testDB.bak';
```

## BACKUP WITH DIFFERENTIAL Example
```sql
BACKUP DATABASE testDB
TO DIST = 'D:\backups\testDB.bak'
WITH DIFFERENTIAL;
```
