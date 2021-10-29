# Are Electric Cars Actually Better for the Climate Than Gas Ones?
Code used to calculate the equivalent litres per hundred kilomoeters (eLHK) of an electric car, on a GHG emission basis.
To calculate the eLHK for an electric car in your region,

  1. Do some research. Find the fraction of total energy generated that each type of power plant is responsible for in your region.
  2. Write down a numpy array with entries equal to the fraction of total energy for each type of plant. The order should be [coal, natural gas, nuclear, hydro, wind, solar, geo, bio]. The array should sum to 1.
  3. Plug that array into `get_kgCO2_per_km` in `kgCO2.py` to obtain the eLHK.
  4. Profit?

The rest of the code is for plotting. Adapt and use it if you dare.
The other file (`eLHK.py`) is now obsolete.
