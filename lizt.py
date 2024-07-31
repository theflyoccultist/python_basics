numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

friends = ["samantha", "sylvie", "adam", "rain", "anna", "sultan"]
starts_s = [friend for friend in friends if friend.startswith('s')]

print(starts_s)