import imp
from urllib import request
from django.shortcuts import render,HttpResponseRedirect 
from .forms import StudentForm
from .models import User
from django.views.generic import View,TemplateView,RedirectView
# Create your views here.
class  UserAddView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = User.objects.all()
        context['form'] = StudentForm()
        return context

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            # form.save()
            # return HttpResponseRedirect('/')
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            record = User(name=name,age=age,password=password)
            record.save()
            return HttpResponseRedirect('/')

class DeleteUserView(RedirectView):
    url = '/'
    def get_redirect_url(self,*args,**kwargs):
        user = User.objects.get(id=kwargs['id'])
        user.delete()
        return super().get_redirect_url(*args, **kwargs)

class UpdateUserView(View):
    def get(self,request,id):
        user = User.objects.get(id=id)
        form = StudentForm(instance=user)
        return render(request,'update.html',{'form':form,'id':id})

    def post(self,request,id):
        user = User.objects.get(id=id)
        form = StudentForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

                

    









    # if request.method =='POST':
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         age = form.cleaned_data['age']
    #         password = form.cleaned_data['password']
    #         record = User(name=name,age=age,password=password)
    #         record.save()
    #         form = StudentForm()
    # else:
    #     form = StudentForm()
    # data = User.objects.all()
    # return render(request,'aboutadd.html',{'form':form,'data':data})

# def update_data(request,id):
#     if request.method == 'POST': 
#         user = User.objects.get(pk=id) 
#         form = StudentForm(request.POST,instance=user)
#         if form.is_valid():
#             form.save()
#     else:
#         user = User.objects.get(pk=id)
#         form = StudentForm(instance=user)
#         return render(request,'update.html',{'form':form,'id':id})
               
#     return HttpResponseRedirect('/')




# def delete_data(request,id):
#     if request.method == 'POST': 
#         user = User.objects.get(pk=id)
#         user.delete()
#         return HttpResponseRedirect('/')




