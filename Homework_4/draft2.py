  # Сначала создадим список с индексами длинной в количество человек
  # Потом надо придумать цикл, который перестроит список начиная с элемента n+1
  # В конце цикла удаляем последний элемент, который окажется n
  # while до того, как элемент не останется один
h = 14
k = 2
lst = list(range(1,h+1))
nlst = []
i = len(lst)
i2 = None
if h >= k:
    while i >= k:
        nlst += lst[k:]
        nlst += lst [0:k]
        del nlst[-1]
        lst = nlst
        nlst = []
        i = int(len(lst))
        print(lst)
    while i2 != 1:
        nlst += lst[k%i:]
        nlst += lst[0:k%i]
        del nlst[-1]
        lst = nlst
        nlst = []
        i = len(range(len(lst)))
        i2 = len(range(len(lst)))
        print(lst)
else:
    while i2 != 1:
        nlst += lst[k % i:]
        nlst += lst[0:k % i]
        del nlst[-1]
        lst = nlst
        nlst = []
        i = len(range(len(lst)))
        i2 = len(range(len(lst)))
        print(lst)