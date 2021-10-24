from scipy.io import loadmat
import numpy as np

def coil20():
    dataset = loadmat('coil20.mat')
    label = np.array([dataset['Y'][i][0] - 1 for i in range(len(dataset['Y']))])
    data = dataset['X']
    n_class = len(np.unique(label))
    return data, label, n_class

def coil20b():
    dataset = loadmat('coil20.mat')
    label = np.array([dataset['Y'][i][0] % 2 for i in range(len(dataset['Y']))])
    data = dataset['X']
    n_class = len(np.unique(label))
    return data, label, n_class

def g50c():
    dataset = loadmat('g50c.mat')
    label = np.array([np.maximum(dataset['y'][i][0], 0) for i in range(len(dataset['y']))])
    data = dataset['X']
    n_class = len(np.unique(label))
    return data, label, n_class

def uspst():
    dataset = loadmat('uspst.mat')
    label = np.array([dataset['y'][i][0] for i in range(len(dataset['y']))])
    data = dataset['X']
    n_class = len(np.unique(label))
    return data, label, n_class

def uspstb():
    dataset = loadmat('uspst.mat')
    label = np.array([dataset['y'][i][0] % 2 for i in range(len(dataset['y']))])
    data = dataset['X']
    n_class = len(np.unique(label))
    return data, label, n_class