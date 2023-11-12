import requests
import tkinter as tk

def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        return None


def show_pokemon_info():
    pokemon_name = entry.get()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"Height: {pokemon_info['height']}")
        print(f"Weight: {pokemon_info['weight']}")
    else:
        print("Pokemon not found.")


window = tk.Tk()
window.title("Pokemon App")
window.minsize(width=450,height=450)

label = tk.Label(window, text="Pokemon Name:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Get Pokemon Info", command=show_pokemon_info)
button.pack()

window.mainloop()