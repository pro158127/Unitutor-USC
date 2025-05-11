from django.shortcuts import redirect, render 
from django.http import HttpResponse ,request,JsonResponse
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from  .forms import *
from  .models import *
from django.contrib.auth import authenticate,login


class index(TemplateView):
    template_name="main/index.html"

class SignUpView(CreateView):
    model = CustomUser
    form_class = Sign_up
    template_name = 'main/sign_up.html'
    success_url = reverse_lazy('indexx')

    def form_valid(self, form):
        print("Datos del formulario:", form.cleaned_data) 
        if CustomUser.objects.filter(username=form.cleaned_data['username']).exists():
            form.add_error('username', 'Este nombre de usuario ya está en uso.')
            return self.form_invalid(form)
        elif CustomUser.objects.filter(email=form.cleaned_data['email']).exists():
            form.add_error('email', 'Este correo electronico ya es en uso.')
            return self.form_invalid(form)
        
        elif CustomUser.objects.filter(telefono=form.cleaned_data['telefono']).exists():
            form.add_error('telefono', 'este telefono  ya esta en uso ')
            return self.form_invalid(form)
     
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Errores del formulario:", form.errors)  # Imprime los errores
        error_string = repr(form.errors)
        return render(self.request, self.template_name, {'form': form, 'raw_errors': error_string})

class LoginView(TemplateView):

    template_name = 'main/Login.html'
    form_class=LoginForm
    success_url= reverse_lazy('indexx')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print('datos del formulario:',form)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form= self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request=request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect(self.success_url)
            else:
                form.add_error(None,'Usuario o contraeña incorrecta')
                print('Errores del formulario:',form.errors)
                return  render(request,self.template_name,{'form':form} )
            

class paneProfesores(TemplateView):
    template_name="panel/teacher.html"

    
    



