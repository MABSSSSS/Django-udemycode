from django.shortcuts import get_object_or_404, redirect, render
from PayRollApp.forms import EmployeeForm
from PayRollApp.models import Employee
# Create your views here.

def EmployeesList(request):
    # Employees =Employee.objects.all()
    Employees = Employee.objects.select_related('EmpDepartment','EmpCountry').all()
    print(Employees.query)
    
    TemplateFile = "PayRollApp/EmployeesList.html"
    Dict={"Employees":Employees}
    return render(request, TemplateFile,Dict)
    
    

def EmployeeDetails(request, id):
    TemplateFile = "PayRollApp/EmployeeDetails.html"
    
    # Use get_object_or_404 to handle the case when the Employee does not exist
    # employee = get_object_or_404(Employee, id=id)
    employee= Employee.objects.select_related('EmpDepartment','EmpCountry').all().filter(id =id)

    # Pass the employee object to the template as context
    context = {"Employee": employee[0]}
    
    return render(request, TemplateFile, context)


def EmployeeDelete(request, id):
    TemplateFile = "PayRollApp/EmployeeDelete.html"
    
    # Use get_object_or_404 to handle the case when the Employee does not exist
    # employee = get_object_or_404(Employee, id=id)
    
    # Pass the employee object to the template as context
    employee= Employee.objects.select_related('EmpDepartment','EmpCountry').all().filter(id =id)
    context = {"Employee": employee[0]}
    
    if request.method == "POST":
        employee.delete()
        return redirect('EmployeesList')
    
    return render(request, TemplateFile, context)


def EmployeeUpdate(request,id):
    TemplateFile="PayRollApp/EmployeeUpdate.html"
    # employee = Employee.objects.get(id=id)
    employee= Employee.objects.select_related('EmpDepartment','EmpCountry').all().filter(id =id)

    for emp in employee:
    # form = EmployeeForm(instance=employee)
       form = EmployeeForm(instance=emp)
       Dict={"form":form}
    
    if request.method=="POST":
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
           form.save() 
        return redirect("EmployeesList")
    
    return render(request,TemplateFile,Dict)

def EmployeeInsert(request):
    TemplateFile="PayRollApp/EmployeeInsert.html"
    form=EmployeeForm()
    
    if request.method == "POST":
        form =EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('EmployeesList')
    
    
    return render(request,TemplateFile, {'form':form})
