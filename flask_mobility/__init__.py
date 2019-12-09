from flask_mobility import decorators
from flask_mobility.mobility import Mobility


VERSION = (1, 0, 0)

__version__ = ".".join(str(v) for v in VERSION)
__all__ = ["Mobility", "decorators"]
