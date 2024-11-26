from django.shortcuts import render
from django.utils import timezone
from .models import Comment
from .forms import CommentForm

# Create your views here.
def home(request):
    return render(request, 'main/home1.html')


def extra(request):
    return render(request, 'main/extra.html')


def essays(request):
    return render(request, 'main/essays_home.html')


def show_essay(request, chapter, subtopic):
    comment_list = Comment.objects.filter(unit=subtopic).order_by('-date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.unit = subtopic
            comment.date = timezone.now().date()
            comment.save()

    else:
        form = CommentForm()

    return render(request, 'main/essays/' + chapter + '/' + subtopic + '.html', {'chapter': chapter, 'subtopic': subtopic, 'form': form, 'comment_list': comment_list})