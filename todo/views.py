from django.shortcuts import redirect, render

from django.http import HttpResponse

from .forms import PersonForm, TodoForm
from .models import Todo, Person
def hello_world_view(request):
    return HttpResponse("Hello, World!")

def addition(request, n1, n2):
    return HttpResponse(f"the sum is  {n1 + n2}")

def hello_html_view(request):
    return render(request, 'todo/hello.html')

def another_view(request):
    return HttpResponse(f'this query is {request.GET.get("q")}')

def special(request):
    return redirect('hello_world')

def post_example(request):
    if request.method == 'POST':
       form = PersonForm(request.POST)
       if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']
            return HttpResponse(f'You posted {name}, {age}, {job}')
    return HttpResponse('Please submit the form.')

def submit_example(request):
    return render(request, 'todo/submit.html')

def submit_django_form(request):
    form = PersonForm()
    return render(request, 'todo/submit_django_form.html', {'form': form})

def template_view(request):
    context = {
        "name" : "Alice",
        "age" : 30,
        "skills" : ["Python", "Django", "JavaScript"]
    }
    return render(request, 'todo/template_view.html', context)


def todos_view(request):
    if request.method == 'POST' :
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return HttpResponse('Todo successfully created')

    else:
        form = TodoForm()
        todos = Todo.objects.all()

        return render(request, 'todo/todos.html', {'todos': todos, 'form': form})
    

def person_details_view(request, person_id):
    person = Person.objects.get(id=person_id)

    return render(request, 'todo/person_details.html', {'person': person})


def delete_todo_view(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todos_view')

def toggle_todo_view(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.done = not todo.done
    todo.save()
    return HttpResponse('Todo status toggled successfully')
    

    