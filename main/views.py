from django.shortcuts import render
from django.views import View, generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"


class UGCWorkView(generic.TemplateView):
    template_name = "work/ugc/index.html"


class CommunicationManagementWorkView(generic.TemplateView):
    template_name = "work/communication_management/index.html"


class ResearchAndCertificationsWorkView(generic.TemplateView):
    template_name = "work/research_and_certifications/index.html"
