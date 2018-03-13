# CAFA PI Challenge

Code for the [CAFA PI challenge](https://www.synapse.org/#!Synapse:syn11533497/wiki/497640).

## Software Requirements

All code, unless otherwise specified, runs with Python 3.

The following Python packages are required:

- [pandas](https://pandas.pydata.org/)

To install these packages with pip, run:

```bash
pip3 install pandas
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