from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 3000 
PROTEIN_GOAL_LIMIT = 180
FAT_GOAL_LIMIT = 80
CARBS_GOAL_LIMIT = 300


today = []

@dataclass
class Food:
    name: str
    calories: int
    proteins:int
    fats: int
    carbs: int


done = False

while not done:
    print("""
    (1) Add a new food
    (2) Visualize progress
    (q) Quit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new food!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        proteins = int(input("Protein: "))
        fats = int(input("Fat: "))
        carbs =int(input("Carbs: "))
        food = Food(name, calories, proteins, fats, carbs)
        today.append(food)
        print("Successfully added!")

    elif choice == "2":
        calories_sum = sum(food.calories for food in today)
        proteins_sum = sum(food.proteins for food in today)
        fats_sum = sum(food.fats for food in today)
        carbs_sum = sum(food.carbs for food in today)

        fig, axis = plt.subplots(2, 2)
        axis[0, 0].pie([proteins_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%" )
        axis[0, 0].set_title("Macronutrients Distribution")

        axis[0, 1].bar([0, 1, 2], [proteins_sum, fats_sum, carbs_sum], width=0.4)
        axis[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL_LIMIT, FAT_GOAL_LIMIT, CARBS_GOAL_LIMIT], width=0.4)
        axis[0, 1].set_title("Macronutrients Progress ")
        
        axis[1, 0].pie([calories_sum, CALORIE_GOAL_LIMIT - calories_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
        axis[1, 0].set_title("Calories Goal Progress")
        axis[1, 1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label="Calories eaten")
        axis[1, 1].plot(list(range(len(today))), [CALORIE_GOAL_LIMIT] * len(today), label="Calorie Goal")
        axis[1, 1].legend()
        axis[1, 1].set_title("Calories Goal Over Time")

        fig.tight_layout()
        plt.show()
    elif choice == "q":
        done = True
    else:
        print("Invalid choice!!")