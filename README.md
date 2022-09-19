# Assignment 1

제출기한: 22.10.02(일) 23:59:59


## problem 1
[w3schools sql tutorial](https://www.w3schools.com/sql/default.asp)을 완료해보자.

### 제출
SQL Home ~ SQL Data Types 까지 진행하고 인증 스크린샷을 problem1에 업로드해주세요.


## problem 2

당신은 medium.com의 서버 개발자가 되어, 블로그 포스트를 모델링하고 이를 crud하는 API를 맡게 되었다.

![미디엄 스크린샷](./%EB%AF%B8%EB%94%94%EC%97%84%20%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7.png)

[medium post detail page](https://mondaynote.com/apples-next-big-thing-a-business-model-change-e9b0145500c9)를 참고하여, 하단 API를 만든다.


```
GET /v1/posts/ list posts
POST /v1/posts/ create a post

GET /v1/posts/:id detail a post
POST /v1/posts/:id update a post
PATCH /v1/posts/:id partial update a post
DELETE /v1/posts/:id delete a post
```


### 제약사항

- 모델링하고, 이를 viewset에 적용하는 일 외 다른 수정사항은 최소화하여 진행한다.
  - authentication, pagination 등은 하지 않는다.
- 하나의 모델 내에서만 모델링을 진행한다. 
  - Foreign Key는 사용하지 마세요.
- 다음 필드들은 꼭 한 번씩 사용해야한다.
  - `CharField, DateTimeField, EmailField, TextField`
  - 힌트: [Django model fields](https://docs.djangoproject.com/en/4.1/ref/models/fields/) 문서를 참고하면서 모델링해보세요.

### 제출

problem2 폴더에 장고 프로젝트를 업로드해주세요.


## problem 3

problem 2에서 작성한 API를 function based view로 같은 동작을 하도록 작성해보자.

힌트: Go To Implementation(command + click)을 적극 활용하여 django 내부 코드를 파악해보세요.

```
GET /v2/posts/ list posts
POST /v2/posts/ create a post

GET /v2/posts/:id detail a post
POST /v2/posts/:id update a post
PATCH /v2/posts/:id partial update a post
DELETE /v2/posts/:id delete a post
```

### 제출

problem2에 업로드된 장고 프로젝트에 해당 뷰를 추가해주세요.