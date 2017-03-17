from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'poll/index.html', context)


def help(request):
    context = {}
    return render(request, 'poll/help.html', context)
