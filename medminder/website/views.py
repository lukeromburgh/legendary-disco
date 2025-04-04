from django.shortcuts import render

# Create your views here.

def website(request):
    """
    Render the index page of the website.
    """
    print("Rendering index page")  # Debug
    return render(request, 'website/sidebar.html')