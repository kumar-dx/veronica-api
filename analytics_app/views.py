from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from django.utils import timezone
from .models import VisitorRecord
from .serializers import VisitorRecordSerializer

API_VERSION = "1.0"

def create_response(data=None, message=None, error=None, status_code=status.HTTP_200_OK):
    """Helper function to create standardized API responses"""
    response = {
        "version": API_VERSION,
        "timestamp": timezone.now().isoformat(),
        "status": "success" if error is None else "error"
    }
    
    if data is not None:
        response["data"] = data
    if message is not None:
        response["message"] = message
    if error is not None:
        response["error"] = error
        
    return Response(response, status=status_code)

@api_view(['GET'])
def home(request):
    """
    API Documentation
    
    Base URL: /api/v1/analytics/
    
    Available Endpoints:
    1. POST /visitors/
       Record visitor analytics from face detection
       Payload: {
           "unique_faces_count": int,
           "store_id": int
       }
       
    2. GET /records/
       Retrieve all visitor records
       
    3. GET /stores/metrics/?store_id=<store_id>&date=<date>
       Get analytics metrics for a specific store
       Query Parameters:
       - store_id: Store identifier (required)
       - date: Date filter in YYYY-MM-DD format (optional)
    """
    return create_response(
        data={
            'version': API_VERSION,
            'description': 'Store Analytics API',
            'endpoints': {
                'Record Visitors': '/api/v1/analytics/visitors/',
                'List Records': '/api/v1/analytics/records/',
                'Store Metrics': '/api/v1/analytics/stores/metrics/',
            }
        },
        message="Welcome to Store Analytics API"
    )

@api_view(['POST'])
def track_visitors(request):
    """
    Record visitor analytics from face detection system.
    
    Payload:
    {
        "unique_faces_count": int,  # Number of unique faces detected
        "store_id": int            # Store identifier
    }
    
    Returns:
    - 201: Record created successfully
    - 400: Invalid request data
    """
    try:
        data = request.data
        if isinstance(data, list):
            data = data[0]
            
        # Validate required fields
        required_fields = ['store_id', 'unique_faces_count']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return create_response(
                error=f"Missing required fields: {', '.join(missing_fields)}",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        # Create record
        record = VisitorRecord.objects.create(
            store_id=str(data['store_id']),
            date=timezone.now().date(),
            unique_visitors=data['unique_faces_count']
        )
        
        serializer = VisitorRecordSerializer(record)
        return create_response(
            data=serializer.data,
            message="Visitor record created successfully",
            status_code=status.HTTP_201_CREATED
        )
    
    except Exception as e:
        return create_response(
            error=str(e),
            status_code=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET"])
def list_records(request):
    """
    Retrieve all visitor records.
    
    Returns:
    - 200: List of all records
    - 500: Server error
    """
    try:
        all_records = VisitorRecord.objects.all()
        serializer = VisitorRecordSerializer(all_records, many=True)
        return create_response(
            data=serializer.data,
            message=f"Retrieved {len(all_records)} records"
        )
    except Exception as e:
        return create_response(
            error=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["GET"])
def store_unique_visitors(request):
    """
    Get analytics metrics for a specific store.
    
    Query Parameters:
    - store_id: Store identifier (required)
    - date: Optional date filter (YYYY-MM-DD format)
    
    Returns:
    - 200: Store metrics
    - 400: Missing store_id or invalid date format
    - 404: Store not found
    - 500: Server error
    """
    try:
        # Get and validate store_id
        store_id = request.query_params.get('store_id')
        if not store_id:
            return create_response(
                error="store_id query parameter is required",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # Check if store exists
        if not VisitorRecord.objects.filter(store_id=store_id).exists():
            return create_response(
                error=f"No records found for store {store_id}",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        # Base query
        query = VisitorRecord.objects.filter(store_id=store_id)
        
        # Apply date filter if provided
        date_str = request.query_params.get('date')
        if date_str:
            try:
                query = query.filter(date=date_str)
            except ValueError:
                return create_response(
                    error="Invalid date format. Use YYYY-MM-DD",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        
        # Get total visitors
        total_visitors = query.aggregate(
            total=models.Sum('unique_visitors')
        )['total'] or 0
        
        response_data = {
            'store_id': store_id,
            'unique_visitors': total_visitors,
            'last_updated': timezone.now().isoformat()
        }
        
        # Add date info if filtered
        if date_str:
            response_data['date'] = date_str
        
        return create_response(data=response_data)
    except Exception as e:
        return create_response(
            error=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
