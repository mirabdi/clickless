-- SQL Script to Add Foreign Key Constraints
-- This script adds foreign key constraints to all Django models that have foreign key relationships

-- Users app foreign key constraints
ALTER TABLE v2_user_delete 
ADD CONSTRAINT fk_user_delete_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_user_delete 
ADD CONSTRAINT fk_user_delete_reason 
FOREIGN KEY (reason_id) REFERENCES v2_user_delete_reason(id);

ALTER TABLE access_code 
ADD CONSTRAINT fk_access_code_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_customer_inquiry 
ADD CONSTRAINT fk_customer_inquiry_user 
FOREIGN KEY (user_id) REFERENCES user(id);

-- Medications app foreign key constraints
ALTER TABLE v2_drug 
ADD CONSTRAINT fk_drug_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_drug_detail 
ADD CONSTRAINT fk_drug_detail_drug 
FOREIGN KEY (drug_id) REFERENCES v2_drug(id);

-- Pain Management app foreign key constraints
ALTER TABLE v2_pain 
ADD CONSTRAINT fk_pain_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_pain 
ADD CONSTRAINT fk_pain_answer 
FOREIGN KEY (answer_id) REFERENCES v2_pain_answer(id);

ALTER TABLE v2_pain 
ADD CONSTRAINT fk_pain_category 
FOREIGN KEY (category_id) REFERENCES v2_pain_category(id);

ALTER TABLE v2_pain 
ADD CONSTRAINT fk_pain_feedback 
FOREIGN KEY (feedback_id) REFERENCES v2_pain_feedback(id);

ALTER TABLE v2_pain_area_detail 
ADD CONSTRAINT fk_pain_area_detail_area 
FOREIGN KEY (area_id) REFERENCES v2_pain_area(id);

ALTER TABLE v2_pain_area_detail 
ADD CONSTRAINT fk_pain_area_detail_pain 
FOREIGN KEY (pain_id) REFERENCES v2_pain(id);

ALTER TABLE v2_pain_article 
ADD CONSTRAINT fk_pain_article_article 
FOREIGN KEY (article_id) REFERENCES v2_article(id);

ALTER TABLE v2_pain_article 
ADD CONSTRAINT fk_pain_article_pain 
FOREIGN KEY (pain_id) REFERENCES v2_pain(id);

ALTER TABLE v2_pain_category 
ADD CONSTRAINT fk_pain_category_question 
FOREIGN KEY (question_id) REFERENCES v2_pain_question(id);

ALTER TABLE v2_pain_feedback 
ADD CONSTRAINT fk_pain_feedback_category 
FOREIGN KEY (category_id) REFERENCES v2_pain_category(id);

ALTER TABLE v2_pain_question 
ADD CONSTRAINT fk_pain_question_category 
FOREIGN KEY (category_id) REFERENCES v2_pain_category(id);

ALTER TABLE v2_pain_question_detail 
ADD CONSTRAINT fk_pain_question_detail_question 
FOREIGN KEY (question_id) REFERENCES v2_pain_question(id);

-- Exercises app foreign key constraints
ALTER TABLE v2_exercise_history 
ADD CONSTRAINT fk_exercise_history_exercise 
FOREIGN KEY (exercise_id) REFERENCES v2_exercise(id);

ALTER TABLE v2_exercise_history 
ADD CONSTRAINT fk_exercise_history_user 
FOREIGN KEY (user_id) REFERENCES user(id);

-- Content app foreign key constraints
ALTER TABLE v2_article 
ADD CONSTRAINT fk_article_category 
FOREIGN KEY (category_id) REFERENCES v2_article_category(id);

ALTER TABLE v2_meditation_history 
ADD CONSTRAINT fk_meditation_history_meditation 
FOREIGN KEY (meditation_id) REFERENCES v2_meditation(id);

ALTER TABLE v2_meditation_history 
ADD CONSTRAINT fk_meditation_history_user 
FOREIGN KEY (user_id) REFERENCES user(id);

-- Surveys app foreign key constraints
ALTER TABLE v2_survey_answer 
ADD CONSTRAINT fk_survey_answer_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_survey_answer 
ADD CONSTRAINT fk_survey_answer_question 
FOREIGN KEY (question_id) REFERENCES v2_survey_question(id);

ALTER TABLE v2_survey_pain_answer 
ADD CONSTRAINT fk_survey_pain_answer_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_survey_pain_area_detail 
ADD CONSTRAINT fk_survey_pain_area_detail_survey_pain_answer 
FOREIGN KEY (survey_pain_answer_id) REFERENCES v2_survey_pain_answer(id);

ALTER TABLE v2_survey_question 
ADD CONSTRAINT fk_survey_question_type 
FOREIGN KEY (type_id) REFERENCES v2_survey_question_type(id);

ALTER TABLE v2_survey_question 
ADD CONSTRAINT fk_survey_question_category 
FOREIGN KEY (question_category_id) REFERENCES v2_survey_question_category(id);

ALTER TABLE v2_survey_question 
ADD CONSTRAINT fk_survey_question_survey 
FOREIGN KEY (survey_id) REFERENCES v2_survey(id);

ALTER TABLE v2_survey_question_category 
ADD CONSTRAINT fk_survey_question_category_survey 
FOREIGN KEY (survey_id) REFERENCES v2_survey(id);

ALTER TABLE v2_survey_question_type_detail 
ADD CONSTRAINT fk_survey_question_type_detail_type 
FOREIGN KEY (type_id) REFERENCES v2_survey_question_type(id);

ALTER TABLE v2_diary 
ADD CONSTRAINT fk_diary_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_diary 
ADD CONSTRAINT fk_diary_question 
FOREIGN KEY (question_id) REFERENCES v2_diary_question(id);

ALTER TABLE v2_diary_question 
ADD CONSTRAINT fk_diary_question_category 
FOREIGN KEY (category_id) REFERENCES v2_diary_question_category(id);

ALTER TABLE v2_diary_question 
ADD CONSTRAINT fk_diary_question_type 
FOREIGN KEY (type_id) REFERENCES v2_diary_question_type(id);

ALTER TABLE v2_diary_question_type_detail 
ADD CONSTRAINT fk_diary_question_type_detail_type 
FOREIGN KEY (type_id) REFERENCES v2_diary_question_type(id);

-- Habits app foreign key constraints
ALTER TABLE v2_habit 
ADD CONSTRAINT fk_habit_category 
FOREIGN KEY (category_id) REFERENCES v2_habit_category(id);

ALTER TABLE v2_habit_answer 
ADD CONSTRAINT fk_habit_answer_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_habit_answer 
ADD CONSTRAINT fk_habit_answer_habit 
FOREIGN KEY (habit_id) REFERENCES v2_habit(id);

ALTER TABLE v2_habit_violation 
ADD CONSTRAINT fk_habit_violation_answer 
FOREIGN KEY (answer_id) REFERENCES v2_habit_answer(id);

-- Notifications app foreign key constraints
ALTER TABLE v2_notification 
ADD CONSTRAINT fk_notification_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_notification_exclusion 
ADD CONSTRAINT fk_notification_exclusion_user 
FOREIGN KEY (user_id) REFERENCES user(id);

ALTER TABLE v2_notification_exclusion 
ADD CONSTRAINT fk_notification_exclusion_category 
FOREIGN KEY (category_id) REFERENCES v2_notification_category(id);

-- Authentication app foreign key constraints (if any exist)
-- Add any authentication-related foreign keys here if needed

-- Core app foreign key constraints (if any exist)
-- Add any core-related foreign keys here if needed 