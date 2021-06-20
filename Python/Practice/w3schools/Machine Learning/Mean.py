
""" Steps to install pip and numpy on Windows 10:

- Open CMD (not necessarily as administrator)
- Type: python -m pip install --upgrade pip
    Press Enter
- Type: pip install numpy
    Press Enter
- Type: python
    Press Enter
- Type: import numpe
    Press Enter
- Type: numpy.version.version
    Press Enter

"""

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)