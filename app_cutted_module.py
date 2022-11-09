from module import find_max

numbers = [10,20,50,14,45,23]
maximum = find_max(numbers)  
print(maximum)

import Package.shippment #longer approach to the package access
Package.shippment.calc_shipping()

from Package.shippment import calc_shipping #faster approach to the package access, I can add more functions in this one module after a , or I can import everything by
from Package import shippment               #                                                                                                                 doing this.
