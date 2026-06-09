from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Collection, Clothe
from .forms import ClotheForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class ClothesListView(ListView):
    model = Clothe
    template_name = 'clothes/catalogue.html'
    context_object_name = 'clothes'

class ClothesDetailView(DetailView):
    model = Clothe
    template_name = 'clothes/clothe_detail.html'
    context_object_name = 'clothe'

class ClothesCreateView(CreateView):
    model = Clothe
    form_class = ClotheForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('catalogue')

class ClothesUpdateView(UpdateView):
    model = Clothe
    form_class = ClotheForm
    template_name = 'clothes/clothes_form.html'
    success_url = reverse_lazy('catalogue')

class ClothesDeleteView(DeleteView):
    model = Clothe
    template_name = 'clothes/clothe_confirm_delete.html'
    context_object_name = 'clothe'
    success_url = reverse_lazy('catalogue')