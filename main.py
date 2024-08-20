import random

import matplotlib.pyplot as plt

# Data for visualization
cycles = list(range(5000))
vesicle_counts = []
rna_counts = []
division_counts = []
reactions = {
    'lipid_precursor': {
        'reactants': {'CH4': 2, 'H2O': 2, 'CO2': 1, 'NH3': 1},
        'energy_required': 50,
        'yield': 5  # High yield for lipid precursors
    },
    'fatty_acid': {
        'reactants': {'lipid_precursor': 2, 'H2': 2, 'CO': 1},
        'energy_required': 600,  # Adjusted energy requirement
        'yield': 20  # High yield for fatty acids
    },
    'lipid': {
        'reactants': {'fatty_acid': 2},
        'energy_required': 80,
        'yield': 4  # High yield for lipids
    },
    'vesicle': {
        'reactants': {'lipid': 2},
        'energy_required': 50,
        'yield': 1
    },
    'nucleotide': {
        'reactants': {'H2O': 2, 'NH3': 1, 'CO2': 1},
        'energy_required': 60,
        'yield': 2
    },
    'amino_acid': {
        'reactants': {'CH4': 1, 'NH3': 1, 'H2': 1},
        'energy_required': 50,
        'yield': 2
    },
    'rna': {
        'reactants': {'nucleotide': 4, 'vesicle': 1},
        'energy_required': 100,
        'yield': 1
    }
}

# Energy sources
energy_sources = {
    'UV': 80000,
    'hydrothermal': 800000
}
# Reset the simulation to gather data for visualization
molecules = {
    'CH4': 100,  # Methane
    'H2O': 100,  # Water
    'CO2': 100,  # Carbon dioxide
    'NH3': 100,  # Ammonia
    'H2': 50,  # Hydrogen
    'CO': 50,  # Carbon monoxide
    'lipid_precursor': 0,  # Lipid precursor
    'fatty_acid': 0,  # Fatty acid
    'lipid': 0,  # Lipid
    'vesicle': 0,  # Vesicle
    'nucleotide': 0,  # Nucleotide
    'amino_acid': 0,  # Amino acid
    'rna': 0  # RNA
}

# Reset the division counter
division_counter = 0


# Function to simulate protocell division and gather data
def simulate_protocell_division(molecules, cycle, division_threshold=100):
    global division_counter
    if molecules['rna'] >= division_threshold:
        # Perform division
        molecules['vesicle'] += 1  # Create a new vesicle
        molecules['rna'] = int(molecules['rna'] / 2)  # Divide RNA evenly between the two vesicles
        division_counter += 1  # Increment the division counter

    # Store data for visualization
    vesicle_counts.append(molecules['vesicle'])
    rna_counts.append(molecules['rna'])
    division_counts.append(division_counter)


# Simulation function with data collection
def simulate_abiotic_synthesis_with_visualization(molecules, reactions, energy_sources, cycles=5000):
    for cycle in range(cycles):
        # Select an energy source randomly
        energy_available = random.choice(list(energy_sources.values()))

        # Attempt to perform all reactions, prioritizing those that produce intermediates
        for reaction_name, reaction in reactions.items():
            if energy_available >= reaction['energy_required']:
                if all(molecules[m] >= reaction['reactants'][m] for m in reaction['reactants']):
                    for reactant in reaction['reactants']:
                        molecules[reactant] -= reaction['reactants'][reactant]
                    molecules[reaction_name] += reaction['yield']

        # Check for protocell division and collect data
        simulate_protocell_division(molecules, cycle)

    return molecules


# Run the simulation with data collection
final_molecules = simulate_abiotic_synthesis_with_visualization(molecules, reactions, energy_sources, cycles=5000)

# Plot the results
plt.figure(figsize=(14, 8))

plt.subplot(3, 1, 1)
plt.plot(cycles, vesicle_counts, label="Vesicle Count", color='blue')
plt.xlabel('Cycles')
plt.ylabel('Vesicle Count')
plt.title('Vesicle Count Over Time')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(cycles, rna_counts, label="RNA Count", color='green')
plt.xlabel('Cycles')
plt.ylabel('RNA Count')
plt.title('RNA Count Over Time')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(cycles, division_counts, label="Protocell Divisions", color='red')
plt.xlabel('Cycles')
plt.ylabel('Division Count')
plt.title('Cumulative Protocell Divisions Over Time')
plt.legend()

plt.tight_layout()
plt.show()

