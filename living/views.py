from django.shortcuts import render


def home(request):
    return render(request, 'living/homepage.html')


def the_messages(request):
    return render (request, 'living/messagepage.html')


def tracks(request):
    return render(request, 'living/trackspage.html')


def ebook(request):
    return render(request, 'living/ebookspage.html')



def series(request):
    return render(request, 'living/seriespage.html')