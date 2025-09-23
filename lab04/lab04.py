# lab04.py

def find_common_elements(list1, list2):
    """Find the common elements between two lists.

    Returns a list containing elements present in both inputs.
    Order of the result does not matter and duplicates are removed.
    """
    if not list1 or not list2:
        return []
    # use set intersection for performance on large lists
    return list(set(list1) & set(list2))


def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Converts the list to a dict for O(1) average-case lookups.
    Returns the user dict or None if not found.
    """
    if not users:
        return None
    user_dict = {user["name"]: user for user in users}
    return user_dict.get(name)


def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    Order of even numbers is preserved.
    """
    return [n for n in numbers if n % 2 == 0]
