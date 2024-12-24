from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        return super().form_valid(form)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Неверне имя пользователя или пароль'})
    return render(request, 'login.html')