# Analytics Progress

- Encoded protein sequences and GO-IDs into one-hot encoding
    - to make it readable for a machine learning model
- Generated synthetic data set
    - created to make sure it works on a simplified version of our problem
- Wrote a convolutional neural network and ran it on synthetic data set
    - to get a rough draft of a working model
    - TensorFLow: good visualization
- Next Steps
    1. Model output probabilities (Jon)
    2. HDF5 storage/retrieval (Kimball)
    3. Fix validation set split (Kimball)
    4. Make RNN (GRU) (Jon)
    5. Optimize CNN (Erica)
    - Non-padded sequences
    - Make binary classifier