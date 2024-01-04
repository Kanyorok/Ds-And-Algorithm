class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)

        return list(dic.values())


if __name__ == '__main__':
    soln = Solution()
    print (soln.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

"""
step 1: loop through the string.
step 2: check the words that match.
step 3: put them into groups.
step 4: append and return the final combined list.
"""
