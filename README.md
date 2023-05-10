# Dask Tutorial

In this tutorial you will learn the basics of Dask, specifically the following:

1.  How to parallelize simple for-loop code with [Dask Futures](https://docs.dask.org/en/stable/futures.html)
2.  How to scale up Pandas code with [Dask Dataframes](https://docs.dask.org/en/stable/dataframes.html)

Additionally you will work on real large scale data using a cluster of machines on the cloud

## Set up

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

    Alternatively, you can run `pip install -r requirements.txt`.
    This may or may not work as well.
    We recommend doing this from a fresh Python environment (this will make
    synchronizing with your cluster easier).

3. **Establish Coiled Access**

    This tutorial will use Dask clusters on the cloud.  We will get these
    clusters using a SaaS product, Coiled.  You can either ...

    1.  Sign up (it's free and there's no commitment) as follows:

        ```
        coiled login
        ```

        You'll be asked to authenticate with GitHub to make an account.  Don't
        worry about connecting to your cloud resources.  We'll add you to the
        `dask-tutorials` team, which is connected to an AWS account of ours.

        To get this access, ask to be added in the #dask-tutorial channel.
        You'll also want to set your default account to `dask-tutorials`:

        ```
        coiled config set account dask-tutorials
        ```

        Alternatively, you can also ...

    2.  Use a short-lived auth token

        ```
        coiled login --token 65924ef194cc4b658ff37c1c11caa357-2ad71e4ceeafd5a771f553306cff95eb9624ee2d --account dask-tutorials
        ```

        This should just work, but will expire in a few days and you won't be
        able to access the web view.

4. **Open Jupyter Lab**

    Once your environment has been activated and you are in the `dask-tutorial` repository, start Jupyter Lab:

    ```
    jupyter lab
    ```

    You will see a notebooks directory, click on there and you will be ready to go.

    *We recommend Jupyter Lab due to the [Dask Jupyter extension](https://github.com/dask/dask-labextension).*

### Run on a Coiled notebook

1. **Setup virtual environment**
    ```
    conda create -n dask-tutorial python=3.10 coiled jupyter
    conda activate dask-tutorial
    ```

2. **Establish Coiled Access**
    1.  Sign up (it's free and there's no commitment) as follows:

        ```
        coiled login
        ```

        You'll be asked to authenticate with GitHub to make an account.  Don't
        worry about connecting to your cloud resources.  We'll add you to the
        `dask-tutorials` team, which is connected to an AWS account of ours.

        To get this access, ask to be added in the #dask-tutorial channel.
        You'll also want to set your default account to `dask-tutorials`:

        ```
        coiled config set account dask-tutorials
        ```

        Alternatively, you can also ...

    2.  Use a short-lived auth token

        ```
        coiled login --token 65924ef194cc4b658ff37c1c11caa357-2ad71e4ceeafd5a771f553306cff95eb9624ee2d --account dask-tutorials
        ```

        This should just work, but will expire in a few days and you won't be
        able to access the web view.

3. **Start Coiled notebook**
    ```
    coiled notebook up --software jupytercon-notebook
    ```

    **Note:** Don't forget to shut down your notebook after you're done!

### Run on mybinder.org

The website [mybinder.org](https://mybinder.org) serves pre-configured Jupyter notebooks for
free that you can also use.  Here is the link → [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mrocklin/dask-tutorial/HEAD).

However, mybinder.org has tragically lost some of their funding recently, and
so availability is not what it once was.  We recommend running locally if
possible.
