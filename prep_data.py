#This script was modify from original https://github.com/coiled/pydata-global-dask/blob/master/prep.py
import time
import sys
import argparse
import os
from glob import glob
import tarfile
import urllib.request

import pandas as pd


def flights():
    start = time.time()

    if not os.path.exists("nycflights.tar.gz"):
        print("- Downloading NYC Flights dataset... ", end="", flush=True)
        url = "https://storage.googleapis.com/dask-tutorial-data/nycflights.tar.gz"
        urllib.request.urlretrieve(url, "nycflights.tar.gz")
        print("done", flush=True)

    if not os.path.exists("nycflights"):
        print("- Extracting flight data... ", end="", flush=True)
        tar_path = "nycflights.tar.gz"
        with tarfile.open(tar_path, mode="r:gz") as flights:
            flights.extractall(".")

        print("done", flush=True)

    else:
        return

    end = time.time()
    print("** Created flights dataset! in {:0.2f}s**".format(end - start))
