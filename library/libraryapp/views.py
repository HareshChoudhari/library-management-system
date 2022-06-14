from multiprocessing import context
from django.shortcuts import redirect,render
from libraryapp.models import Book



# Create your views here.

def Add_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        issued_date = request.POST.get('issued_date')
        submitted_date = request.POST.get('submitted_date')

        s1 = Book(name=name, issued_date=issued_date, submitted_date=submitted_date)
        s1.save()

        return redirect('/Display')

    return render(request,'libraryapp/Add.html')

def Display_view(request):

    data =Book.objects.all()

    context ={'data': data}

    return render(request,'libraryapp/Display.html',context)


def Delete_view(request):

    return render(request,'libraryapp/Delete.html')

def Update_view(request,id):
    s1=Book.objects.get(pk=id)

    return render(request,'libraryapp/Update.html',{'s1':s1, })