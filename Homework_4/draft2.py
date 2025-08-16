if h >= k:
    while i > k:
        nlst += lst[k:]
        nlst += lst [:k]
        del nlst[-1]
        lst = nlst
        nlst = []
        i = int(len(lst))
    while i2 > 1:
        nlst += lst[k%i:]
        nlst += lst[:k%i]
        del nlst[-1]
        lst = nlst
        nlst = []
        i = len(range(len(lst)))
        i2 = len(range(len(lst)))
else:
    while i2 > 1:
        nlst += lst[k % i:]
        nlst += lst[:k % i]
        del nlst[-1]
        lst = nlst
        print(lst)
        nlst = []
        i = len(range(len(lst)))
        i2 = len(range(len(lst)))