from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Create Django Template Variable.

    This function creates and links the template tag from my first_app templates.
    Use the render() function to return the content of the key call in the tag 
    template 'insert_me'
    """
    my_dict = {'insert_me': "Hello! I am at first_app/views.py"}
    return render(request, 'first_app/index.html', context=my_dict)
