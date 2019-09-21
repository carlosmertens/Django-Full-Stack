from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.


def index(request):
    """Create Django Template Variable.

    This function creates and links the template tag from my first_app templates.
    Use the render() function to return the content of the key call in the tag 
    template 'insert_me'
    """
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)
