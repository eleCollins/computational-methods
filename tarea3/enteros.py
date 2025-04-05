from automatas import NFA

nfa_states= {0, 1, 2}
nfa_alphabet = {'+', '-', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
nfa_transitions = {
    0: {
      '': [1], 
      '+': [1], 
      '-': [1]
    },
    1: {
      '0': [2], 
      '1': [2], 
      '2': [2], 
      '3': [2], 
      '4': [2], 
      '5': [2], 
      '6': [2], 
      '7': [2], 
      '8': [2], 
      '9': [2]
    },
    2: {
    '': [1]
    },
}
nfa_start_state = 0
nfa_final_states = {2}

nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states)
enteros = nfa.to_dfa()
