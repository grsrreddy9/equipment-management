import uuid
from django.db import models
from Main.models import ProductGranulation, User


class CleanType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clean_type = models.CharField(max_length=50)


class CleaningDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clean_type = models.ForeignKey(CleanType, on_delete=models.DO_NOTHING)
    equipment_cleaned_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_equipment_cleaned_by')
    equipment_cleaned_on = models.DateTimeField()
    room_cleaned_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_room_cleaned_by')
    room_cleaned_on = models.DateTimeField()
    product_details = models.ForeignKey(ProductGranulation, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        permissions = [('can_create_cleaning_details', 'Can create cleaning details')]


class LogBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qa_checked_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_qa_checked', blank=True, null=True)
    qa_checked_on = models.DateTimeField(blank=True, null=True)
    product_details = models.ForeignKey(ProductGranulation, on_delete=models.DO_NOTHING, blank=True, null=True)
    cleaning_details = models.ForeignKey(CleaningDetail, on_delete=models.DO_NOTHING, blank=True, null=True)
    cleaning_checked_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_cleaning_checked', null=True, blank=True)
    cleaning_checked_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        permissions = [
            ('qa_checking', 'Can authorize new product production'),
            ('cleaning_verification', 'Can verify cleaning')
        ]
