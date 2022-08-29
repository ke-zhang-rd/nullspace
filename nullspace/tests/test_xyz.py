import sys
import numpy as np
sys.path.append("../")


def test_xyz():
    from nullspace.svd_wrapper import xyz
    x = np.random.random((3))
    xyz(x)
