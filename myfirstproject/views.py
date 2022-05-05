from multiprocessing import context
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

def home(request):
    name=["farhad","kamal","jitu","farlin"]
    context={
        'name':name
    }
    return render (request , 'home.html',context)


class HomeView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["msg"] = "Motka"
        context["msg2"] = "Motka2"
        return context
    

  