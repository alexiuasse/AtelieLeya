#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/11/2020 11:16.

from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_tables2 import RequestConfig, LazyPaginator

from .forms import *
from .tables import *


########################################################################################################################

@login_required
@require_http_methods(["GET"])
@staff_member_required()
@permission_required('homepage.view_homepage', raise_exception=True)
def homepage_view(request):
    if HomePage.objects.all().count() == 0:
        obj = HomePage(
            title='Atêlie Leya Monteiro',
            subtitle='',
            whatsapp='(00) 0 0000-0000',
        ).save()
    else:
        obj = HomePage.objects.first()
    # testimonials = Testimonials.objects.all()
    # testimonials_table = TestimonialsTable(testimonials)
    # RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(testimonials_table)
    # clients_image = ClientsImage.objects.all()
    # clients_image_table = ClientsImageTable(clients_image)
    # RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(clients_image_table)
    return render(request, "homepage/homepage/homepage.html", {
        'obj': obj,
        # 'testimonials_table': testimonials_table,
        # 'clients_image_table': clients_image_table,
    })


class HomePageEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = HomePage
    form_class = HomePageForm
    template_name = 'homepage/homepage/form.html'
    permission_required = 'homepage.change_homepage'
    success_url = reverse_lazy('homepage:homepage:view')
    title = _('Homepage')
    subtitle = _('Edit')

########################################################################################################################


# class TestimonialsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     model = Testimonials
#     form_class = TestimonialsForm
#     template_name = 'homepage/homepage/form.html'
#     permission_required = 'homepage.add_testimonials'
#     back_url = reverse_lazy('homepage:homepage:view')
#     title = _('Testimonials')
#     subtitle = _('Create')
#
#     def get_back_url(self):
#         return self.back_url
#
#
# class TestimonialsEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     model = Testimonials
#     form_class = TestimonialsForm
#     template_name = 'homepage/homepage/form.html'
#     permission_required = 'homepage.change_testimonials'
#     success_url = reverse_lazy('homepage:homepage:view')
#     title = _('Testimonials')
#     subtitle = _('Edit')
#
#
# class TestimonialsDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
#     model = Testimonials
#     template_name = "homepage/homepage/confirm_delete.html"
#     permission_required = 'homepage.del_testimonials'
#     success_url = reverse_lazy('homepage:homepage:view')
#     title = _('Testimonials')
#     subtitle = _('Delete')
#
#     def get_context_data(self, **kwargs):
#         context: Dict[str, Any] = super().get_context_data(**kwargs)
#         collector = NestedObjects(using='default')  # or specific datahomepage
#         collector.collect([context['object']])
#         to_delete = collector.nested()
#         context['extra_object'] = to_delete
#         return context


########################################################################################################################


# class ClientsImageCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     model = ClientsImage
#     form_class = ClientsImageForm
#     template_name = 'homepage/homepage/form.html'
#     permission_required = 'homepage.add_clientsimage'
#     back_url = reverse_lazy('homepage:homepage:view')
#     title = _('Clients Image')
#     subtitle = _('Create')
#
#     def get_back_url(self):
#         return self.back_url
#
#
# class ClientsImageEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     model = ClientsImage
#     form_class = ClientsImageForm
#     template_name = 'homepage/homepage/form.html'
#     permission_required = 'homepage.change_clientsimage'
#     success_url = reverse_lazy('homepage:homepage:view')
#     title = _('Clients Image')
#     subtitle = _('Edit')
#
#
# class ClientsImageDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
#     model = ClientsImage
#     template_name = "homepage/homepage/confirm_delete.html"
#     permission_required = 'homepage.del_clientsimage'
#     success_url = reverse_lazy('homepage:homepage:view')
#     title = _('Clients Image')
#     subtitle = _('Delete')
#
#     def get_context_data(self, **kwargs):
#         context: Dict[str, Any] = super().get_context_data(**kwargs)
#         collector = NestedObjects(using='default')  # or specific datahomepage
#         collector.collect([context['object']])
#         to_delete = collector.nested()
#         context['extra_object'] = to_delete
#         return context
