from django.shortcuts import render
<<<<<<< HEAD
from .models import Product, Contact, Orders, orderUpdate
from django.http import HttpResponse
from math import ceil
import json
=======
from .models import Product
from django.http import HttpResponse
from math import ceil
>>>>>>> 24802ca1dac3961a98947c235dfbc0f60ec727a7

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))

    # params = {'no_of_slides' : nSlides, 'range' : range(1,nSlides), 'product' : products}
    # allProds = [[products, range(1, nSlides), nSlides],
    # 			[products, range(1, nSlides), nSlides]]

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
    	prod = Product.objects.filter(category=cat)
    	n = len(prod)
    	nSlides = n//4 + ceil((n/4) - (n//4))
    	allProds.append([prod, range(1, nSlides), nSlides])
<<<<<<< HEAD
    params = {'allProds' : allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds' : allProds, 'msg': ''}
    if len(allProds) == 0 or len(query) < 2:
        params = {'msg': 'Please make sure to enter relevant search query'}
    return render(request, 'shop/search.html', params)

=======

    params = {'allProds' : allProds}
    return render(request, 'shop/index.html', params)

>>>>>>> 24802ca1dac3961a98947c235dfbc0f60ec727a7
def about(request):
    return render(request, 'shop/about.html')

def contact(request):
<<<<<<< HEAD
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        # return HttpResponse(f"{orderId} and {email}")
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = orderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                # return HttpResponse('Else Block Occur')
                return HttpResponse('{status": "no item"}')
        except Exception as e:
            # return HttpResponse(f'exception {e}')
            return HttpResponse('{status": "error"}')
    return render(request, 'shop/tracker.html')

=======
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')
>>>>>>> 24802ca1dac3961a98947c235dfbc0f60ec727a7

def productview(request, myid):
    #fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodview.html', {'product' : product[0]})

def checkout(request):
<<<<<<< HEAD
    if request.method == "POST":
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        idd = order.order_id
        update = orderUpdate(order_id=order.order_id, update_desc='The order has been placed')
        update.save()
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':idd})
=======
>>>>>>> 24802ca1dac3961a98947c235dfbc0f60ec727a7
    return render(request, 'shop/checkout.html')