from django.shortcuts import render,redirect
from frontapp.models import product,order
from frontapp.forms import  orderForm,productForm

# Create your views here.
def main(request):
    return render(request,'frontapp/main.html')
def contact(request):
     name='karthika'
     email="dglkarthika97@gmil.com"
     context={'name':name,'email':email}
     return render(request,'frontapp/index.html',context)
def pmodel(request):
    detail=product.objects.all()
    return render(request,'frontapp/model.html',{'det':detail})

def omodel(request):
    dis=order.objects.all()
    return render(request,'frontapp/order.html',{'det':dis})
def oForm(request):
    details=orderForm()
    if request.method == 'POST':
        details=orderForm(request.POST)
        if details.is_valid():
             details.save()
             return redirect('/frontapp/omodel/')
    return render(request,'frontapp/forms.html',{'data':details})
def pForm(request):
     data=productForm()
     if request.method=='POST':
         data=productForm(request.POST)
         if data.is_valid():
              data.save()
         return redirect('/frontapp/pmodel/')
     return render(request,'frontapp/update.html',{'form':data})
def pdelete(request,id):
     pdel=product.objects.get(id=id)
     pdel.delete()
     return redirect('/frontapp/pmodel/')
def pupdate(request,id):
     pdel=product.objects.get(id=id)
     context={'pdel':productForm(instance=pdel)}
     if request.method=='POST':
         data=productForm(request.POST,instance=pdel)
         if data.is_valid():
              data.save()
         return redirect('/frontapp/pmodel/')
     return render(request,'frontapp/pupdate.html',context)
    
def dele(request,id):
      dis=order.objects.get(id=id)
      dis.delete()
      return redirect('/frontapp/omodel/')
def update(request,id):
      details= order.objects.get(id=id)
      context={
           'data':orderForm(instance=details)
           }
      if request.method == 'POST':
            forms = orderForm(request.POST,instance=details)
            if forms.is_valid():
               forms.save()
               return redirect("/frontapp/omodel/")
           
      return render(request,'frontapp/forms.html',context)


      
      

    