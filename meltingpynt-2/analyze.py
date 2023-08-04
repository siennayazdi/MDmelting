import matplotlib.pyplot as plt
import numpy as np
from ase.io import read


def main():
    atoms = read("example.extxyz", ":")

    # volume
    V = [atom.get_volume() for atom in atoms]
    t = np.arange(0, 10000, 100) * 5
    plt.plot(t, V)
    plt.xlabel("Time (fs)")
    plt.ylabel(r"Volume ($\rm \AA^3$)")
    plt.savefig("volume.png")

    # energy
    E = [atom.get_potential_energy() for atom in atoms]
    plt.plot(t, E)
    plt.xlabel("Time (fs)")
    plt.ylabel("Energy (eV)")
    plt.savefig("energy.png")


if __name__ == "__main__":
    main()
