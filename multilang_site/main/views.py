from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db.models import Q

from .models import Article
from openai import OpenAI
import requests
import json

client = OpenAI(
    ## Tested with a real api key, but for lack of resources here's a placeholder ##
    api_key='test',
)

def home(request):
    return render(request, 'main/home.html') ## REDIRECTS THE REQUEST TO THE PAGE ##

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})
    
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'main/article_detail.html', {'article': article})

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')

        ## Obtain the session message history ##
        messages = request.session.get('messages', [])
        messages.append({'role': 'user', 'content': message})

        ## Use the OpenAI API with the updated syntax ##
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-3.5-turbo",
        )

        bot_message = chat_completion.choices[0].message.content
        print(bot_message)
        messages.append({'role': 'bot', 'content': bot_message})

        ## Save the message history in the session ##
        request.session['messages'] = messages

        return JsonResponse({'response': bot_message})
    else:
        ## Load message history ##
        messages = request.session.get('messages', [])
        return render(request, 'main/chatbot.html', {'messages': messages})

def search(request):
    return render(request, 'main/search_form.html')

def search_results(request):
    query = request.GET.get('query', '').strip()

    if query:
        results = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        results = None

    return render(request, 'main/search_results.html', {'results': results, 'query': query})