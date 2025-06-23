# Clickless Database Schema Summary

## Core Architecture
```
CustomModel (Abstract Base)
├── deleted: Boolean
└── deleted_at: DateTime
```

## 1. USER MANAGEMENT (users app)
```
user (Central Hub)
├── id: BigAutoField (PK)
├── email: CharField(255, unique)
├── nickname: CharField(255)
├── gender: IntegerField
├── aws_user_id: CharField(45)
├── birth_date: DateField
├── is_lock: TextField
└── created_at: DateTime

sign_in_history
├── id: BigAutoField (PK)
├── email: CharField(255)
├── device_name: CharField(255)
├── device_token: CharField(255)
├── language: CharField(255)
├── os: CharField(255)
├── status: CharField(255)
└── created_at: DateTime

v2_user_delete (OneToOne with user)
├── user_id: OneToOneField (PK)
├── reason_id: ForeignKey → v2_user_delete_reason
├── created_at: DateTime
└── updated_at: DateTime

v2_user_delete_reason
├── id: SmallAutoField (PK)
├── reason: CharField(255)
├── orders: IntegerField
└── created_at: DateTime

access_code
├── access_code: CharField(255) (PK)
├── user_id: ForeignKey → user
├── created_at: DateTime
├── expired_at: DateTime
├── activated_at: DateTime
└── completed_survey_week: IntegerField

v2_customer_inquiry
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── inquiry: CharField(255)
└── created_at: DateTime
```

## 2. CONTENT MANAGEMENT (content app)
```
v2_article_category
├── id: BigAutoField (PK)
├── name: CharField(255)
├── orders: IntegerField
├── is_common: TextField
└── created_at: DateTime

v2_article
├── id: BigAutoField (PK)
├── category_id: ForeignKey → v2_article_category
├── title: CharField(255)
├── orders: IntegerField
└── created_at: DateTime

v2_article_detail
├── id: BigAutoField (PK)
├── article_id: ForeignKey → v2_article
├── title: CharField(255)
├── content: CharField(500)
├── image: CharField(255)
├── orders: IntegerField
└── created_at: DateTime

v2_article_view_history
├── id: BigAutoField (PK)
├── article_id: ForeignKey → v2_article
├── user_id: ForeignKey → user
└── created_at: DateTime

v2_education_video
├── id: BigAutoField (PK)
├── url: CharField(200)
├── title: CharField(100)
├── content: CharField(2000)
├── orders: IntegerField
└── created_at: DateTime

v2_education_video_view_history
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── video_id: ForeignKey → v2_education_video
└── created_at: DateTime

v2_meditation
├── id: BigAutoField (PK)
├── url: CharField(200)
├── title: CharField(100)
├── type: CharField(100)
├── orders: IntegerField
└── created_at: DateTime

v2_meditation_history
├── id: BigAutoField (PK)
├── meditation_id: ForeignKey → v2_meditation
├── user_id: ForeignKey → user
└── created_at: DateTime

v2_banner
├── id: BigAutoField (PK)
├── title: CharField(100)
├── subtitle: CharField(100)
├── image: CharField(200)
├── route: CharField(20)
├── background_color: CharField(20)
├── orders: IntegerField
├── index: IntegerField
└── created_at: DateTime

v2_faq
├── id: BigAutoField (PK)
├── question: CharField(255)
├── answer: CharField(500)
├── orders: IntegerField
└── created_at: DateTime

v2_medical_device
├── id: BigAutoField (PK)
├── label: CharField(255)
├── content: TextField
├── is_markdown: IntegerField
├── orders: IntegerField
└── created_at: DateTime

v2_notice
├── id: BigAutoField (PK)
├── title: CharField(255)
├── content: TextField
├── created_at: DateTime
└── updated_at: DateTime

v2_privacy_policy
├── id: BigAutoField (PK)
├── title: CharField(255)
├── content: TextField
├── created_at: DateTime
└── updated_at: DateTime

v2_term
├── id: BigAutoField (PK)
├── title: CharField(255)
├── content: TextField
├── created_at: DateTime
└── updated_at: DateTime

v2_confidential_term
├── id: BigAutoField (PK)
├── type: CharField(255)
├── content: TextField
└── created_at: DateTime
```

