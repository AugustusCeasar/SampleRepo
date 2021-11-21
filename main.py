def main():
    test = [5, 4, 3, 2, 1, 0]
    evens_test = [x for x in test if x%2==0]
    for i in evens_test:
        print(i)


if __name__ == '__main__':
    main()
