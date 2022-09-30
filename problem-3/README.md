# Medium REST API

- 작성자 : 박용주(2022/9/30)
- 이 문서는 function based view로 구현한 Medium Post CRUD API를 안내합니다. 
  

목차
- [Medium REST API](#medium-rest-api)
  - [개요](#개요)
  - [HTTP Method 요약](#http-method-요약)
  - [GET /v1/posts/](#get-v1posts)
  - [POST /v1/posts/](#post-v1posts)
  - [GET /v1/posts/:id/](#get-v1postsid)
  - [PUT /v1/posts/:id/](#put-v1postsid)
  - [PATCH /v1/posts/:id/](#patch-v1postsid)
  - [DELETE /v1/posts/:id/](#delete-v1postsid)
- [더보기](#더보기)
    - [셀프 후기](#셀프-후기)
    - [개발 환경](#개발-환경)

<br></br>

## 개요

views.py 함수를 제외한 모든 부분은 [problem-2](/problem-2)와 동일합니다. 


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
``` python
def blog_list(request):
    if request.method == 'GET': 
        post = Post.objects.all()
        data = serializers.serialize('json', post)
        return JsonResponse(data, status=200, safe=False)
    ...
```
현재 존재하는 모든 posts를 리턴합니다. 

<br></br>

## POST /v1/posts/
``` Bash
POST /v1/posts/
```
``` python
def blog_list(request):
    if request.method == 'GET': 
        ...
    if request.method == 'POST': 
        data = loads(request.body)
        post = Post.objects.create(
            date=timezone.now(),
            title=data['title'],  
            link=data['link'],
            description=data['description'],
            tags=data['tags'],
            author_email=data['author_email'],
            content_format=data['content_format'],
            content=data['content'],
            canonical_url=data['canonical_url'],
            public_status=data['public_status'],
            notify_followers=data['notify_followers']

        )
        post.save()
        return HttpResponse(status=201)
```
새로운 Post 객체를 생성합니다. 

<br></br>

## GET /v1/posts/:id/
``` Bash
GET /v1/posts/:id/
```
```python

def blog_detail(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        print(post)
        print(type(post))
        post_json = dict()
        post_json['title'] = post.title
        post_json['link'] = post.link
        post_json['description'] = post.description
        post_json['tags'] = post.tags
        post_json['author_email'] = post.author_email
        post_json['content_format'] = post.content_format
        post_json['content'] = post.content
        post_json['canonical_url'] = post.canonical_url
        post_json['public_status'] = post.public_status
        post_json['notify_followers'] = post.notify_followers
        return JsonResponse(post_json, status=200, safe=False)

```
하나의 Post를 id로 불러옵니다. 
<br></br>

## PUT /v1/posts/:id/
``` Bash
PUT /v1/posts/:id/
```
```python
def blog_detail(request, pk):
    if request.method == 'PUT':  # 작동함
        post = get_object_or_404(Post, pk=pk)
        data = loads(request.body)
        post.title = data['title']
        post.link = data['link']
        post.description = data['description']
        post.tags = data['tags']
        post.author_email = data['author_email']
        post.content_format = data['content_format']
        post.content = data['content']
        post.canonical_url = data['canonical_url']
        post.public_status = data['public_status']
        post.notify_followers = data['notify_followers']
        post.save()

        return HttpResponse(status=200)
```
id번째 POST를 완전히 새롭게 바꿉니다. 
<br></br>

## PATCH /v1/posts/:id/
``` Bash
PATCH /v1/posts/:id/
```
``` python
def blog_detail(request, pk):
    if request.method == 'PATCH':
        post = get_object_or_404(Post, pk=pk)
        data = request.body
        my_data = data.decode('utf8').replace("'", '"')
        my_data = loads(my_data)

        if 'title' in my_data:
            post.title = my_data['title']
        if 'link' in my_data:
            post.link = my_data['link']
        if 'description' in my_data:
            post.description = my_data['description']
        if 'tags' in my_data:
            post.tags = my_data['tags']
        if 'author_email' in my_data:
            post.author_email = my_data['author_email']
        if 'content_format' in my_data:
            post.content_format = my_data['content_format']
        if 'content' in my_data:
            post.content = my_data['content']
        if 'canonical_url' in my_data:
            post.canonical_url = my_data['canonical_url']
        if 'public_status' in my_data:
            post.public_status = my_data['public_status']
        if 'notify_followers' in my_data:
            post.notify_followers = my_data['notify_followers']
        post.save()

        return HttpResponse(status=200)
```
POST를 부분적으로 수정합니다. 
<br></br>

## DELETE /v1/posts/:id/
``` Bash
DELETE /v1/posts/:id/
```
```python
def blog_detail(request, pk):
    if request.method == 'DELETE':  # 작동함
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return HttpResponse(status=200)

```
Post 객체를 삭제합니다. 
<br></br>

# 더보기
### 셀프 후기
- 에러 처리에 어떤 케이스가 있는지 잘 모르겠다. 
- djangorestframework에서 주어지는 모듈 커스터마이즈해서 쓰는 것 더 공부하기

### 개발 환경
- environment : Windows WSL2 Ubuntu
- python pip list : [requirement.txt](/problem-1/requirements.txt)

