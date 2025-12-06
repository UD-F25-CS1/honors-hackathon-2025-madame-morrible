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

@dataclass
class State:
    pass

@route
def index(state: State) -> Page:
    return Page(state, ["Hello ___!"])


start_server(State())
