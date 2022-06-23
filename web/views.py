from django.shortcuts import render
from django.http import HttpResponse

from web.forms import CommentForm
from web.models import Card, Comment


def index(request):
    cards = Card.objects.all()
    return render(request, 'index.html', {'cards': cards})



def detail(request, pk):
    card = Card.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                body=form.cleaned_data['body'],
                card=card
            )
            comment.save()
    comments = Comment.objects.filter(card_id=pk)
    context = {
        "card": card,
        "comments": comments,
        "form": form
    }
    return render(request, "detail.html", context)
