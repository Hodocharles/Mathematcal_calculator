"""
tk_calc_with_menus.py
A Tkinter calculator GUI (SymPy-based) with keypad and fraction button
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog, simpledialog
import sympy as sp

# ---------- SymPy symbols ----------
x, y = sp.symbols('x y')

# ---------- COMPUTATION FUNCTIONS ----------
def compute_simplify(expr_str: str) -> str:
    expr = sp.sympify(expr_str)
    return str(sp.simplify(expr))

def compute_differentiate(expr_str: str) -> str:
    expr = sp.sympify(expr_str)
    return str(sp.diff(expr, x))

def compute_integrate(expr_str: str) -> str:
    expr = sp.sympify(expr_str)
    return str(sp.integrate(expr, x))

def compute_factor(expr_str: str) -> str:
    expr = sp.sympify(expr_str)
    return str(sp.factor(expr))

def compute_newton_raphson(expr_str: str, init_guess, iterations=6) -> str:
    func = sp.sympify(expr_str)
    fprime = sp.diff(func, x)
    root = sp.N(init_guess)
    for i in range(iterations):
        fval = sp.N(func.subs(x, root))
        fprime_val = sp.N(fprime.subs(x, root))
        if fprime_val == 0:
            raise ZeroDivisionError("Derivative became zero during Newton-Raphson.")
        root = root - fval / fprime_val
    return str(sp.N(root, 12))

def compute_solve(expr_str: str) -> str:
    if '=' in expr_str:
        left, right = expr_str.split('=', 1)
        eq = sp.Eq(sp.sympify(left), sp.sympify(right))
        sols = sp.solve(eq, x)
    else:
        expr = sp.sympify(expr_str)
        sols = sp.solve(sp.Eq(expr, 0), x)
    return str(sols)

def compute_limit(expr_str: str, point_str: str) -> str:
    expr = sp.sympify(expr_str)
    pt = sp.sympify(point_str)
    return str(sp.limit(expr, x, pt))

# ---------- GUI ----------
class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("C-Calculator (with Menus)")
        master.geometry("800x720")
        self.theme = "dark"
        self._make_styles()
        self._build_widgets()
        self._build_menus()
        self._bind_shortcuts()

    def _make_styles(self):
        self.colors = {
            "dark": {
                "bg": "#1e1e2e",
                "fg": "white",
                "entry_bg": "#2b2b3a",
                "output_bg": "#282a36",
                "button_bg": "#3a3f58",
                "insert_bg": "#ff6600"  # orange cursor for better visibility
            },
            "light": {
                "bg": "#f6f7fb",
                "fg": "#111111",
                "entry_bg": "white",
                "output_bg": "white",
                "button_bg": "#e0e4f2",
                "insert_bg": "#ff6600"
            },
            "mature": {  # More mature color theme
                "bg": "#4b003f",
                "fg": "#d98fd6",
                "entry_bg": "#6e1e5b",
                "output_bg": "#3f004d",
                "button_bg": "#800080",
                "insert_bg": "#ff66ff"
            }
        }

    def _apply_theme(self):
        c = self.colors[self.theme]
        self.master.config(bg=c["bg"])
        self.title_label.config(bg=c["bg"], fg=c["fg"])
        self.input_frame.config(bg=c["bg"])
        self.output_area.config(bg=c["output_bg"], fg=c["fg"], insertbackground=c["insert_bg"])
        self.entry_expr.config(bg=c["entry_bg"], fg=c["fg"], insertbackground=c["insert_bg"])
        self.entry_init.config(bg=c["entry_bg"], fg=c["fg"], insertbackground=c["insert_bg"])
        for b in self.action_buttons:
            b.config(bg=c["button_bg"], fg=c["fg"])
        for btn in self.keypad_buttons:
            btn.config(bg=c["button_bg"], fg=c["fg"])

    def _build_widgets(self):
        c = self.colors[self.theme]
        self.title_label = tk.Label(self.master, text="🧮 C-Calculator", font=("Helvetica", 20, "bold"),
                                    bg=c["bg"], fg=c["fg"])
        self.title_label.pack(pady=8)

        self.input_frame = tk.Frame(self.master, bg=c["bg"])
        self.input_frame.pack(padx=12, pady=6, fill="x")

        tk.Label(self.input_frame, text="Expression (use 'x'):", bg=c["bg"], fg=c["fg"], font=("Arial", 7)).grid(row=0, column=0, sticky="w")
        self.entry_expr = tk.Entry(self.input_frame, font=("Arial", 8), width=30, insertbackground=c["insert_bg"])
        self.entry_expr.grid(row=1, column=0, columnspan=5, sticky="w", pady=6)

        tk.Label(self.input_frame, text="Initial guess (Newton-Raphson):", bg=c["bg"], fg=c["fg"], font=("Arial", 7)).grid(row=2, column=0, sticky="w", pady=(8,0))
        self.entry_init = tk.Entry(self.input_frame, width=15, font=("Arial", 8), insertbackground=c["insert_bg"])
        self.entry_init.grid(row=3, column=0, sticky="w", pady=4)

        self.output_area = scrolledtext.ScrolledText(self.master, width=88, height=6, font=("Courier", 9),
                                                     bg=c["output_bg"], fg=c["fg"], insertbackground=c["insert_bg"])
        self.output_area.pack(padx=12, pady=8, fill="both", expand=False)

        func_btn_frame = tk.Frame(self.master, bg=c["bg"])
        func_btn_frame.pack(pady=8)

        btn_config = {"font": ("Arial", 5, "bold"), "width": 9, "height": 2}
        self.action_buttons = []
        b1 = tk.Button(func_btn_frame, text="Simplify", command=self.on_simplify, **btn_config)
        b2 = tk.Button(func_btn_frame, text="Differentiate", command=self.on_diff, **btn_config)
        b3 = tk.Button(func_btn_frame, text="Integrate", command=self.on_integrate, **btn_config)
        b4 = tk.Button(func_btn_frame, text="Factor", command=self.on_factor, **btn_config)
        b5 = tk.Button(func_btn_frame, text="Newton-Raphson", command=self.on_newton, **btn_config)
        b6 = tk.Button(func_btn_frame, text="Solve (eqn)", command=self.on_solve, **btn_config)
        b7 = tk.Button(func_btn_frame, text="Limit", command=self.on_limit, **btn_config)
        b8 = tk.Button(func_btn_frame, text="Clear Output", command=self.clear_output, **btn_config)

        func_buttons = [b1,b2,b3,b4,b5,b6,b7,b8]
        for i,btn in enumerate(func_buttons):
            btn.grid(row=i//4, column=i%4, padx=5, pady=5)
            self.action_buttons.append(btn)

        keypad_frame = tk.Frame(self.master, bg=c["bg"])
        keypad_frame.pack(pady=4)

        def add_to_entry(val):
            widget = self.master.focus_get()
            if widget == self.entry_init or widget == self.entry_expr:
                widget.insert(tk.INSERT, val)
            else:
                self.entry_expr.insert(tk.INSERT, val)

        def delete_one_char():
            widget = self.master.focus_get()
            if widget == self.entry_init or widget == self.entry_expr:
                current = widget.get()
                if current:
                    # Delete last character
                    widget.delete(len(current)-1, tk.END)

        def insert_fraction():
            widget = self.master.focus_get()
            if widget == self.entry_init or widget == self.entry_expr:
                pos = widget.index(tk.INSERT)
                widget.insert(pos, "(()/())")
                widget.icursor(pos + 1)

        def clear_all():
            self.entry_expr.delete(0, tk.END)
            self.entry_init.delete(0, tk.END)
            self.clear_output()

        btns = [
            ["1", "2", "3", "(", ")"],
            ["4", "5", "6", "+", "-"],
            ["7", "8", "9", "*", "/"],
            ["Fraction", "0", ".", "^", "Clear"],
            ["√", "sin(", "cos(", "tan(", "π"],
            ["sec(", "cosec(", "x", "ln(", "e"]
        ]

        self.keypad_buttons = []
        for r, row in enumerate(btns):
            for c_, val in enumerate(row):
                if val == "Clear":
                    action = delete_one_char  # Changed here to delete one char at a time
                elif val == "Fraction":
                    action = insert_fraction
                elif val == "π":
                    action = lambda v="pi": add_to_entry(v)
                elif val == "√":
                    action = lambda v="sqrt(": add_to_entry(v)
                elif val in ["sin(", "cos(", "tan(", "sec(", "cosec(", "ln("]:
                    action = lambda v=val: add_to_entry(v)
                elif val == "e":
                    action = lambda v="E": add_to_entry(v)
                elif val == "x":
                    action = lambda v="x": add_to_entry(v)
                else:
                    action = lambda v=val: add_to_entry(v)
                btn = tk.Button(keypad_frame, text=val, width=4, height=2, command=action,
                                bg=c["button_bg"], fg=c["fg"], font=("Arial", 8, "bold"))
                btn.grid(row=r, column=c_, padx=2, pady=2)
                self.keypad_buttons.append(btn)

        self._apply_theme()

        # Disable Android on-screen keyboard popup by forcing focus
        self.entry_expr.focus_force()

    def _build_menus(self):
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Expression...", accelerator="Ctrl+O", command=self.open_expression_from_file)
        file_menu.add_command(label="Save Output...", accelerator="Ctrl+S", command=self.save_output_to_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Copy Output", accelerator="Ctrl+C", command=self.copy_output)
        edit_menu.add_command(label="Paste to Expression", accelerator="Ctrl+V", command=self.paste_to_expression)
        edit_menu.add_command(label="Clear Output", accelerator="Ctrl+L", command=self.clear_output)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Simplify", command=self.on_simplify)
        tools_menu.add_command(label="Differentiate", command=self.on_diff)
        tools_menu.add_command(label="Integrate", command=self.on_integrate)
        tools_menu.add_command(label="Factor", command=self.on_factor)
        tools_menu.add_command(label="Newton-Raphson", command=self.on_newton)
        tools_menu.add_command(label="Solve (eqn)", command=self.on_solve)
        tools_menu.add_command(label="Limit", command=self.on_limit)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Toggle Theme", command=self.toggle_theme, accelerator="Ctrl+T")
        menubar.add_cascade(label="View", menu=view_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Docs / How to use", command=self.show_help)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.master.config(menu=menubar)

    def _bind_shortcuts(self):
        self.master.bind_all("<Control-s>", lambda e: self.save_output_to_file())
        self.master.bind_all("<Control-o>", lambda e: self.open_expression_from_file())
        self.master.bind_all("<Control-q>", lambda e: self.master.quit())
        self.master.bind_all("<Control-c>", lambda e: self.copy_output())
        self.master.bind_all("<Control-v>", lambda e: self.paste_to_expression())
        self.master.bind_all("<Control-l>", lambda e: self.clear_output())
        self.master.bind_all("<Control-t>", lambda e: self.toggle_theme())

    # ---------- Action methods ----------
    def _get_expr(self) -> str:
        return self.entry_expr.get().strip()

    def _get_init(self):
        ig = self.entry_init.get().strip()
        if ig == "":
            ig = simpledialog.askstring("Initial guess", "Enter initial guess for Newton-Raphson:", parent=self.master)
            if ig is None:
                raise ValueError("No initial guess provided.")
        return ig

    def on_simplify(self):
        expr = self._get_expr()
        if not expr:
            messagebox.showinfo("Input required", "Please enter an expression first.")
            return
        try:
            res = compute_simplify(expr)
            self._append_output(f"Simplified:\n{res}\n")
        except Exception as e:
            messagebox.showerror("Error (simplify)", str(e))

    def on_diff(self):
        expr = self._get_expr()
        if not expr:
            messagebox.showinfo("Input required", "Please enter an expression first.")
            return
        try:
            res = compute_differentiate(expr)
            self._append_output(f"Derivative wrt x:\n{res}\n")
        except Exception as e:
            messagebox.showerror("Error (differentiate)", str(e))

    def on_integrate(self):
        expr = self._get_expr()
        if not expr:
            messagebox.showinfo("Input required", "Please enter an expression first.")
            return
        try:
            res = compute_integrate(expr)
            self._append_output(f"Integral wrt x:\n{res}\n")
        except Exception as e:
            messagebox.showerror("Error (integrate)", str(e))

    def on_factor(self):
        expr = self._get_expr()
        if not expr:
            messagebox.showinfo("Input required", "Please enter an expression first.")
            return
        try:
            res = compute_factor(expr)
            self._append_output(f"Factored form:\n{res}\n")
        except Exception as e:
            messagebox.showerror("Error (factor)", str(e))

    def on_newton(self):
        expr = self._get_expr()
        if not expr:
            messagebox.showinfo("Input required", "Please enter an expression first.")
            return
        try:
            ig = self._get_init()
            res = compute_newton_raphson(expr, ig)
            self._append_output(f"Newton-Raphson root (approx):\n{res}\n")
        except Exception as e:
            messagebox.showerror("Error (Newton-Raphson)", str(e))

    def on_solve(self):
        expr = self._get_expr()
        if not expr:
            messagebox.showinfo("Input required", "Please enter an equation or expression first.")
            return
        try:
            res = compute_solve(expr)
            self._append_output(f"Solve result:\n{res}\n")
        except Exception as e:
            messagebox.showerror("Error (solve)", str(e))

    def on_limit(self):
        expr = self._get_expr()
        if not expr:
            messagebox.showinfo("Input required", "Please enter an expression first.")
            return
        point = simpledialog.askstring("Limit point", "Limit as x → (enter a value or oo for infinity):", parent=self.master)
        if point is None:
            return
        try:
            res = compute_limit(expr, point)
            self._append_output(f"Limit as x→{point}:\n{res}\n")
        except Exception as e:
            messagebox.showerror("Error (limit)", str(e))

    # ---------- Utility ----------
    def open_expression_from_file(self):
        fn = filedialog.askopenfilename(title="Open expression file", filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not fn:
            return
        try:
            with open(fn, 'r', encoding='utf-8') as f:
                txt = f.read().strip()
            self.entry_expr.delete(0, tk.END)
            self.entry_expr.insert(0, txt)
            self._append_output(f"[Loaded expression from {fn}]\n")
        except Exception as e:
            messagebox.showerror("Open file error", str(e))

    def save_output_to_file(self):
        fn = filedialog.asksaveasfilename(title="Save output", defaultextension=".txt", filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not fn:
            return
        try:
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(self.output_area.get("1.0", tk.END))
            messagebox.showinfo("Saved", f"Output saved to: {fn}")
        except Exception as e:
            messagebox.showerror("Save error", str(e))

    def copy_output(self):
        txt = self.output_area.get("1.0", tk.END).strip()
        if not txt:
            return
        self.master.clipboard_clear()
        self.master.clipboard_append(txt)
        self._append_output("[Output copied to clipboard]\n")

    def paste_to_expression(self):
        try:
            txt = self.master.clipboard_get()
        except Exception:
            txt = ""
        if txt:
            self.entry_expr.delete(0, tk.END)
            self.entry_expr.insert(0, txt)

    def clear_output(self):
        self.output_area.delete("1.0", tk.END)

    def _append_output(self, text: str):
        self.output_area.insert(tk.END, text + "\n")
        self.output_area.see(tk.END)

    def toggle_theme(self):
        # Cycle themes: dark -> light -> mature ->        
        if self.theme == "dark":
            self.theme = "light"
        elif self.theme == "light":
            self.theme = "mature"
        else:
            self.theme = "dark"
        self._apply_theme()

    def show_about(self):
        messagebox.showinfo("About", "C-Calculator\nTkinter + SymPy\nKeypad-enabled GUI\n(©Hodo Charles 2025)\nDedicated to AFIT(Mathematics Dept) \n & C-learn Team")

    def show_help(self):
        help_text = (
            "How to use:\n"
            "• Type or click buttons to enter expression(equation).\n"
            "• Use 'x' for variable, sqrt() for roots.\n"
            "•example of expression is\n x**3-3*x-6 which is the same as \n x^3-3*x-6\n"
            "• trig functions should have \na closing bracket cos(x)\n"
               "• Use oo (small leter o)\nfor infinity in limits.\n"
            "• Click Tools button or menu for operations.\n"
            "• Newton-Raphson requires initial guess.\n"
            "• Toggle theme with Ctrl+T."
        )
        messagebox.showinfo("Docs / How to use", help_text)

# ---------- Run ----------
def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
        
# ---------------------------------------------------------
#  MyProgram™ v1.0
#  Author: Hodo Charles
#  © 2025 Hodo Charles. All rights reserved.
#  This software is protected under trademark law.
#  Unauthorized copying or use is prohibited.
# ---------------------------------------------------------

