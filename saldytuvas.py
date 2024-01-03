def main():
    pass

def insert_item(item_name: str, item_quantity: float): #Balys
    fridge_items = []
    item_add = {"Item name:": item_name, "Item quantity": item_quantity}
    fridge_items.append(item_add)
    print(f"{item_quantity}x{item_name} was added to the fridge")
    return fridge_items

def remove_iems(item_name: list, item_quantity: int) -> list:
    removed_task = item_name.pop(item_quantity)
    print(f"Removed task: {removed_task['name']}")
    return fridge_items
        


def search_item():
    pass

def print_items(fridge_items): 
    if not fridge_items:
        print('Šaldytuvas yra tuščias. Badauk arba įdėk ką nors')
    else:
        print('Šaldytuve esantys produktai:')
        for index, (item_name, item_quantity) in enumerate(fridge_items.items(), start=1):
            print(f'{index}. {item_name} : {item_quantity}')
            return



def remove_iems(produktai: list, task_index: int) -> list:
    removed_task = produktai.pop(task_index)
    print(f"Removed task: {removed_task['name']}")
    return produktai


""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""
