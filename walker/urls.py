from django.urls import path
from . import views

app_name = "walker"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail_algorithm/", views.detail_algorithm, name="detail_algorithm"),
    path("detail_one/", views.detail_one, name="detail_one"),
    path("detail_two/", views.detail_two, name="detail_two"),
    path("detail_three/", views.detail_three, name="detail_three"),
    path("detail_four/", views.detail_four, name="detail_four"),
    path("detail_five/", views.detail_five, name="detail_five"),
    path("detail_six/", views.detail_six, name="detail_six"),
    path("detail_seven/", views.detail_seven, name="detail_seven"),
    path("detail_eight/", views.detail_eight, name="detail_eight"),
    path("detail_nine/", views.detail_nine, name="detail_nine"),
    path("detail_ten/", views.detail_ten, name="detail_ten"),
    path("detail_eleven/", views.detail_eleven, name="detail_eleven"),
    path("purchase/", views.purchase, name="purchase"),
    path('address/', views.save_address, name='address'),
]