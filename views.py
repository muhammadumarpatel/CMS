from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import qrcode
from io import BytesIO
from django.core.files import File
from .models import Coupon
from .forms import BulkCouponForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ...

def redeem_coupon(request, coupon_code):
    coupon = get_object_or_404(Coupon, coupon_code=coupon_code)
    
    if request.method == 'POST':
        customer_mobile = request.POST.get('customer_mobile')
        distributor_code = request.POST.get('distributor_code')

        if coupon.redeemed_count < coupon.redeemable_count:
            coupon.redeemed_count += 1
            coupon.save()

            # Save customer mobile and distributor code, you may need to create a new model for this
            # ...

            return render(request, 'coupons/redeem_coupon_success.html')
        else:
            return render(request, 'coupons/redeem_coupon_failure.html')

    context = {
        'coupon': coupon
    }

    return render(request, 'coupons/redeem_coupon.html', context)
