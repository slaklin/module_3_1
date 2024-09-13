calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    info_about_line = len(string), string.upper(), string.lower()
    return info_about_line


def is_contains(string, list_to_search):
    count_calls()
    new_string = string.lower()
    new_list_to_search = []
    for i in list_to_search:
        new_list_to_search.append(i.lower())
    if new_string in new_list_to_search:
        return True
    else:
        return False


print(string_info("Urban"))
print(string_info("Megatron"))
print(is_contains('uRban', ['Daf', 'home', 'Urban']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

