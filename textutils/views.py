# I have created this file - Krishna
from copyreg import remove_extension
from itertools import count
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!@#$%^&*():;,'[""]{}-~<>\/?.'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzing = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == "" and djtext[index+1] == ""):
                analyzing = analyzing + char
        params = {'purpose': 'Removed Extra space',
                  'analyzing_text': analyzing}
        djtext = analyzing

    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)
