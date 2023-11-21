from flask_mobility import decorators
from flask_mobility.mobility import Mobility


VERSION = (2, 0, 1)

__version__ = ".".join(str(v) for v in VERSION)
__all__ = ["Mobility", "decorators"]
