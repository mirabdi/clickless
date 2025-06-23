#!/usr/bin/env python
"""
Script to import all models from all Django apps in the project.
This script provides a comprehensive import of all models for easy access.
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clickless.settings')
django.setup()

# Core app models
from core.models import (
    CustomModel,
    AppIntegrity,
    AppIntegrityHistory,
    ClinicalTrialAccess,
    CustomAdmin,
)

# Users app models
from users.models import (
    User,
    SignInHistory,
    UserDelete,
    UserDeleteReason,
    AccessCode,
    CustomerInquiry,
)

# Authentication app models
from authentication.models import (
    Admin,
)

# Content app models
from content.models import (
    Article,
    ArticleCategory,
    ArticleDetail,
    ArticleViewHistory,
    Banner,
    ConfidentialTerm,
    EducationVideo,
    EducationVideoViewHistory,
    Faq,
    MedicalDevice,
    Meditation,
    MeditationHistory,
    Notice,
    PrivacyPolicy,
    Term,
)

# Pain Management app models
from pain_management.models import (
    Pain,
    PainAnswer,
    PainArea,
    PainAreaDetail,
    PainArticle,
    PainCategory,
    PainFeedback,
    PainQuestion,
)

# Surveys app models
from surveys.models import (
    Survey,
    Answer,
    PainAnswer,
    PainAreaDetail,
    Question,
    QuestionCategory,
    QuestionType,
    QuestionTypeDetail,
    Diary,
    DiaryQuestion,
    DiaryQuestionCategory,
    DiaryQuestionType,
    DiaryQuestionTypeDetail,
)

# Exercises app models
from exercises.models import (
    Exercise,
    ExerciseHistory,
    ExerciseTime,
)

# Habits app models
from habits.models import (
    Habit,
    HabitAnswer,
    HabitCategory,
    HabitViolation,
)

# Medications app models
from medications.models import (
    Drug,
    DrugDetail,
    DrugType,
)

# Notifications app models
from notifications.models import (
    Notification,
    NotificationCategory,
    NotificationExclusion,
)

# Dictionary of all models organized by app
ALL_MODELS = {
    'core': {
        'CustomModel': CustomModel,
        'AppIntegrity': AppIntegrity,
        'AppIntegrityHistory': AppIntegrityHistory,
        'ClinicalTrialAccess': ClinicalTrialAccess,
        'CustomAdmin': CustomAdmin,
    },
    'users': {
        'User': User,
        'SignInHistory': SignInHistory,
        'UserDelete': UserDelete,
        'UserDeleteReason': UserDeleteReason,
        'AccessCode': AccessCode,
        'CustomerInquiry': CustomerInquiry,
    },
    'authentication': {
        'Admin': Admin,
    },
    'content': {
        'Article': Article,
        'ArticleCategory': ArticleCategory,
        'ArticleDetail': ArticleDetail,
        'ArticleViewHistory': ArticleViewHistory,
        'Banner': Banner,
        'ConfidentialTerm': ConfidentialTerm,
        'EducationVideo': EducationVideo,
        'EducationVideoViewHistory': EducationVideoViewHistory,
        'Faq': Faq,
        'MedicalDevice': MedicalDevice,
        'Meditation': Meditation,
        'MeditationHistory': MeditationHistory,
        'Notice': Notice,
        'PrivacyPolicy': PrivacyPolicy,
        'Term': Term,
    },
    'pain_management': {
        'Pain': Pain,
        'PainAnswer': PainAnswer,
        'PainArea': PainArea,
        'PainAreaDetail': PainAreaDetail,
        'PainArticle': PainArticle,
        'PainCategory': PainCategory,
        'PainFeedback': PainFeedback,
        'PainQuestion': PainQuestion,
    },
    'surveys': {
        'Survey': Survey,
        'Answer': Answer,
        'PainAnswer': PainAnswer,
        'PainAreaDetail': PainAreaDetail,
        'Question': Question,
        'QuestionCategory': QuestionCategory,
        'QuestionType': QuestionType,
        'QuestionTypeDetail': QuestionTypeDetail,
        'Diary': Diary,
        'DiaryQuestion': DiaryQuestion,
        'DiaryQuestionCategory': DiaryQuestionCategory,
        'DiaryQuestionType': DiaryQuestionType,
        'DiaryQuestionTypeDetail': DiaryQuestionTypeDetail,
    },
    'exercises': {
        'Exercise': Exercise,
        'ExerciseHistory': ExerciseHistory,
        'ExerciseTime': ExerciseTime,
    },
    'habits': {
        'Habit': Habit,
        'HabitAnswer': HabitAnswer,
        'HabitCategory': HabitCategory,
        'HabitViolation': HabitViolation,
    },
    'medications': {
        'Drug': Drug,
        'DrugDetail': DrugDetail,
        'DrugType': DrugType,
    },
    'notifications': {
        'Notification': Notification,
        'NotificationCategory': NotificationCategory,
        'NotificationExclusion': NotificationExclusion,
    },
}

# Flat list of all models
ALL_MODELS_FLAT = {}
for app_models in ALL_MODELS.values():
    ALL_MODELS_FLAT.update(app_models)

# List of all model names
ALL_MODEL_NAMES = list(ALL_MODELS_FLAT.keys())

# List of all apps
ALL_APPS = list(ALL_MODELS.keys())

def get_model_by_name(model_name):
    """
    Get a model class by its name.
    
    Args:
        model_name (str): Name of the model
        
    Returns:
        Model class or None if not found
    """
    return ALL_MODELS_FLAT.get(model_name)

def get_models_by_app(app_name):
    """
    Get all models for a specific app.
    
    Args:
        app_name (str): Name of the app
        
    Returns:
        dict: Dictionary of model names to model classes
    """
    return ALL_MODELS.get(app_name, {})

def print_all_models():
    """
    Print all models organized by app.
    """
    print("All Models by App:")
    print("=" * 50)
    
    for app_name, models in ALL_MODELS.items():
        print(f"\n{app_name.upper()} ({len(models)} models):")
        print("-" * 30)
        for model_name in sorted(models.keys()):
            print(f"  - {model_name}")
    
    print(f"\nTotal: {len(ALL_MODEL_NAMES)} models across {len(ALL_APPS)} apps")

if __name__ == "__main__":
    print_all_models() 