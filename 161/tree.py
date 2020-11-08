import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    
    number_of_files = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

    number_of_directories = len([f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))])

    return (number_of_directories, number_of_files)