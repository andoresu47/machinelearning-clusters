import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join


def scrape_file(path, export=True):
    """
    Function to scrape relevant data from an input file and export it as a DataFrame.

    Args:
        path (str): file path
        export (bool): exports data to DataFrame if True.

    Returns:
        pandas.DataFrame: table containing scraped data.

    """

    file = open(path, "r")
    coordinates_set = []

    for line in file:
        if line.startswith("ATOMIC_POSITIONS"):
            coordinates = []
            next_line = next(file)
            while not (next_line.startswith("\n") or next_line.startswith("End")):
                coordinates.append(next_line.strip().split())
                next_line = next(file)
            coordinates_set.append(coordinates)

    return np.array(coordinates_set)


def scrape_folder(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for f in files:
        scrape_file(join(path, f))


if __name__ == '__main__':
    array = (scrape_file("../data/output.out"))
    print(array)
    # df = pd.DataFrame.from_records([array]).transpose()
