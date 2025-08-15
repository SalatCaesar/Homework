  # Сначала создадим список с индексами длинной в количество человек
  # Потом надо придумать цикл, который перестроит список начиная с элемента n+1
  # В конце цикла удаляем последний элемент, который окажется n
  # while до того, как элемент не останется один
h = 80
k = 2
lst = list(range(1,h+1))
nlst = []
i = len(range(len(lst)))
i2 = len(range(len(lst)))
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
print(str(lst))