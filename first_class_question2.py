def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Lilia", "age": 28},
    {"name": "Odin the Great", "age": 877},
    {"name": "Nyarlathotep", "age": 8888811},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Nyarlathotep", get_friend_name))