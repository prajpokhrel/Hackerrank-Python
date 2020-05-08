if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = list()
    for value in integer_list:
        t.append(value)
    print(hash(tuple(t)))
    
