from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Todo
from django.core.serializers import serialize
#Siempre le pasamos un request
def todo(request, id):
    #todo = (Todo.objects.get(id=id).delete()) Esto ultimo es para borrar
    #todo.title = new_title // para actualizar valores de un todo, es decir, te traes lo que quieres y le cambias el valor a los campos quequieras del objeto a actualizar 
    #todo.save() // para guardar los cambios 
    #return HttpResponse(todo)
    #return HttpResponse(data, content_type="application/json")
    
    return HttpResponse(f'Todo {id}')

def get_all(request):
    todos = Todo.objects.all()
    filter = Todo.objects.filter(status=False)
    context = {
     'todos': todos,
     #'filter': filter
    }
    #data = serialize("json", todos, fields=("title", "status", "text"))
    #return HttpResponse(data, content_tydatos a usar en la paginape="application/json")
    #en caso de querer renderizar un HTML seria de la siguietnte manera:
    return render(request, "alltodos.html", {context})
    #return HttpResponse(f'All todos')
