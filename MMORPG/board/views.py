from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad
from .forms import AdForm


class AdList(ListView):
    model = Ad
    ordering = 'title'
    template_name = 'ad.html'
    context_object_name = 'ad'


class AdDetail(DetailView):
    model = Ad
    template_name = 'post.html'
    context_object_name = 'post'


class AdCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board.add_ad',)
    raise_exception = True
    form_class = AdForm
    model = Ad
    template_name = 'ad_create.html'


class AdEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.edit_ad',)
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'


class AdDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_ad',)
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ad_list')
