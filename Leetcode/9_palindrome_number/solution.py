def isPalindrome(n):
  temp = n
  reversedNumber = 0
  while n > 0:
    lastDigit = n % 10
    reversedNumber = reversedNumber * 10 + lastDigit
    n = n // 10

  return temp == reversedNumber

if __name__ == "__main__":
  print(isPalindrome(121))
  print(isPalindrome(1211))
  print(isPalindrome(-1211))
  print(isPalindrome(-121))