from django.shortcuts import render
from django.http import HttpResponse
from .forms import Employeeform
from django.shortcuts import redirect
from .models import Employee

# Create your views here.
# def home(request):
#     return HttpResponse('hi')


# create view 
def create_employee(request):
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
            print("Employee saved!") 
            return redirect('blog:list')
    else:
        form = Employeeform()

    return render (request, 'blog/create.html', {'form':form})    



#list view
#list view

#list view
def employee_list(request):
    context = Employee.objects.all()
    return render(request, 'blog/list.html', {'Employees':context})



#update view 
def update_employee(request, pk):
    context = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = Employeeform(request.POST, instance=context)
        if form.is_valid():
            form.save()
            return redirect('blog:list')  
    else:
        form = Employeeform(instance=context)
    return render(request, 'blog/update.html', {'form':form})    


def delete_employee(request, pk):
    context = Employee.objects.get(id=pk)

    if request.method == 'POST':
        context.delete()

    return redirect('blog:list')    

