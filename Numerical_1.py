import sympy as sp
from sympy import symbols, simplify,sympify
from sympy.core.sympify import SympifyError



#A function to simplify an arithmetic expression
def simplify_eqn(expr):
	try:
		# Define symbols.
		x, y = symbols('x y')
		# Example: Define the expression you want to simplify
		
		
		# Simplify the expression
		simplified_expr = simplify(expr)
		# Output result
		print("Original Expression:", expr)
		print(f"Simplified Expression:{ simplified_expr}\n")
		return simplified_expr
	
	except (SympifyError, ValueError,Exception):
		print("check your equation\n")
		return None
	

		
#function for the derivative
def differentiate(function):
    try:
	 # Define the symbols also knom as  variable
	       x = sp.symbols('x')
	       # Input the function to differentiate
	       
	       # Convert the string to an expression
	       f = sp.sympify(function)
	       # Differentiate the function
	       derivative = sp.diff(f, x)
	       # Display the result of the derivative
	       print(f"The derivative of {f} with respect to x is: {derivative}\n")
	       return derivative
    except (sp.SympifyError, Exception):
        print("Invalid function. Please check your syntax.\n")
        return None
        
        
        
def Raphson(function):
	       print("Enter initial root: ")
	       root=input()
	       
	       expr_diff= differentiate(function)
	       result=simplify_eqn(x-function/expr_diff)
	       print(result)
	       
	       
#Function for operations to carry out
def menu(option):
	if option==1:
		print("###")
	elif option==2:
			simplify_eqn(function)
	elif option==3:
		differentiate(function)
	elif option==4:
		Raphson(function)
		
				




# a loop that keeps running in ordee to ask for the user's request'
while True:
			function = input("To quit the program, type exit\nEnter the function in terms of x : ")
			if function.lower()=="exit":
			     	print("goodbye")
			     	break
			#Menu
			print("Please, select an option")
			print("=====================")
			print("1. Instructions and guidelines\n2. Perform Algebraic Simplification\n3. Perform Differentiation\n4. Perform NRM")
			menu(int(input("SELECT: ")))
			









	       
