from db import fetch_all

clubs = fetch_all("SELECT * FROM clubs")

print("Връзката работи успешно!")
print(clubs)