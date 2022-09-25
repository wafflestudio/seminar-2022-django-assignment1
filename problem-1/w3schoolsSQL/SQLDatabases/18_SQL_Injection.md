# SQL Injection
## SQL Injection
데이터베이스에 악성 코드를 배치하여 데이터베이스를 파괴할 수 있는 코드 삽입 기술

## SQL in Web Pages
```sql
txtUserId = getRequestString("UserId");
txtSQL = "SELECT * FROM Users WHERE UserId = " + txtUserId;
```
username, ID 같은 입력을 요청할 때
실행할 SQL문을 삽입한다. 

## SQL Injection Based on 1=1 is Always True
```sql
SELECT UserId, Name, Password FROM Users WHERE UserId = 105 or 1=1;
```
항상 참인 구문이기에 모든 사용자의 이름, 암호에 엑세스할 수 있다. 


## SQL Injection Based on ""="" is Always True
```javascript
uName = getRequestString("username");
uPass = getRequestString("userpassword");

sql = 'SELECT * FROM Users WHERE Name ="' + uName + '" AND Pass ="' + uPass + '"'
```

```sql
SELECT * FROM Users WHERE Name="John Doe" AND Pass = "myPass";
```

## SQL Injection Based on Batched SQL Statements
```sql
SELECT * FROM Users; DROP TABLE Suppliers;
```
