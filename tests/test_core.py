import pandas as pd
import pytest
from dataframe_optimizer import optimize

def test_optimize_memory():
    df = pd.DataFrame({
        'a': range(1000000),
        'b': ['foo'] * 1000000
    })
    optimized_df = optimize(df)
    assert optimized_df.memory_usage(deep=True).sum() < df.memory_usage(deep=True).sum()

def test_optimize_performance():
    df = pd.DataFrame({'a': range(1000000), 'b': range(1000000)})
    optimized_df = optimize(df)
    assert optimized_df.shape == df.shape

def test_optimize_in_place():
    df = pd.DataFrame({'a': range(1000000), 'b': range(1000000)})
    optimize_in_place(df)
    assert df.memory_usage(deep=True).sum() < df.memory_usage(deep=True).sum()

def test_optimize_category_conversion():
    df = pd.DataFrame({'a': ['cat', 'dog'] * 500000})
    optimized_df = optimize(df)
    assert optimized_df['a'].dtype == 'category'

def test_optimize_downcast():
    df = pd.DataFrame({'a': [1, 2, 3] * 333333})
    optimized_df = optimize(df)
    assert optimized_df['a'].dtype == 'int32'