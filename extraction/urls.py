from django.urls import path
from .views import *

urlpatterns = [
    path("scan/start", StartExtractionView.as_view()),
    path("scan/status/<uuid:job_id>", JobStatusView.as_view()),
    path("scan/result/<uuid:job_id>", JobResultView.as_view()),
    path("scan/cancel/<uuid:job_id>", CancelJobView.as_view()),
    path("scan/remove/<uuid:job_id>", RemoveJobView.as_view()),
]
