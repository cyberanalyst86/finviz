import pandas as pd
from check_fundamentals_module import *
from highlight_cell_module import *


def main():

    inputfile = input("Enter excel file: ")

    df_input = pd.read_excel(inputfile)

    df_list = []



    print('Ticker' + "\t" + 'ROE_5%' + "\t" + 'ROE_15%' + "\t" + 'DividendYield' + "\t" + \
          'Debt/Equity' + "\t" + 'NetMargin_10%' + "\t" + 'NetMargin_20%' + "\t" + 'ROA_5' + "\t" + 'ROA_7' + "\t" \
            'PB' + "\t" + 'PE')

    for index, row in df_input.iterrows():

        df = check_fundamentals(row["ticker"])

        stock_description_list = get_description(row["ticker"])

        df['Stock Description'] = stock_description_list

        column_to_move = df.pop('Stock Description')  # Remove the column 'b' and store it in a variable
        df.insert(0, 'Stock Description', column_to_move)  # Insert the column 'b' at the first position

        df_list.append(df)

    df_concat = pd.concat(df_list)

    # -----------------------------------Sort Data Frame by Name -----------------------------------

    df_concat.set_index('Ticker', inplace=True)



    df_format = df_concat.style.apply(highlight_cell, axis=0, subset=['ROE_5%','ROE_15%',\
            'DividendYield',\
            'Debt/Equity',\
            'NetMargin_10%',\
            'NetMargin_20%',\
            'ROA_5%',\
            'ROA_7%',\
            'PB']).set_properties(**{
            'text-align': 'center',
            'border-color': 'black',
            'border-width': '1px',
            'border-style': 'solid'
            })

    df_format.to_excel('sample.xlsx', engine='openpyxl')

if __name__ == "__main__":
    main()