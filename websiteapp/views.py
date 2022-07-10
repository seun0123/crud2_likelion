from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from django.utils import timezone
from .models import Blog

# Create your views here.
def main(request):
    return render(request, 'main.html')

def write(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = BlogForm
        return render(request, 'write.html', {'form':form})

def read(request):
    blogs = Blog.objects
    return render(request, 'read.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'read.html', {'blog': blog})

def edit(request, id):
    edit_post = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'edit_post': edit_post})

def update(request, id):
    update_post = Blog.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.pub_date = timezone.now()
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('detail', id)

def delete(request,id):
    delete_post = Blog.objects.get(id=id)
    delete_post.delete()
    return redirect('read')