"""
Helper utilities for Exploratory Data Analysis (EDA).
"""

from typing import Optional
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_csv(path: str, nrows: Optional[int] = None, **kwargs) -> pd.DataFrame:
    """Load a CSV into a DataFrame.

    Args:
        path: path to CSV file
        nrows: optionally load only first nrows (for large files)
        **kwargs: passed to pd.read_csv
    """
    return pd.read_csv(path, nrows=nrows, **kwargs)


def profile_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a quick summary (dtypes, non-null counts, unique counts, sample)"""
    summary = pd.DataFrame({
        'dtype': df.dtypes.astype(str),
        'non_null': df.notnull().sum(),
        'unique': df.nunique(dropna=False),
        'pct_missing': (df.isnull().mean() * 100).round(2)
    })
    return summary


def plot_missing_values(df: pd.DataFrame, top_n: int = 20):
    """Bar plot of columns with most missing values."""
    miss = (df.isnull().mean() * 100).sort_values(ascending=False).head(top_n)
    plt.figure(figsize=(min(12, 0.4 * len(miss)), 6))
    sns.barplot(x=miss.values, y=miss.index, palette='viridis')
    plt.xlabel('Percent missing')
    plt.title('Top columns by % missing values')
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame, numeric_only: bool = True, figsize=(10, 8)):
    """Plot correlation heatmap for numeric columns."""
    if numeric_only:
        data = df.select_dtypes(include=[np.number])
    else:
        data = df.copy()
    corr = data.corr()
    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=False, cmap='coolwarm', center=0)
    plt.title('Correlation heatmap')
    plt.show()


def plot_target_distribution(df: pd.DataFrame, target: str, kind: str = 'hist'):
    """Plot distribution (hist or count) for a target column."""
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not in DataFrame")
    plt.figure(figsize=(8, 5))
    if pd.api.types.is_numeric_dtype(df[target]):
        sns.histplot(df[target].dropna(), kde=True)
    else:
        sns.countplot(y=target, data=df, order=df[target].value_counts().iloc[:20].index)
    plt.title(f'Distribution of {target}')
    plt.show()


def sample_inspect(df: pd.DataFrame, n: int = 5):
    """Return a small sample and prints basic info."""
    print('\nDataframe shape:', df.shape)
    print('\nColumn summary:')
    print(profile_summary(df))
    return df.sample(n=min(n, len(df)))
