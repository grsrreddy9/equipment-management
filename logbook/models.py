import uuid
from django.db import models
from Main.models import ProductGranulation, User


class CleanType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clean_type = models.CharField(max_length=50)


class LogBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qa_checked_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_qa_checked')
    qa_checked_on = models.DateTimeField()
    product_details = models.ForeignKey(ProductGranulation, on_delete=models.DO_NOTHING)
    clean_type = models.ForeignKey(CleanType, on_delete=models.DO_NOTHING)
    equipment_cleaned_on = models.DateTimeField()
    room_cleaned_on = models.DateTimeField()
    equipment_clean_done_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_equipment_clean_done')
    room_clean_done_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_room_clean_done')
    cleaning_checked_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_cleaning_checked')
