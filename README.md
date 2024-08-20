# Protocell Simulation

![Protocell Formation.png](https://github.com/chrisk60331/protocell-simulation/blob/main/ProtoCell%20Formation.png)

This project simulates the formation and division of protocells, representing a model for the early stages of life. The simulation tracks the creation of essential molecules, including lipids, nucleotides, amino acids, and RNA, and models the behavior of protocells, including their division when they reach a critical threshold of RNA.

## Features

- **Abiotic Synthesis:** Simulates the formation of lipid precursors, fatty acids, lipids, and other organic molecules from simple precursors like methane, water, carbon dioxide, and ammonia.
- **Protocell Formation:** Models the formation of vesicles (protocells) from lipids and tracks the accumulation of RNA and other contents within these protocells.
- **Protocell Division:** Implements a mechanism where protocells divide when they contain a certain amount of RNA, mimicking the early replication processes of life.
- **Data Visualization:** Provides visualizations of the vesicle count, RNA count, and cumulative protocell divisions over time.

## Requirements
You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```
## Usage
To run the simulation and visualize the results:

1. Clone this repository:
    ```bash
    git clone https://github.com/chrisk60331/protocell-simulation.git
    cd protocell-simulation
    ```

2. Run the simulation script:
    ```bash
    python main.py
    ```

The simulation will output the final counts of molecules and the number of protocell divisions. Additionally, it will generate plots showing the vesicle count, RNA count, and cumulative protocell divisions over time.

## Simulation Parameters

- **Energy Sources:** The simulation uses UV and hydrothermal energy sources, with configurable energy levels.
- **Reaction Yields:** Each reaction in the simulation has a configurable yield and energy requirement, allowing you to explore different scenarios of early chemical evolution.
- **Division Threshold:** The number of RNA molecules required to trigger a protocell division is adjustable, affecting how frequently divisions occur.

## Visualization

The simulation produces three key plots:
1. **Vesicle Count Over Time:** Shows the number of vesicles formed throughout the simulation.
2. **RNA Count Over Time:** Tracks the accumulation of RNA within the protocells.
3. **Cumulative Protocell Divisions:** Displays the total number of protocell divisions that have occurred.

These visualizations help to understand the dynamics of early protocell formation and division.

```