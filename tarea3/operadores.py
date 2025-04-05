from automatas import NFA

nfa_states = {0, 1}
nfa_alphabet = set('=+-*/^')
nfa_transitions = {
  0: {
    **{char: [1] for char in nfa_alphabet}
  }
}
nfa_initial_state = 0
nfa_final_states = {1}

nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_initial_state, nfa_final_states)
operadores = nfa.to_dfa()