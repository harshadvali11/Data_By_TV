from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
class SendDataByTV(TemplateView):
    template_name='SendDataByTV.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Ashu'
        ECDO['age']=4
        ECDO['ESFO']=StudentForm()
        return ECDO
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Invalid')
        





