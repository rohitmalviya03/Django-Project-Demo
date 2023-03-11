from django.shortcuts import render,redirect
from Home.models import Customer,Product,Category
# Create your views here.


def homepage(request): 
    cat= Category.getCategory()
    catId = request.GET.get('category')  
    pid=request.GET.get('pid')
   
    if request.method=='POST':
       pricevalue=request.POST['price1']
       pricevalue=int(pricevalue)*15
       print(pricevalue)
       prod=Product.getProductbyPrice(0,pricevalue)
        
    else:    

        # catIdname = request.GET.get('name')
        # print(catIdname)
        if catId:
            prod=Product.getProductbyId(catId)
        else:    
            prod= Product.objects.all()[:10]
        
    data={}
    data['products']=prod
    data['category']=cat
    return render(request,'index.html',data)


def handleCart(request):
    print(request.method)
    
    cart = request.session['cart']
    if request.method == 'POST':
        remove=request.POST.get('remove')
       
        product=request.POST.get('pid')
        print(remove)
        qnty=cart.get(product)
        print(qnty)
        if product:
            if qnty:
               cart[product]=qnty+1
            else:
                cart[product]=1  
            if remove:
                if qnty > 1:
                   cart[product]=qnty-1
                else:
                    cart.pop(product)     
        else:   

            pass

        
        request.session['cart']=cart 
        print(request.session.get('cart'))
    else:
          
        cart=request.session['cart']
#{1:1,2:1,}
# 
# {'123':12}
#{request.session[pid]:qnty}

    return redirect('/')
   

def getLogin(request):
    msg={}
    if request.method == "POST":
        email=request.POST['email']
        password1=request.POST['password']
        print(email,password1)
        if email:
            customer= Customer.getCustomerByemail(email)
            
        else:
            msg["error"]="Please enter Email first"
            customer=''
            print(customer.name)
            return render(request,'login.html',msg)
        
      
        if customer:
            
            if customer.password == password1:
                name=customer.name
                email=customer.email
                cart={}
                request.session['cart']=cart
                request.session['userid']=name
                request.session['id']=email
                print("hello",request.session.get('userid'))
               
                return redirect('/')  
            else:
                msg["error"]="Email id or pwd Incorect"
                return render(request,'login.html',msg)       
    return render(request,'login.html')  

def logout(request):
        cat= Category.getCategory()
        prod= Product.objects.all()[:10]
        data={}
        request.session.clear()
        data['category']=cat

        data['products']=prod
        data['flag']=False 
        return render(request,"index.html",data)

def getRegister(request):

    if request.method == 'POST':
    
      name= request.POST['name']
      email=request.POST['email']
      pwd=request.POST['pwd']
      address=request.POST['address']
      print(request.method)
      msg="Customer Registration done Succesfully..." 
      customer={'name':name,'email':email,'pwd':pwd,'address':address}
      print(customer)
      cust =Customer(name=name,email=email,password=pwd,address=address)
      cust.save()
      data= Customer.objects.all()
      d=Customer.objects.filter(name="Rohan")
      print(d)
      return render(request,'data.html',{'customer':customer,'msg':msg,'data':data})
    
    
    print(request.method)
    return render(request,'registration.html')      
def viewcart(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    print(products)
    return render(request , 'cart.html' , {'products' : products} )



def shopnow(request):
    prod=Product.objects.all()
    return render(request,'shop.html',{'products':prod})

def search(request):
    cat= Category.getCategory()
    if request.method == 'POST':
        val =request.POST['searchvalue']
        prod=Product.objects.filter(pname__startswith=val)
        data={}
        if prod:
            data['products']=prod
        else:
            data['msg']="Products not found"
        data['category']=cat
        print(val)
    return render(request,'index.html',data)

def checkout(request):
    
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    customer = request.session.get('customer')
    cart = request.session.get('cart')
    products = Product.get_products_by_id(list(cart.keys()))
    print(address, phone, customer, cart, products)
    for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
    request.session['cart'] = {}

    return redirect('cart')