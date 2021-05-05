from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from datetime import datetime

# Create your views here.
class Login(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True  # redirects user if already logged in

    def get_success_url(self):
        return reverse_lazy("home")


class Signup(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Signup, self).form_valid(form)


@login_required
def list(request):
    print(request.session)
    obj = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = (
                request.user
            )  # sets the user model as current logged in user
            form.save()
        return redirect("/")

    # we need to show tasks made by each user
    context = {
        "count": obj.filter(completed=False).count(),
        "tasks": obj.filter(user=request.user),
        "form": form,
    }
    return render(request, "todo.html", context)


def register(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            obj = User.objects.create_user(username=username)
            obj.save()
            obj.set_password(password)
            obj.save
            return redirect("/")
    context = {"form": form}
    return render(request, "signup.html", context)


@login_required
def update(request, pk):
    obj = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=obj)
    if request.method == "POST":
        # creates a new object instead of updating it if 'instance' is not added as arg
        if form.is_valid:
            form = TaskForm(request.POST, instance=obj)
            if request.POST.get("completed") != None:
                deleted_at = datetime.now()
                obj = Task.objects.get(id=pk)
                obj.completed_at = deleted_at
                obj.save()
                print("\n" * 3)
                print(deleted_at)
                print(obj.completed_at)
            form.save()
        return redirect("home")

    context = {"form": form}

    return render(request, "update.html", context)


@login_required
def delete(request, pk):
    obj = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("home")
    context = {"task": obj}
    return render(request, "delete.html", context)
