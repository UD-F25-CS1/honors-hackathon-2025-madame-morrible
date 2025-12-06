from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

from meta import *

# hide_debug_information()
# set_website_framed(False)
set_website_title("What's in My Fridge")
set_site_information(
    "Anavi Chintam and Alekhya Veeramachineni",
    """
Our site helps user catalog items in their fridge and shows the expiration date. This helps
users keep track of everything in their fridge and encourages users to use food before they expire. 
""",
    [],
    [],
    [],
)


set_website_style("none")
add_website_css("""
body {
    background-color: thistle;
    font-size: 25px;
}

.name-box {
    background-color: pink;
    float: right;
}

button {
    padding: 12px 24px;
    font-size: 18px;
    border-radius: 20px;
    border: 2px solid black;
    background-color: lavenderblush;
    cursor: pointer;
}

select {
    padding: 12px 20px;
    font-size: 15px;
    cursor: pointer;
}

select:hover {
    background-color: plum;
}
""")



@dataclass
class Food:
    name: str
    exp: str  

@dataclass
class State:
    food_name: str
    current_date: str
    foods: list[Food]
    current_expiration: str
    history: list[str]

@route
def index(state: State) -> Page:
    return Page(state, [
        "What's in my fridge?",
        "Enter today's date (mm/dd/yyyy):",
        TextBox("date", state.current_date),
        Button("Next", food_list)
    ])

@route
def food_list(state: State) -> Page:
    if not state.foods:
        return Page(state, [
            "No foods added yet.",
            Button("Add Food", add_food),
            Button("Change date", index),
        ])
    else:
        state.history = []
        for food in state.foods:
            state.history.append("Food: " + food.name + " | Expiration: " + food.exp)
        return Page(state, [
            *state.history,
            Button("Add Food", add_food),
            Button("Change date", index),
            Button("Clear foods", clear_food)
        ])
    
@route
def clear_food(state: State) -> Page:
    state.foods = []
    return Page(state, [
        "All Foods Removed.",
        Button("Back", food_list)
    ])

@route
def add_food(state: State) -> Page:
    return Page(state, [
        "What is the name of the food you want to add?",
        TextBox("food", state.food_name),
        "When does this food expire? (mm/dd/yyyy)",
        TextBox("expired", state.current_expiration),
        Button("Add", check_food),
        Button("Back", food_list)
    ])

@route
def check_food(state: State, food: str, expired: str) -> Page:
    new_food = Food(food.strip(), expired.strip())
    
    state.foods.append(new_food)
    state.food_name = ""
    state.current_expiration = ""
    return Page(state, [
        "Food added successfully!",
        Button("Back", food_list)
    ])

start_server(State("", "", [], "", []))




