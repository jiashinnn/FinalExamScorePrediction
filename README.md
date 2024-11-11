# Final Exam Score Prediction

## Overview
This assignment aims to predict students' final exam scores based on various academic and extracurricular factors using Lasso Regression. By analyzing these predictors, the model can help identify key areas that influence academic performance and provide insights into optimizing study habits and attendance.
 
## Dataset Description
The dataset contains the following features:
**study_hours_per_week:** Number of hours the student studies each week.
**attendance_rate:** The percentage of classes the student attended.
**previous_exam_scores:** The average score from previous exams.
**assignments_completed:** Number of assignments the student completed.
**extracurricular_participation:** Number participation in extracurricular activities.
**study_attendance_interaction:** An interaction term between study hours and attendance rate.
**study_hours_per_week_squared:** The square of study hours per week, to capture non-linear effects.
**attendance_rate_squared:** The square of attendance rate, to capture non-linear effects.
**assignments_per_week:** Average assignments completed per week.
**final_exam_score:** The target variable, representing the score in the final exam.

## Model Selection
**Lasso Regression** was chosen for this project because it not only helps in predicting the final exam scores but also performs feature selection by removing less important variables. This can lead to a more interpretable model by reducing the number of predictors used and it is simple to use.

## Simple Interface
![image](https://github.com/user-attachments/assets/8d7f5344-3ab6-45a9-839f-14e0983f4432)
