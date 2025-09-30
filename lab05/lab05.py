"""
Lab 05: Functions and Error Handling
"""

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
    {"name": "eve", "is_active": True, "email": "eve@example.com"},
]


def calculate_average_age(users_list):
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users_list : list of dict
        A list of user dictionaries. Each dictionary may contain an "age" key.

    Returns
    -------
    float
        The average age of valid users, or 0.0 if the list is empty
        or no valid ages are found.

    Notes
    -----
    This function skips users whose "age" is not an integer.
    It handles empty lists and division by zero gracefully.
    """
    total_age = 0
    count = 0
    try:
        for user in users_list:
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


def get_active_user_emails(users_list):
    """
    Get the email addresses of active users.

    Parameters
    ----------
    users_list : list of dict
        A list of user dictionaries. Each dictionary may contain
        "is_active" and "email" keys.

    Returns
    -------
    list of str
        A list of email addresses for users who are active.
        Returns an empty list if none are found.

    Notes
    -----
    This function handles missing keys gracefully and returns
    an empty list instead of crashing.
    """
    active_emails = []
    try:
        for user in users_list:
            if user.get("is_active") and user.get("email"):
                active_emails.append(user["email"])
        return active_emails
    except KeyError as e:
        print(f"error: missing key {e} in user data.")
        return []


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
