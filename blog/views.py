from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Virat Kohli",
        "title": "Centuries",
        "content": "I have made 71 centuries",
        "date_posted": "19th Dec, 2023",
    },
    {
        "author": "Ravichandran Ashwin",
        "title": "Wickets",
        "content": "I have taken 500 wickets",
        "date_posted": "20th Dec, 2023",
    },
]


# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About Page"})
