from django.conf.urls import url,include
from app.api.views import (CompanyListApi,ProductListApi,ProductSearch,ProductCreateAPIView,ProductDetailAPIView,
ProductListCreateAPIView,ProductRetrieveUpdateAPIView,ProductRetrieveDestroyAPIView,ProductRetrieveUpdateDestroyAPIView)

urlpatterns = [
    url(r'^company/', CompanyListApi.as_view()),
    url(r'^product/', ProductListApi.as_view()),
    url(r'^productsearch/', ProductSearch.as_view()),
    url(r'^productcreate/', ProductCreateAPIView.as_view()),
    url(r'^delete/(?P<id>\d+)/$', ProductDetailAPIView.as_view()),
    url(r'^listncreate/$', ProductListCreateAPIView.as_view()),
    url(r'^listnupdate/(?P<id>\d+)/$', ProductRetrieveUpdateAPIView.as_view()),
    url(r'^listndelete/(?P<id>\d+)/$', ProductRetrieveDestroyAPIView.as_view()),
    url(r'^listnupdatendelete/(?P<id>\d+)/$', ProductRetrieveUpdateDestroyAPIView.as_view()),





]