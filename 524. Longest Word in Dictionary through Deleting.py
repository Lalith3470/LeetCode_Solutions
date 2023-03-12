class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        mx=0
        lst=[]
        for i in dictionary:
            if i==s:
                lst.append([i,len(i)])
                mx=max(len(i),mx)
            else:
                st=""
                s1,s2=0,0
                while s1<len(s) and s2<len(i):
                    if s[s1]==i[s2]:
                        st+=i[s2]
                        s2+=1
                        s1+=1
                    else:
                        s1+=1
                if len(st)==len(i):
                    lst.append([st,len(i)])
                    mx=max(len(i),mx)
        lst.sort(key=itemgetter(0),reverse=True)
        val=[]
        for i in lst:
            if i[1]==mx:
                val.append(i[0])
        val.sort()
        if lst:return val[0]
        return ""
