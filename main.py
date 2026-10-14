# Student club member checker
from pyscript import display, document

def student_club(e):
    document.getElementById('checkmember').innerHTML = " "

    firstname = document.getElementById('first_name').value.strip()
    lastname = document.getElementById('last_name').value.strip()

    # List of registered art club members
    artclub_members = [
        "Jane Doe",
        "John Doe",
        "Tai Lung",
        "Lotus Po"
    ]

    member_checker = f'{firstname} {lastname}' in artclub_members

    display_message = (
        f'Sorry, {firstname} {lastname}, you are not a member.',
        f'Welcome, {firstname} {lastname}! You are a member.'
    )

    display(display_message[member_checker], target="checkmember")