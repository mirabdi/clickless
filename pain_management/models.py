from django.db import models
from core.models import CustomModel
from users.models import User
from content.models import Article, ArticleCategory

# Create your models here.

class Pain(CustomModel):
    id = models.BigAutoField(primary_key=True)
    answer = models.ForeignKey('PainAnswer', models.DO_NOTHING, db_column='answer_id', blank=True, null=True, related_name='pain_records')
    category = models.ForeignKey('PainCategory', models.DO_NOTHING, db_column='category_id', related_name='pain_records')
    content = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='pain_records')
    feedback = models.ForeignKey('PainFeedback', models.DO_NOTHING, db_column='feedback_id', related_name='pain_records')

    class Meta:
        
        db_table = 'v2_pain'

    def __str__(self):
        return f"Pain {self.id} - User: {self.user.email}, Category: {self.category.name}"

class PainAnswer(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=50)
    orders = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey('PainCategory', models.DO_NOTHING, blank=True, null=True, related_name='pain_answers')
    article_category = models.ForeignKey(ArticleCategory, models.DO_NOTHING, db_column='article_category_id', related_name='pain_answers')
    has_text_area = models.TextField()  # This field type is a guess.

    class Meta:
        
        db_table = 'v2_pain_answer'

    def __str__(self):
        return f"{self.name} ({self.article_category.name})"

class PainArea(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=15)
    is_right = models.TextField()  # This field type is a guess.
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        
        db_table = 'v2_pain_area'

    def __str__(self):
        return f"{self.name} (Right: {self.is_right}, Position: {self.x}, {self.y})"

class PainAreaDetail(CustomModel):
    id = models.BigAutoField(primary_key=True)
    area = models.ForeignKey(PainArea, models.DO_NOTHING, db_column='area_id', related_name='area_details')
    created_at = models.DateTimeField()
    value = models.IntegerField()
    pain = models.ForeignKey(Pain, models.DO_NOTHING, blank=True, null=True, related_name='area_details')

    class Meta:
        
        db_table = 'v2_pain_area_detail'

    def __str__(self):
        return f"Pain Area Detail {self.id} - Area: {self.area.name}, Value: {self.value}"

class PainArticle(CustomModel):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(Article, models.DO_NOTHING, db_column='article_id', related_name='pain_articles')
    created_at = models.DateTimeField()
    pain = models.ForeignKey(Pain, models.DO_NOTHING, blank=True, null=True, related_name='pain_articles')

    class Meta:
        
        db_table = 'v2_pain_article'

    def __str__(self):
        return f"Pain Article {self.id} - {self.article.title}"

class PainCategory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=50)
    orders = models.IntegerField(blank=True, null=True)
    question = models.ForeignKey('PainQuestion', models.DO_NOTHING, db_column='question_id', blank=True, null=True, related_name='pain_categories')

    class Meta:
        
        db_table = 'v2_pain_category'

    def __str__(self):
        return self.name

class PainFeedback(CustomModel):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    category = models.ForeignKey(PainCategory, models.DO_NOTHING, db_column='category_id', related_name='pain_feedbacks')

    class Meta:
        
        db_table = 'v2_pain_feedback'

    def __str__(self):
        return f"{self.content} ({self.category.name})"

class PainQuestion(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'v2_pain_question'

    def __str__(self):
        return self.name or f"Pain Question {self.id}"
