# API Endpoints Documentation

## Authentication App (`/auth/`)
- GET `/auth/admins/` - List all admins
- GET `/auth/admins/{id}/` - Get specific admin
- POST `/auth/admins/login/` - Admin login

## Users App (`/users/`)
- GET `/users/users/` - List all users
- GET `/users/users/{id}/` - Get specific user
- GET `/users/sign-in-history/` - List sign-in history
- GET `/users/sign-in-history/{id}/` - Get specific sign-in record
- GET `/users/user-deletes/` - List user deletions
- GET `/users/user-deletes/{id}/` - Get specific user deletion
- GET `/users/user-delete-reasons/` - List delete reasons
- GET `/users/user-delete-reasons/{id}/` - Get specific delete reason
- GET `/users/access-codes/` - List access codes
- GET `/users/access-codes/{id}/` - Get specific access code

## Surveys App (`/surveys/`)
- GET `/surveys/surveys/` - List all surveys
- GET `/surveys/surveys/{id}/` - Get specific survey
- GET `/surveys/survey-answers/` - List survey answers
- GET `/surveys/survey-answers/{id}/` - Get specific survey answer
- GET `/surveys/survey-pain-answers/` - List pain survey answers
- GET `/surveys/survey-pain-answers/{id}/` - Get specific pain survey answer
- GET `/surveys/survey-pain-area-details/` - List pain area details
- GET `/surveys/survey-pain-area-details/{id}/` - Get specific pain area detail
- GET `/surveys/survey-questions/` - List survey questions
- GET `/surveys/survey-questions/{id}/` - Get specific survey question
- GET `/surveys/survey-question-categories/` - List question categories
- GET `/surveys/survey-question-categories/{id}/` - Get specific question category
- GET `/surveys/survey-question-types/` - List question types
- GET `/surveys/survey-question-types/{id}/` - Get specific question type
- GET `/surveys/survey-question-type-details/` - List question type details
- GET `/surveys/survey-question-type-details/{id}/` - Get specific question type detail

## Content App (`/content/`)
- GET `/content/articles/` - List all articles
- GET `/content/articles/{id}/` - Get specific article
- GET `/content/article-categories/` - List article categories
- GET `/content/article-categories/{id}/` - Get specific article category
- GET `/content/article-details/` - List article details
- GET `/content/article-details/{id}/` - Get specific article detail
- GET `/content/article-view-histories/` - List article view history
- GET `/content/article-view-histories/{id}/` - Get specific article view record
- GET `/content/banners/` - List all banners
- GET `/content/banners/{id}/` - Get specific banner
- GET `/content/education-videos/` - List education videos
- GET `/content/education-videos/{id}/` - Get specific education video
- GET `/content/education-video-view-histories/` - List video view history
- GET `/content/education-video-view-histories/{id}/` - Get specific video view record
- GET `/content/meditations/` - List all meditations
- GET `/content/meditations/{id}/` - Get specific meditation
- GET `/content/meditation-histories/` - List meditation history
- GET `/content/meditation-histories/{id}/` - Get specific meditation history record
- GET `/content/notices/` - List all notices
- GET `/content/notices/{id}/` - Get specific notice
- GET `/content/privacy-policies/` - List privacy policies
- GET `/content/privacy-policies/{id}/` - Get specific privacy policy
- GET `/content/terms/` - List terms
- GET `/content/terms/{id}/` - Get specific term

## Core App (`/core/`)
- No specific endpoints defined

## Exercises App (`/exercises/`)
- GET `/exercises/exercises/` - List all exercises
- GET `/exercises/exercises/{id}/` - Get specific exercise
- GET `/exercises/exercise-histories/` - List exercise history
- GET `/exercises/exercise-histories/{id}/` - Get specific exercise history record
- GET `/exercises/exercise-times/` - List exercise times
- GET `/exercises/exercise-times/{id}/` - Get specific exercise time

## Habits App (`/habits/`)
- GET `/habits/habits/` - List all habits
- GET `/habits/habits/{id}/` - Get specific habit
- GET `/habits/habit-answers/` - List habit answers
- GET `/habits/habit-answers/{id}/` - Get specific habit answer
- GET `/habits/habit-categories/` - List habit categories
- GET `/habits/habit-categories/{id}/` - Get specific habit category
- GET `/habits/habit-violations/` - List habit violations
- GET `/habits/habit-violations/{id}/` - Get specific habit violation

## Medications App (`/medications/`)
- GET `/medications/drugs/` - List all drugs
- GET `/medications/drugs/{id}/` - Get specific drug
- GET `/medications/drug-details/` - List drug details
- GET `/medications/drug-details/{id}/` - Get specific drug detail
- GET `/medications/drug-types/` - List drug types
- GET `/medications/drug-types/{id}/` - Get specific drug type

## Notifications App (`/notifications/`)
- GET `/notifications/notifications/` - List all notifications
- GET `/notifications/notifications/{id}/` - Get specific notification
- GET `/notifications/notification-categories/` - List notification categories
- GET `/notifications/notification-categories/{id}/` - Get specific notification category
- GET `/notifications/notification-exclusions/` - List notification exclusions
- GET `/notifications/notification-exclusions/{id}/` - Get specific notification exclusion

## Pain Management App (`/pain-management/`)
- GET `/pain-management/pains/` - List all pains
- GET `/pain-management/pains/{id}/` - Get specific pain record
- GET `/pain-management/pain-answers/` - List pain answers
- GET `/pain-management/pain-answers/{id}/` - Get specific pain answer
- GET `/pain-management/pain-areas/` - List pain areas
- GET `/pain-management/pain-areas/{id}/` - Get specific pain area
- GET `/pain-management/pain-area-details/` - List pain area details
- GET `/pain-management/pain-area-details/{id}/` - Get specific pain area detail
- GET `/pain-management/pain-categories/` - List pain categories
- GET `/pain-management/pain-categories/{id}/` - Get specific pain category
- GET `/pain-management/pain-feedbacks/` - List pain feedbacks
- GET `/pain-management/pain-feedbacks/{id}/` - Get specific pain feedback
- GET `/pain-management/pain-questions/` - List pain questions
- GET `/pain-management/pain-questions/{id}/` - Get specific pain question

## Admin Interface
- GET `/admin/` - Django admin interface 