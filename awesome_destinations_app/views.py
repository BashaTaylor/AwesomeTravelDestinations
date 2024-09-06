from django.shortcuts import render, redirect, get_object_or_404 
from TravelDestinations_app.models import Destination
from .forms import DestinationForm
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def index(request):
    destinations = Destination.objects.all()
    return render(request, 'index.html', {'destinations': destinations})

# def index(request):
    # Print the directories where Django will search for templates
    # print(f"Template directories: {settings.TEMPLATES[0]['DIRS']}")

    # destinations = Destination.objects.all()
    # return render(request, 'index.html', {'destinations': destinations})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def travel_blog(request):
    return render(request, 'travel_blog.html')

def gallery(request):
    return render(request, 'gallery.html')

def search_results(request):
    query = request.GET.get('query', '')  # Get the search query from the URL parameters
    if query:
        results = Destination.objects.filter(name__icontains=query)  # Filter destinations by the query
    else:
        results = Destination.objects.all()  # If no search query, return all destinations
    return render(request, 'search_results.html', {'results': results, 'query': query})

def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after saving
    else:
        form = DestinationForm()
    return render(request, 'add_destination.html', {'form': form})


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'destination_detail.html', {'destination': destination})
    

def edit_destination(request, id):
    destination = get_object_or_404(Destination, id=id)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to index page after editing
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'edit_destination.html', {'form': form, 'destination': destination})

def delete_destination(request, id):
    destination = get_object_or_404(Destination, id=id)
    if request.method == 'POST':
        destination.delete()
        return redirect('index')  # Redirect to index page after deleting
    return render(request, 'confirm_delete.html', {'destination': destination})

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                subject,
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],  # Sender's email
                fail_silently=False,
            )
            
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form processing here (e.g., send an email)
            return redirect('success')  # Redirect to success page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})