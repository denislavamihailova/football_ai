from clubs_repository.clubsrepositories import (
    add_club,
    list_clubs,
    update_club,
    delete_club
)


print("---- СПИСЪК ПРЕДИ ----")
print(list_clubs())

# ADD
club_id = add_club("Черно море", "Варна", 1913)
print("Добавен клуб с ID:", club_id)

print("---- СПИСЪК СЛЕД ADD ----")
print(list_clubs())

# UPDATE
update_club(club_id, "Черно море Варна", "Варна", 1913)
print("---- СЛЕД UPDATE ----")
print(list_clubs())

# DELETE
delete_club(club_id)
print("---- СЛЕД DELETE ----")
print(list_clubs())