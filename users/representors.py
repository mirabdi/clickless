from core.representors import CustomRepresentor
from .models import User, SignInHistory, UserDelete, UserDeleteReason, AccessCode, CustomerInquiry
from django.db.models import Count, Avg, Min, Max, Q
from django.utils import timezone
from datetime import timedelta

class UserRepresentor(CustomRepresentor):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'gender', 'is_lock', 'nickname', 'aws_user_id', 'birth_date', 'created_at',
            # Related fields from habits app
            'habit_answers',
            # Related fields from surveys app
            'answers', 'pain_answers', 'diary_entries',
            # Related fields from pain_management app
            'pain_records',
            # Related fields from medications app
            'drugs',
            # Related fields from notifications app
            'notifications', 'notification_exclusions',
            # Related fields from exercises app
            'exercise_histories', 'exercise_times',
            # Related fields from content app
            'article_view_histories', 'education_video_view_histories', 'meditation_histories',
            # Related fields from users app
            'access_codes', 'customer_inquiries',
            # Stats field
            'stats'
        ]

    def get_stats(self, obj):
        """Calculate comprehensive user statistics."""
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)
        seven_days_ago = now - timedelta(days=7)
        
        stats = {
            # User account statistics
            'account': {
                'age_days': (now - obj.created_at).days if obj.created_at else 0,
                'is_locked': obj.is_lock == '1' if hasattr(obj, 'is_lock') else False,
                'has_birth_date': bool(obj.birth_date),
                'gender': obj.gender if hasattr(obj, 'gender') else None
            },
            
            # Survey and diary statistics
            'surveys': {
                'total_answers': obj.answers.count() if hasattr(obj, 'answers') else 0,
                'total_pain_answers': obj.pain_answers.count() if hasattr(obj, 'pain_answers') else 0,
                'total_diary_entries': obj.diary_entries.count() if hasattr(obj, 'diary_entries') else 0,
                'recent_answers_7d': obj.answers.filter(created_at__gte=seven_days_ago).count() if hasattr(obj, 'answers') else 0,
                'recent_answers_30d': obj.answers.filter(created_at__gte=thirty_days_ago).count() if hasattr(obj, 'answers') else 0,
                'avg_answer_value': obj.answers.aggregate(avg=Avg('value'))['avg'] if hasattr(obj, 'answers') and obj.answers.exists() else None,
                'unique_weeks': obj.answers.values('week').distinct().count() if hasattr(obj, 'answers') else 0
            },
            
            # Pain management statistics
            'pain': {
                'total_records': obj.pain_records.count() if hasattr(obj, 'pain_records') else 0,
                'recent_records_7d': obj.pain_records.filter(created_at__gte=seven_days_ago).count() if hasattr(obj, 'pain_records') else 0,
                'recent_records_30d': obj.pain_records.filter(created_at__gte=thirty_days_ago).count() if hasattr(obj, 'pain_records') else 0,
                'categories': list(obj.pain_records.values('category__name').annotate(count=Count('id')).values('category__name', 'count')) if hasattr(obj, 'pain_records') else [],
                'first_record': obj.pain_records.aggregate(first=Min('created_at'))['first'] if hasattr(obj, 'pain_records') and obj.pain_records.exists() else None,
                'last_record': obj.pain_records.aggregate(last=Max('created_at'))['last'] if hasattr(obj, 'pain_records') and obj.pain_records.exists() else None
            },
            
            # Medication statistics
            'medications': {
                'total_drugs': obj.drugs.count() if hasattr(obj, 'drugs') else 0,
                'active_drugs': obj.drugs.filter(finished_at__gt=now).count() if hasattr(obj, 'drugs') else 0,
                'completed_drugs': obj.drugs.filter(finished_at__lte=now).count() if hasattr(obj, 'drugs') else 0,
                'drug_types': list(obj.drugs.values('type').annotate(count=Count('id')).values('type', 'count')) if hasattr(obj, 'drugs') else [],
                'avg_drug_duration_days': self._calculate_avg_drug_duration(obj) if hasattr(obj, 'drugs') else None
            },
            
            # Notification statistics
            'notifications': {
                'total_notifications': obj.notifications.count() if hasattr(obj, 'notifications') else 0,
                'unread_notifications': obj.notifications.filter(is_read='0').count() if hasattr(obj, 'notifications') else 0,
                'read_notifications': obj.notifications.filter(is_read='1').count() if hasattr(obj, 'notifications') else 0,
                'notification_types': list(obj.notifications.values('type').annotate(count=Count('id')).values('type', 'count')) if hasattr(obj, 'notifications') else [],
                'recent_notifications_7d': obj.notifications.filter(created_at__gte=seven_days_ago).count() if hasattr(obj, 'notifications') else 0,
                'notification_exclusions': obj.notification_exclusions.count() if hasattr(obj, 'notification_exclusions') else 0
            },
            
            # Exercise statistics
            'exercises': {
                'total_exercise_histories': obj.exercise_histories.count() if hasattr(obj, 'exercise_histories') else 0,
                'face_exercises': obj.exercise_histories.filter(is_face=1).count() if hasattr(obj, 'exercise_histories') else 0,
                'non_face_exercises': obj.exercise_histories.filter(is_face=0).count() if hasattr(obj, 'exercise_histories') else 0,
                'exercise_times': obj.exercise_times.count() if hasattr(obj, 'exercise_times') else 0,
                'recent_exercises_7d': obj.exercise_histories.filter(created_at__gte=seven_days_ago).count() if hasattr(obj, 'exercise_histories') else 0,
                'recent_exercises_30d': obj.exercise_histories.filter(created_at__gte=thirty_days_ago).count() if hasattr(obj, 'exercise_histories') else 0,
                'avg_exercise_time': obj.exercise_times.aggregate(avg=Avg('time_since_midnight'))['avg'] if hasattr(obj, 'exercise_times') and obj.exercise_times.exists() else None
            },
            
            # Content engagement statistics
            'content': {
                'article_views': obj.article_view_histories.count() if hasattr(obj, 'article_view_histories') else 0,
                'video_views': obj.education_video_view_histories.count() if hasattr(obj, 'education_video_view_histories') else 0,
                'meditation_sessions': obj.meditation_histories.count() if hasattr(obj, 'meditation_histories') else 0,
                'recent_article_views_7d': obj.article_view_histories.filter(created_at__gte=seven_days_ago).count() if hasattr(obj, 'article_view_histories') else 0,
                'recent_video_views_7d': obj.education_video_view_histories.filter(created_at__gte=seven_days_ago).count() if hasattr(obj, 'education_video_view_histories') else 0,
                'recent_meditation_7d': obj.meditation_histories.filter(created_at__gte=seven_days_ago).count() if hasattr(obj, 'meditation_histories') else 0,
                'unique_articles_viewed': obj.article_view_histories.values('article').distinct().count() if hasattr(obj, 'article_view_histories') else 0,
                'unique_videos_viewed': obj.education_video_view_histories.values('video').distinct().count() if hasattr(obj, 'education_video_view_histories') else 0,
                'unique_meditations': obj.meditation_histories.values('meditation').distinct().count() if hasattr(obj, 'meditation_histories') else 0
            },
            
            # Habit statistics
            'habits': {
                'total_habit_answers': obj.habit_answers.count() if hasattr(obj, 'habit_answers') else 0,
                'habit_violations': sum(answer.violations.count() for answer in obj.habit_answers.all()) if hasattr(obj, 'habit_answers') else 0,
                'recent_habit_answers_7d': obj.habit_answers.filter(created_at__gte=seven_days_ago).count() if hasattr(obj, 'habit_answers') else 0,
                'recent_habit_answers_30d': obj.habit_answers.filter(created_at__gte=thirty_days_ago).count() if hasattr(obj, 'habit_answers') else 0,
                'unique_habits': obj.habit_answers.values('habit').distinct().count() if hasattr(obj, 'habit_answers') else 0
            },
            
            # User activity statistics
            'activity': {
                'access_codes': obj.access_codes.count() if hasattr(obj, 'access_codes') else 0,
                'activated_access_codes': obj.access_codes.filter(activated_at__isnull=False).count() if hasattr(obj, 'access_codes') else 0,
                'customer_inquiries': obj.customer_inquiries.count() if hasattr(obj, 'customer_inquiries') else 0,
                'recent_inquiries_30d': obj.customer_inquiries.filter(created_at__gte=thirty_days_ago).count() if hasattr(obj, 'customer_inquiries') else 0,
                'last_activity': self._get_last_activity(obj),
                'engagement_score': self._calculate_engagement_score(obj)
            }
        }
        
        return stats
    
    def _calculate_avg_drug_duration(self, obj):
        """Calculate average drug duration in days."""
        if not hasattr(obj, 'drugs') or not obj.drugs.exists():
            return None
        
        total_duration = 0
        valid_drugs = 0
        
        for drug in obj.drugs.all():
            if drug.created_at and drug.finished_at:
                duration = (drug.finished_at - drug.created_at).days
                if duration > 0:
                    total_duration += duration
                    valid_drugs += 1
        
        return round(total_duration / valid_drugs, 1) if valid_drugs > 0 else None
    
    def _get_last_activity(self, obj):
        """Get the most recent activity timestamp across all user activities."""
        activities = []
        
        if hasattr(obj, 'answers') and obj.answers.exists():
            activities.append(obj.answers.aggregate(last=Max('created_at'))['last'])
        
        if hasattr(obj, 'pain_records') and obj.pain_records.exists():
            activities.append(obj.pain_records.aggregate(last=Max('created_at'))['last'])
        
        if hasattr(obj, 'exercise_histories') and obj.exercise_histories.exists():
            activities.append(obj.exercise_histories.aggregate(last=Max('created_at'))['last'])
        
        if hasattr(obj, 'article_view_histories') and obj.article_view_histories.exists():
            activities.append(obj.article_view_histories.aggregate(last=Max('created_at'))['last'])
        
        if hasattr(obj, 'habit_answers') and obj.habit_answers.exists():
            activities.append(obj.habit_answers.aggregate(last=Max('created_at'))['last'])
        
        return max(activities) if activities else None
    
    def _calculate_engagement_score(self, obj):
        """Calculate a simple engagement score based on recent activity."""
        score = 0
        now = timezone.now()
        seven_days_ago = now - timedelta(days=7)
        thirty_days_ago = now - timedelta(days=30)
        
        # Recent survey activity (7 days)
        if hasattr(obj, 'answers'):
            recent_answers = obj.answers.filter(created_at__gte=seven_days_ago).count()
            score += min(recent_answers * 2, 20)  # Max 20 points
        
        # Recent pain records (7 days)
        if hasattr(obj, 'pain_records'):
            recent_pain = obj.pain_records.filter(created_at__gte=seven_days_ago).count()
            score += min(recent_pain * 3, 15)  # Max 15 points
        
        # Recent exercise activity (7 days)
        if hasattr(obj, 'exercise_histories'):
            recent_exercise = obj.exercise_histories.filter(created_at__gte=seven_days_ago).count()
            score += min(recent_exercise * 2, 20)  # Max 20 points
        
        # Content engagement (30 days)
        if hasattr(obj, 'article_view_histories'):
            recent_articles = obj.article_view_histories.filter(created_at__gte=thirty_days_ago).count()
            score += min(recent_articles, 10)  # Max 10 points
        
        if hasattr(obj, 'meditation_histories'):
            recent_meditation = obj.meditation_histories.filter(created_at__gte=thirty_days_ago).count()
            score += min(recent_meditation * 2, 10)  # Max 10 points
        
        # Habit tracking (7 days)
        if hasattr(obj, 'habit_answers'):
            recent_habits = obj.habit_answers.filter(created_at__gte=seven_days_ago).count()
            score += min(recent_habits, 15)  # Max 15 points
        
        return min(score, 100)  # Cap at 100

class SignInHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = SignInHistory
        fields = ['id', 'device_name', 'device_token', 'email', 'language', 'os', 'status', 'created_at']

class UserDeleteRepresentor(CustomRepresentor):
    class Meta:
        model = UserDelete
        fields = ['user', 'reason', 'created_at', 'updated_at']

class UserDeleteReasonRepresentor(CustomRepresentor):
    class Meta:
        model = UserDeleteReason
        fields = ['id', 'reason', 'created_at', 'orders']

class AccessCodeRepresentor(CustomRepresentor):
    class Meta:
        model = AccessCode
        fields = ['access_code', 'created_at', 'expired_at', 'user', 'activated_at', 'completed_survey_week']

class CustomerInquiryRepresentor(CustomRepresentor):
    class Meta:
        model = CustomerInquiry
        fields = ['id', 'created_at', 'inquiry', 'user'] 