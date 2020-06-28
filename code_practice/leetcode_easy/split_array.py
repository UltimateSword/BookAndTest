"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Constraints:

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4


链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum

"""


class Solution(object):
    def canThreePartsEqualSum_slow(self, A: list) -> bool:
        for i in range(1, len(A)-1):
            one = sum(A[:i])
            for j in range(i+1, len(A)):
                two = sum(A[i:j])
                three = sum(A[j:])
                if one == two == three:
                    return True
        return False

    def canThreePartsEqualSum(self, A: list) -> bool:
        all_a = sum(A)
        if all_a % 3:
            return False
        target = all_a / 3
        i = 0
        j = 0
        one = 0
        while i < len(A) - 2:
            one += A[i]
            if one == target:
                j = i+1
                break
            else:
                i += 1
        if j == 0:
            return False
        two = 0
        while j < len(A) - 1:
            two += A[j]
            if two == target:
                return True
            else:
                j += 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canThreePartsEqualSum([1,1,-1]))
