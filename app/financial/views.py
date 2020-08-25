#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/08/2020 10:53.

from typing import Dict, Any

from config.models import StatusPayment
from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from service.models import OrderOfService

from .conf import *
from .forms import *
from .tables import *


# class InvoiceProfile(LoginRequiredMixin, View):
#     template = 'financial/profile.html'
#     title = TITLE_VIEW_INVOICE
#     subtitle = SUBTITLE_INVOICE
#
#     def get(self, request, cpk, pk):
#         return render(request, self.template, {'obj': Invoice.objects.get(pk=pk)})
#
#
# class InvoiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
#     model = Invoice
#     table_class = InvoiceTable
#     filterset_class = InvoiceFilter
#     paginator_class = LazyPaginator
#     permission_required = 'financial.view_invoice'
#     template_name = 'financial/view.html'
#     title = TITLE_VIEW_INVOICE
#     subtitle = SUBTITLE_INVOICE
#     new = reverse_lazy('financial:index')

def invoice_payment_success(request, pk):
    if request.user.is_superuser and request.user.is_authenticated:
        instance = get_object_or_404(Invoice, pk=pk)
        instance.status = get_object_or_404(StatusPayment, pk=settings.STATUS_PAYMENT_SUCCESS)
        instance.save()
        return redirect(instance.order_of_service.get_absolute_url())
    else:
        raise PermissionDenied()


class InvoiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'financial/form.html'
    permission_required = 'financial.create_invoice'
    title = TITLE_CREATE_INVOICE
    subtitle = SUBTITLE_INVOICE

    def get_success_url(self):
        orderofservice = OrderOfService.objects.get(pk=self.kwargs['spk'])
        return orderofservice.get_absolute_url()

    def get_back_url(self):
        orderofservice = OrderOfService.objects.get(pk=self.kwargs['spk'])
        return orderofservice.get_absolute_url()

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.order_of_service = OrderOfService.objects.get(pk=self.kwargs['spk'])
            instance.save()
        return HttpResponseRedirect(self.get_success_url())


class InvoiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'financial/form.html'
    permission_required = 'financial.edit_invoice'
    title = TITLE_EDIT_INVOICE
    subtitle = SUBTITLE_INVOICE

    def get_delete_url(self):
        return reverse_lazy('financial:invoice:delete', kwargs={'spk': self.kwargs['spk'], 'pk': self.object.pk})


class InvoiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Invoice
    template_name = "financial/confirm_delete.html"
    permission_required = 'financial.del_invoice'
    title = TITLE_DEL_INVOICE
    subtitle = SUBTITLE_INVOICE

    def get_success_url(self):
        orderofservice = OrderOfService.objects.get(pk=self.kwargs['spk'])
        return orderofservice.get_absolute_url()

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific datafinancial
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
