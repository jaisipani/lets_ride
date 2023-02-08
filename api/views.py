from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AssetTransportRequest, ShareTravelInfo
from .serializers import AssetTransportRequestSerializer, ShareTravelInfoSerializer, MatchedRidesSerializer
from rest_framework.pagination import LimitOffsetPagination
from datetime import datetime
from .helpers import get_pagination


class AssetTransportationRequestCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = AssetTransportRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TravelInfoShareView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ShareTravelInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AssetTransportationRequestListView(APIView):

    def get(self, request, *args, **kwargs):
        AssetTransportRequest.objects.filter(date_time__gt=datetime.now()).update(status='EXPIRED')
        asset_requests = AssetTransportRequest.objects.all()

        status = request.query_params.get('status', None)
        page_index = request.query_params.get('page_index', None)
        page_size = request.query_params.get('page_size', None)
        sort = request.query_params.get('sort', None)
        if status:
            asset_requests = asset_requests.filter(status__icontains=status)

        asset_type = request.query_params.get('asset_type', None)
        if asset_type:
            asset_requests = asset_requests.filter(asset_type__icontains=asset_type)
        if sort == 'asc':
            asset_requests = asset_requests.order_by('date_time')
        elif sort == 'desc':
            asset_requests = asset_requests.order_by('-date_time')
        data = get_pagination(asset_requests, page_index, page_size)

        serializer = AssetTransportRequestSerializer(data['queryset'], many=True)

        return Response(serializer.data, status=200)


class AssetTransportationRidesListView(APIView):

    def get(self, request, *args, **kwargs):
        requester_requests = AssetTransportRequest.objects.filter(
            status='pending',
            from_location=request.query_params.get('from_location', None),
            to_location=request.query_params.get('to_location', None),
            date_time=request.query_params.get('date_time', None),
        )
        page_index = request.query_params.get('page_index', None)
        page_size = request.query_params.get('page_size', None)
        matched_rides = []
        for requester_request in requester_requests:
            rides = ShareTravelInfo.objects.filter(
                from_location=requester_request.from_location,
                to_location=requester_request.to_location,
                date_time=requester_request.date_time,
            )
            matched_rides.extend(rides)

        data = get_pagination(matched_rides, page_index, page_size)
        serializer = MatchedRidesSerializer(data['queryset'], many=True)

        return Response(serializer.data, status=200)


class TravelInfoApplyView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            travel_info = ShareTravelInfo.objects.get(id=request.data.get('id'))
        except:
            return Response({'message':'Travel info not found'}, status=404)
        travel_info.status = 'APPLIED'
        travel_info.save()
        return Response({'message':'Travel info Applied'}, status=200)
