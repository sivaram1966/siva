# Exploratory Data Analysis (EDA)

This folder contains a starter project for performing Exploratory Data Analysis on tabular datasets.

Structure
- README.md - this file
- requirements.txt - Python dependencies
- data/ - place datasets here (not committed)
- notebooks/01-eda.ipynb - starter Jupyter notebook
- src/eda_utils.py - helper functions for loading and quick EDA

Getting started
1. Create and activate a virtual environment (recommended):
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows

2. Install dependencies:
   pip install -r requirements.txt

3. Place your dataset (CSV) in eda/data/ and open the notebook:
   jupyter lab

4. The notebook imports eda.src.edautils (or use src/eda_utils.py) and demonstrates a basic EDA flow: load data, summary, missing values, correlation, and simple visualizations.

What to add next
- Add sample dataset(s) in eda/data/ (small CSVs) or link to remote data.
- Add more analysis notebooks, automated profiling (pandas-profiling), or integrate with nbconvert to export reports.
