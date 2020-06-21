from time import perf_counter
import os
from threading import Thread

import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import shuffle
from joblib import effective_n_jobs

from monitor import benchmark

def read_uci(dataset, stats=False):
    path = f'{dataset}.txt'
    df = pd.read_csv(path, delim_whitespace=True, header=None)
    df = df.astype('float64')
    data = df.values
    X, Y = data[:, 1:], data[:, 0].astype('int32')
    if Y.min() == 1:
        Y -= 1
    X = MinMaxScaler().fit_transform(X)
    if stats:
        labels, freq = np.unique(Y, return_counts=True)
        print(dataset, X.shape, len(labels), freq.min()/freq.max(), freq)
    return shuffle(X, Y, random_state=42)

def puget():
    N = 20_000
    A = np.random.rand(N,N).astype('float32')
    B = np.random.rand(N,N).astype('float32')

    nrm = np.linalg.norm(A@B)

if __name__=='__main__':
    #benchmark(puget)
    puget()

    


# cv = RepeatedStratifiedKFold(n_splits=10,n_repeats=10)
# c = SVC()

# clf = make_pipeline(PCA(),c)
# r = cross_val_score(clf,X,y,cv=cv,n_jobs=12)