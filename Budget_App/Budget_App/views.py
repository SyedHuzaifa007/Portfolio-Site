# I have created this file ---> 007
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Hello World!</h1>''')