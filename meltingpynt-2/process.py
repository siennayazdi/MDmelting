from ase.io import read, write
from ase.io import Trajectory






def cal_avg_pe(traj_file, start_frame):

        atoms = read(traj_file, ':')
        sliced_atoms = atoms[start_frame:]
        potential_energies = [atoms.get_potential_energy() for atoms in sliced_atoms]
        average_potential_energy = sum(potential_energies) / len(potential_energies)
        return average_potential_energy

def calc_avg_ke(traj_file, start_frame):

        atoms = read(traj_file, ':')
        sliced_atoms = atoms[start_frame:]
        kinetic_energies = [atoms.get_kinetic_energy() for atoms in sliced_atoms]
        average_kinetic_energy = sum(kinetic_energies) / len(kinetic_energies)
        return average_kinetic_energy

def calc_avg_volume(traj_file, start_frame):
        atoms = read(traj_file, ':')
        sliced_atoms = atoms[start_frame:]
        volumes = [atoms.get_volume() for atoms in sliced_atoms]
        average_volume = sum(volumes) / len(volumes)
        return average_volume

def main(T):

    traj_file = 'run2/npt_' + str(T) + '.traj'
    atoms = read(traj_file, ':')
    start_frame = 20 
    average_potential_energy = cal_avg_pe(traj_file, start_frame)
    average_kinetic_energy = calc_avg_ke(traj_file, start_frame) 
    average_volume = calc_avg_volume(traj_file, start_frame)
    print(T, average_potential_energy, average_kinetic_energy, average_volume)
    atomm = write(traj_file + ".extxyz", atoms, "extxyz")
if __name__ == "__main__":
    Ts = [40, 50, 60, 70, 80, 90, 100, 110, 120]
    for T in Ts:
        main(T)
