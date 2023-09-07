
from django.urls import path

from filoksenia import views
app_name='filoksenia'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('slug/<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='ProCatDetail')
]

