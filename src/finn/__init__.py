# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "FINN"
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound

import os

WS = os.getenv('FINN_WS')
VIVADO_HLS_INCLUDE = os.getenv('VIVADO_PATH')+'/include'



