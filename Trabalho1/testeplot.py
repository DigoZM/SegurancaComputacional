import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import warnings
warnings.filterwarnings("ignore")

freq_l = [0.02702702702702703, 0.02702702702702703, 0.013513513513513514, 0, 0.06756756756756757, 0.05405405405405406, 0.04054054054054054, 0.05405405405405406, 0.06756756756756757, 0.013513513513513514, 0.02702702702702703, 0.02702702702702703, 0.02702702702702703, 0.013513513513513514, 0.013513513513513514, 0, 0.04054054054054054, 0.02702702702702703, 0.04054054054054054, 0.04054054054054054, 0.02702702702702703, 0.04054054054054054, 0, 0.02702702702702703, 0.013513513513513514, 0.02702702702702703]

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

l = plt.bar(alfabeto, freq_l)
plt.title('Decifrando Frequencia')



class Index(object):
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(alfabeto)
        alfabeto.insert(0, alfabeto.pop())
        freq_l.insert(0, freq_l.pop())
        for r1, r2 in zip(l,freq_l):
            r1.set_height(r2)
        ax.set_xticklabels(alfabeto)
        plt.draw()

    def prev(self, event):
        self.ind += 1
        i = self.ind % len(alfabeto)
        alfabeto.append(alfabeto.pop(0))
        
        freq_l.append(freq_l.pop(0))
        for r1, r2 in zip(l,freq_l):
            r1.set_height(r2)
        ax.set_xticklabels(alfabeto)
        plt.draw()




callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)


plt.show()