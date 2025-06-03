from django.shortcuts import render

# Create your views here.

def elemnts_view(request):
    template_view = "index.html"
    return render(request,template_name=template_view)