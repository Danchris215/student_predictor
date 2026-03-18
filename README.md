# Student Predictor

A simple machine learning project that trains and evaluates a logistic regression model to predict whether a student passes based on study and academic features.

## Project Structure

```text
student_predictor/
  app/
  configs/
    config.yaml
  data/
    raw/
      students.csv
  models/
    model.pkl
  notebooks/
  src/
    config.py
    data/
    evaluation/
    features/
    models/
  tests/
  requirements.txt
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

Train model:

```bash
python -m src.models.train_model
```

Evaluate model:

```bash
python -m src.evaluation.evaluate_model
```

Predict one sample:

```bash
python -m src.models.predict_model
```

## Notes

- Internal file paths are centralized in `src/config.py`.
- Data expected at `data/raw/students.csv`.
- Trained model is saved to `models/model.pkl`.
