
from pyscript import document

my_list = [
    "Rhejz Cabonilas",
    "Maleek Beh",
    "Liam Isaac Estrella",
    "John Nathan Vasallo",
    "Grace Cindy Jung",
    "Renzel Andrei Clarino",
    "Czania Michail Tupaz",
    "Rizalina Narciso",

]

def check_candidate(e):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    full_name = first_name + " " + last_name

    is_member = full_name.casefold() in [
        name.casefold() for name in my_list
    ]

    messages = {
        True: "Congratulations " + full_name +
              "! You are now part of the COCC club.",
        False: "Sorry " + full_name +
               ", your name is not on the list."
    }

    result = document.getElementById("result")
    result.innerHTML = messages[is_member]

    result.style.backgroundColor = (
        "#e5f1e2" if is_member else "#f7e9e6"
    )
    result.style.color = "#405744"
