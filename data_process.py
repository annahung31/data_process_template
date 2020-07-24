import pandas as pd
import json



def get_subset(ratio=0.1):
    raise NotImplementedError("not implemented!")




def func_a():
    raise NotImplementedError("not implemented!")


def data_cleaning(data):
    clean_data = data
    return clean_data
    



def main():
    src_csv = '/Users/chingtien/Downloads/open-shopee-code-league-logistic/delivery_orders_march.csv'
    data = pd.read_csv(src_csv)
    print(a.shape)
    data.head()

    subset_data = get_subset()
    print(subset_data.shape)

    clean_data = data_cleaning(data)


    #apply function
    which_axis = 1
    clean_data['column_a'] = clean_data.apply(lambda x:func_a(x.column_b, x.column_c), axis = which_axis)


    #output and save
    NAME = 'wotcha_submission3.csv'
    clean_data.to_csv(NAME, index = False)








