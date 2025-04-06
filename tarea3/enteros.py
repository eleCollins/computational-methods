from automatas import NFA

# Set of NFA states
nfa_states= {0, 1, 2}

# Input alphabet: includes digits, optional '+' or '-' sign, and '' for epsilon (empty) transitions
nfa_alphabet = {'+', '-', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

# NFA Transition Function:
# - The automaton optionally starts with '+' or '-' or nothing (via ε-transition).
# - It then must read a digit to move to the accepting state.
# - Once in the accepting state, it can loop back to allow more digits.
nfa_transitions = {
    0: {
      '': [1],  # Epsilon transition from state 0 to 1 
      '+': [1], # Optional '+' sign
      '-': [1]  # Optional '-' sign
    },
    1: {
        # From state 1 to accepting state 2 upon reading any digit
      **{char: [2] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}},
    },
    2: {
    '': [1] # Epsilon transition back to state 1 (to allow additional digits)
    },
}

# Start state of the NFA
nfa_start_state = 0

# Accepting state(s) — where a valid integer ends
nfa_final_states = {2}

# Create the NFA instance
nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states)

# Convert the NFA to an equivalent DFA
enteros = nfa.to_dfa()
