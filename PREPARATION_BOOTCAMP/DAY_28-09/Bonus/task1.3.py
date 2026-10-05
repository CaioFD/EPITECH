def make_custom_sandwich(ingredients):
    if not any(i in ("ham", "tomato") for i in ingredients):
        print("Error: A sandwich needs ham or tomato!")
        return
    if ingredients.count("bread") < 2:
        print("Error: A sandwich needs top and bottom bread!")
        return
    for i in ingredients:
        print(i)

make_custom_sandwich(["bread", "lettuce", "tomato", "ham", "bread"])  
make_custom_sandwich(["bread", "lettuce", "tomato"])                  
make_custom_sandwich(["bread", "lettuce", "bread"])                   