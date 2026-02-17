import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


def get_connection():
    """
    Създава и връща връзка към MySQL базата.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print("❌ Грешка при свързване към базата:", e)
        return None


def execute(sql, params=None):
    """
    Използва се за INSERT, UPDATE, DELETE.
    Връща: (lastrowid, affected_rows)
    """
    connection = get_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(sql, params or ())
        connection.commit()

        last_id = cursor.lastrowid
        affected = cursor.rowcount

        cursor.close()
        return last_id, affected

    except Error as e:
        print("❌ SQL грешка:", e)
        return None

    finally:
        connection.close()


def fetch_all(sql, params=None):
    """
    Връща списък от редове (SELECT много резултати).
    """
    connection = get_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        results = cursor.fetchall()
        cursor.close()
        return results

    except Error as e:
        print("❌ SQL грешка:", e)
        return []

    finally:
        connection.close()


def fetch_one(sql, params=None):
    """
    Връща един ред (SELECT един резултат).
    """
    connection = get_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        result = cursor.fetchone()
        cursor.close()
        return result

    except Error as e:
        print("❌ SQL грешка:", e)
        return None

    finally:
        connection.close()