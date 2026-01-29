import re

def extract_parameter(pattern, content, group=1, default="Not found"):
    match = re.search(pattern, content)
    return match.group(group).strip() if match else default

# Read the SCF output
with open("scf.out", "r") as file:
    content = file.read()

# Extract all parameters as before...
program_name       = extract_parameter(r"Program (\w+)", content)
version            = extract_parameter(r"Program \w+ v\.([\d.]+)", content)
start_datetime     = extract_parameter(r"starts on (\d+\w+\d+) at (\d+:\d+:\d+)", content, group=0)
processors         = extract_parameter(r"running on\s+(\d+)\s+processors", content)
unit_cell_volume   = extract_parameter(r"unit-cell volume\s+=\s+([\d.Ee+-]+)", content)
n_atoms            = extract_parameter(r"number of atoms/cell\s+=\s+(\d+)", content)
n_types            = extract_parameter(r"number of atomic types\s+=\s+(\d+)", content)
n_electrons        = extract_parameter(r"number of electrons\s+=\s+([\d.]+)", content)
n_bands            = extract_parameter(r"number of Kohn-Sham states=\s+(\d+)", content)
ecutwfc            = extract_parameter(r"kinetic-energy cutoff\s+=\s+([\d.]+)", content)
ecutrho            = extract_parameter(r"charge density cutoff\s+=\s+([\d.]+)", content)
conv_thr           = extract_parameter(r"convergence threshold\s+=\s+([\d.Ee+-]+)", content)
n_kpoints          = extract_parameter(r"number of k points=\s+(\d+)", content)
potential_files    = re.findall(r"Pseudopotential file:\s+(\S+)", content)
valence_e_per_atom = re.findall(r"valence electrons\s*=\s*([\d.]+)", content)
n_iterations       = len(re.findall(r"iteration #", content))
total_energy       = extract_parameter(r"!\s+total energy\s+=\s+([\d\.\-Ee+]+)", content)
stop_datetime      = extract_parameter(r"ends on (\d+\w+\d+) at (\d+:\d+:\d+)", content, group=0)
walltime           = extract_parameter(r"This run was terminated on\s+([\d.]+) secs", content)

# Pack into a dictionary (optional)
params = {
    "Program Name"               : program_name,
    "Version"                    : version,
    "Start DateTime"             : start_datetime,
    "Processors Used"            : processors,
    "Unit-cell Volume"           : unit_cell_volume,
    "Number of Atoms"            : n_atoms,
    "Number of Atomic Types"     : n_types,
    "Number of Electrons"        : n_electrons,
    "Number of Bands"            : n_bands,
    "Kinetic-energy Cutoff (Ry)" : ecutwfc,
    "Charge Density Cutoff (Ry)" : ecutrho,
    "Convergence Threshold"      : conv_thr,
    "Number of k-points"         : n_kpoints,
    "Potential Files"            : ", ".join(potential_files) or "Not found",
    "Valence Electrons/Atom"     : ", ".join(valence_e_per_atom) or "Not found",
    "Number of Iterations"       : n_iterations,
    "Total Energy (Ry)"          : total_energy,
    "Stop DateTime"              : stop_datetime,
    "Walltime (sec)"             : walltime,
}

# Write to text file
with open("scf_params.txt", "w") as out:
    for key, val in params.items():
        out.write(f"{key}: {val}\n")

print("All parameters written to scf_params.txt")

