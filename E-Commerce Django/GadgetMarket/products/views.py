from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from .models import Products
from  django.utils import timezone
from categories.models import Categories

# Create your views here.)
def index(request):
    productsData = Products.objects.all()[:100]
    return render(request,"products/products.html",{'data':productsData})

def addProduct(request):
    AllCategory = Categories.objects.filter(status='1')
    # print(AllCategory)
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        cat_id = request.POST.get("category")
        category = Categories.objects.get(id=cat_id)
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        status = request.POST.get("status")
        status = 1 if status=="active" else 0
        userid = request.user.id

        add_data = Products(name=name, description=description, category=category, price=price, quantity=quantity, status=status, created_at = timezone.now(), updated_at = timezone.now(),created_by_id=userid, updated_by_id=userid)

        add_data.save()

    return render(request, "products/add.html", context = {"categories" : AllCategory})

def editProduct(request,id):
    data = {}
    productData = Products.objects.get(id=id)

    data['name'] = productData.name
    data['description'] = productData.description
    data['category_id'] = Categories.objects.filter(status='1')
    data['price'] = productData.price
    data['quantity'] = productData.quantity
    data['status'] = productData.status


    productUpdate = get_object_or_404(Products,id=id)
    if request.method == "POST":

        productUpdate.name = request.POST.get('name')
        productUpdate.description = request.POST.get('description')
        productUpdate.category_id = request.POST.get('category_id')
        productUpdate.price = request.POST.get('price')
        productUpdate.status = 1 if request.POST.get("status").lower() == "active" else 0
        productUpdate.updated_by_id = request.user.id
        productUpdate.updated_at = timezone.now()
        productUpdate.save()
        return  redirect('products')
    return render(request,"products/add.html",data)


def deleteProduct(request, id):
    productId = get_object_or_404(Products, id=id)
    productId.delete()
    return redirect('products')