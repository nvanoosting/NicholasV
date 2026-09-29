# --- Practice Questions ---

list = [40, 80, 10, 30, 50, 20]

def maximum(a):
    return max(a)

def minimum(a):
    return min(a)

print("max:", maximum(list), "min:", minimum(list))

# --- Prime Number Checker ---

def is_prime(num):
    if num <= 0 or type(num) != int:
        return "try again. choose a new number"
    else:  
        if num == 1:
            return "neither"
        elif num == 2:
            return "is a prime"
        else:
            if num % 2 == 0:
                return "composite number, divisible by 2"
            else:
                for i in range(2, num):
                    if num % i == 0:
                        return f"composite number{i}"
                    else:
                        return "prime numnber"

print(is_prime(9))