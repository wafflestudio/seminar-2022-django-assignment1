<!-- TODO -->
# catfact REST API

- 작성자 : 박용주(2022/9/11)
- 이 문서는 REST API를 이용한 catfact CRUD API를 안내합니다. 
  

목차
- [catfact REST API](#catfact-rest-api)
- [개요](#개요)
    - [Access Control / HTTP Method 요약](#access-control--http-method-요약)
- [인증 Authentication](#인증-authentication)
    - [유저 생성하기](#유저-생성하기)
    - [로그인하기](#로그인하기)
- [catfact](#catfact)
  - [catfact/](#catfact-1)
    - [GET](#get)
    - [POST](#post)
  - [catfact/<int:pk>](#catfactintpk)
    - [GET](#get-1)
    - [PUT](#put)
    - [DELETE](#delete)
- [더보기](#더보기)
    - [개발 환경](#개발-환경)
    - [참고자료](#참고자료)

  
# 개요
![장고as0-최종](https://user-images.githubusercontent.com/81140673/190882388-f290c860-d240-47af-bfa1-589ebe9b1694.png)


- catfact API
- CRUD
  - Django REST Framework로 개발한 catfact API로 catfact를 등록, 수정, 삭제할 수 있습니다. 
- 엑세스 컨트롤
  - catfact API는 user 생성, login API으로 authentication 기능을 구현하였습니다. 

### Access Control / HTTP Method 요약

- Access Control을 위한 API
  - POST catfact/users/  
  - POST catfact/login/  

  
    

- URI : catfact/  

||Authentication 유무|
|---|---|
|GET|X|
|POST|O|



- URI : catfact/<int:pk>/

||Authentication 유무|
|---|---|
|GET|X|
|PUT|O|
|DELETE|O|



# 인증 Authentication
### 유저 생성하기
``` Bash
POST catfact/user/
```
``` JSON
{
  "username": {user_name},
  "email":{user_email},
  "password":{user_password}
} 
```
username, email, password 필드로 유저를 생성합니다.   

- Status Code
  - 201 Created
  - 400 Bad Request


### 로그인하기
``` Bash
POST catfact/login/
```
```JSON
{
  "username":{user_name},
  "password":{user_password}
}
```
username, password 필드로 로그인합니다. 
- Status Code
  - 200 OK
  - 400 Bad Request


# catfact
## catfact/
### GET
``` Bash
GET catfact/
```
등록된 catfact 리스트를 20개까지 리턴합니다. 
- Status Code
  - 200 OK
  - 400 Bad Request

### POST
``` Bash
POST catfact/
```
```JSON
{
		"fact": {catfact.fact},
		"length": {catfact.length}
}
```
``` Bash
  HTTP Header
  
  - header : Authorization
  - value : Token {Token.value}
```
catfact/ Update에는 로그인이 요구됩니다. 
로그인할 때 발급된 토큰을 HTTP 헤더에 포함시켜 HTTP Request를 보냅니다. 

- Status Code
  - 201 Created
  - 400 Bad Request
  - 401 Unauthorized
  - 403 Forbidden


## catfact/<int:pk>
### GET
``` Bash
GET catfact/<int:pk>/
```
pk번째 catfact를 리턴합니다.  

- Status Code
  - 200 OK
  - 400 Bad Request
  - 404 Not Found



### PUT
``` Bash
PUT catfact/<int:pk>/
```
```JSON
{
		"fact": {catfact.fact},
		"length": {catfact.length}
}
```
catfact/<int:pk>/의 값을 수정합니다. 
로그인이 요구되므로 로그인에서 발행된 토큰을 HTTP 헤더에 포함시킵니다. 

- Status Code
  - 200 OK
  - 400 Bad Request
  - 401 Unauthorized



### DELETE
``` Bash
DELETE catfact/<int:pk>/
```
- Status Code
  - 200 OK
  - 400 Bad Request
  - 401 Unauthorized

catfact/<int:pk>/를 삭제합니다. 

# 더보기
### 개발 환경
- environment : Windows WSL2 Ubuntu
- python pip list : [requirement.txt](/problem-1/requirements.txt)
  
### 참고자료
[구글 개발자 가이드](https://developers.google.com/docs/api/reference/rest)  
[카카오 개발자 가이드](
https://developers.kakao.com/docs/latest/ko/kakaotalk-social/rest-api)  
[위키독스 장고 프로젝트](https://wikidocs.net/110807)  
[DRF 장고 튜토리얼](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)
[stackoverflow DRF User 이용법](https://stackoverflow.com/questions/28086890/django-rest-framework-drf-set-current-user-id-as-field-value)