from django.utils import timezone
from .models import ExtractedRecord

def simulate_extraction(job):
    job.status = "in_progress"
    job.started_at = timezone.now()
    job.save()

    for i in range(5):
        ExtractedRecord.objects.create(
            job=job,
            email=f"user{i}@example.com",
            first_name=f"First{i}",
            last_name=f"Last{i}",
            id_from_service=str(i),
        )

    job.status = "completed"
    job.record_count = 5
    job.completed_at = timezone.now()
    job.save()
