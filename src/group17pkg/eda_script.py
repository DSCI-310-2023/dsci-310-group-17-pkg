import argparse
import pandas as pd
import os
import matplotlib.pyplot as plt
from pandas.plotting import table
from eda import plot_correlations

def main(input_path, output_folder):
    """
    Takes in a dataframe from the input_path, creates a directory for the output folder if not already
    present, and then creates two figures with the dataframe, a table produced by df.describe(), and
    a correlation matrix using plot_correlations. Then saves these figures to the desired folder with 
    given filenames. Also uses argument parser to prompt the user and provide help descriptions. 

    Parameters
    -------
    input_path: String
        The path of the dataframe to input

    output_folder: String
        The path of the folder that is the desired location for the figures produced. 
    
    Returns
    -------
    None. Assigns the figures to the given folder with file names "/data_described.csv" and
    "/correlation_of_numeric_features.png". 

    Example
    -------
    Inputting a dataframe and recieving EDA figures as output
    >>> import hyperthyroid_classifier as hyp
        Inputting the specified paths into the function 
    >>> hyp.main("hyperthyroid.csv", "results/figures")
        The figures should now be found at "results/figures/data_described.csv" and 
        "results/figures/correlation_of_numeric_features.png"

    """
    df = pd.read_csv(input_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # save and plot data description to png
    ax = plt.subplot(111, frame_on = False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    table(ax, df.describe(), rowLabels=['']*df.describe().shape[0], loc='center')
    desc = df.describe()
    df.describe().to_csv(output_folder + "/data_described.csv")
    #save data description to csv/dataframe
    plot_correlations(df).savefig(output_folder + "/correlation_of_numeric_features.png", bbox_inches='tight')


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Creates ans saves figures from clean data")
    parse.add_argument("file_path", help = "Path to clean data file")
    parse.add_argument("output_path", help = "Filename to save ")
    arg = parse.parse_args()
    main(arg.file_path, arg.output_path)
