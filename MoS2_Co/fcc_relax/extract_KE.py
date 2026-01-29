import re

def extract_parameter(pattern, content, group=1, default="Not found"):
    match = re.search(pattern, content)
    return match.group(group).strip() if match else default

# Read the SCF output
with open("relax_MoS2_Co.out", "r") as file:
    content = file.read()

# Extract Total Energy to eventually determine most stable configuration
total_energy       = extract_parameter(r"\s+Final energy\s+=\s+([\d\.\-Ee+]+)", content)

# Pack into a dictionary for efficiency
params = {
    
    "Total Energy (Ry)"          : total_energy,

}

# Write to text file
with open("relax_MoS2_Co.txt", "w") as out:
    for key, val in params.items():
        out.write(f"{key}: {val}\n")

print("Parameters written to relax_MoS2_Co.txt")

