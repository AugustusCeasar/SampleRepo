def main():
    test = range(200)
    evens_test = [x for x in test if x%2==0]
    for i in evens_test:
        print(i)


if __name__ == '__main__':
    main()
