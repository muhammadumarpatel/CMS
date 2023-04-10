from django.db import models
from django.utils.crypto import get_random_string

class Coupon(models.Model):
    coupon_code = models.CharField(max_length=10, unique=True)
    start_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    scheme_details = models.TextField()
    created_by = models.CharField(max_length=100)
    redeemable_count = models.PositiveIntegerField()
    redeemed_count = models.PositiveIntegerField(default=0)

    @staticmethod
    def generate_unique_code():
        unique = False
        while not unique:
            code = get_random_string(length=10)
            unique = not Coupon.objects.filter(coupon_code=code).exists()
        return code

    def __str__(self):
        return self.coupon_code
