import copy

class Matrix:
    def printM(self, A: list):
        for i in A:
            for j in i:
                print(f'{j}\t', end='')

            print()

    def det(self, A: list, p: bool = True) -> int:
        if not self.isSquare(A):
            return None

        result = 0

        if len(A) == 2:
            result = A[0][0] * A[1][1] - A[1][0] * A[0][1]

            return result

        if p:
            print('\ndet(A) = ', end='')

        for i in range(len(A)):

            newA = copy.deepcopy(A)
            newA.pop(i)

            for j in newA:
                j.pop(0)

            # printM(newA)
            # print('\n')

            x = ((-1)**(i+2))*(A[i][0] * self.det(newA, False))

            if p:
                print(x, end=' + ' if i < len(A) - 1 else '')

            result += x

        return result

    def isSquare(self, A: list) -> bool:
        if len(A) == len(A[0]):
            return True

        return False

    def product(self, A: list, B: list) -> list:
        C = []
        B = self.transpose(B)

        for i in range(len(A)):
            row = []

            for j in range(len(B)):
                temp = self.productVector(A[i], B[j])
                row.append(temp)

            C.append(row)

        return C

    def productVector(self, A: list, B: list) -> int:
        result = 0

        for i in range(len(A)):
            result += A[i] * B[i]

        return result

    def transpose(self, A: list) -> list:
        B = []
        row = len(A)
        column = len(A[0])

        for i in range(column):
            temp = []
            for j in range(row):
                temp.append(A[j][i])

            B.append(temp)

        return B

    def isMatrix(self, A: list) -> bool:
        if A == []:
            return False

        if type(A[0]) != list:
            return False

        row = len(A)
        column = len(A[0])

        for i in range(row):
            if type(A[i]) != list:
                return False

            if len(A[i]) != column:
                return False

        return True

    def isVector(self, A: list) -> bool:
        if A == []:
            return False

        row = len(A)

        for i in range(row):
            if type(A[i]) == list:
                return False

        return True

    def sizeof(self, A: list) -> list[int, int]:
        if self.isMatrix(A):
            return [len(A), len(A[0])]

        elif self.isVector(A):
            return [len(A), 0]

        return None

    def minValue(self, A: list) -> int:
        min = None

        if self.isVector(A):
            min = A[0]

            for i in range(len(A)):
                min = A[i] if min > A[i] else min

        elif self.isMatrix(A):
            min = A[0][0]

            for i in range(len(A)):
                for j in range(len(A[i])):
                    min = A[i][j] if min > A[i][j] else min

        return min

    def maxValue(self, A: list) -> int:
        max = None

        if self.isVector(A):
            max = A[0]

            for i in range(len(A)):
                max = A[i] if max < A[i] else max

        elif self.isMatrix(A):
            max = A[0][0]

            for i in range(len(A)):
                for j in range(len(A[i])):
                    max = A[i][j] if max < A[i][j] else max

        return max

    def isDiag(self, A: list) -> bool:
        if not self.isMatrix(A):
            return None

        if not self.isSquare(A):
            return False

        for i in range(len(A)):
            for j in range(len(A[i])):
                if i != j and A[i][j] != 0:
                    return False

        return True

    def isNull(self, A: list) -> bool:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] != 0:
                    return False

        return True

    def isUnit(self, A: list) -> bool:
        if not self.isDiag(A):
            return False

        for i in range(len(A)):
            for j in range(len(A[i])):
                if i == j and A[i][j] != 1:
                    return False

        return True
