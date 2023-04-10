import argparse
import pandas as pd

def main(file1_path, file2_path, output_path, column_names):
    """
    Takes in two different file paths (of dataframes), and merges them together with the specified column 
    names. Also removes extraneous characters from column names. 
    Then saves the resulting dataframe at the specified output path.  
    Also utilizing an argument parser to prompt the user and provide help descriptions.

    Parameters
    -------
    file1_path: String
        file path to first CSV file
    file2_path: String
        file path to second CSV file
    output_path: String
        file path to store the resulting dataframe at
    column_names: list
        A list of the column names of the two initial data frames
    
    Returns
    -------
    None. Produces a dataframe at the specified output path and prints the reformatted column names

    Examples
    -------
    Merge two dataframes with the same column names
    >>> import hyperthyroid_classifier as hyp
        Input paths to dataframes, column names and output path
    >>> hyp.main("data1.csv", "data2.csv", ['col1', 'col2', ''col3'], "data/hyperthyroid.csv")
    >>> ['col1'], ['col2'], ['col3']
        The combined dataframe will now be present at data/hyperthyroid.csv with column names as above
    """ 
    columns = (column_names.strip('][').split('.'))[0].split(", ")
    df1 = pd.read_csv(file1_path, names = columns)
    df2 = pd.read_csv(file2_path, names = columns)

    output = pd.concat([df1, df2])

    output.to_csv(output_path, index = False)
    print (columns)

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Merges 2 CSV files into 1 based on specific columns")
    parse.add_argument("file1_path", help = "Path to first CSV")
    parse.add_argument("file2_path",  help = "Path to second CSV")
    parse.add_argument("output_path", help = "Path to save the file to")
    parse.add_argument("column_names", help = "List of columns you want to keep when file is merged")
    
    arg = parse.parse_args()
    main(arg.file1_path, arg.file2_path, arg.output_path, arg.column_names)




