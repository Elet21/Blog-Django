from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View
from django.core.paginator import Paginator

from .forms import PostForm, TagForm
from .utils import *
from .models import Post,Tag
from .forms import TagForm, PostForm

#Выодит список постов
def post_list(requests):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)

    page_number = requests.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(requests, 'blog/post_list.html', context=context)

class PostUpdate(ObjectsUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'



class PostCreate(ObjectsCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostDelete(ObjectDeleteMixin,View):
    model = Post
    template = 'blog/post_delete.html'
    url = 'posts_list_url'


class TagUpdate(ObjectsUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'


class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectsCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    url = 'tag_list_url'


def tag_list(requests):
    tags = Tag.objects.all()
    return render(requests, 'blog/tag_list.html', context={'tags':tags})
