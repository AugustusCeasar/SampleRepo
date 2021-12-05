def print_all_the_things(list, **kwargs):
    for x in list:
        print(x)
    if kwargs:
        for k,v in **kwargs.items():
            print(f"{k}:{v}")