from db import execute, fetch_all, fetch_one


# CREATE
def add_club(name, city=None, founded_year=None):
    if not name or name.strip() == "":
        raise ValueError("Името на клуба не може да е празно.")

    sql = """
    INSERT INTO clubs (name, city, founded_year)
    VALUES (%s, %s, %s)
    """

    result = execute(sql, (name, city, founded_year))

    if result is None:
        raise Exception("Грешка при добавяне на клуб (възможно е дублиране).")

    club_id, _ = result
    return club_id


# READ – всички
def list_clubs():
    sql = "SELECT * FROM clubs ORDER BY name"
    return fetch_all(sql)


# READ – по ID
def get_club_by_id(club_id):
    sql = "SELECT * FROM clubs WHERE id = %s"
    return fetch_one(sql, (club_id,))


# READ – по име
def find_club_by_name(name):
    sql = "SELECT * FROM clubs WHERE name = %s"
    return fetch_one(sql, (name,))


# UPDATE
def update_club(club_id, name, city=None, founded_year=None):
    if not club_id:
        raise ValueError("Невалиден ID.")

    if not name or name.strip() == "":
        raise ValueError("Името не може да е празно.")

    sql = """
    UPDATE clubs
    SET name = %s, city = %s, founded_year = %s
    WHERE id = %s
    """

    result = execute(sql, (name, city, founded_year, club_id))

    if result is None:
        raise Exception("Грешка при update.")

    _, affected_rows = result
    return affected_rows


# DELETE
def delete_club(club_id):
    if not club_id:
        raise ValueError("Невалиден ID.")

    sql = "DELETE FROM clubs WHERE id = %s"
    result = execute(sql, (club_id,))

    if result is None:
        raise Exception("Грешка при изтриване.")

    _, affected_rows = result
    return affected_rows