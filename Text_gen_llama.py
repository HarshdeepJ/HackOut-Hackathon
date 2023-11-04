import json
from llama_cpp import Llama

print("Loading model ....")
llm = Llama(model_path=r"model\llama-2-7b-chat.Q5_K_S.gguf")
print("model loaded")

print("Running Model...")
output = llm(
    """Question: give me a prompt to create an image for the given text:  Photosynthesis is the process by which green plants, algae, and some bacteria convert light energy from the sun into chemical energy in the form of glucose (a sugar). It occurs in chloroplasts, specialized structures in plant cells. Here's a simplified overview:

Light Absorption: Chlorophyll, a green pigment in chloroplasts, captures light energy from the sun.

Water Uptake: Plants take in water through their roots, and this water is used in the process.

Carbon Dioxide (CO2) Intake: Plants also absorb carbon dioxide from the air through tiny openings called stomata.

Conversion: In the chloroplasts, light energy is used to combine water and carbon dioxide to produce glucose and oxygen. This chemical reaction is represented as:

6 CO2 + 6 H2O + light energy → C6H12O6 (glucose) + 6 O2

Sugar Production: Glucose is used for energy and stored as starch for later use.

Oxygen Release: Oxygen (O2) is released into the atmosphere as a byproduct of photosynthesis, which is essential for the respiration of animals and other organisms.

In summary, photosynthesis is the process through which plants use sunlight to convert carbon dioxide and water into glucose, providing them with energy and releasing oxygen into the atmosphere.Answer: """,
    max_tokens=200,
    temperature=0.9,
    echo=True
)

print(json.dumps(output, indent=2))