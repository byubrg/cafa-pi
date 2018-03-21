# CAFA PI Challenge

Code for the [CAFA PI challenge](https://www.synapse.org/#!Synapse:syn11533497/wiki/497640).

## Software Requirements

All code, unless otherwise specified, runs with Python 3.

The following Python packages are required:

- [pandas](https://pandas.pydata.org/)

To install these packages with pip, run:

```bash
pip3 install pandas tensorflow sklearn
```

## Teams:

### Data acquisition

- Ashton, Calvin, Dan

### Data transformation

- Dane, Dallas
- Gage, Ben

### Analytics

- Kimball, Daniel
- Jonathan, Erica

## Generating the parsed data

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
python3 ml/simulate_data.py
```

The data can then be found in `{project root}/data/example/train_simulated.csv`.

## Loading the data

In order to load a csv into a format usable by TensorFlow, run the following in Python:

```python
from ml.embeddings import load_data

data, targets = load_data("./data/example/train_fake.csv")
```