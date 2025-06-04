from django.db import models

# Create your models here.

class Drug(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_drug'

class DrugDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    drug_id = models.BigIntegerField()
    time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_drug_detail'

class DrugType(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    orders = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'v2_drug_type'
