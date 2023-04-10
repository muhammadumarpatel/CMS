from django import forms
from .models import Coupon

class BulkCouponForm(forms.Form):
    number_of_coupons = forms.IntegerField(min_value=1, initial=1, required=True)
    start_date = forms.DateTimeField(required=True)
    expiry_date = forms.DateTimeField(required=True)
    scheme_details = forms.CharField(widget=forms.Textarea, required=True)
    created_by = forms.CharField(max_length=100, required=True)
    redeemable_count = forms.IntegerField(min_value=1, initial=1, required=True)
