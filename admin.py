from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_code', 'start_date', 'expiry_date', 'scheme_details', 'created_by', 'redeemable_count', 'redeemed_count')
