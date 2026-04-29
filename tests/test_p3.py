import numpy as np
import pytest
from cbfpdg.one_step_socp import p3  # replace 'your_module' with actual module name

def test_p3_solution():
    # Setup example problem
    u_dim = 2

    Lfh = 0.5
    Lgh = np.array([1.0, -0.5])
    alpha_h = 1.0

    LfV = -0.2
    LgV = np.array([0.3, 0.7])
    gamma_V = 0.5

    rho2 = 2.0

    u_opt, status = p3(
        Lfh, Lgh, alpha_h,
        LfV, LgV, gamma_V,
        rho2,
        u_dim
    )

    # Check solver succeeded
    assert status == "optimal"