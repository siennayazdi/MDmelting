import numpy as np
from ase.io import read
import matplotlib.pyplot as plt


def main():
    traj = read("npt.extxyz", ":")
    time = np.arange(0, 5000 * 5, 5 * 50)
    vol = [x.get_volume() for x in traj]
    plt.plot(time, vol)
    plt.xlabel("Time (fs)")
    plt.ylabel("Volume (A^3)")
    plt.text(0.1, 0.9, f"Initial volume = {vol[0]}", transform=plt.gca().transAxes)
    plt.savefig("volume.png")


if __name__ == "__main__":
    main()
