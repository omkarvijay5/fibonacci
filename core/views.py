# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# django imports
from django.shortcuts import render
from django.http import HttpResponse


def nth_number(request):
	 return HttpResponse("Fibonaccii series")
