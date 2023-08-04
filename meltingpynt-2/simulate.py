from ase import units
from ase.build import bulk, make_supercell
from ase.calculators.lj import LennardJones
from ase.io import Trajectory
from ase.md.npt import NPT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
import numpy as np
rng=np.random.default_rng(9000)


def main(P, T, N):
    dt = 5.0 * units.fs
    atoms = make_supercell(bulk("Ar", cubic=True), [[N, 0, 0], [0, N, 0], [0, 0, N]])
    atoms.calc = LennardJones(sigma=3.4, epsilon=120 * units.kB)
    MaxwellBoltzmannDistribution(atoms, temperature_K=T, rng=rng)
    ptime = 75 * units.fs
    dyn = NPT(atoms, timestep=dt, temperature_K=T, externalstress=P, ttime=25 * units.fs,
              pfactor=ptime ** 2 * 100 * units.GPa)
    filename = 'run2/npt_' + str(T) + '.traj'
    traj = Trajectory(filename, 'w', atoms)
    dyn.attach(traj.write, interval=100)

    def printenergy(a=atoms):  # store a reference to atoms in the definition.
        """Function to print the potential, kinetic and total energy."""
        epot = a.get_potential_energy() / len(a)
        ekin = a.get_kinetic_energy() / len(a)
        print('Energy per atom: Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  '
              'Etot = %.3feV' % (epot, ekin, ekin / (1.5 * units.kB), epot + ekin))

    # Now run the dynamics
    dyn.attach(printenergy, interval=100)
    printenergy()
    dyn.run(5000)


if __name__ == "__main__":
    Ps = [1] #pressures
    Ts = [40, 50, 60, 70, 80, 90, 100, 110, 120]
    Ns = [5] # 5 on x axiz, 5 on y axis, and 5 on z axis = 125
    for P in Ps:
        for T in Ts:
            for N in Ns: 
                main(P * units.bar, T, N)