## 3. PAIN MANAGEMENT (pain_management app)
```
v2_pain_question
├── id: BigAutoField (PK)
├── name: CharField(255)
└── created_at: DateTime

v2_pain_category
├── id: BigAutoField (PK)
├── question_id: ForeignKey → v2_pain_question
├── name: CharField(50)
├── orders: IntegerField
└── created_at: DateTime

v2_pain_answer
├── id: BigAutoField (PK)
├── category_id: ForeignKey → v2_pain_category
├── article_category_id: ForeignKey → v2_article_category
├── name: CharField(50)
├── orders: IntegerField
├── has_text_area: TextField
└── created_at: DateTime

v2_pain_feedback
├── id: BigAutoField (PK)
├── category_id: ForeignKey → v2_pain_category
├── content: CharField(100)
└── created_at: DateTime

v2_pain
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── category_id: ForeignKey → v2_pain_category
├── answer_id: ForeignKey → v2_pain_answer
├── feedback_id: ForeignKey → v2_pain_feedback
├── content: CharField(255)
└── created_at: DateTime

v2_pain_area
├── id: BigAutoField (PK)
├── name: CharField(15)
├── is_right: TextField
├── x: FloatField
├── y: FloatField
└── created_at: DateTime

v2_pain_area_detail
├── id: BigAutoField (PK)
├── area_id: ForeignKey → v2_pain_area
├── pain_id: ForeignKey → v2_pain
├── value: IntegerField
└── created_at: DateTime

v2_pain_article
├── id: BigAutoField (PK)
├── article_id: ForeignKey → v2_article
├── pain_id: ForeignKey → v2_pain
└── created_at: DateTime
```

## 4. SURVEYS & DIARY (surveys app)
```
v2_survey
├── id: BigAutoField (PK)
├── name: CharField(50)
├── explanation: CharField(50)
├── type: CharField(30)
├── is_pain: IntegerField
├── orders: IntegerField
└── created_at: DateTime

v2_survey_question_type
├── id: BigAutoField (PK)
├── type: CharField(20)
└── created_at: DateTime

v2_survey_question_type_detail
├── id: BigAutoField (PK)
├── type_id: ForeignKey → v2_survey_question_type
├── name: CharField(50)
├── orders: IntegerField
└── created_at: DateTime

v2_survey_question_category
├── id: BigAutoField (PK)
├── survey_id: ForeignKey → v2_survey
├── name: CharField(255)
├── orders: IntegerField
└── created_at: DateTime

v2_survey_question
├── id: BigAutoField (PK)
├── survey_id: ForeignKey → v2_survey
├── type_id: ForeignKey → v2_survey_question_type
├── question_category_id: ForeignKey → v2_survey_question_category
├── name: CharField(255)
├── orders: IntegerField
├── question_category: CharField(255)
└── created_at: DateTime

v2_survey_answer
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── question_id: ForeignKey → v2_survey_question
├── value: IntegerField
├── week: IntegerField
└── created_at: DateTime

v2_survey_pain_answer
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── content: CharField(255)
├── week: IntegerField
└── created_at: DateTime

v2_survey_pain_area_detail
├── id: BigAutoField (PK)
├── survey_pain_answer_id: ForeignKey → v2_survey_pain_answer
├── value: IntegerField
└── created_at: DateTime

-- DIARY TABLES --

v2_diary_question_category
├── id: BigAutoField (PK)
├── name: CharField(255)
├── orders: IntegerField
└── created_at: DateTime

v2_diary_question_type
├── id: BigAutoField (PK)
├── type: CharField(20)
└── created_at: DateTime

v2_diary_question_type_detail
├── id: BigAutoField (PK)
├── type_id: ForeignKey → v2_diary_question_type
├── name: CharField(50)
├── orders: IntegerField
└── created_at: DateTime

v2_diary_question
├── id: BigAutoField (PK)
├── category_id: ForeignKey → v2_diary_question_category
├── type_id: ForeignKey → v2_diary_question_type
├── name: CharField(255)
├── orders: IntegerField
├── enum_name: CharField(255)
└── created_at: DateTime

v2_diary
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── question_id: ForeignKey → v2_diary_question
├── value: IntegerField
└── created_at: DateTime
```

