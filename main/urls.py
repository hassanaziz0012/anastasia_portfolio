from django.urls import path
from main.views import CommunicationManagementWorkView, IndexView, ResearchAndCertificationsWorkView, UGCWorkView
from django.views.generic import TemplateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("work/ugc", UGCWorkView.as_view(), name="ugc-work"),
    path("work/ugc/automotive", TemplateView.as_view(template_name="work/ugc/automotive.html"), name="ugc-automotive"),
    path("work/ugc/catering", TemplateView.as_view(template_name="work/ugc/catering.html"), name="ugc-catering"),
    path("work/ugc/lifestyle", TemplateView.as_view(template_name="work/ugc/lifestyle.html"), name="ugc-lifestyle"),
    path("work/ugc/fitness", TemplateView.as_view(template_name="work/ugc/fitness.html"), name="ugc-fitness"),
    path("work/ugc/e-products", TemplateView.as_view(template_name="work/ugc/e_products.html"), name="ugc-e-products"),
    path("work/ugc/ai-generated", TemplateView.as_view(template_name="work/ugc/ai_generated.html"), name="ugc-ai-generated"),

    
    path("work/communication-management", CommunicationManagementWorkView.as_view(), name="communication-management-work"),
    
    
    path("work/research-and-certifications", ResearchAndCertificationsWorkView.as_view(), name="research-certifications-work"),
]