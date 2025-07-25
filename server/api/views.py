import csv
import io
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status


class VehicleUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        # take CSV file from the request
        csv_file = request.FILES.get('file')
        if not csv_file:
            return Response({"error": "CSV file is required."}, status=400)

        # Read the CSV file
        decoded_file = csv_file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(decoded_file), delimiter=';')
        csv_data = list(reader)

        #Take access token from Baubuddy API
        login_url = "https://api.baubuddy.de/index.php/login"
        login_payload = {
            "username": "365",
            "password": "1"
        }
        login_headers = {
            "Authorization": "Basic QVBJX0V4cGxvcmVyOjEyMzQ1NmlzQUxhbWVQYXNz",
            "Content-Type": "application/json"
        }
        login_response = requests.post(login_url, json=login_payload, headers=login_headers)
        token = login_response.json().get("oauth", {}).get("access_token")

        if not token:
            return Response({"error": "Failed to authenticate with Baubuddy API"}, status=500)

        # Fetch vehicle data

        vehicle_url = "https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active"
        auth_headers = {
            "Authorization": f"Bearer {token}"
        }
        vehicle_response = requests.get(vehicle_url, headers=auth_headers)
        vehicles = vehicle_response.json()

        # Keep only entries where the 'hu' field is not null

        filtered = [v for v in vehicles if v.get("hu")]

        # Resolve labelIds
        for v in filtered:
            label_ids = v.get("labelIds")
            if label_ids:
                if isinstance(label_ids, str):
                    label_ids = [int(id.strip()) for id in label_ids.split(",")]
                resolved_colors = []
                for lid in label_ids:
                    label_url = f"https://api.baubuddy.de/dev/index.php/v1/labels/{lid}"
                    label_resp = requests.get(label_url, headers=auth_headers)
                    if label_resp.status_code == 200:
                        label_data = label_resp.json()
                        if "colorCode" in label_data:
                            resolved_colors.append(label_data["colorCode"])
                v["resolvedColorCodes"] = resolved_colors
            else:
                v["resolvedColorCodes"] = []

        return Response(filtered, status=200)
