import sys

from ase.io import read, write


def main(path):
    atoms = read(path, ":")
    write(path.replace(".traj", ".extxyz"), atoms, "extxyz")


if __name__ == "__main__":
    main(sys.argv[1])
