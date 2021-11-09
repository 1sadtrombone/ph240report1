import numpy as np
import matplotlib.pyplot as plt

# USE THE BELOW FUNCTIONS IN YOUR CALCULATION

def get_kgCO2_per_km(breakdown):
    kgCO2_per_km = kWh_per_100km * np.sum(kg_CO2_per_kWh_chem*breakdown) /100
    return kgCO2_per_km
def get_kgCO2_per_km_from_LHK(LHK):
    kgCO2_per_km = LHK * 1/(Lgas_per_kgCO2)* 1/100
    return kgCO2_per_km

# approx., from chemistry
Lgas_per_kgCO2 = 1/2.3

# For the Kia Soul EV 2018
kWh_per_100km = 19.3

# [coal, natural gas, nuclear, hydro, wind, solar, geo, bio]
# IGNORES PETROLEUM (TINY CONTRIBUTION ANYWAY, NO DATA)
# chose pv since CSP seems dead for now [cite]
# IPCC report (not used)
#kg_CO2e_per_kWh = np.array([1004, 472, 17, 4, 13, 47, 47, 39])/1000

# calculations from chemistry
kg_CO2_per_kWh_chem = np.array([0.99, 0.65, 0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
  # assume "wind & solar" means equal of each, and that "other" means equal of geo and bio
  breakdown_ca = np.array([0.2, 85.8, 16.2, 38.4, 21.05, 21.05, 9.55, 9.55])
  breakdown_ca /= np.sum(breakdown_ca)

  breakdown_qc = np.array([0, 0.1, 0, 95, 4, 0.1, 0.5, 0.5])
  breakdown_qc /= np.sum(breakdown_qc)

  print("kg CO2 per 100 km for a Kia Soul EV 2018...")
  print("...in California:")
  print(get_kgCO2_per_km(breakdown_ca))
  print("...in Quebec:")
  print(get_kgCO2_per_km(breakdown_qc))
  print("...fueled entirely using coal:")
  print(get_kgCO2_per_km([1,0,0,0,0,0,0,0]))

  # just for plotting. decipher if you dare
  '''
  labels = np.array(["Coal", "Natural Gas", "Nuclear", "Hydro", "Wind", "Solar", "Geothermal", "Biomass"])
  colors = np.array(['k', 'darkorange', 'lime', 'royalblue', 'skyblue', 'gold', 'red', 'green'])

  def plot_breakdown(ax, breakdown, title):
      used_indices = np.where(breakdown>0)[0]
      ax.set_title(title, fontsize=30)
      ax.pie(breakdown[used_indices], labels=labels[used_indices], colors=colors[used_indices], labeldistance=None)
      ax.legend(fontsize=16)

  fig = plt.figure(figsize=[10,20])  
  ax1, ax2 = fig.subplots(2,1)
  plot_breakdown(ax1, breakdown_ca, "California Local Electricity Sources 2021")
  plot_breakdown(ax2, breakdown_qc, "Quebec Local Electricity Sources 2019")

  plt.show()
  
  # [CA, QC, prius, beetle, odyssey]
  labels = ['Kia Soul (CA)', 'Kia Soul (QC)', 'Kia Coal', 'Toyota Prius', 'VW Beetle', 'Honda Odyssey']
  lpks = [get_kgCO2_per_km(breakdown_ca), get_kgCO2_per_km(breakdown_qc), get_kgCO2_per_km([1,0,0,0,0,0,0,0]), get_kgCO2_per_km_from_LHK(4.5), get_kgCO2_per_km_from_LHK(8.2), get_kgCO2_per_km_from_LHK(10.7)]

  print(lpks)
  fig = plt.figure(figsize=[10,10])  
  ax = fig.add_subplot(1,1,1)
  ax.set_axisbelow(True)
  ax.set_title("kgCO$_2$e per km Comparison", fontsize=30)
  ax.yaxis.grid(color='gray', linestyle='dashed')
  ax.set_ylabel('kgCO$_2$e per km', fontsize=20)
  plt.yticks(size=20)
  plt.xticks(size=15)
  bars = ax.bar(labels, lpks)
  ax.xaxis.set_tick_params(rotation=45)
  colors=['darkorange', 'royalblue', 'black', 'green', 'gold', 'purple']
  for i, color in enumerate(colors):
      bars[i].set_color(color)
  plt.show()
  '''
