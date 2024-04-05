def longestCommonPrefix( strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        arr = []
        for i in strs:
                arr.append(i[0:2])
        print(arr)
        for x in range(len(arr)):
                for y in range(len(arr)+1):
                        if x == y:
                                print(arr[x])
                        
                



longestCommonPrefix(["ower","flow","flight"])
        