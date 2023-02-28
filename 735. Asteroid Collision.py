class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in asteroids:
            while stack and stack[-1]>0 and stack[-1]<-i:
                stack.pop()
            if stack and stack[-1]>0 and i<0:
                if abs(stack[-1])==abs(i):stack.pop()
            else:
                stack.append(i)
        return stack
