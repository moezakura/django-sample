from datetime import datetime
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.template import loader

from myproject.models import Post


def index(request: WSGIRequest):
    template = loader.get_template('myproject/index.html')
    return HttpResponse(template.render({
        'posts': getPosts(),
    }, request))


def post(request: WSGIRequest):
    if request.method != 'POST':
        return HttpResponse("not allow method", status=405)

    error_message = ''
    try:
        text = request.POST['text']
        name = request.POST['name']
        post = Post.objects.create(text=text, name=name, post_date=datetime.now())
        post.save()
    except:
        error_message = '投稿処理に失敗しました'

    template = loader.get_template('myproject/index.html')
    return HttpResponse(template.render({
        'error_message': error_message,
        'posts': getPosts(),
    }, request))


def getPosts():
    try:
        last_posts = Post.objects.order_by('-post_date')[:30]
        posts = last_posts.all()
        return posts
    except:
        return {}
