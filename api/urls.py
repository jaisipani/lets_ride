from django.urls import path
from . import views

urlpatterns=[
    path('asset-transportation-request/create',views.AssetTransportationRequestCreateView.as_view(),name='asset_transportation_request_create' ),
    path('travel-info/share',views.TravelInfoShareView.as_view(),name='share_travel_info'),
    path('asset-transportation-request/list', views.AssetTransportationRequestListView.as_view(),name='asset_transportation_request_list'),
    path('asset-transportation-ride/list', views.AssetTransportationRidesListView.as_view(), name='asset_transportation_ride_list'),
    path('travel-info/apply',views.TravelInfoApplyView.as_view(),name='apply_travel_info'),
]
