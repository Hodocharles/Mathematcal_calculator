from sympy import symbols, simplify, factor, sympify, limit, oo


x = symbols('x')

def func_limit(expr_str):
    try:
        expr = sympify(expr_str)       # Turn text into math
        expr = simplify(expr)          # Simplify it
        print("➡️==> Simplified expression:", expr)

        factored = factor(expr)        # Factorize it
        print("➡️==> Factored Expression:", factored)

        tend = sympify(input("x tends to: "))#so that i can use infinity 
        print("="*60)
        print(f"✅LIMIT as x tends to {tend} is:", limit(expr, x, tend))
        print("="*60)
    except Exception as e:
            print("limit Error check equation: ", str(e))

# Run
if __name__=="__main__":
    print(" runs here only")
    
    func_limit(input("Enter expression in terms of x: "))