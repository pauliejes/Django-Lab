# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("<h1 style='color: blue;'> ~ TEST ~ </h1>")
