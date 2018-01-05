# -*- coding: utf-8 -*-
"""
Regular Polygons: polysum

A regular polygon has 'n' number of sides. Each side has length 's'.

* The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
* The perimeter of a polygon is: length of the boundary of the polygon
"""
# import math module
import math
# define ploysum function
def polysum(n, s):
    # area
    area = 0.25*n*s**2/math.tan(math.pi/n)
    # perimeter
    perimeter = n*s
    
    # return required sum after rounding 4 decimal pllaces
    return round(area + perimeter**2, 4)