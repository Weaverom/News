from django.urls import path
from .views import NewsList, PostList, PostSearch, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
   path('', NewsList.as_view(), name='post_list'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:pk>', PostList.as_view(), name='post_detail'),
   path('create/', NewsCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
]
