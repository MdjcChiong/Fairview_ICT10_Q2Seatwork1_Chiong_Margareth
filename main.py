
from pyscript import document

club_members = [
    "Cianna Del Prado",
    "Jamie Garcia",
    "Mateo Salacup",
    "Juan Cruz"
]

def verify_candidate(event):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    full_name = first_name + " " + last_name

    is_member = full_name.lower() in [
        name.lower() for name in club_members
    ]

    member_message = f"Congratulations {full_name}! You are now part of the Rainbow Catering Club."
    non_member_message = f"Sorry {full_name}, your name is not on the list."

    document.getElementById("result").innerText = (
        member_message if is_member else non_member_message
    )
