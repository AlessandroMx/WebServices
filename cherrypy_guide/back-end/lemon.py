"""
    Created on Mar 22 2019
    @author: 212690718  Ibrahim Chávez
    File description
    ------------------------
    Just a module for making some typical back-end operations.

    File log
    ------------------------
    ===========         =============        ================
    Date                Author               Comments
    ===========         =============        ================
    Mar 22 2019           Ibrahim C.         Original version
    ===========         =============        ================
"""
import pandas as pd


def sum_column(col_name):
    """Pretty simple function that gets the sum of a DataFrame column

    Parameters
    ----------
    col_name : str
        The name of the DataFrame column to sum

    Returns
    -------
    numpy.float64
        The sum of the whole column
    """
    df = pd.read_csv('../assets/FL_insurance_sample.csv')
    return df[col_name].sum()
