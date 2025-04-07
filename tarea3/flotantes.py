from automatas import NFA

# States in the NFA
nfa_states = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
# Input alphabet includes digits, signs, decimal point, exponent indicators, and ε
nfa_alphabet = {'+', '-', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'e', 'E', '.'}

# Transition function of the NFA
# Handles signed numbers, decimals, and scientific notation using ε-moves
nfa_transitions = {
  0: {
    **{char: [1] for char in {'+', '-', ''}} # Optional sign at start
  }, 
  1: {
    '': [2, 6] # Two possible branches: digit before decimal or directly with decimal
  },
  # Branch 1: Integer part followed by optional decimal
  2: {
    **{char: [3] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}},  
  },
  3: {
    '': [2],  # Loop on digits
    '.': [4], # Decimal point
  },
  4: {
    **{char: [5] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ''}},
  },
  5: {
    '': [4, 10] # Loop over digits or move to exponent/acceptance
  },
  # Branch 2: Starts directly with decimal
  6: {
    **{char: [7] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ''}},
  },
  7: {
    '': [6],  # Loop on digits
    '.': [8], # Decimal point
  },
  8: {
    **{char: [9] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}}, # Digits after decimal
  },
  9: {
    '': [8, 10],   # Loop on digits or move to exponent/acceptance
  },
  10: {
    '': [13],   # Accept without exponent
    'e': [11],  # Start of exponent (lowercase)
    'E': [11],  # Start of exponent (uppercase)
  },
  11: {
    **{char: [12] for char in {'+', '-', ''}},  # Optional sign in exponent
  },
  12: {
    **{char: [13] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}},   # Must have at least one digit in exponent
  },
  13: {
    '': [12]  # Loop on exponent digits
  }
}
# Initial state of the NFA
nfa_start_state = 0

# Final (accepting) states
nfa_final_states = {13}

# Create NFA instance and convert it to a DFA
nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states)
flotantes = nfa.to_dfa()