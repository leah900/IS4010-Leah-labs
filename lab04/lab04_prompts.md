
# Lab 04: AI-assisted Data Structure Selection

---

### 1. Finding Common Items
**Prompt:**
> I have two very large lists involving product IDs from two suppliers. I need to find product IDs that both lists show. The order doesn’t matter, and performance matters. For what should I use a particular Python data structure?

**Recommended Data Structure:**
- `set`

**Why?**
- Sets use hash tables, so checking membership and finding intersections is super fast (average O(1) per check).
- You can convert both lists to sets and use `set1 & set2` to get all common product IDs efficiently.

---

### 2. User Profile Lookup
**Prompt:**
> My application loads a database list of user profiles. Each user has a unique username, an age, and an email. I have a frequent need to look up users by their username. It is critical that this performs well. Why should I use which Python data structure in particular?

**Recommended Data Structure:**
- `dict` (dictionary)

**Why?**
- Dictionaries are also hash tables, so you get O(1) average-time lookups by key.
- If you use the username as the key, you can instantly get any user’s profile without searching through a list.

---

### 3. Listing Even Numbers in Order
**Prompt:**
> A list of integers showing sensor readings is given to me. I need to make up a report that only contains each of the even numbers; these numbers must be put in the exact same order as they appear in the list. Which Python data structure should I utilize along with the reasons for doing so?

**Recommended Data Structure:**
- `list`

**Why?**
- Lists keep the order of elements, so you can filter out the even numbers and keep their sequence.
- A list comprehension like `[n for n in numbers if n % 2 == 0]` makes this easy and efficient.
