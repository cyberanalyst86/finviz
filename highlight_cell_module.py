# Import Module
import os
import re
import pandas as pd

def highlight_cell(series):

    green_colour = 'background-color: #4ABA00'
    default = ''

    return [green_colour if (e == "YES")
    else default for e in series]

def highlight_criteria(row):
    # check if the value in the column "No. of Criteria Met" is greater than or equal to a threshold
    if row["No. of Criteria Met"] >= 5:
        # return a list of styles with yellow background for the whole row
        return ["background-color: yellow"] * len(row)
    else:
        # return a list of styles with no background for the whole row
        return [""] * len(row)











