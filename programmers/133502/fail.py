class Chef:
    def __init__(self):
        self.recipe = [1, 2, 3, 1]
        self.idx = 0
        self.cnt = 0

    def requestIngredient(self, ingredient_stack):
        if ingredient_stack[-1] == self.recipe[self.idx]:
            ingredient_stack.pop()
            self.idx += 1
            if self.idx == len(self.recipe):
                self.idx = 0
                self.cnt += 1

            return True
        else:
            return False


def solution(ingredient):

    stack = []
    chef = Chef()

    for i in ingredient:
        stack.append(i)
        while stack and chef.requestIngredient(stack):
            pass

    return chef.cnt


def main():
    ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
    ans = solution(ingredient)
    print(ans)
    assert ans == 2

    ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
    ans = solution(ingredient)
    print(ans)
    assert ans == 0


main()
