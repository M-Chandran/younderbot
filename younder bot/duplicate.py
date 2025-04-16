def duplicate(s):
    seen = set()
    duplicates = []
    for char in s:
        if char in seen and char not in duplicates:
            duplicates.append(char)
        else:
            seen.add(char)
    return ''.join(duplicates)
s = "Hello,World!"
print(duplicate(s))