## 5. EXERCISES (exercises app)
```
v2_exercise
├── id: BigAutoField (PK)
├── title: CharField(100)
├── type: CharField(100)
├── url: CharField(200)
├── tutorial: CharField(200)
├── orders: IntegerField
├── has_face: IntegerField
└── created_at: DateTime

v2_exercise_history
├── id: BigAutoField (PK)
├── exercise_id: ForeignKey → v2_exercise
├── user_id: ForeignKey → user
├── is_face: IntegerField
└── created_at: DateTime

v2_exercise_time
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── time_since_midnight: IntegerField
├── created_at: DateTime
└── updated_at: DateTime
```

## 6. HABITS (habits app)
```
v2_habit_category
├── id: BigAutoField (PK)
├── name: CharField(50)
├── is_etc: IntegerField
├── orders: IntegerField
└── created_at: DateTime

v2_habit
├── id: BigAutoField (PK)
├── category_id: ForeignKey → v2_habit_category
├── name: CharField(50)
├── orders: IntegerField
└── created_at: DateTime

v2_habit_answer
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── habit_id: ForeignKey → v2_habit
└── created_at: DateTime

v2_habit_violation
├── id: BigAutoField (PK)
├── answer_id: ForeignKey → v2_habit_answer
└── created_at: DateTime
```

## 7. MEDICATIONS (medications app)
```
v2_drug_type
├── id: BigAutoField (PK)
├── type: CharField(15)
├── orders: IntegerField
└── created_at: DateTime

v2_drug
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── name: CharField(15)
├── type: CharField(15)
├── created_at: DateTime
└── finished_at: DateTime

v2_drug_detail
├── id: BigAutoField (PK)
├── drug_id: ForeignKey → v2_drug
├── time: IntegerField
└── created_at: DateTime
```

## 8. NOTIFICATIONS (notifications app)
```
v2_notification_category
├── id: SmallAutoField (PK)
├── name: CharField(255)
├── orders: IntegerField
├── enum_name: CharField(255)
├── created_at: DateTime
└── updated_at: DateTime

v2_notification
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── title: CharField(255)
├── content: CharField(255)
├── type: CharField(255)
├── is_read: TextField
├── created_at: DateTime
└── updated_at: DateTime

v2_notification_exclusion
├── id: BigAutoField (PK)
├── user_id: ForeignKey → user
├── category_id: ForeignKey → v2_notification_category
└── created_at: DateTime
```

## 9. SYSTEM TABLES (core app)
```
v2_app_integrity
├── id: BigAutoField (PK)
├── recent_version: CharField(30)
├── min_version: CharField(30)
├── android_debug_hash: CharField(255)
├── android_release_hash: CharField(255)
├── ios_hash: CharField(255)
└── created_at: DateTime

v2_app_integrity_history
├── id: BigAutoField (PK)
├── user_id: IntegerField
├── app_version: CharField(30)
├── status: CharField(10)
├── mode: CharField(255)
└── created_at: DateTime

clinical_trial_access
├── id: BigAutoField (PK)
└── access_key_id: CharField(255)

custom_admin
├── id: BigAutoField (PK)
├── email: CharField(254, unique)
├── is_active: IntegerField
├── created_at: DateTime
└── updated_at: DateTime

my_admin (authentication app)
├── id: BigAutoField (PK)
├── email: EmailField(unique)
├── is_active: BooleanField
├── created_at: DateTime
└── updated_at: DateTime
```

## Key Relationships Summary

### Central Hub: User
- **user** table is the central hub with relationships to 13+ tables
- Most user activity tracking tables reference user via ForeignKey

### Cross-App Dependencies
1. **pain_management** → **content** (v2_pain_answer.article_category_id, v2_pain_article.article_id)
2. **surveys** → **pain_management** (v2_survey_pain_area_detail references pain areas)
3. **All apps** → **core** (inherit from CustomModel)

### Inheritance Structure
- All business models inherit from `CustomModel` (abstract)
- Provides soft delete functionality (deleted, deleted_at fields)

### Database Naming Convention
- Most tables use `v2_` prefix indicating version 2
- Some legacy tables without prefix (user, sign_in_history, access_code)
- System tables have descriptive names (clinical_trial_access, custom_admin)

### Total Tables: ~50 tables across 9 Django apps 