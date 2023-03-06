class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        path=path.split("/")
        path=[i for i in path if i and i!="/" and i!="."]
        for i in path:
            if i==".." and stack:
                stack.pop()
            elif i!="..":
                stack.append(i)
        return "/"+"/".join(stack)
