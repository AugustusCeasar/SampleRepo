def main():
    test = range(100)
    for i in test:
        print(test)
    
    test2 = range(200)
    evens_test = [x for x in test2 if x%2==0]
    for i in evens_test:
        print(i / 2)


if __name__ == '__main__':
    main()
