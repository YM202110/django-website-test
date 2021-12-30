from django.shortcuts import render
from django.views.generic import TemplateView

# TemplateViewを使うとhtmlをそのままユーザーに返せる
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
