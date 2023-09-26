class Iterable:
    MAX_VALUE = 20
    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()

n = int(input("record per iter: \n"))
c = CustomIterator()
list = [i for i in c]
print("\n")
print(Iterable.MAX_VALUE/n)
print(Iterable.MAX_VALUE%n)
print(Iterable.MAX_VALUE//n)


def iteratinon(list1):
    start=0
    end=n
    for i in range(Iterable.MAX_VALUE//n):
        print(list1[start:end])
        start+=n
        end+=n
    print(list1[start:end+Iterable.MAX_VALUE%n])


iteratinon(list)