from solver.equation_solver import parse_latex_to_sympy, solve_equation, generate_steps
from checker.mistake_checker import detect_mistakes

latex = r"2*(x + 3) = 14"
sym = parse_latex_to_sympy(latex)
print("Parsed:", sym)

sol = solve_equation(sym)
print("Solution:", sol)

steps = generate_steps(sym)
print("Steps:", steps)

mistakes = detect_mistakes(latex, sym)
print("Mistakes:", mistakes)
