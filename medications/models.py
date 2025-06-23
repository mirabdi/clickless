from django.db import models
from core.models import CustomModel
from users.models import User

# Create your models here.
class Drug(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='drugs')
    name = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_drug'

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.user.email}"

class DrugDetail(CustomModel):
    id = models.BigAutoField(primary_key=True)
    drug = models.ForeignKey(Drug, models.DO_NOTHING, related_name='details')
    time = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_drug_detail'

    def __str__(self):
        return f"Drug Detail {self.id} - {self.drug.name} at time {self.time}"

class DrugType(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    orders = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'v2_drug_type'

    def __str__(self):
        return self.type
