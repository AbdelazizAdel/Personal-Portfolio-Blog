from django.shortcuts import render
from . import models, forms
# Create your views here.
def blog_index_view(request):
    posts = models.Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)

def blog_category_view(request, category):
    posts = models.Post.objects.filter(categories__name__contains=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog_category.html', context)

def blog_details_view(request, id):
    post = models.Post.objects.get(id=id)
    comments = models.Comment.objects.filter(post_id=id)
    form = forms.CommentForm()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comment(**form.cleaned_data, post= post)
            comment.save()
            form = forms.CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog_details.html', context)