def fizzbuzz(n):
    for i in range(1,n+1):
        s = ''
        if i%3 and i%5:
            print(i)
        if not i%3:
            s += 'fizz'
        if not i%5:
            s += 'buzz'
        if s:
            print(s)

fizzbuzz(50)