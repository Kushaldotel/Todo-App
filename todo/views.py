from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
# def index(request):
#     todo = Todo.objects.all()

    # if request.method == 'POST':
    #     if not request.POST.get('title'):

        
    #         new_todo = Todo(
    #             title = request.POST['title']
    #         )
    #         new_todo.save()
    #         return redirect('/')
        # else:
        #     return redirect('/')


def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            new_todo = Todo(title=title)
            new_todo.save()
        return redirect('/')
    return render(request, 'index.html', {'todos': todo})

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

