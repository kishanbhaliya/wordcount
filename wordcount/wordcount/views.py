from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    print(word_list)
    list_length = len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            #increase value by 1
            worddictionary[word] += 1
        else:
            #add to the worddictionary and set Value to 1
            worddictionary[word] = 1
    return render(request, 'count.html', {'fulltext': data, 'words_length': list_length, 'word_dict': worddictionary})
