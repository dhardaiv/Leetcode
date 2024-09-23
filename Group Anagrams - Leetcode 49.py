class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for word in strs: 
            word_sort = ''.join(sorted(word))
            if word_sort in hash: 
                hash[word_sort].append(word)
            else: 
                hash[word_sort] = [word]
        return hash.values()
