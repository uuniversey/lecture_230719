

from my_package.math import my_math
from my_package.statistics import tools

# from my_package.statistics.tools import mod로 직접적으로 가져올 수도 있다.


result_a = my_math.add(1, 2)
print(result_a)

result_b = tools.mod(5, 3)
print(result_b)
