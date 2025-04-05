from automatas import NFA

# NFA para el paréntesis izquierdo '('
nfa_left_parenthesis_states = {0, 1}
nfa_left_parenthesis_alphabet = {'('}
nfa_left_parenthesis_transitions = {
    0: {'(': [1]}
}
nfa_left_parenthesis_start_state = 0
nfa_left_parenthesis_final_states = {1}

parentesis_izq = NFA(
    nfa_left_parenthesis_states,
    nfa_left_parenthesis_alphabet,
    nfa_left_parenthesis_transitions,
    nfa_left_parenthesis_start_state,
    nfa_left_parenthesis_final_states
).to_dfa()

# NFA para el paréntesis derecho ')'
nfa_right_parenthesis_states = {0, 1}
nfa_right_parenthesis_alphabet = {')'}
nfa_right_parenthesis_transitions = {
    0: {')': [1]}
}
nfa_right_parenthesis_start_state = 0
nfa_right_parenthesis_final_states = {1}

parentesis_der = NFA(
    nfa_right_parenthesis_states,
    nfa_right_parenthesis_alphabet,
    nfa_right_parenthesis_transitions,
    nfa_right_parenthesis_start_state,
    nfa_right_parenthesis_final_states
).to_dfa()

