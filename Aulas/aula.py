def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

result = factorial(4)
print(f"4! = {result}")

def eh_palindromo(txt):
    txt = txt.lower().replace(" ", "")
    if len(txt) <= 1:
        return True
    if txt[0] != txt[-1]:
        return False
    return eh_palindromo(txt[1:-1])

print(eh_palindromo("arara"))   # True
print(eh_palindromo("python"))  # False

