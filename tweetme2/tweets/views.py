import random
from django.http import Http404, JsonResponse
from django.shortcuts import render

from .forms import TweetForm
from .models import Tweet


# urls('')
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

# urls('create-tweet')
def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save ()
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})

# urls('tweet/')
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 100)} for x in qs]
    data = {
        "is_user": False,
        "response": tweets_list
    }
    return JsonResponse(data)

# urls('tweet/<int:tweet_id>')
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404       
    return JsonResponse(data, status= status)
