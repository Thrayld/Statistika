import sympy as sy

import data

L = sy.Symbol('l')  # lambda estimate
i = sy.Symbol('i')  # index in product
n = sy.Symbol('n')  # size of data; upper limit in product
x = sy.IndexedBase('x')  # observations


general_likelihood = sy.Product(L * sy.exp(-L * x[i]), (i, 1, n))

my_likelihood = general_likelihood\
    .subs(n, data.size)\
    .doit()\
    .subs([(x[i + 1], data.sample[i]) for i in range(data.size)])

my_log_likelihood = sy.log(my_likelihood)

# second_derivative = sy.diff(my_log_likelihood, l, l).simplify()
#
# sy.plot(
#     second_derivative
# )
