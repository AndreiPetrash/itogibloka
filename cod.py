array = ["hello", "2", "world", ":-)"]
def filter_less_than_three(array: list):
    res = []
    for element in array:
        if len(element) <= 3:
            res.append(element)
    return res

print(filter_less_than_three(array))