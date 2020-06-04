import random
from django.conf import settings

from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url

from .forms import TweetForm
from .models import Tweets

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World!!</h1>")
    print(request.user)
    return render(request, "pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    #print("ajax", request.is_ajax() )
    form = TweetForm(request.POST or None)
    next_url= request.POST.get("next") or None

    if form.is_valid():
        obj = form.save(commit=False)
        #do other form related logic 
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201) #201-> created items
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/forms.html', context={"form":form})


def tweet_list_view(request, *args, **kwargs):
    qs= Tweets.objects.all()
    tweets_list= [x.serialize() for x in qs]
    data={
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data={
        "id": tweet_id,
    }
    status = 200
    try:
        obj= Tweets.objects.get(id=tweet_id) 
        data['content'] = obj.content
    except:
        data['content'] = "not found"
        status=404

    
    return JsonResponse(data,status=status)