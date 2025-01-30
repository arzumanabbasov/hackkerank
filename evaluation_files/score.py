"""
Evaluation Script for User Interface Submissions

This script evaluates the results submitted by users against the expected output.  
The scoring system is based on the following logic:

Scoring Formula:
----------------
1. Base Score = (Number of correct matches) ÷ (Number of expected items)  
   - If there are no expected items, the base score is 0.
   
2. Penalty = (Number of submitted items - Number of expected items) ÷ (Number of expected items)  
   - Applies only if the submitted count exceeds the expected count.
   
3. Final Score = max(Base Score - Penalty, 0)  
   - Ensures the score does not go negative.

Guidelines:
-----------
- Users must select exactly the expected features to achieve the highest score.
- Submitting additional features will incur a penalty.
- Incorrect selections will reduce the base score.

Usage:
------
Run the script with the following command:
    python evaluation_files/score.py evaluation_files/expected_output.csv submission.csv

Author: [Arzuman Abbasov]
"""

import csv

def evaluate_score(expected_csv, submission_csv):
    with open(expected_csv, 'r', newline='', encoding='utf-8') as f:
        expected = [row[0] for row in csv.reader(f)]
    with open(submission_csv, 'r', newline='', encoding='utf-8') as f:
        submitted = [row[0] for row in csv.reader(f)]

    expected_set = set(expected)
    submitted_set = set(submitted)

    correct_matches = len(expected_set.intersection(submitted_set))
    base_score = correct_matches / len(expected_set) if expected_set else 0

    if len(submitted) > len(expected):
        penalty = (len(submitted) - len(expected)) / len(expected)
        base_score -= penalty

    return max(base_score, 0)