import pandas as pd
import pastas as ps
import numpy as np


def test_summary():
    """Test all signatures for minimal functioning."""
    idx = pd.date_range("2000", "2010")
    head = pd.Series(index=idx, data=np.random.rand(len(idx)), dtype=float)
    ps.stats.signatures.summary(head)


def test_colwell_components():
    """Example Tree C from the publication."""
    n = 9
    x = ["200{}-04-01".format(t) for t in range(0, n)] + \
        ["200{}-08-02".format(t) for t in range(0, n)] + \
        ["201{}-08-01".format(t) for t in range(0, n)]
    y = [1] * n + [2] * n + [3] * n
    obs = pd.Series(y, index=pd.to_datetime(x))
    ps.stats.signatures.colwell_components(obs, freq="4M", bins=3)
    return obs


def test_colwell_predictability():
    """Example Tree C from the publication."""
    obs = test_colwell_components()
    p = ps.stats.signatures.colwell_components(obs, freq="4M", bins=3)[0]
    assert p.round(2) == 1.0


def test_colwell_constancy():
    """Example Tree C from the publication."""
    obs = test_colwell_components()
    c = ps.stats.signatures.colwell_components(obs, freq="4M", bins=3)[1]
    assert c.round(2) == 0.42


def test_colwell_contingency():
    """Example Tree C from the publication."""
    obs = test_colwell_components()
    m = ps.stats.signatures.colwell_components(obs, freq="4M", bins=3)[2]
    assert m.round(2) == 0.58
