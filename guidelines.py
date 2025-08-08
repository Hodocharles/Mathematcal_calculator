from rich import print
from rich.align import Align


def instructions():
    title=Align.center("[bold magenta]..........C-calculator..........\n Instructions and guidelines\n[/bold magenta]")
    print(title)
    
    print("="*22)
    func_msg="[bold magenta]Functions Expression: [/bold magenta]"
    print(func_msg)
    print("="*22)
    
    func_txt= " Using functions in this calculator requires you to type them in a specific manner otherwise, the results will be inaccurate or even develope a bug. \n Examples: to type in the function [bold red] x⁴+3x³-2x+1[/bold red]  into the calculator, you need to express it as [bold blue] x**4 +3*x**3-2*x+1[/bold blue] special functions like trigonometric and eular identities should be typed as [bold blue] log(x), cos(x), sin(x), sin(3*x**2), e**3, e**(4*x), sin(x)+4*x[/bold blue]. When expressing algrbraic functions, it is advised to use a bracket e.g [bold blue] (x+3)-(x+4)/(2*x) is not equal to ((x+3)-(x+4))/(2*x)\n[/bold blue]"
    print(func_txt)
    print("="*22)
    Err_msg="[bold magenta]Error Messages🚨: [/bold magenta]"
    print(Err_msg)
    print("="*22)
    Err_txt="[bold red]check your equation[/bold red]: Check the operators in the function (*,+,-,/)\n[bold red]Invalid function. Please check your syntax:[/bold red] Check the operators in the function (*,+,-, /) and how the function is expressed.\n[bold red]Derivative is zero. Equation ended:[/bold red] This is usually associated with the Newton Raphson Method (NRM). This signifies that the derivative of your function is 0 and as such the NRM can not be applied\n[bold red]NRM Error:[/bold red] The Newton Raphson Method calculation failed.\n"
    print (Err_txt)
    
    
    print("="*22)
    Menu_msg="[bold magenta]Menu Selection: [/bold magenta]"
    print(Menu_msg)
    print("="*22)
    Menu_txt="The select an option from the menu, use the numbers assigned to each option (e.g 1, 2,3)\n"
    print(Menu_txt)
    print("=="*60)
    msg2=" [bold red]🚨 IMPORTANT/ACTION NEEDED!: [/bold red]: DO NOT ALTER ANY PART OF THIS PROGRAM WITHOUT APPROPRIATE PERMISSION. IN ORDER TO MAXIMIZE THE PERFORMANCE OF THIS PROGRAM, PLEASE INSTALL THE REQUIRED LIBRARIES FOLLOWING THE STEPS BELOW:\n In your terminal window, type the following to install the required library;\n[bold magenta]sympy[/bold magenta]: pip install sympy\n[bold magenta]rich[/bold magenta]: pip install rich\n"
    print(msg2)
    print("© Hodocharle 2025")




    
    
if __name__=="__main__":
    print(" runs here only")
    instructions()
    
    
# ---------------------------------------------------------
#  MyProgram™ v1.0
#  Author: Hodo Charles
#  © 2025 Hodo Charles. All rights reserved.
#  This software is protected under trademark law.
#  Unauthorized copying or use is prohibited.
# ---------------------------------------------------------

