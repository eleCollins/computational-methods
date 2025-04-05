from automatas import NFA

nfa_states = {0, 1, 2, 3, 4}
nfa_alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\ \t")  # Σ (todos los caracteres excepto '\n')
nfa_transitions = {
    0: {
        '/': [1]  # Transición del estado 0 al 1 con '/'
    },
    1: {
        '/': [2]  # Transición del estado 1 al 2 con '/'
    },
    2: {
        **{char: [2] for char in nfa_alphabet},  # Transición del estado 2 al 2 con cualquier carácter de Σ
        '\n': [3]  # Transición del estado 2 al 3 con '\n'
    },
    3: {}  # Estado de aceptación, sin transiciones
}
nfa_start_state = 0
nfa_final_states = {3}

nfa = NFA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states)
comentarios = nfa.to_dfa()