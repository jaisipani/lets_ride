from django.urls import path
from . import views

urlpatterns=[
    path('asset-transportation-request/create',views.AssetTransportationRequestCreateView.as_view(),name='asset_transportation_request_create' ), #creating transportation requests
    path('travel-info/share',views.TravelInfoShareView.as_view(),name='share_travel_info'), #rider can shares his travel info
    path('asset-transportation-request/list', views.AssetTransportationRequestListView.as_view(),name='asset_transportation_request_list'), #listing all the transportation requests
    path('asset-transportation-ride/list', views.AssetTransportationRidesListView.as_view(), name='asset_transportation_ride_list'), #lists all the riders going from the location passed in query params
    path('travel-info/apply',views.TravelInfoApplyView.as_view(),name='apply_travel_info'), #requester can apply for his studd to be carried by a rider (need to pass rider ID as a param)
]
