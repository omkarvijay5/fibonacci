# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# third party imports
from core.forms import FibonacciForm


class NthNumber(View):
    form_class = FibonacciForm
    template_name = 'core/nth_fibonacci_number.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})
