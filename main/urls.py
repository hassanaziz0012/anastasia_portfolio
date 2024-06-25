from django.urls import path
from main.views import CommunicationManagementWorkView, IndexView, ResearchAndCertificationsWorkView, UGCWorkView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("work/ugc", UGCWorkView.as_view(), name="ugc-work"),
    path("work/communication-management", CommunicationManagementWorkView.as_view(), name="communication-management-work"),
    path("work/research-and-certifications", ResearchAndCertificationsWorkView.as_view(), name="research-certifications-work"),
]