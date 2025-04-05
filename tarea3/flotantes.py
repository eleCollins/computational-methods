from automatas import NFA

nfa_states = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
nfa_alphabet = {'+', '-', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'e', 'E', '.'}

nfa_transitions = {
  0: {
    **{char: [1] for char in {'+', '-', ''}}
  }, 
  1: {
    '': [2, 6]
  },
  2: {
    **{char: [3] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}},  
  },
  3: {
    '': [2],
    '.': [4],
  },
  4: {
    **{char: [5] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ''}},
  },
  5: {
    '': [4, 10]
  },
  6: {
    **{char: [7] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ''}},
  },
  7: {
    '': [6],
    '.': [8],
  },
  8: {
    **{char: [9] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}},
  },
  9: {
    '': [8, 10],
  },
  10: {
    '': [13],
    'e': [11],
    'E': [11],
  },
  11: {
    **{char: [12] for char in {'+', '-', ''}},
  },
  12: {
    **{char: [13] for char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}},
  },
  13: {
    '': [12]
  }
}
nfa_start_state = 0
nfa_final_states = {13}

nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states)
flotantes = nfa.to_dfa()