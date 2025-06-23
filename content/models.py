from django.db import models
from core.models import CustomModel
from users.models import User

# Create your models here.

class Article(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    title = models.CharField(max_length=255)
    orders = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey('ArticleCategory', models.DO_NOTHING, blank=True, null=True, related_name='articles')

    class Meta:
        
        db_table = 'v2_article'

    def __str__(self):
        return f"{self.title} ({self.category.name if self.category else 'No category'})"

class ArticleCategory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    orders = models.IntegerField(blank=True, null=True)
    is_common = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        
        db_table = 'v2_article_category'

    def __str__(self):
        return self.name

class ArticleDetail(CustomModel):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(Article, models.DO_NOTHING, db_column='article_id', related_name='details')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    image = models.CharField(max_length=255)
    orders = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'v2_article_detail'

    def __str__(self):
        return f"{self.title} - {self.article.title}"

class ArticleViewHistory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(Article, models.DO_NOTHING, db_column='article_id', related_name='view_histories')
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='article_view_histories')

    class Meta:
        
        db_table = 'v2_article_view_history'

    def __str__(self):
        return f"Article View - {self.article.title} by {self.user.email}"

class Banner(CustomModel):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=200)
    background_color = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    orders = models.IntegerField()
    route = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    index = models.IntegerField(blank=True, null=True)
    background_color_swatch = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        
        db_table = 'v2_banner'

    def __str__(self):
        return f"{self.title} - {self.subtitle}"

class ConfidentialTerm(CustomModel):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    type = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'v2_confidential_term'

    def __str__(self):
        return f"Confidential Term - {self.type}"

class EducationVideo(CustomModel):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_education_video'

    def __str__(self):
        return f"{self.title}"

class EducationVideoViewHistory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='education_video_view_histories')
    video = models.ForeignKey(EducationVideo, models.DO_NOTHING, related_name='view_histories')
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_education_video_view_history'

    def __str__(self):
        return f"Video View - {self.video.title} by {self.user.email}"

class Faq(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    answer = models.CharField(max_length=500, blank=True, null=True)
    orders = models.IntegerField()
    question = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'v2_faq'

    def __str__(self):
        return f"{self.question or 'No question'}"

class MedicalDevice(CustomModel):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    is_markdown = models.IntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)
    orders = models.IntegerField()

    class Meta:
        
        db_table = 'v2_medical_device'

    def __str__(self):
        return f"{self.label or 'Medical Device'}"

class Meditation(CustomModel):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=100)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        
        db_table = 'v2_meditation'

    def __str__(self):
        return f"{self.title} ({self.type or 'No type'})"

class MeditationHistory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    meditation = models.ForeignKey(Meditation, models.DO_NOTHING, related_name='histories')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='meditation_histories')
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_meditation_history'

    def __str__(self):
        return f"Meditation History - {self.meditation.title} by {self.user.email}"

class Notice(CustomModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'v2_notice'

    def __str__(self):
        return self.title

class PrivacyPolicy(CustomModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'v2_privacy_policy'

    def __str__(self):
        return self.title

class Term(CustomModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'v2_term'

    def __str__(self):
        return self.title
