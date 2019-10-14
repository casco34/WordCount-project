from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html') # if someone wants to view the homepage, and instead of viewing this http HttpResponse, lets give them the home.html
#def home(request):  #above we add the request object, and pass in the name of the HTML file we want people to see                                             # so we  import shortcuts from django importing render.
    #return HttpResponse('hello world') #we cant just send a string request, so it has to be using an http HttpResponse
def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1

        else:
            #add to the disctionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key= operator.itemgetter(1), reverse=True)



    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedwords': sortedwords})
