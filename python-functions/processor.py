def process_numbers(rawList):
    filtered = []

    if isinstance(rawList, list) == False:
        return filtered

    for data in rawList:
        if str(data).isnumeric():
            filtered.append(int(data))

    filtered.sort()
    return filtered


def process_names(rawList):
    filtered = []

    if isinstance(rawList, list) == False:
        return filtered

    for data in rawList:
        if str(data).isnumeric() == False:
            filtered.append(data)

    filtered.sort()
    return filtered
