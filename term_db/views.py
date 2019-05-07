from .models import Terminal, MeasuredData
from rest_framework import viewsets
from .serializers import TerminalSerializer, MeasuredDataSerializer

from rest_framework.permissions import IsAuthenticated
from django.views.generic.base import TemplateView


class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer

    permission_classes = (IsAuthenticated, )


class MeasuredDataViewSet(viewsets.ModelViewSet):
    queryset = MeasuredData.objects.all()
    serializer_class = MeasuredDataSerializer

    permission_classes = (IsAuthenticated, )


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        pass


class AboutView(TemplateView):

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        pass
