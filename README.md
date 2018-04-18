# CAFA PI Challenge

Code for the [CAFA PI challenge](https://www.synapse.org/#!Synapse:syn11533497/wiki/497640).

## Software Requirements

All code, unless otherwise specified, runs with Python 3.

To install Python dependencies with pip, run:

```bash
pip3 install pandas tensorflow sklearn
# Dask needs to be upgraded for tensorflow to work
pip3 install dask --upgrade
```

## Generating the parsed data

### Target Data

Download the data files:

```bash
bash data_acquisition/Scripts/download_test_data.sh
```

And parse them:

```bash
python parse/targets.py
```

### Cafa 3

The parsed data file is about 240 MB, so it's better to parse it on your own machine than to store in source control.

To parse it, run the following from the project root:

```bash
python3 parse/cafa3.py
```

### Simulated data for testing

This data isn't actually useful for training a model, but may be useful in testing whether a model works on very simple data.  The script's random seed is set so that this data will be the same each time it's generated.

To generate the simulated data, run the following from the project root:

```bash
python3 -m ml.simulate_data
```

The data can then be found in `{project root}/data/example/train_simulated.csv`.

## Loading the data

In order to load a csv into a format usable by TensorFlow, run the following in Python:

```python
from ml.embeddings import load_data

data, targets = load_data("./data/example/train_fake.csv")
```

## Running the Model

### Viewing results

```bash
tensorboard --logdir log/
```

Then go to http://127.0.0.1:6006 in your browser to see the results.

You may need to delete the `log/` directory before running the model a second time in order to clear old results.

### CNN

```bash
python3 -m ml.cnn
```

## Teams:

### Data acquisition

- Ashton, Calvin, Dan

#### 3/30/2018:
    So far we have collected all available protein data for Pseudemonas and the yeast, as well as GO annotations for these proteins.
    Summary statistics of these datasets are available in the README.txt file in the data_acquisition directory.
    We also have a script that retrieves the JSON data for a given GO term.
    We are currently working on a script to generate summary statistics of protein sequences, a script to update GO term to a relevant 
    parent term, and also to find more proteins with our desired annotations to enrich our dataset.

### Data transformation

- Dane, Dallas
- Gage, Ben

### Analytics

- Kimball, Daniel
- Jonathan, Erica
