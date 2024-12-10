from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for word in strs[1:]:
            wss = list()
            for i in range( min(len(res), len(word)) ):
                if res[i] == word[i]:
                    wss.append(res[i])
                else:
                    break
            res = ''.join(wss)
            if res == '': # empty result
                break # exit the outer cycle
        return res

if __name__ == '__main__':
    test_data = ['flow', 'flower', 'flight']
    inst = Solution()
    result = inst.longestCommonPrefix(test_data)
    print(result)
    assert(result == 'fl')
