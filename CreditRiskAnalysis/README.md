# Credit Risk Scoring & Probability of Default Model

## Executive Summary
This project develops an econometric credit scoring model designed to predict borrower default risk. By applying Logistic Regression to financial and demographic attributes, the model estimates individual Probability of Default (PD) and implements an automated decision rule to minimize non-performing loans (NPLs).

## Dataset Overview
The analysis utilizes a portfolio of 32,581 retail credit records. Key variables include:
* **Income (`person_income`)**: Annual gross income.
* **Loan Amount (`loan_amnt`)**: Total borrowing requested.
* **Interest Rate (`loan_int_rate`)**: Assigned loan interest rate.
* **Age (`person_age`)**: Borrower age.
* **Target (`loan_status`)**: 0 = Fully Paid, 1 = Default.

## Methodology
1. **Data Preprocessing**: Handling missing records via listwise deletion to ensure model stability.
2. **Exploratory Data Analysis (EDA)**: Portfolio-level default rate evaluation and risk profiling across home ownership categories.
3. **Econometric Modeling**: Implementation of a Logistic Regression classifier using an 80/20 train-test split (`random_state=42`, `max_iter=1000`).
4. **Decision Boundary**: Establishing a cut-off threshold at 25% Probability of Default for automated underwriting decisions.

## Results & Impact
* **Model Accuracy**: ~81.55% out-of-sample prediction accuracy.
* **Risk Management Implication**: Enables dynamic underwriting by replacing binary approvals with quantitative default probabilities.
