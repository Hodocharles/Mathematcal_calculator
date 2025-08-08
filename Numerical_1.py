import guidelines as gd
import sympy as sp
import limit
from sympy import symbols, simplify,sympify
from sympy.core.sympify import SympifyError
from rich import print
from rich.align import Align


x, y = symbols('x y')  # Define globally so all functions can use

#A function to simplify an arithmetic expression
def simplify_eqn(expr):
	try:
		
		# Example: Define the expression you want to simplify
		
		
		# Simplify the expression
		simplified_expr = simplify(expr)
		# Output result
		print("\nOriginal Expression:", expr)
		print(f"✅Simplified Expression:{ simplified_expr}\n")
		return simplified_expr
	
	except (SympifyError, ValueError,Exception):
		print("check your equation\n")
		return None
	

		
#function for the derivative
def differentiate(function):
    try:
	 # Define the symbols also knom as  variable
	       x = sp.symbols('x')
	       
	       
	       # Convert the string to an expression
	       f = sp.sympify(function)
	       # Differentiate the function
	       derivative = sp.diff(f, x)
	       # Display the result of the derivative
	       print(f"✅The derivative of {f} with respect to x is: {derivative}\n")
	       return derivative
    except (sp.SympifyError, Exception):
        print("Invalid function. Please check your syntax.\n")
        return None
        
        
# Newton-Raphson method (1 iteration)
def Raphson(function_eqn):
    try:
        n=1 #this represents the number of iterations
        
        root = float(input("Enter initial root: "))

        function = sympify(function_eqn)
       
       #func_prime refers to the first derivative
        func_prime = differentiate(function_eqn)       
        if func_prime is None:
            return
        for i in range(1,4):
            
            f_val = function.subs(x, root)
            f_prime_val = func_prime.subs(x, root)
            if f_prime_val == 0:
                print("Derivative is zero. Equation ended .\n")
                return
                # Newton-Raphson formula: x(n+1) = xn - f(xn)/f'(xn)
            new_root_expr = x - function / func_prime
            simplified = simplify_eqn(new_root_expr)
            new_root = root - f_val / f_prime_val
            print(f"➡️==> f({root}) = {f_val}")
            print(f"➡️==> f'({root}) = {f_prime_val}")
            print("="*60)
            print(f"✅NEW ROOT after {n} iteration: {new_root}\n")
            print("="*60)
            root=new_root
            n+=1 #increament the iteration by 1

    except Exception as e:
        print("NRM Error:", str(e))
	       
	        
#Function for operations to carry out
def menu(option):
    if option == 1:
        gd.instructions()
    elif option == 2:
        simplify_eqn(function)
    elif option == 3:
        differentiate(function)
    elif option == 4:
        Raphson(function)
    elif option==5:
        limit.func_limit(function)
    else:
        print("[bold red]Invalid option, enter a valid option 1-5[/bold red]")
		
				


# a loop that keeps running in ordee to ask for the user's request'
calc_title=Align.center("[bold magenta]=====WELCOME TO C-CALC====[/bold magenta]\n")
print(calc_title)
advise="[bold red]Please, read the imstructions before using this calculator in order to understand how to use it efficiently. To use the instruction manual, type any number and press enter, select option 1\n[/bold red]"
print(advise)
while True:
			print("To quit the program, type [bold red]exit[/bold red]\nEnter function in terms of x (2*x**3) : ", end=" ")
			function = input()
			if function.strip().lower()=="exit":
			     	print("[bold red]Thanks for Using our Calculator......[/bold red]")
			     	break
			#Menu
			print("Please, select an option (1-4)")
			print("======================"*2)
			print("1. Instructions and guidelines\n2. Perform Algebraic Simplification\n3. Perform Differentiation\n4. Perform NRM\n5. Calculate limit")
			print("======================"*2)
			choice = input("[SELECT]: ").strip().lower()
			if choice == "exit":
			     print("[bold red]Thanks for using our Calculator![/bold red]")
			     break
			     
			     # Validation — check if it's a number
			     
			if not choice.isdigit():
			     print("[bold red]Invalid input! Please enter a number between 1 and 5, or 'exit' to quit.[/bold red]\n")
			     continue
			option = int(choice)
			if not (1 <= option <= 5):
			             print("[bold red]Invalid option! Please enter 1, 2, 3, 4 or 5.[/bold red]\n")
			             continue
			menu(option)
		 	



# ---------------------------------------------------------
#  MyProgram™ v1.0
#  Author: Hodo Charles
#  © 2025 Hodo Charles. All rights reserved.
#  This software is protected under trademark law.
#  Unauthorized copying or use is prohibited.
# ---------------------------------------------------------
