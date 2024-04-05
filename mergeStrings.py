
def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_arr = []
        for i in word1:
                
                for j in word2:
                        new_arr.append(i)
                        new_arr.append(j)

        print(new_arr)

mergeAlternately('abc', 'pqr')