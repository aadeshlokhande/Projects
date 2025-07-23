from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Categories
from django.http import JsonResponse
from django.db.models import  Q
from django.utils import  timezone

# Create your views here.
@login_required
def index(request):
    categoryData = Categories.objects.all()

    return render(request,"categories/categories.html",{'data':categoryData})

@login_required
def getAjaxList(request):
    # Get pagination parameters from DataTables
    draw = int(request.POST.get('draw', 1))
    start = int(request.POST.get('start', 0))  # Offset
    length = int(request.POST.get('length', 10))  # Limit
    search_value = request.POST.get('search[value]', '')
    if search_value is not None:
        categoryObj = Categories.objects.filter(
            Q(name__icontains=search_value)|
            Q(description__icontains=search_value)|
            Q(status__icontains=search_value)
        )
    else:
        categoryObj = Categories.objects.all()

    totalFiltered = categoryObj.count()
    total_records = Categories.objects.count()

    records = categoryObj[start:start+length]

    # Prepare data for DataTables
    data = []
    for category in records:
        data.append([
            category.id,
            category.name,
            category.description,
            'Active' if category.status==1 else "Inactive",
            str(category.created_by),
            str(category.updated_by),
            category.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Format date
            category.updated_at.strftime('%Y-%m-%d %H:%M:%S'),  # Format date
            f"""<a href="./edit/{category.id}" class='btn btn-primary'>EDIT</a> <a href="./delete/{category.id}" class='btn btn-danger'>DELETE</a>""",
        ])
        # / edit/123
    response = {
        "draw": draw,
        "recordsTotal": total_records,
        "recordsFiltered": total_records if not search_value else totalFiltered,
        "data": data,
    }
    return JsonResponse(response)

@login_required
def addCategory(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get("status")
        userid = request.user.id
        status = 1 if status=='active' else 0
        add_data = Categories(name=name,description=description,status=status,created_by_id=userid, updated_by_id=userid,created_at=timezone.now(),updated_at = timezone.now() )
        add_data.save()

    return render(request, "categories/add.html")

@login_required
def edit(request, id):
    data = {}
    categoryData = Categories.objects.get(id=id)
    data['name'] = categoryData.name
    data['description'] = categoryData.description
    data['status'] = categoryData.status

    categoryUpdate = get_object_or_404(Categories,id=id)
    if request.method == "POST":

        categoryUpdate.name = request.POST.get('name')
        categoryUpdate.description = request.POST.get('description')
        categoryUpdate.status = 1 if request.POST.get("status").lower() == "active" else 0
        categoryUpdate.updated_by_id = request.user.id
        categoryUpdate.updated_at = timezone.now()
        categoryUpdate.save()
        return  redirect('categories')
    return render(request,"categories/add.html", data)

@login_required
def delete(request, id):
    student = get_object_or_404(Categories, id=id)
    student.delete()
    return redirect('categories')