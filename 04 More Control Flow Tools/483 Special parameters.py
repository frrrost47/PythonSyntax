# без ограничений
def standard_arg(arg):
    print(arg)


# вызывается только так  pos_only_arg(33). Хороший вариант для безопасности
def pos_only_arg(arg, /):
    print(arg)

# вызывается только так kwd_only_arg(arg=3)
def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


def typeSafeFunc(text: str) -> str:
    return text

print(typeSafeFunc('123'))