# Medium REST API

- 작성자 : 박용주(2022/9/28)
- 이 문서는 REST API를 이용한 Medium Post CRUD API를 안내합니다. 
  

목차
- [Medium REST API](#medium-rest-api)
- [개요](#개요)
  - [Post 모델 개요](#post-모델-개요)
  - [HTTP Method 요약](#http-method-요약)
  - [GET /v1/posts/](#get-v1posts)
  - [POST /v1/posts/](#post-v1posts)
  - [GET /v1/posts/:id/](#get-v1postsid)
  - [PUT /v1/posts/:id/](#put-v1postsid)
  - [PATCH /v1/posts/:id/](#patch-v1postsid)
  - [DELETE /v1/posts/:id/](#delete-v1postsid)
- [더보기](#더보기)
    - [개발 환경](#개발-환경)

<br></br>

# 개요

![API 개요](https://user-images.githubusercontent.com/81140673/192932855-69ee05ad-3eb6-4515-8558-d694d29a756d.png)


Medium Blog와 Medium 공식 API를 참고하여 개발한 Medium Post API입니다. 
 
<br></br>
 
 
 
## Post 모델 개요

Post Model은 Medium 공식 API를 참고하여 11개의 필드로 구성하였습니다. 

|Field 이름|Field 타입|Field 기능|
|-|-|-|
|title|CharField|Post의 제목|
|date|DateTimeField|Post가 발생된 날짜, 시간|
|link|URLField|Post가 발행되는 url|
|description|TextField|Post의 부제목|
|tags|JSONField|Post의 내용을 나타내는 태크|
|author_email|EmailField|Post를 발행한 저자의 이메일|
|content_format|CharField|Post가 markdown인지 html인지 나타냄|
|canonical_url|URLField|검색 엔진에 올리기 위한 공식 URL|
|public_status|CharField|Post를 public, private 중 어떻게 올릴 것인지|
|notify_followers|BooleanField|Post author를 팔로우하는 유저에게 알림을 울릴 것인지|



<br></br>


## HTTP Method 요약
```
GET /v1/posts/ list posts
POST /v1/posts/ create a post

GET /v1/posts/:id detail a post
POST /v1/posts/:id update a post
PATCH /v1/posts/:id partial update a post
DELETE /v1/posts/:id delete a post
```
<br></br>

## GET /v1/posts/
``` Bash
GET /v1/posts/
```
현재 존재하는 모든 posts를 리턴합니다. 

<br></br>

## POST /v1/posts/
``` Bash
POST /v1/posts/
```
새로운 Post 객체를 생성합니다. 

<br></br>

## GET /v1/posts/:id/
``` Bash
GET /v1/posts/:id/
```
하나의 Post를 id로 불러옵니다. 
<br></br>

## PUT /v1/posts/:id/
``` Bash
PUT /v1/posts/:id/
```
id번째 POST를 완전히 새롭게 바꿉니다. 
<br></br>

## PATCH /v1/posts/:id/
``` Bash
PATCH /v1/posts/:id/
```
POST를 부분적으로 수정합니다. 
<br></br>

## DELETE /v1/posts/:id/
``` Bash
DELETE /v1/posts/:id/
```
Post 객체를 삭제합니다. 
<br></br>

# 더보기
### 개발 환경
- environment : Windows WSL2 Ubuntu
- python pip list : [requirement.txt](/problem-1/requirements.txt)

