def add (a, b):
    return a + b

def minus(a, b):
    """Subtract b from a."""
    return a - b

def root(x: float) -> float:
    """주어진 수의 제곱근을 반환합니다."""
    if x < 0:
        raise ValueError("음수는 제곱근을 계산할 수 없습니다.")
    return x ** 0.5

def multiply (a, b):
    return a * b
  
def square(a, b):
    """a square b"""
    return a ** b

def divide(a, b):
    return a / b

