from django.shortcuts import render, redirect
from .models import Todolist, Category

def index(request):
    todos = Todolist.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            todo = Todolist(title=title, content=content, due=date, category=Category.objects.get(name=category))
            todo.save()
            return redirect("/")

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = Todolist.objects.get(id=int(todo_id))
                todo.delete()


    return render(request, 'index.html', {"todos": todos, "categories": categories})
