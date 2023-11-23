from django.shortcuts import render

# Create your views here.
def online_form(request):
    return render(request,'online_form.html')