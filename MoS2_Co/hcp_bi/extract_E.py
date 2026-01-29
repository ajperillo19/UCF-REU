import re


### Create a function to extract the last iteration of magnetization calculation
def extract_last(pattern, content, default = None, flags = 0):
    #findall method returns a list of all captured groups
    matches = re.findall(pattern, content, flags)
    #Get the results of the last element in the list
    return matches[-1] if matches else default

# Read the SCF output
with open("hcp_bi.out", "r") as file:
    content = file.read()

# Extract Total Energy to eventually determine most stable configuration
final_pat       = r"\s+Final energy\s+=\s+([\d\.\-Ee+]+)"
total_pat          = r"\s+total magnetization\s+=\s+([\d\.\-Ee+]+)"
absolute_pat       = r"\s+absolute magnetization\s+=\s+([\d\.\-Ee+]+)"

#Find final magnetizations
final_energy = extract_last(final_pat, content, default = "Not found")
total_mag = extract_last(total_pat, content, default = "Not found")
absolute_mag = extract_last(absolute_pat, content, default = "Not found")

# Pack into a dictionary for efficiency
params = {
    
    "Total Energy (Ry)"                  : final_energy,
    "Total Magnetization (μB/cell)"      : total_mag,
    "Absolute Magnetization (μB/cell)"   : absolute_mag, 

}

# Write to text file
with open("hcp_bi.txt", "w") as out:
    for key, val in params.items():
        out.write(f"{key}: {val}\n")

print("Parameters written to hcp_bi.txt")

