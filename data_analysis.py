import os
import django
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import openpyxl
from openpyxl.styles import PatternFill, Font
from django.db import connection
from django.db.models import Count, Avg, F, Q
from django.utils import timezone
import pytz

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clickless.settings')
django.setup()

# Import models
from pain_management.models import Pain, PainCategory, PainArea, PainAreaDetail
from exercises.models import Exercise, ExerciseHistory, ExerciseTime
from users.models import User
from surveys.models import Survey, Answer

def analyze_pain_patterns():
    """Analyze pain patterns and correlations"""
    # Pain frequency by category
    pain_by_category = Pain.objects.filter(
        deleted_at__isnull=True
    ).values(
        'category_id'
    ).annotate(
        count=Count('id')
    ).order_by('-count')
    
    # Get category names
    category_names = {pc.id: pc.name for pc in PainCategory.objects.all()}
    pain_by_category = pd.DataFrame(pain_by_category)
    pain_by_category['category_name'] = pain_by_category['category_id'].map(category_names)
    
    # Pain intensity over time
    pain_intensity = PainAreaDetail.objects.filter(
        deleted_at__isnull=True
    ).values(
        'created_at__date'
    ).annotate(
        avg_intensity=Avg('value')
    ).order_by('created_at__date')
    
    # Pain location analysis
    pain_locations = PainAreaDetail.objects.filter(
        deleted_at__isnull=True
    ).values(
        'area_id'
    ).annotate(
        count=Count('id')
    ).order_by('-count')
    
    # Get area names
    area_names = {pa.id: pa.name for pa in PainArea.objects.all()}
    pain_locations = pd.DataFrame(pain_locations)
    pain_locations['area_name'] = pain_locations['area_id'].map(area_names)
    
    return {
        'by_category': pain_by_category,
        'intensity': pd.DataFrame(pain_intensity),
        'locations': pain_locations
    }

def analyze_exercise_patterns():
    """Analyze exercise patterns and user engagement"""
    # Exercise completion rates by type
    exercise_stats = []
    for exercise_type in Exercise.objects.filter(deleted_at__isnull=True).values_list('type', flat=True).distinct():
        exercises = Exercise.objects.filter(type=exercise_type, deleted_at__isnull=True)
        completions = ExerciseHistory.objects.filter(exercise_id__in=exercises.values_list('id', flat=True)).count()
        exercise_stats.append({
            'type': exercise_type,
            'total_exercises': exercises.count(),
            'completions': completions
        })
    
    # Exercise timing patterns
    exercise_times = ExerciseTime.objects.values(
        'time_since_midnight'
    ).annotate(
        count=Count('id')
    ).order_by('time_since_midnight')
    
    # User engagement with exercises
    user_engagement = []
    for user_id in ExerciseHistory.objects.values_list('user_id', flat=True).distinct():
        user_exercises = ExerciseHistory.objects.filter(user_id=user_id)
        user_engagement.append({
            'user_id': user_id,
            'total_exercises': user_exercises.count(),
            'face_exercises': user_exercises.filter(is_face=True).count()
        })
    
    return {
        'completion_rates': pd.DataFrame(exercise_stats),
        'timing_patterns': pd.DataFrame(exercise_times),
        'user_engagement': pd.DataFrame(user_engagement)
    }

