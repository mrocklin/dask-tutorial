# Dask Tutorial

In this tutorial you will learn the basics of Dask, specifically the following:

1.  How to parallelize simple for-loop code with [Dask Futures](https://docs.dask.org/en/stable/futures.html)
2.  How to scale up Pandas code with [Dask Dataframes](https://docs.dask.org/en/stable/dataframes.html)
3.  How to understand parallel computations and distributed memory with the Dask Dashboard

Additionally you will work on real large scale data using a cluster of machines on the cloud

## Get set up

We have two options for you to follow this tutorial:

### Run locally

If you are joining for a live session please make sure you do the setup in advance, and be ready to go once the session starts.

1. **Clone this repository**
    In your terminal:

    ```
    git clone https://github.com/mrocklin/dask-tutorial
    cd dask-tutorial
    ```
    Alternatively, you can download the zip file of the repository at the top of the main page of the repository. This is a good option if you don't have experience with git.

2. **Create Conda Environment**

    In your terminal navigate to the directory where you have cloned/downloaded the `dask-tutorial` repository and install the required packages:

    ```
    conda env create -f binder/environment.yml
    ```

    This will create a new environment called `dask-tutorial`. To activate the environment do:

    ```
    conda activate dask-tutorial
    ```

4. **Open Jupyter Lab**

    Once your environment has been activated and you are in the `dask-tutorial` repository, in your terminal do:

    ```
    jupyter lab
    ```

    You will see a notebooks directory, click on there and you will be ready to go.


### Run on a cloud notebook

Click on this button → [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mrocklin/dask-tutorial/HEAD) to run in a pre-configured cloud environment.

If you are joining the live session, please click on the button few minutes before we start so we are ready to go.

