import matplotlib.pyplot as plt
from ase.io import read
import pandas as pd

procdata = pd.read_csv("run1/proc_data.txt", delimiter=" ", names=["Temp", "Epot", "Ekin", "Vol"])
print(procdata)

proc2data = pd.read_csv("run2/proc2_data.txt", delimiter=" ", names=["Temp", "Epot", "Ekin", "Vol"])
print(proc2data)

plt.plot(procdata.Temp, procdata.Epot, "ko--", label="Run1") 
plt.plot(proc2data.Temp, proc2data.Epot, "r--", label="Run 2")

plt.xlabel = 'Temperatures'
plt.ylabel = 'Epot'
plt.title = 'Epot v Temps'
plt.legend()
plt.show()

plt.plot(procdata.Temp, procdata.Ekin, "ko--", label="Run1")
plt.plot(proc2data.Temp, proc2data.Ekin, "r--", label="Run 2")

plt.xlabel = 'Temperatures'
plt.ylabel = 'Ekin'
plt.title = 'Ekin v Temps'
plt.legend()
plt.show()

plt.plot(procdata.Temp, procdata.Vol, "ko--", label="Run1")
plt.plot(proc2data.Temp, proc2data.Vol, "r--", label="Run 2")

plt.xlabel = 'Temperatures'
plt.ylabel = 'Volume'
plt.title = 'Volume v Temps'
plt.legend()
plt.show()