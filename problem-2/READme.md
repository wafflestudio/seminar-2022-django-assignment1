
## problem 2

당신은 medium.com의 서버 개발자가 되어, 블로그 포스트를 모델링하고 이를 crud하는 API를 맡게 되었다.

https://github.com/Medium/medium-api-docs#3-resources
medium-api 이용해서 구현하기


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
  - Foreign Key는 사용하지 않는다.
- 힌트: [Django model fields](https://docs.djangoproject.com/en/4.1/ref/models/fields/) 문서를 참고하면서 모델링해보세요.

### 제출

problem-2 폴더에 장고 프로젝트를 업로드해주세요.

[medium-post-api-example](https://github.com/david-fernando/medium-posts-api)

궁금한 것
rest_framework.generic
rest_framework.serializer
rest_framework.queryset
rest_framework.serializer_class
