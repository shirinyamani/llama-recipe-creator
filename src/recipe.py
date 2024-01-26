from utils import *

class RecipeGenerator:
    def __init__(self):
            
        self.list_of_ingredients = self.ask_for_ingredients()

    @staticmethod
    def ask_for_ingredients():
        list_of_ingredients = []
        while True:
            ingredient = input("Enter an ingredient (or type 'done' to finish): ")
            if ingredient.lower() == "done":
                break
            list_of_ingredients.append(ingredient)
        print(f"Your ingredients are: {', '.join(list_of_ingredients)}")
        return list_of_ingredients

    def generate_recipe(self):
        prompt = RecipeGenerator.create_recipe_prompt(self.list_of_ingredients)
        if RecipeGenerator._verify_prompt(prompt):
            response = RecipeGenerator.generate(prompt)
            return response
        print("Sorry about that!")

    @staticmethod
    def create_recipe_prompt(list_of_ingredients):
        prompt = f"Create a detailed recipe based on only the following ingredients: {', '.join(list_of_ingredients)}."
        return prompt

    @staticmethod
    def _verify_prompt(prompt):
        print(prompt)
        response = input("Are you happy with the prompt? (y/n)")
        if response.upper() == "Y":
            return True
        return False

    @staticmethod
    def generate(prompt):
        response = call_llama2(
            model='llama2', 
            prompt=prompt, 
            stream=False)
        return response

    def store_recipe(self, recipe, filename):
        with open(filename, "w") as f:
            f.write(recipe)

