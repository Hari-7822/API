from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Demo, DemoForm

def is_ajax(request):
    return request.META.get('HPPT_X_REQUESTED_WITH')=='XMLHttpRequest'

def index(req):
    data=Demo.objects.all()
    # if req.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     list=[{'name': d.name} for d in data]
    #     return JsonResponse({'data': list})
    return render(req, 'index.j2', {'data': data})        





def add(req):
    if req.method=="POST":
        form=DemoForm(req.POST)
        if form.is_valid():
            form_name=form.cleaned_data['name']
            demo= Demo.objects.create(name=form_name)
            demo.save()
            return JsonResponse({'success': True, 'name': form_name})
        else: 
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form=DemoForm()
    return render(req, 'form.j2', {'form': form})



