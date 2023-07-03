from django.urls import path
from .views import AdList, AdDetail, AdCreate, AdEdit, AdDelete


urlpatterns = [
    path('', AdList.as_view(), name='ad_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad_detail'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/edit/', AdEdit.as_view(), name='ad_edit'),
    path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
]
