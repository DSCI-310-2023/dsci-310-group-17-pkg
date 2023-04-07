import numpy as np


def relabel_bclass(hyper_df):
    """
    Dataset provided by UCI is backwards for hyperthyroid classification, "P" referse to negative diagnosis
        while "N" refers to positive diagnosis. This function relabels the binaryClass column correctly
        and assigns all extra values to np.nan.
        (http://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/)

    Parameters
    -------
    hyper_df: pd.DataFrame()
    Pandas data frame containing raw hyperthyroid datasets
        If a non pd.DataFrame() value is passed into the function, it will fail. 

    Returns
    -------
    output_df: pd.DataFrame()
        Modified pandas data frame containing relabeled values for the 'binaryClass' column
            A pandas data frame with new representations for the binaryClass column, which represents the 
            presence of hyperthyroid disease or not, where Negative ("P") and Positive ("N") are labelled, 
            along with replacing all other values with np.nan. 
    Example
    -------
    Convert the 'binaryClass' column of a mock dataframe to the correct values

    >>> import hyperthyroid_classifier as hyp

        We first read in a dataframe with the relevant features and incorrect values for the 'binaryClass'
        column
    >>> hyper_df = pd.read_csv("hyperthyroid.csv")
    >>> hyper_df.BinaryClass.unique().tolist()
    >>> ['n.*', 'h.*', 'T.*', 's.*', 'g.*']

        Now use relabel_bclass to create the correct labels in 'binaryClass'
    >>> hyper_relabeled = hyp.relabel_bclass(hyper_df)
    >>> hyper_relabeled.Binaryclass.unique().tolist()
    >>> ['P', 'N', nan]
    """

    output_df = hyper_df.replace({'binaryClass': {r'n.*': 'P',
                                                  r'h.*': 'N',
                                                  r'T.*': np.nan,
                                                  r'g.*': np.nan,
                                                  r's.*': np.nan}}, regex=True)
    return(output_df)


def col_dtype_reformat(num_cols, cat_cols, hyper_df):
    """
     Reformats the data types of specified numerical and categorical columns to the corresponding 'float64'
        and 'category' dtypes for classification analysis. All rows with np.nan values will be dropped to
        ensure that data types are correctly casted
    Parameters
    -------
    num_cols: list
        list of column names to be casted to 'float64'
    cat_cols: list
        list of column names to be casted to 'category'
    hyper_df: pd.DataFrame()
        Pandas data frame containing hyperthyroid datasets. This initial dataset will have incorrect
        data types for certain columns

    Returns
    -------
    output_df: pd.DataFrame()
        Modified pandas data frame with columns reformatted to the correct data type. 
            All columns passed in num_cols will be converted to float64 dtype, 
            all columns passed in cat_cols will be converted to category type

    Examples 
    -------
    Convert certain columns of a data frame to float64 and category data types 
    >>> import hyperthyroid_classifier as hyp

        First we read in the data frame and find specified columns to convert
    >>> hyper_df = pd.read_csv("hyperthyroid.csv")
    >>> num_cols = ['age', 'TSH', 'TT4', 'T4U', 'FTI']
    >>> cat_cols = ['sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
            'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid',
            'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'psych', 'binaryClass', 'hypopituitary']
    
        And then we use col_dtype_reformat to reformat the column datatypes
    >>> hyper_reformatted = hyp.col_dtype_reformat(num_cols, cat_cols, hyper_df)
    >>> hyper_reformatted[num_cols].dtype()
    >>> 'float64'
    >>> hyper_reformatted[cat_cols].dtype()
    >>> 'category'
    """
    # Ensures dropping of np.nan values to ensure correct casting
    output_df = hyper_df.dropna()

    output_df[num_cols] = output_df[num_cols].astype('float64')
    output_df[cat_cols] = output_df[cat_cols].astype('category')

    return(output_df)
