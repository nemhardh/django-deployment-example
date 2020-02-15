from django.shortcuts import render
from first_app.models import User


# Create your views here.

def index(request):
    web_list = User.objects.order_by('first_Name')
    list_dict = { "user_records": web_list}
    return render(request, 'first_app/index.html',list_dict)
