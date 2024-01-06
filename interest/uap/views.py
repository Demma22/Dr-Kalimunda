from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# now we are including our filters from the 'filters' file so that they are ued by the view


#here we include the models so that the views can use these models incase of posting 


##Handling redirection after deletion
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

#including our model forms created in the forms file


def home(request):
    return render(request, 'products/index.html')

# @login_required
# def index(request):
#     return render(request, 'products/aboutDrkalimunda.html')

# #Crete aview for product_detail
# @login_required
# def product_detail(request, product_id):
#     product = Product.objects.get(id = product_id)
#     return  render(request, 'products/product_detail.html', {'product':product})

# @login_required
# def issue_item(request,pk):
#     issued_item = Product.objects.get(id = pk)
#     sales_form = SaleForm(request.POST)

#     if request.method == 'POST':
#         #checks if the input is as its supposed to be
#         if sales_form.is_valid():
#             new_sale = sales_form.save(commit = False)
#             new_sale.item = issued_item
#             new_sale.unit_price = issued_item.unit_price
#             new_sale.save()
#             #to keep track of the remainning stock after sales
#             issued_quantity = int(request.POST['quantity'])
#             issued_item.total_quantity -= issued_quantity
#             issued_item.save
#             print(issued_item.item_name)
#             print(request.POST['quantity'])
#             print(issued_item.total_quantity)

#             return redirect('receipt')
        
#     return render(request, 'products/issue_item.html', {'sales_form': sales_form})   

# #this handles receipt issuing
# @login_required
# def receipt(request):
#     sales = Sale.objects.all().order_by('-id')
#     return render(request,'products/receipts.html', {'sales':sales})

 
# @login_required
# def add_to_stock(request, pk):
#     issue_item = Product.objects.get(id = pk)
#     form = AddForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             added_quantity = int(request.POST['received_quantity'])
#             issue_item.total_quantity += added_quantity
#             issue_item.save()
#         #to add to the remaining stock bcz quantity is reducing
#             print(added_quantity)
#             print(issue_item.total_quantity)
#             return redirect('home')
#     return render(request, 'products/add_to_stock.html',{'form':form})    

# @login_required
# def all_sales(request):
#     sales = Sale.objects.all()
#     total = sum([items.ammount_received for items in sales])
#     change = sum([items.get_change() for items in sales])
#     net = total - change
#     return render(request, 'products/all_sales.html',{
#         'sales':sales,
#         'total':total,
#         'net':net,
#         'change':change
#     })

# @login_required
# def receipt_detail(request,receipt_id):
#     receipt = Sale.objects.get(id = receipt_id)
#     return render(request, 'products/receipt_detail.html', {'receipt':receipt})

# @login_required
# def delete_detail(request, product_id):
#     delete = Product.objects.get(id = product_id)
#     delete.delete()
#     return HttpResponseRedirect(reverse('index'))