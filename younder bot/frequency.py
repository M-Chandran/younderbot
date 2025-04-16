from collections import Counter
def frequent(lst):
    return Counter(lst).most_common(1)[0] if lst else (None, 0)
list = [1, 2, 2, 3, 3, 3, 4]
element, frequency = frequent(list)
print(f"Most frequent element: {element} with frequency: {frequency}")
