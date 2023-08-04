import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lammps.formats import LogFile


def main():
    logfile = LogFile("log.lammps")
    # number of runs
    nruns = len(logfile.runs)
    print("Number of runs: {}".format(nruns))
    T = []
    Epot = []
    Ekin = []
    U = []
    P = []
    V = []
    for run in logfile.runs[1:]:
        df = pd.DataFrame(run)
        # number of steps
        nsteps = len(df)
        df_eq = df.iloc[nsteps // 2:]
        T.append(df_eq["Temp"].mean())
        Epot.append(df_eq["PotEng"].mean())
        Ekin.append(df_eq["KinEng"].mean())
        U.append(df_eq["TotEng"].mean())
        P.append(df_eq["Press"].mean())
        V.append(df_eq["Volume"].mean())
    plt.plot(T, Epot, "o:", label="Epot")
    plt.plot(T, U, "o:", label="U")
    plt.xlabel("T (K)")
    plt.ylabel("E (kcal/mol)")
    plt.savefig("Epot_U_vs_T.png")


if __name__ == "__main__":
    main()
