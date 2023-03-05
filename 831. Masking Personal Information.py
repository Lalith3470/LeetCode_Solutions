class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if "@" and "." in s:
            for i in range(len(s)):
                if s[i]=="@":
                    return (s[0]+"*"*5+s[i-1:]).lower()
        else:
            num=""
            for i in s:
                if i.isalnum():
                    num+=i
            ln= len(num)
            if ln == 10:
                return ('***-***-'+num[-4:])
            elif ln == 11:
                return ("+*-***-***-"+num[-4:])
            elif ln==12:
                return ("+**-***-***-"+num[-4:])
            elif ln==13:
                return ("+***-***-***-"+num[-4:])
