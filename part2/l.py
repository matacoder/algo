def is_correct_bracket_seq(string):
    equal_open = {
        '{': '}',
        '[': ']',
        '(': ')',
    }

    if string == '':
        return True

    if len(string) % 2 != 0:
        return False

    stack_to_close = []

    for item in string:
        if item in equal_open:
            stack_to_close.append(equal_open[item])
        else:
            try:
                if item == stack_to_close[-1]:
                    del stack_to_close[-1]
                else:
                    return False
            except Exception:
                return False
    return True


print(
    is_correct_bracket_seq(input())
)