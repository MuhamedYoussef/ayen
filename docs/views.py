from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Doc

@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class Docs(View):

    def get(self, request):
        return render(request, 'docs/docs.html')
    
    def post(self, request):
        name = request.POST['name']
        file = request.FILES['file']
        Doc.objects.create(owner=request.user, name=name, file=file)
        return redirect('docs')