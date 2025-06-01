
from django.views.generic import TemplateView

class MessageView(TemplateView):
    template_name = 'home.html'





#2
# from django.shortcuts import render
# from django.views import View
#
#
# class MessageView(View):
#     def get(self, request):
#         return render(request, 'home.html')


#1
# def message_view(request):
#     return render(request, 'home.html')
