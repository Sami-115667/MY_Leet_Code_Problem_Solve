class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        li = []
        for i, y in enumerate(words):
            if x in y:
                li.append(i)
        return li