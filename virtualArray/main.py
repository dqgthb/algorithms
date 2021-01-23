class MultiplyByTwo:
    def __getitem__(self, n):
        return n*2

arr = MultiplyByTwo()
print(arr[10000000000])