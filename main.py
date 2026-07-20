import numpy as np
from typing import Final

from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler

from modules.persist_acc_01 import compute_accelerated_persistence
from modules.persist_acc_02 import compute_topological_features
from modules.persist_acc_keppler import compare_methods
from modules.persist_acc_keppler import run_refined_mapper


if __name__ == "__main__":
    data_points = np.random.rand(100, 3)
    compute_accelerated_persistence(data_points)
    compute_topological_features(data_points)

    X_raw = load_diabetes().data
    X: Final = StandardScaler().fit_transform(X_raw)
    compare_methods(X)
    run_refined_mapper(X)
