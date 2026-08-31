class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError()
        self.capacity = capacity
        self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.capacity:
            raise ValueError()
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) >= self.capacity:
            self.resize()
        self.array.append(n)

    def popback(self) -> int:
        if self.getSize() < 1:
            raise ValueError()
        return self.array.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity