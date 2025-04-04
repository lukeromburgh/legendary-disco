from django.shortcuts import render, HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.
def landing(request):
    form = SignUpForm()
    print("Rendering landing page")  # Debug
    return render(request, 'landing.html', {'form': form})

def signup(request):
    print("Signup view called")  # Debug
    if request.method == 'POST':
        print("POST request received")  # Debug
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug
            user = form.save()
            print(f"User {user.username} saved with ID {user.id}")  # Debug
            login(request, user)
            return redirect('landing')  # Temporarily redirect to landing
        else:
            print("Form invalid:", form.errors)  # Debug
            return render(request, 'landing.html', {'form': form})  # Show errors
    else:
        print("GET request to signup, redirecting")  # Debug
        return redirect('landing')