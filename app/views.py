from django.shortcuts import render
from app.models import *

# Create your views here.
def online_form(request):
    if request.method == 'POST':
        First = request.POST['First']
        Middle = request.POST['Middle']
        Father = request.POST['Father']
        Mother = request.POST["Mother"]
        Current = request.POST['Current']
        Permanent = request.POST["Permanent"]
        Phone = request.POST["Phone"]
        Landline = request.POST['Landline']
        DOB = request.POST['DOB']
        POB = request.POST["POB"]
        OFO = Information.objects.get_or_create(First_Name= First, Middle_Name = Middle, Father_Name= Father, Mother_Name = Mother, Current_Address = Current, Permanent = Permanent, Phone_number = Phone, Land_line = Landline, Date_of_Birth= DOB,  Place_of_Birth = POB )[0]
        OFO.save()
        OFo = Information.objects.all()
        data = {'onlineForm' : OFo}
        return render(request, 'display.html', data)

    return render(request,'online_form.html')