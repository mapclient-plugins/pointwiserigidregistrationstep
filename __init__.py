
'''
MAP Client Plugin
'''
__version__ = '0.1.0'
__author__ = 'Ju Zhang'

import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    # Using __file__ will not work if py2exe is used,
    # Possible problem of OSX10.6 also.
    sys.path.insert(0, current_dir)

# import class that derives itself from the step mountpoint.
from pointwiserigidregistrationstep import step

( _, tail ) = os.path.split(current_dir)
print("Plugin '{0}' version {1} by {2} loaded".format(tail, __version__, __author__))