def analyze_user_behavior():
    """Analyze user behavior and engagement patterns"""
    # User activity patterns
    user_activity = []
    for user in User.objects.filter(deleted_at__isnull=True):
        pain_entries = Pain.objects.filter(user_id=user.id, deleted_at__isnull=True).count()
        exercise_completions = ExerciseHistory.objects.filter(user_id=user.id).count()
        survey_responses = Answer.objects.filter(user_id=user.id).count()
        
        user_activity.append({
            'user_id': user.id,
            'email': user.email,
            'pain_entries': pain_entries,
            'exercise_completions': exercise_completions,
            'responses': survey_responses
        })
    
    # User retention analysis
    retention_data = []
    for user in User.objects.filter(deleted_at__isnull=True):
        first_activity = min(
            Pain.objects.filter(user_id=user.id, deleted_at__isnull=True).values_list('created_at', flat=True).first() or timezone.now(),
            ExerciseHistory.objects.filter(user_id=user.id).values_list('created_at', flat=True).first() or timezone.now(),
            Answer.objects.filter(user_id=user.id).values_list('created_at', flat=True).first() or timezone.now()
        )
        last_activity = max(
            Pain.objects.filter(user_id=user.id, deleted_at__isnull=True).values_list('created_at', flat=True).last() or timezone.now(),
            ExerciseHistory.objects.filter(user_id=user.id).values_list('created_at', flat=True).last() or timezone.now(),
            Answer.objects.filter(user_id=user.id).values_list('created_at', flat=True).last() or timezone.now()
        )
        # Make datetimes timezone-unaware
        if hasattr(first_activity, 'tzinfo') and first_activity.tzinfo is not None:
            first_activity = first_activity.replace(tzinfo=None)
        if hasattr(last_activity, 'tzinfo') and last_activity.tzinfo is not None:
            last_activity = last_activity.replace(tzinfo=None)
        retention_data.append({
            'user_id': user.id,
            'first_activity': first_activity,
            'last_activity': last_activity,
            'days_active': (last_activity - first_activity).days
        })
    
    return {
        'activity': pd.DataFrame(user_activity),
        'retention': pd.DataFrame(retention_data)
    }

def create_excel_report(analysis_results):
    """Create a comprehensive Excel report with all analyses"""
    writer = pd.ExcelWriter('clickless_analysis.xlsx', engine='openpyxl')
    
    # Pain Analysis Sheets
    analysis_results['pain']['by_category'].to_excel(writer, sheet_name='Pain Categories', index=False)
    analysis_results['pain']['intensity'].to_excel(writer, sheet_name='Pain Intensity', index=False)
    analysis_results['pain']['locations'].to_excel(writer, sheet_name='Pain Locations', index=False)
    
    # Exercise Analysis Sheets
    analysis_results['exercise']['completion_rates'].to_excel(writer, sheet_name='Exercise Completion', index=False)
    analysis_results['exercise']['timing_patterns'].to_excel(writer, sheet_name='Exercise Timing', index=False)
    analysis_results['exercise']['user_engagement'].to_excel(writer, sheet_name='User Exercise Engagement', index=False)
    
    # User Behavior Sheets
    analysis_results['user']['activity'].to_excel(writer, sheet_name='User Activity', index=False)
    analysis_results['user']['retention'].to_excel(writer, sheet_name='User Retention', index=False)
    
    writer.close()

def create_visualizations(analysis_results):
    """Create visualizations for the analysis results"""
    # Pain Category Distribution
    plt.figure(figsize=(12, 6))
    sns.barplot(data=analysis_results['pain']['by_category'], x='category_name', y='count')
    plt.title('Pain Distribution by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('pain_categories.png')
    plt.close()
    
    # Pain Intensity Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(analysis_results['pain']['intensity']['created_at__date'], 
             analysis_results['pain']['intensity']['avg_intensity'])
    plt.title('Average Pain Intensity Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('pain_intensity.png')
    plt.close()
    
    # Exercise Completion Rates
    plt.figure(figsize=(12, 6))
    exercise_data = analysis_results['exercise']['completion_rates']
    exercise_data['completion_rate'] = exercise_data['completions'] / exercise_data['total_exercises']
    sns.barplot(data=exercise_data, x='type', y='completion_rate')
    plt.title('Exercise Completion Rates by Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('exercise_completion.png')
    plt.close()
    
    # User Activity Distribution
    plt.figure(figsize=(12, 6))
    user_activity = analysis_results['user']['activity']
    sns.histplot(data=user_activity, x='pain_entries', bins=30)
    plt.title('Distribution of Pain Entries per User')
    plt.tight_layout()
    plt.savefig('user_activity.png')
    plt.close()

def main():
    print("Starting comprehensive data analysis...")
    
    # Perform analyses
    analysis_results = {
        'pain': analyze_pain_patterns(),
        'exercise': analyze_exercise_patterns(),
        'user': analyze_user_behavior()
    }
    
    # Create reports
    create_excel_report(analysis_results)
    print("Excel report created: clickless_analysis.xlsx")
    
    create_visualizations(analysis_results)
    print("Visualizations created:")
    print("- pain_categories.png")
    print("- pain_intensity.png")
    print("- exercise_completion.png")
    print("- user_activity.png")
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main() 