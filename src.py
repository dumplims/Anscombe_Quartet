import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import warnings
warnings.filterwarnings("ignore")
print('set up finished')


quartet_data = pd.read_csv('Anscombe_quartet_data.csv')

print(quartet_data)
pd.DataFrame(quartet_data)

# Figure 1 fit:
x1 = quartet_data['x123']
y1 = quartet_data['y1']
m1,c1 = np.polyfit(x1, y1, 1)
# Figure 2 fit:
x2 = quartet_data['x123']
y2 = quartet_data['y2']
m2,c2 = np.polyfit(x2, y2, 1)
# Figure 3 fit:
x3 = quartet_data['x123']
y3 = quartet_data['y3']
m3,c3 = np.polyfit(x3, y3, 1)
# Figure 4 fit:
x4 = quartet_data['x4']
y4 = quartet_data['y4']
m4,c4 = np.polyfit(x4, y4, 1)
# plot all four plots in a multiplot:
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(18,9))
plt.xlim(3,20)
plt.ylim(2,14)
axs[0, 0].set_title('Figure 1', fontsize=16)
axs[0, 0].plot(x1, y1, 'yo', x1, m1*x1+c1) 
axs[0, 1].set_title('Figure 2', fontsize=16)
axs[0, 1].plot(x2, y2, 'yo', x2, m2*x2+c2)
axs[1, 0].set_title('Figure 3', fontsize=16)
axs[1, 0].plot(x3, y3, 'yo', x3, m3*x3+c3) 
axs[1, 1].set_title('Figure 4', fontsize=16)
axs[1, 1].plot(x4, y4, 'yo', x4, m4*x4+c4);


#make a table for info like intercept, x bar

