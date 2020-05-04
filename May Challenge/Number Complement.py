class Solution:
    def findComplement(self, num: int) -> int:
        def log_a_base_b(a, b):
            return log(a) / log(b)

        if num == 0:
            return 1

        num_bits = int(log_a_base_b(num, 2)) + 1
        mask = (2 ** num_bits) - 1

        return mask ^ num