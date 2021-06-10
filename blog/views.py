from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def post_new(request):
    if request.method == "POST":
        # Templateでrequest送信click -> 'POST'が追加される
        form = PostForm(request.POST)
        # 'blank=true' -> フォーム空欄でstart
        if form.is_valid():
            # commit=False: Dont commit to change in db.
            # commit=False: Modelオブジェクト取得。追加データを、追加保存する為に必要
            # No variable type required during declaretion.
            # post.strip(): Care of type
            post = form.save(commit=False)
            print(type(post))

            # Add  other field.
            post.author = request.user
            post.published_date = timezone.now()
            # Only data saving.
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})