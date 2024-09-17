## Naive GUI app for generating the context-free grammar (CFG) from an input deterministic finite automaton (DFA)

### DFA Representation
- **States (Q)**: Set of states in the DFA.
- **Alphabet (Σ)**: Set of symbols that the DFA accepts.
- **Transitions (δ)**: Rules for moving from one state to another based on input symbols.
- **Start State (q0)**: The initial state of the DFA.
- **Accept States (F)**: States that indicate successful acceptance of an input string.

### CFG Components
- **Variables (Non-terminals)**: Each state in the DFA will correspond to a non-terminal in the CFG.
- **Terminals**: The alphabet symbols of the DFA.
- **Production Rules**: Rules that define how non-terminals are expanded into terminals and other non-terminals.
- **Start Variable**: A non-terminal that represents the start state of the DFA.

  #### Conversion Process
  1. Create Non-terminals for Each State `For each state qi in the DFA , create a corresponding non-terminal Ai in the CFG`
  2. Create Production Rules for Transitions `For each transition in DFA , create corresponding production rules in the CFG.If there is a transition from state q_i to q_j on input symbol "a",add the rule:  A_i -> aA_j`     
  4. Handle Accept States `For each accept state 𝑞𝑖 in the DFA, add a production rule that allows the non-terminal corresponding to 𝑞𝑖 to generate an empty string: A_i -> ϵ`

### Steps to execute the code:
1. Install Python 3.11
2. Use `pip` command to install the imported libraries
3. Go to terminal , use `cd <location_of_file>` to go to the directory
4. Run `python dfa2cfg.py`
  
   
