from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('create_bulk_coupons/', views.create_bulk_coupons, name='create_bulk_coupons'),
    path('generate_qr_codes/', views.generate_qr_codes, name='generate_qr_codes'),
    path('redeem_coupon/<str:coupon_code>/', views.redeem_coupon, name='redeem_coupon'),
]
