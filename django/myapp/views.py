from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.db.models import Q

# Create your views here.

# view for homepage
def index(request):
    form = TodoForm(request.POST or None)
    query = request.GET.get('query', '')
    items = Todo.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    
    if query:
        items = Todo.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))

    return render(request, 'myapp/index.html', {'items': items[:10], 'form': form, 'query': query})


# view for update page
def update(request, pk):
    item = get_object_or_404(Todo, pk = pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
        
    else:
        form = TodoForm(instance=item)
    return render(request, 'myapp/update.html', {'form': form})


# view for deleting items
def delete(request, pk):
    item = get_object_or_404(Todo, pk = pk)
    item.delete()
    return redirect('myapp:index')
