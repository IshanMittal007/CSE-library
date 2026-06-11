from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from.models import resource
from.models import subject

def home(response):
    context = {
        'resources': resource.objects.all()
    }
    return render(response, 'library/home.html', context)

class LibraryListView(ListView):
    model = subject
    template_name = 'library/home.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return subject.objects.prefetch_related('resources').all()

class LibraryDetailView(DetailView):
    model = resource
    template_name = 'library/resource_detail.html'    

class LibraryCreateView(LoginRequiredMixin,CreateView):
    model = resource
    template_name = 'library/resource_form.html'
    fields = ['subject','title' , 'description' , 'file']

class LibraryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = resource
    template_name = 'library/resource_form.html'
    fields = ['subject','title' , 'description' , 'file']

    def test_func(self):
        return self.request.user.is_staff

class LibraryDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = resource
    template_name = 'library/resource_delete.html'
    success_url = '/library'

    def test_func(self):
        return self.request.user.is_staff 