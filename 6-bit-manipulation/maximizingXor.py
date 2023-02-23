""" Maximizing XOR
https://www.hackerrank.com/challenges/maximizing-xor/problem
 """

# TODO: Approach 1: Brute Force - Using 2 loops         [O(len(l-r)*len(l-r)) & O(1)]s
# TODO: Approach 2: Using << and format(number, 'b')    [O(1) & O(1)]


class Solution:
    def maximizingXor1(self, l, r) -> int:
        maxValue = 0
        if l > r:
            l ^= r
            r ^= l
            l ^= r

        for i in range(l, r+1):
            for j in range(l, r+1):
                if (i ^ j > maxValue):
                    maxValue = i ^ j

        return maxValue

    def maximizingXor2(self, l, r) -> int:
        xored = l ^ r

        bitString = format(xored, 'b')
        shiftLeft = 1 << len(bitString)

        return (1 << (len(format(xored, 'b')))) - 1


if __name__ == "__main__":
    # [num1, num2] = 5, 6     # ? Output = 3
    [num1, num2] = 23, 28   # ? Output = 15
    # [num1, num2] = 8, 31   # ? Output = 31
    # [num1, num2] = 85, 108  # ? Output = 63
    # [num1, num2] = 11, 130  # ? Output = 255

    s = Solution()
    result1 = s.maximizingXor1(num1, num2)
    result2 = s.maximizingXor2(num1, num2)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result2))


""" Explanation:

*L ^ R - gets you the maximum XOR value between l and r.

*format( a_number, 'b') - returns the binary string of a_number

*wrapping that in a len() gets you the length of that binary string which is what you want the length of all 1s to be.

*<< - is a bitshift operator, for example x << y shifts the binary of x to the left y times. ie. 2('10') << 1 = 4('100'). 4('100') << 1 = 8('1000')

Put it all together and you have 1 left-bitshifted by the length of the number that l^r gives minus 1.
you subtract by 1 for two reasons: 
!A: when you shift 1 by that number, you have one extra bit in your bitstring for example, 
!   if you 1<<3 you get 8, which is 1000, but the len() is 3, so you want 3 bits of all 1s which brings us to B) 
!B: when you subtract 8(1000) by 1 you get 7(111) which is the len() of all 1s
 """
