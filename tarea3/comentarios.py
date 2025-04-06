from automatas import NFA

# Set of states used in the NFA
nfa_states = {0, 1, 2, 3, 4}
# Input alphabet: All printable characters
nfa_alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\ \t")  # Σ (All characters except '\n')

# NFA Transition Function:
# - This NFA matches comments that begin with "//" and end with a newline '\n'.
# - It loops over all valid characters (excluding newline) until '\n' is encountered.
nfa_transitions = {
    0: {
        '/': [1]  # From state 0 to state 1 upon reading '/'
    },
    1: {
        '/': [2]  # From state 1 to state 2 upon reading second '/'
    },
    2: {
        # Loop on all allowed characters in Σ (except '\n') to stay in state 2
        **{char: [2] for char in nfa_alphabet},
        '\n': [3] # From state 2 to accepting state 3 on newline
    },
    3: {}  # Final (accepting) state with no outgoing transitions
}
# Starting state of the NFA
nfa_start_state = 0

# Set of accepting (final) states
nfa_final_states = {3}

# Create the NFA instance
nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states)

# Convert the NFA to an equivalent DFA
comentarios = nfa.to_dfa()