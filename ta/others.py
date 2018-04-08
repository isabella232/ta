import pandas as pd


def daily_return(close):
    """Daily Return (DR)
    
    Args:
        close(pandas.Series): dataset 'Close' column.
        
    Returns:
        pandas.Series: New feature generated.
    """
    dr = (close / close.shift(1)) - 1
    return pd.Series(dr*100, name='d_ret')


def cumulative_return(close):
    """Cumulative Return (CR)
   
    Args:
        close(pandas.Series): dataset 'Close' column.
        
    Returns:
        pandas.Series: New feature generated.
    """
    cr = (close / close.iloc[0]) - 1
    return pd.Series(cr*100, name='cum_ret')