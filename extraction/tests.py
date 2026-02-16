from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class ExtractionTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_start_job(self):
        response = self.client.post("/api/v1/scan/start", {"api_token": "test"})
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn("job_id", response.data)
