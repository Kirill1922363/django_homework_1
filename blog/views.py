from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request: HttpRequest):

    context = {
        "blog_name": "Tech Blog",
        "description": "A blog about the latest in technology."
    }

    return render(request, "blog/home.html", context)


def all_posts(request: HttpRequest) -> HttpResponse:

    posts = [
        {"title": "First Post", "content": "This is the content of the first post."},
        {"title": "Second Post", "content": "This is the content of the second post."},
        {"title": "Third Post", "content": "This is the content of the third post."}
       ]

    context = {
        "blog_name": "Tech Blog",
        "count_posts": len(posts),
        "posts": posts
    }

    # This view will eventually list all blog posts
    return render(request, "blog/all_posts.html", context)



def weather(request: HttpRequest):
    context = {
        'city': 'Київ',
        'temperature': 18,
        'humidity': 65,
        'conditions': ['Сонячно', 'Вітряно'],
        'forecast': [
            {'day': 'Завтра', 'temp': 20},
            {'day': 'Післязавтра', 'temp': 15},
            {'day': 'Четвер', 'temp': 22}
        ]
    }

    return render(request, "blog/weather.html", context)

def contact(request: HttpRequest):
    context = {
        'email': 'contact@example.com',
        'phone': '+1234567890',
        'address': '123 Tech Street, Innovation City'
    }

    return render(request, "blog/contact.html", context)