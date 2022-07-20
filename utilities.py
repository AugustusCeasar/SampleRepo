def print_all_the_things(list, debug=false, **kwargs):
    for x in list if ("reverse" not in kwargs or not kwargs["reverse]) else reverse(list):
        print(x)
    if debug and kwargs:
        for k,v in **kwargs.items():
            print(f"{k}:{v}")
