import argparse
import os

def main(file_name):
    """
    Deletes files with the specified file name or path. Checks that the provided file name is present,
    otherwise prints "File file_name is not found"
    Intended for temporary files produced. 
    Utilizes an argument parser to prompt the user and provide help descriptions for parameters. 

    Parameters
    -------
    file_name: String
        file path/name to file planned for deletion

    Returns
    -------
    None

    Example
    -------
    Delete files at the specified path
    >>> import hyperthyroid_classifier as hyp
        Deleting all files in the results folder:
    >>> hyp.main("results/*)
        All files in the results folder should be removed now
    """ 

    #check if file exists and then remove
    if (os.path.isfile(file_name)):
        os.remove(file_name)
    else:
        print("File %s not found" % file_name)
    



if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Removes files")
    parse.add_argument("file_name", help = "Path to file to delete")
    arg = parse.parse_args()
    main(arg.file_name)




