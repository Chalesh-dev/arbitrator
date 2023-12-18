import time

from matplotlib import pyplot as plt

# import matplotlib.pyplot as plt
from trading_arbitrator.primitives import Pool, Converter
from trading_arbitrator.amm import constant_product_amm, constant_sum_amm
from trading_arbitrator.arbitrator import Arbitrator

# First we instantiate the rules of exchange:
converter = Converter(name="CPAMM", conversion_formula=constant_product_amm, fee=1)  # Fee is in %, so 5%
# Now we can create a pool:
pool1 = Pool(name="pool1", assets=["A", "B"], amounts=[100, 20000], converter=converter)
pool2 = Pool(name="pool2", assets=["A", "B"], amounts=[500, 405], converter=converter)
pool3 = Pool(name="pool3", assets=["A", "B"], amounts=[500, 400], converter=converter)

pls = [ pool1, pool2, pool3]

arb = Arbitrator(pools=pls, initial_assets=["A"])
loops = arb.get_loops(sizes=[2, 3, 4, 5])



d = []
for i in range(0,10000):
    d.append(loops[0].convert(amount=i/10, with_fees=True)-i/10)
print(max(d))

print(loops[0].get_max_absolute_profit())
print(loops[0])
results = []
for i in range(0,200):
    results.append(loops[0].convert(i) - i)
plt.plot(results)
plt.xlabel("Initial investment")
plt.ylabel("Simulated absolute profits\n(returns - initial investment)")
plt.grid()
plt.show()

