import sys
import os


def palindrome(s):  
    s = s.lower()  
    return s == s[::-1]


def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
