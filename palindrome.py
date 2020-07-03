def isPalindrome(x) -> bool:
       if x < 0:
           return "abc"
       else:
            a = list(str(x))
            a.reverse()
            b = "".join(a)
            e = int(b)
            if x == e:
               return "xyz"
            else:
               return e
a = isPalindrome(int(input("enter:")))
print(a)

    