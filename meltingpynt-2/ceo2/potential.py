import matplotlib.pyplot as plt
import numpy as np

q = 1.602176634e-19  # C
N_A = 6.02214076e23  # 1 / mol
epsilon_0 = 8.8541878128e-12  # F / m
Coulomb_const = 1 / (4 * np.pi * epsilon_0)  # N * m^2 / C^2


def bmh(z_i, z_j, A_ij, rho_ij, C_ij, r_ij_in_A):
    r_ij_in_m = r_ij_in_A * 1e-10  # m

    # Coulomb interaction
    U_Coulomb_in_J = Coulomb_const * z_i * z_j * q ** 2 / r_ij_in_m  # J
    U_Coulomb_in_kJ_per_mol = U_Coulomb_in_J / 1000 * N_A  # kJ / mol

    # Repulsive potential
    U_repulsive_in_kJ_per_mol = A_ij * np.exp(-r_ij_in_A / rho_ij)  # kJ / mol

    # van der Waals interaction
    U_vdW_in_kJ_per_mol = -C_ij / r_ij_in_A ** 6  # kJ / mol

    # Total potential
    U = U_Coulomb_in_kJ_per_mol + U_repulsive_in_kJ_per_mol + U_vdW_in_kJ_per_mol

    return U, U_Coulomb_in_kJ_per_mol, U_repulsive_in_kJ_per_mol, U_vdW_in_kJ_per_mol


def main():
    z_Ce = 4  # Ce4+
    z_O = -2  # O2-
    A_CeO = 11.350e4  # kJ/mol
    A_OO = 21.960e5  # kJ/mol
    rho_CeO = 0.3810  # Å
    rho_OO = 0.1490  # Å
    C_CeO = 0.0  # kJ * Å^6 / mol
    C_OO = 2.691e3  # kJ * Å^6 / mol
    r_ij = np.linspace(1.0, 10.0, 1000)  # Å
    U_CeO, U_CeO_Coulomb, U_CeO_repulsive, U_CeO_vdW = bmh(z_Ce, z_O, A_CeO, rho_CeO, C_CeO, r_ij)
    U_OO, U_OO_Coulomb, U_OO_repulsive, U_OO_vdW = bmh(z_O, z_O, A_OO, rho_OO, C_OO, r_ij)
    fig, axs = plt.subplot_mosaic([["CeO", "OO"]], figsize=(6, 4))
    axs["CeO"].plot(r_ij, U_CeO, label="Ce-O")
    axs["CeO"].plot(r_ij, U_CeO_Coulomb, ":", label="Ce-O Coulomb")
    axs["CeO"].plot(r_ij, U_CeO_repulsive, "--", label="Ce-O repulsive")
    axs["CeO"].plot(r_ij, U_CeO_vdW, "-.", label="Ce-O vdW")
    axs["CeO"].set_xlabel("r (Å)")
    axs["CeO"].set_ylabel("U (kJ/mol)")
    axs["CeO"].legend()
    axs["OO"].plot(r_ij, U_OO, label="O-O")
    axs["OO"].plot(r_ij, U_OO_Coulomb, ":", label="O-O Coulomb")
    axs["OO"].plot(r_ij, U_OO_repulsive, "--", label="O-O repulsive")
    axs["OO"].plot(r_ij, U_OO_vdW, "-.", label="O-O vdW")
    axs["OO"].set_xlabel("r (Å)")
    axs["OO"].set_ylabel("U (kJ/mol)")
    axs["OO"].legend()
    plt.tight_layout()
    plt.savefig("potential.png")


if __name__ == "__main__":
    main()
