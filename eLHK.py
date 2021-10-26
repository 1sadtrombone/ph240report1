"""
Code written by Taj Dyson, 24 Oct. 2021.
Python is an interpreted language.

See main text for sources on the numbers here.
"""

import numpy as np
import matplotlib.pyplot as plt

def get_Leq_per_100km(breakdown):
  Lgas_per_kgCO2 = 1/2.3
  kWh_per_100km = 19.3 # Kia Soul EV 2018
  # [coal, natural gas, nuclear, hydro, wind, solar, geo, bio]
  # IGNORES PETROLEUM (TINY CONTRIBUTION ANYWAY, NO IPCC DATA)
  kg_CO2e_per_kWh = np.array([1004, 472, 17, 4, 13, 47, 47, 39])/1000
  
  kgCO2_per_100km = kWh_per_100km * np.sum(kg_CO2e_per_kWh*breakdown)
  Leq_per_100km = kgCO2_per_100km * Lgas_per_kgCO2
  return Leq_per_100km
  
def plot_breakdown(ax, breakdown, title):
    used_indices = np.where(breakdown>0)[0]
    ax.set_title(title, fontsize=30)
    ax.pie(breakdown[used_indices], labels=labels[used_indices], colors=colors[used_indices], labeldistance=None)
    ax.legend(fontsize=20)

if __name__=='__main__':
  # assume "wind & solar" means equal of each, and that "other" means equal of geo and bio
  breakdown_ca = np.array([0.2, 85.8, 16.2, 38.4, 21.05, 21.05, 9.55, 9.55])
  breakdown_ca /= np.sum(breakdown_ca)

  breakdown_qc = np.array([0, 0.1, 0, 95, 4, 0.1, 0.5, 0.5])
  breakdown_qc /= np.sum(breakdown_qc)

  print(get_Leq_per_100km(breakdown_ca))
  print(get_Leq_per_100km(breakdown_qc))
  print(get_Leq_per_100km([1,0,0,0,0,0,0,0]))
  
  labels = np.array(["Coal", "Natural Gas", "Nuclear", "Hydro", "Wind", "Solar", "Geothermal", "Biomass"])
  colors = np.array(['k', 'darkorange', 'lime', 'royalblue', 'skyblue', 'gold', 'red', 'green'])
  fig = plt.figure(figsize=[20,10])  
  ax1, ax2 = fig.subplots(1,2)
  plot_breakdown(ax1, breakdown_ca, "California Local Electricity Sources 2021")
  plot_breakdown(ax2, breakdown_qc, "Quebec Local Electricity Sources 2019")

  plt.show()
  
  # [CA, QC, prius, beetle, odyssey]
  labels = ['Kia Soul (CA)', 'Kia Soul (QC)', 'Kia Coal', 'Toyota Prius', 'VW Beetle', 'Honda Odyssey']
  lpks = [Leq_per_100km_ca, Leq_per_100km_qc, get_Leq_per_100km([1,0,0,0,0,0,0,0]), 4.5, 8.2, 10.7]

  print(lpks)
  fig = plt.figure(figsize=[10,10])  
  ax = fig.add_subplot(1,1,1)
  ax.set_axisbelow(True)
  ax.set_title("Liters per 100 km Comparison", fontsize=30)
  ax.yaxis.grid(color='gray', linestyle='dashed')
  ax.set_ylabel('eLHK (Electric) or LHK (Gas)', fontsize=20)
  plt.yticks(size=20)
  plt.xticks(size=15)
  bars = ax.bar(labels, lpks)
  ax.xaxis.set_tick_params(rotation=45)
  colors=['darkorange', 'royalblue', 'black', 'green', 'gold', 'purple']
  for i, color in enumerate(colors):
      bars[i].set_color(color)
  plt.show()
