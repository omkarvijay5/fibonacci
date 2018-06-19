# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def nth_number(request):
	context = {}
	return render(request, "core/nth_fibonacci_number.html", context)
