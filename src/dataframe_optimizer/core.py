import pandas as pd
import numpy as np

def optimize(df: pd.DataFrame) -> pd.DataFrame:
    """Optimize a pandas DataFrame for performance and memory usage.
    
    Args:
        df (pd.DataFrame): The DataFrame to optimize.

    Returns:
        pd.DataFrame: An optimized DataFrame.
    """
    # Convert object types to category if there are many repeated values
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')

    # Downcast numeric columns to reduce memory usage
    df_int = df.select_dtypes(include=['int'])
    df[df_int.columns] = df_int.apply(pd.to_numeric, downcast='integer')

    df_float = df.select_dtypes(include=['float'])
    df[df_float.columns] = df_float.apply(pd.to_numeric, downcast='float')

    return df

def optimize_in_place(df: pd.DataFrame) -> None:
    """Optimize a pandas DataFrame in place for performance and memory usage.
    
    Args:
        df (pd.DataFrame): The DataFrame to optimize.
    """
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')

    df_int = df.select_dtypes(include=['int'])
    df[df_int.columns] = df_int.apply(pd.to_numeric, downcast='integer')

    df_float = df.select_dtypes(include=['float'])
    df[df_float.columns] = df_float.apply(pd.to_numeric, downcast='float')

# Additional utility functions can be added here