import numpy as np
import h5py
import scipy.io


def load_data(path):
    # Load .mat file
    mat = scipy.io.loadmat(path)
    # Access variables in the .mat file
    variable = mat['X']
    # Convert variables to NumPy arrays
    variable_np = np.array(variable)

    return variable_np


def main_function():
    train_data = load_data("./dataset/ex4data1.mat")
    print(train_data.shape)

if __name__ == '__main__':
    main_function()
    