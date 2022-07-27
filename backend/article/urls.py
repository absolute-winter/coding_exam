from django.urls import path
from .views import ArticleList, ArticleCreate, ArticleDetail, ArticleEdit, ArticleDelete

urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('create/', ArticleCreate.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('edit/<int:pk>', ArticleEdit.as_view(), name='edit'),
    path('delete/<int:pk>', ArticleDelete.as_view(), name='delete')
]