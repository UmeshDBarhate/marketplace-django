from django.urls import path
from . import views 

app_name= 'conversation'

urlpatterns = [
    path('',views.inbox, name='inbox'),
    path('<int:pk>/',views.detail,name='detail'),
    #we send primary key of product to get product image 
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]
