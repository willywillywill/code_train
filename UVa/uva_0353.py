def isPalindrome(s):
    return s[::-1] == s

while 1:
    try:
        ans = set()
        word = input()
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                if isPalindrome(word[i:j]):
                    ans.add(word[i:j])
        print("The string '%s' contains %d palindromes."%(word,len(ans)))
    except:
        break





"""
The string 'boy' contains 3 palindromes.

AAA8VUXAAXUV8AAB
AMTUXXV8VXXUTMA
NOTAPALINDROME
"""