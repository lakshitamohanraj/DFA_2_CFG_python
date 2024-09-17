import tkinter as tk
from tkinter import messagebox

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = set(states.split(','))
        self.alphabet = set(alphabet.split(','))
        self.transitions = {}
        for transition in transitions.split(';'):
            if transition:
                state, symbol, next_state = transition.split(',')
                self.transitions[(state, symbol)] = next_state
        self.start_state = start_state
        self.accept_states = set(accept_states.split(','))

class CFG:
    def __init__(self):
        self.variables = set()
        self.terminals = set()
        self.productions = []
        self.start_variable = None

    def add_variable(self, variable):
        self.variables.add(variable)

    def add_terminal(self, terminal):
        self.terminals.add(terminal)

    def add_production(self, lhs, rhs):
        self.productions.append((lhs, rhs))

    def set_start_variable(self, variable):
        self.start_variable = variable

    def __str__(self):
        result = []
        result.append(f"Start Variable: {self.start_variable}")
        result.append("Variables:")
        result.extend(self.variables)
        result.append("Terminals:")
        result.extend(self.terminals)
        result.append("Productions:")
        for lhs, rhs in self.productions:
            result.append(f"{lhs} -> {rhs}")
        return "\n".join(result)

def dfa_to_cfg(dfa):
    cfg = CFG()
    
    # Add variables (non-terminals)
    for state in dfa.states:
        cfg.add_variable(f"A_{state}")
    
    # Set the start variable
    cfg.set_start_variable(f"A_{dfa.start_state}")
    
    # Add productions for transitions
    for (state, symbol), next_state in dfa.transitions.items():
        cfg.add_production(f"A_{state}", f"{symbol}A_{next_state}")
    
    # Add productions for accepting states
    for state in dfa.accept_states:
        cfg.add_production(f"A_{state}", "")
    
    return cfg

def on_convert():
    try:
        states = states_entry.get().strip()
        alphabet = alphabet_entry.get().strip()
        transitions = transitions_entry.get().strip()
        start_state = start_state_entry.get().strip()
        accept_states = accept_states_entry.get().strip()

        if not states or not alphabet or not transitions or not start_state:
            raise ValueError("All DFA fields must be filled out.")

        dfa = DFA(states, alphabet, transitions, start_state, accept_states)
        cfg = dfa_to_cfg(dfa)
        
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, cfg)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("DFA to CFG Converter")

# Create and place widgets
tk.Label(root, text="States (comma-separated):").pack(pady=5)
states_entry = tk.Entry(root, width=50)
states_entry.pack(pady=5)

tk.Label(root, text="Alphabet (comma-separated):").pack(pady=5)
alphabet_entry = tk.Entry(root, width=50)
alphabet_entry.pack(pady=5)

tk.Label(root, text="Transitions (format: state,symbol,next_state;):").pack(pady=5)
transitions_entry = tk.Entry(root, width=50)
transitions_entry.pack(pady=5)

tk.Label(root, text="Start State:").pack(pady=5)
start_state_entry = tk.Entry(root, width=50)
start_state_entry.pack(pady=5)

tk.Label(root, text="Accept States (comma-separated):").pack(pady=5)
accept_states_entry = tk.Entry(root, width=50)
accept_states_entry.pack(pady=5)

tk.Button(root, text="Convert to CFG", command=on_convert).pack(pady=10)

tk.Label(root, text="Generated CFG:").pack(pady=5)
result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=5)

# Start the GUI event loop
root.mainloop()
