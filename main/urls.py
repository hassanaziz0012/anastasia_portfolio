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
    path(
        "work/communication-management/social-media-performance-reports",
        TemplateView.as_view(template_name="work/communication_management/social_media.html"),
        name="cm-social-media"
    ),
    path(
        "work/communication-management/content-management", 
        TemplateView.as_view(template_name="work/communication_management/content_management.html"), 
        name="cm-content-management"
    ),
    path(
        "work/communication-management/marketing",
        TemplateView.as_view(template_name="work/communication_management/marketing.html"),
        name="cm-marketing"
    ),
    
    path("work/research-and-certifications", ResearchAndCertificationsWorkView.as_view(), name="research-certifications-work"),
    path(
        "work/research-and-certifications/business-plans", 
        TemplateView.as_view(template_name="work/research_and_certifications/business_plans.html"), 
        name="rc-business-plans"
    ),
    path(
        "work/research-and-certifications/university-work", 
        TemplateView.as_view(template_name="work/research_and_certifications/university_work.html"), 
        name="rc-university-work"
    ),
]