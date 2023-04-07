import os
import urllib.request
import argparse

def main(url, output_path):
    """
    Downloads a file online based on the URL given and saves it to
    a specified output path. If an HTTP error is present, print out 
    the error code along with error reason. Also prompts the user 
    utilizing an argument parser along with providing help descriptions
    for the parameters. 

    Parameters
    -------
    url: String
        The url to the dataset that is desired to be stores at a certain path

    output_path: String
        The path that the data retrieved from the url is to be saved at. 
    
    Returns
    -------
    None. Stores a file at the specified output path. 

    Examples
    ------- 
    Relocating a url file to a specified path in your own computer
    >>> import hyperthyroid_classifier as hyp
        Reading in the URL and saving the file contents to the specified path
    >>> hyp.main("https://thisdataframe.ca, "hyperthyroid/data/dat.csv")
        The file contents should be saved in hyperthyroid/data/dat.csv
    """
    try:
        urllib.request.urlretrieve(url, output_path)
    except urllib.error.HTTPError as error:
        print(f'HTTP Error {error.code} {error.reason}')

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Downloads a file based on a URL and saves it to a given file path")
    parse.add_argument("url", help = "URL of the file")
    parse.add_argument("output_path", help = "Path to save the file to")
    arg = parse.parse_args()
    main(arg.url, arg.output_path)