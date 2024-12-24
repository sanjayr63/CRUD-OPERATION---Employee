from django.shortcuts import render, redirect
from .models import Field

# Create your views here.
def home(request):
   mydata = Field.objects.all()
   if(mydata!=''):
       return render(request,'home.html',{'Field':mydata})
   else:
       return render(request,'home.html')
       
   

def addData(request):
     if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        department=request.POST['department']
        date_of_joining=request.POST['date_of_joining']

        obj=Field()
        obj.Name=name
        obj.Email=email
        obj.Department=department
        obj.Date_of_joining=date_of_joining
        obj.save()
        mydata=Field.objects.all()
        return redirect('home')
     return render(request,'home.html')

def updatedata(request,id):
    mydata = Field.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        department=request.POST['department']
        date_of_joining=request.POST['date_of_joining']

        mydata.Name = name
        mydata.Email = email
        mydata.Department = department
        mydata.Date_of_joining = date_of_joining
        mydata.save()
        return redirect('home')

    return render(request,'update.html',{'fields': mydata})



def deletedata(request, id): 
    # Fetch the object with the given id
    mydata = Field.objects.get(id=id)
    
    # Delete the object
    mydata.delete()
    
    # Redirect to the home page or wherever you want after deletion
    return redirect('home')
