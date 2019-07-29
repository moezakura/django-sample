from datetime import datetime
from datetime import timezone
from datetime import timedelta
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
    text = request.POST['text']
    name = request.POST['name']

    if len(name) == 0:
        error_message = '名前を入力してください'
    elif len(text) == 0:
        error_message = '内容を入力してください'
    elif len(name) > 20:
        error_message = '名前は20文字以内で入力してください'
    elif len(text) > 65535:
        error_message = '内容は65535文字以内で入力してください'

    if error_message == '':
        try:
            current_time = datetime.now()
            post = Post.objects.create(text=text, name=name, post_date=current_time)
            post.save()
            name = ''
            text = ''
        except:
            error_message = '投稿処理に失敗しました'

    template = loader.get_template('myproject/index.html')
    return HttpResponse(template.render({
        'error_message': error_message,
        'posts': getPosts(),
        'name': name,
        'text': text,
    }, request))


def getPosts():
    posts_object = []
    # try:
    last_posts = Post.objects.order_by('-post_date')[:30]
    posts = last_posts.all()
    for post in posts:
        jst = post.post_date.astimezone(timezone(timedelta(hours=+9)))
        obj = {
            'name': post.name,
            'text': post.text,
            'post_date_str': jst.strftime('%H:%M'),
        }
        posts_object.append(obj)
    return posts_object
# except:
#     return {}
