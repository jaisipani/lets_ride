from django.db import models
# import datetime

# class Rider(models.Model):
#     from_location = models.CharField(max_length=255)
#     to_location = models.CharField(max_length=255)
#     date_time = models.DateTimeField()
#     flexible_timings = models.BooleanField(default=False)
#     travel_medium = models.CharField(max_length=20)
#     asset_quantity = models.PositiveIntegerField()
    
#     def __str__(self):
#         return f'Rider from {self.from_location} to {self.to_location} on {self.date_time}'
    

# class Requester(models.Model):
#     from_location = models.CharField(max_length=255)
#     to_location = models.CharField(max_length=255)
#     date_time = models.DateTimeField()
#     flexible_timings = models.BooleanField(default=False)
#     no_of_assets = models.PositiveIntegerField()
#     asset_type = models.CharField(max_length=20)
#     asset_sensitivity = models.CharField(max_length=20)
#     whom_to_deliver = models.CharField(max_length=255)
#     status = models.CharField(max_length=20, default='Pending')
    
#     def __str__(self):
#         return f'Requester from {self.from_location} to {self.to_location} on {self.date_time}'
    

# class Match(models.Model):
#     requester = models.ForeignKey(Requester, on_delete=models.CASCADE)
#     rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, default='NOT_APPLIED')
    
#     def __str__(self):
#         return f'Match between requester {self.requester.id} and rider {self.rider.id}'


class AssetTransportRequest(models.Model):
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)
    flexible_timings = models.BooleanField(default=False)
    no_of_assets = models.PositiveSmallIntegerField()
    asset_type = models.CharField(max_length=50, choices=(
        ('LAPTOP', 'laptop'),
        ('TRAVEL_BAG', 'travel bag'),
        ('PACKAGE', 'package')
    ))
    asset_sensitivity = models.CharField(max_length=50, choices=(
        ('HIGHLY_SENSITIVE', 'highly sensitive'),
        ('SENSITIVE', 'sensitive'),
        ('NORMAL', 'normal')
    ))
    whom_to_deliver = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='PENDING', choices=(
        ('PENDING', 'pending'),
        ('EXPIRED', 'expired')
    ))


    def __str__(self):
        return f"AssetTransportRequest from {self.from_location} to {self.to_location} on {self.date_time}"


class ShareTravelInfo(models.Model):
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    flexible_timings = models.BooleanField(default=False)
    travel_medium = models.CharField(max_length=50, choices=(
        ('BUS', 'bus'),
        ('CAR', 'car'),
        ('TRAIN', 'train')
    ))
    asset_quantity = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=50, default='NOT_APPLIED', choices=(
        ('NOT_APPLIED', 'Not Applied'),
        ('APPLIED', 'Applied')
    ))
    def __str__(self):
        return f"ShareTravelInfo from {self.from_location} to {self.to_location} on {self.date_time} by {self.travel_medium}"
