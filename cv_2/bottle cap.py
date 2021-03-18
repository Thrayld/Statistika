import matplotlib.pyplot as plt

from data import DATA, ORDER, BATCH_SIZE, estimate


plt.plot(
    ORDER,
    DATA,
    'bo'
)
plt.axhline(estimate * BATCH_SIZE, color='r')
plt.title(f'Počet hlav v sériích délky {BATCH_SIZE}')
plt.legend(['Hlavy v sérii', 'Průměr'])
plt.yticks(list(range(max(DATA)+2)))
plt.xticks(list(filter(lambda x: x % 2, ORDER)))
plt.show()
