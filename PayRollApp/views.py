from django.shortcuts import get_object_or_404, redirect, render
from PayRollApp.forms import EmployeeForm, PartTimeEmployeeForm, PartTimeEmployeeFormSet
from PayRollApp.models import Employee, PartTimeEmployee
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger 
from django.conf import settings 
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


def BulkInsertDemo(request):
    extra_forms = 10
    forms =[PartTimeEmployeeForm(request.POST or None, prefix=f'employee-{i}') for i in range(extra_forms)]
    Status=""
    
    if request.method == 'POST':
        for form in forms:
            if form.is_valid() and form.cleaned_data.get('First Name',''):
                form.save()
                Status="Records were inserted successfully.."
    
    return render(request, 'PayRollApp/parttimeemployee_list.html',{'forms':forms, 'extra_forms': range(extra_forms),"Status":Status})

def NewBulkInsertDemo(request):
    formset = PartTimeEmployeeFormSet(queryset =PartTimeEmployee.objects.none(),prefix='employee')
    
    if request.method == 'POST':
        formset = PartTimeEmployeeFormSet(request.POST,prefix='employee')
        if formset.is_valid():
            employees = format.save(commit=False)
            PartTimeEmployee.objects.bulk_create(employees)
            return redirect('bulk_insert')
    else:
        formset = PartTimeEmployeeFormSet(queryset=PartTimeEmployee.objects.none(),prefix='employee')
    
    return render(request,"PayRollApp/NewBulkInsert.html", {'formset':formset})

def BulkUpdateDemo(request):
    employees=PartTimeEmployee.objects.all()
    forms = [PartTimeEmployeeForm(request.POST or None, instance=employee, prefix=f'employee-{employee.id}') for employee in employees]
 
    if request.method=='POST':
        updated_data=[]
        for form in forms:
            if form.is_valid():
                employee=form.instance 
                employee.FirstName=form.cleaned_data['FirstName']  
                employee.LastName=form.cleaned_data['LastName']   
                employee.TitleName=form.cleaned_data['TtileName']   
                updated_data.append(employee)
                
        PartTimeEmployee.objects.bulk_update(updated_data,['FirstName','LastName','TitleName'])
 
    return render(request, 'PayRollApp/BulkUpdate.html', {'forms':forms, 'employees': employees})

def BulkDeleteDemo(request):
    page_size = int(request.GET.get('page_size', getattr(settings, 'PAGE_SIZE', 5)))
    page = request.GET.get('page', 1)
    employees=PartTimeEmployee.objects.all()
    
    if request.method=='POST':
        selected_ids = request.POST.getlist('selected_ids')
        
        if selected_ids:
            PartTimeEmployee.objects.filter(pk_in=selected_ids).delete()
            return redirect('BulkDeleteDemo')
    
    return render(request, 'PayRollApp/BulkDelete.html',{'employees':employees})


def DeleteUsingRadio(request):
    employees=PartTimeEmployee.objects.all
    
    if request.method=='POST':
        selected_id=request.POST.get('selected_id')
        if selected_id:
            PartTimeEmployee.objects.filter(pk=selected_id).delete()
            return redirect('DeleteUsingRadio')
    
    return render(request,'PayRollApp/DeleteUsingRadio.html',{'employees':employees})

def PageWiseEmployeesList(request):
    page_size = int(request.GET.get('page_size', getattr(settings, 'PAGE_SIZE',5)))
    page = request.GET.get('page', 1)
    
    employees =PartTimeEmployee.objects.all()
    paginator = Paginator(employees, page_size)
    
    try:
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        employees_page = paginator.page(1)
    return render(request, 'PayRollApp/PageWiseEmployees.html', {'employees_page':employees_page, 'page_size':page_size})







    