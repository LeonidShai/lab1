from django.shortcuts import render
from django.views.generic import View


from django.http import Http404

# Create your views here.

class Err404View(View):
    def get(self, request):
        return render(request, 'err404/index.html')
