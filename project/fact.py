import random
fact_list = ["The first computer mouse: Made of wood", "18% of total emissions comes from operating our homes.", "LED light bulbs use up to 80% less energy than traditional incandescent bulbs"]


fact = random.choices(fact_list,k=1)
print(fact)