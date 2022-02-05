from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from .models import Task
from django.views.generic import ListView, UpdateView,DeleteView
from django.views.generic.detail import DetailView


class listview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task'

class detailview(DetailView):
    model = Task
    template_name = 'copy.html'
    context_object_name = 'task1'

class updateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todo:cbvdetail',kwargs={'pk':self.object.id})


def deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url=reverse_lazy('todo:cbvhome')





# Create your views here.
def add(request):
    if request.method=='POST':
       name=request.POST.get('task','')
       priority = request.POST.get('priority', '')
       date=request.POST.get('date','')
       task=Task(name=name,priority=priority,date=date)
       task.save()
    task1=Task.objects.all()

    return render(request,"home.html",{'task':task1})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})