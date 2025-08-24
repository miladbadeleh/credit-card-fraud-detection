# Credit Card Fraud Detection Model

## Problem Statement
[Briefly describe the problem and the goal, as we did in Phase 1]

## Dataset
[Link to the Kaggle dataset. Mention the imbalance and PCA features.]

## Approach
1.  **Exploratory Data Analysis (EDA):** Investigated the severe class imbalance.
2.  **Data Preprocessing:** Scaled 'Time' and 'Amount' features using RobustScaler.
3.  **Handling Imbalance:** Experimented with strategies like SMOTE and class-weighted models.
4.  **Model Building & Evaluation:** Trained and tuned Logistic Regression and Random Forest models. Focused on Precision, Recall, and F1-Score instead of Accuracy.
5.  **Results:** The tuned Random Forest model achieved an F1-Score of X and a Recall of Y, significantly outperforming the baseline.

## Key Skills Demonstrated
*   Handling highly imbalanced datasets
*   Feature Scaling (RobustScaler)
*   Resampling techniques (SMOTE)
*   Model Training & Hyperparameter Tuning (GridSearchCV)
*   Model Evaluation (Precision-Recall Curves, Confusion Matrix)
*   Python, Pandas, Scikit-learn, Imbalanced-learn

## How to Run
1.  Clone this repo: `git clone [your-repo-link]`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the Jupyter Notebook: `jupyter notebook credit_card_fraud_detection.ipynb`

## Results and Visualizations
![Precision-Recall Curve](images/pr_curve.png)
![Confusion Matrix](images/confusion_matrix.png)
