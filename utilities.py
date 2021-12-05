def print_all_the_things(list, **kwargs):
    for x in list:
        print(x)
    if kwargs:
        for k,v in kwargs.items():
            print(f"{k}:{v}")

def test_this_file():
    test_l = [1,2,3,4,5,6,7]
    print_all_the_things([1,2,3,4,5,6,7])
    print_all_the_things([1,2,3,4,5,6,7], randomarg="testin")

if __name__ == '__main__':
    test_this_file()
