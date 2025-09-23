# Lab 04: AI-assisted data structure selection

## Problem 1: Finding common items
**Prompt:**  
“I have two very large lists involving product IDs from two suppliers. I need to find product IDs that both lists show. The order doesn’t matter, and performance matters. For what should I use a particular Python data structure?”

**AI Response and Reasoning:**  
You should use a **set**.  
- **Reasoning:** Sets in Python are implemented as hash tables, which makes membership checks and intersections very fast (average O(1) time per check). By converting both lists into sets and using the intersection operation (`&`), you can efficiently find all product IDs that appear in both lists.

---

## Problem 2: User profile lookup
**Prompt:**  
“My application loads a database list of user profiles. Each user has a unique username, an age, and an email. I have a frequent need to look up users by their username. It is critical that this performs well. Why should I use which Python data structure in particular?”

**AI Response and Reasoning:**  
You should use a **dictionary** with the username as the key and the user profile as the value.  
- **Reasoning:** Dictionaries in Python are implemented as hash tables, allowing O(1) average-time lookups by key. By creating a dictionary where usernames map to user profiles, you can instantly retrieve a user’s data without iterating through a list.

---

## Problem 3: Listing even numbers in order
**Prompt:**  
“A list of integers showing sensor readings is given to me. I need to make up a report that only contains each of the even numbers; these numbers must be put in the exact same order as they appear in the list. Which Python data structure should I utilize along with the reasons for doing so?”

**AI Response and Reasoning:**  
You should use a **list**.  
- **Reasoning:** Lists in Python maintain the order of elements. By iterating through the original list and selecting only the even numbers, you can create a new list that preserves the sequence exactly. A list comprehension makes this operation concise and efficient.
