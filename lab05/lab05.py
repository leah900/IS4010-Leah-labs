# Messy script to be refactored
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

def calculate_average_age(users):
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users : list of dict
        A list of user dictionaries. Each may contain an 'age' key.

    Returns
    -------
    float
        Average age of users with valid ages.
        Returns 0.0 if no valid ages are found or if the list is empty.
    """
    total_age = 0
    count = 0

    try:
        for user in users:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                count += 1

        if count == 0:
            raise ZeroDivisionError

        return total_age / count

    except ZeroDivisionError:
        print("error: cannot calculate average age of an empty list or no valid ages.")
        return 0.0
    except Exception as e:
        print(f"unexpected error while calculating average age: {e}")
        return 0.0


def get_active_user_emails(users):
    """
    Get a list of emails for active users.

    Parameters
    ----------
    users : list of dict
        A list of user dictionaries. Each may contain 'is_active' and 'email'.

    Returns
    -------
    list of str
        A list of emails belonging to active users.
        Returns an empty list if no active users with emails exist.
    """
    emails = []
    try:
        for user in users:
            if user.get("is_active") and user.get("email"):
                emails.append(user["email"])
        return emails
    except Exception as e:
        print(f"unexpected error while collecting emails: {e}")
        return []


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
