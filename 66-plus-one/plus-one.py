class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = "".join([str(num) for num in digits])
        result = 1 + int(str_num)

        plus_one = []
        while result:
            plus_one.append(result % 10)
            result = result // 10

        plus_one.reverse()
        return plus_one
        