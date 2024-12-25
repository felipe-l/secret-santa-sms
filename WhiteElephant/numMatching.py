import json
import random

def number_participants(input_file, output_file):
    """Reads participants from a JSON file, assigns random numbers to them, writes to an output file, and generates a visualization."""
    with open(input_file, "r") as file:
        data = json.load(file)
    
    participants = data.get("participants", [])
    
    # Generate a list of random numbers for each participant
    random_numbers = random.sample(range(1, len(participants) + 1), len(participants))
    
    numbered_participants = [
        {"numero": random_numbers[i], "nombre": participant["name"], "telefono": participant["phone"]}
        for i, participant in enumerate(participants)
    ]
    
    with open(output_file, "w") as file:
        json.dump({"participantes": numbered_participants}, file, indent=4)
    
    # Generate a simple text-based visualization to show the queue order
    visualization = "\nOrden de Cola de Participantes:\n"
    for participant in sorted(numbered_participants, key=lambda x: x["numero"]):
        visualization += f"{participant['numero']}: {participant['nombre']}\n"
    
    with open("orden_de_cola_de_participantes_visualizacion.txt", "w") as file:
        file.write(visualization)

# Define input and output file paths
input_file = "../participants.json"
output_file = "participantes_numerados.json"

# Number the participants, write to the output file, and generate a visualization
number_participants(input_file, output_file)
