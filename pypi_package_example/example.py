import math
from typing import Tuple, Any
import numpy as np
from scipy.stats import pearsonr


def abs_sin(x: float = 0) -> float:
    return math.sin(abs(x))


def abs_pearson(x: list, y: list) -> Tuple[float, Any]:
    return pearsonr(np.absolute(x), np.absolute(y))