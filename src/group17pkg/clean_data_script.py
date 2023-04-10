import argparse
import pandas as pd
import numpy as np
from clean_data import relabel_bclass, col_dtype_reformat

def main(file_path, output_path):
    """
    Takes in the initial file path to the dataset, relabels the 'binaryClass' column using the 
    relabel_bclass() function, replaces all '?' cell values with np.nan, drops unneccesary columns, 
    and utilizes the col_dtype_reformat function to reformat column datatypes as desired. Then converts
    the final cleaned dataset to a csv file at the specified output path. Also formats the function so that
    the user will be prompted with the description of the function along with having help descriptions for
    the parameters. 

    Parameters
    --------
    file_path: String
        A path to the dataset that is to be used as input for the data cleaning
    output_path: String
        The desired path for the output csv file. 

    Returns
    -------
    None. A csv file is allocated to the provided output path representing the reformatted dataset

    Example
    -------
    Perform data cleaning and transformation on the initial dataset
    >>> import hyperthyroid_classifier as hyp
        Perform data cleaning/reformatting with the desired input and output paths by using main
    >>> hyp.main("hyperthyroid.csv", "data/hyperthyroid_clean.csv")
        The new dataframe can now be accessed at data/hyperthyroid_clean.csv
    
    """
    

    df = pd.read_csv(file_path)
    df = relabel_bclass(df)

    #i think this line is useless?
    df.binaryClass.unique().tolist()

    hyperthyroid = df.replace("?", np.nan)

    hyper = hyperthyroid.drop(columns=["TBG", "TBG measured", "T3", "T3 measured", "TSH measured",
                                   "TT4 measured", "FTI measured", "T4U measured", "referral source"])
    hyper_clean = hyper.dropna()
    num_cols = ['age', 'TSH', 'TT4', 'T4U', 'FTI']
    cat_cols = ['sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
            'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid',
            'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'psych', 'binaryClass', 'hypopituitary']
    hyper_clean = col_dtype_reformat(num_cols, cat_cols, hyper_clean)
    hyper_clean['binaryClass'] = hyper_clean['binaryClass'].replace(["N", "P"], [1, 0])
    
    hyper_clean.to_csv(output_path)




if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Cleans data ans saves it to a CSV")
    parse.add_argument("file_path", help = "Path to unclean CSV file")
    parse.add_argument("output_path", help = "Path to save clean CSV file to")
    
    arg = parse.parse_args()
    main(arg.file_path, arg.output_path)




