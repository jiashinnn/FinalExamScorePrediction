# Final Exam Score Prediction

## Overview
This assignment is a simple web application that predicts a student's final exam scores based on key factors such as study hours, attendance rate, previous exam scores, assignments completed, and extracurricular participation using Lasso Regression model. This app is built using Pyhton's Flask framework.
 
## Dataset Description
Dataset can be obtained from the csv file above.
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
**Lasso Regression** was chosen for this project because it not only helps in predicting the final exam scores but also performs feature selection by removing coefficients of less important features to zero. This can lead to a more interpretable model by reducing the number of predictors used and it is simple to use.

## Simple Interface
![image](https://github.com/user-attachments/assets/8d7f5344-3ab6-45a9-839f-14e0983f4432)

## Showing in action
| Input all the fields                                  | Result                                      |
|-------------------------------------------------------|---------------------------------------------|
| ![Input Form](https://github.com/user-attachments/assets/c8db5202-3d08-4c16-9dde-95487c43d37d) | ![Prediction Result](https://github.com/user-attachments/assets/cceb5336-069a-444c-a33d-c85f9912383f) |
 


**You can also go through my .ipynb file to see what I explored. Hope you feel well with my working! :)**
