from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ExtractionJob
from .serializers import *
from .services import simulate_extraction

class StartExtractionView(APIView):
    def post(self, request):
        serializer = StartExtractionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        job = ExtractionJob.objects.create(
            api_token=serializer.validated_data["api_token"]
        )

        simulate_extraction(job)

        return Response({"job_id": job.id}, status=status.HTTP_202_ACCEPTED)


class JobStatusView(APIView):
    def get(self, request, job_id):
        job = get_object_or_404(ExtractionJob, id=job_id)
        return Response(ExtractionJobSerializer(job).data)


class JobResultView(APIView):
    def get(self, request, job_id):
        job = get_object_or_404(ExtractionJob, id=job_id)

        if job.status != "completed":
            return Response(
                {"error": "Job not completed"},
                status=status.HTTP_409_CONFLICT,
            )

        serializer = ExtractedRecordSerializer(job.records.all(), many=True)
        return Response(serializer.data)


class CancelJobView(APIView):
    def post(self, request, job_id):
        job = get_object_or_404(ExtractionJob, id=job_id)

        if job.status in ["completed", "failed"]:
            return Response(
                {"error": "Cannot cancel this job"},
                status=status.HTTP_409_CONFLICT,
            )

        job.status = "cancelled"
        job.save()
        return Response({"message": "Job cancelled"})


class RemoveJobView(APIView):
    def delete(self, request, job_id):
        job = get_object_or_404(ExtractionJob, id=job_id)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
