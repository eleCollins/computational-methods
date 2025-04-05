from automatas import NFA

nfa_states = {0, 1}
nfa_alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
nfa_transitions = {
    0: {
        **{char: [1] for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    },
    1: {
        **{char: [1] for char in nfa_alphabet},
    }
}
nfa_start_state = 0
nfa_final_states = {1}

nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states)
variables = nfa.to_dfa()