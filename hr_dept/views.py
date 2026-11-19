from django.shortcuts import render,redirect
from hr_dept.forms import employee_form
# Create your views here.

def new_employee(request):
    form =employee_form()
    if request.method=='POST':
        form=employee_form(request.POST)
        if form.is_Valid():
            form.save()
            return redirect('home')
    return render(request,"hr_temp/emp_form.html",


    {'form':form})


















