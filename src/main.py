from recipe import RecipeGenerator




if __name__ == "__main__":
    """
    Test RecipeGenerator class without creating an image of the dish.
    """

    gen = RecipeGenerator()
    recipe = gen.generate_recipe()
    print(recipe)