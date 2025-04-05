from automatas import NFA

# Define a function to create a DFA for a single operator
def create_operator_dfa(operator):
    dfa_states = {0, 1}
    dfa_alphabet = {operator}
    dfa_transitions = {
        0: {
          operator: [1]
          },
    }
    dfa_initial_state = 0
    dfa_final_states = {1}
    return NFA(dfa_states, dfa_alphabet, dfa_transitions, dfa_initial_state, dfa_final_states).to_dfa()

# List of operators
operators = '=+-*/^'

# Create a dictionary of DFAs, one for each operator
operator_dfas = {op: create_operator_dfa(op) for op in operators}