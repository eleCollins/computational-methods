class NFA:
    def __init__(
        self, 
        states: set[int],  # Correct: A set of integers representing NFA states.
        alphabet: set[str],  # Correct: A set of strings representing the input symbols.
        transitions: dict[int, dict[str, list[int]]],  # Correct: Maps a state to a dictionary of symbol-to-list-of-states.
        start_state: int,  # Correct: An integer representing the start state.
        final_states: set[int]  # Correct: A set of integers representing final states.
    ):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def epsilon_closure(self, state):
        stack = [state]
        closure = set(stack)
        
        while stack:
            current_state = stack.pop()
            for next_state in self.transitions.get(current_state, {}).get('', []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        
        return closure

    def to_dfa(self):
        dfa_states = []
        dfa_transitions = {}
        dfa_start_state = frozenset(self.epsilon_closure(self.start_state))
        dfa_states.append(dfa_start_state)
        unprocessed_states = [dfa_start_state]
        dfa_final_states = set()

        while unprocessed_states:
            current_dfa_state = unprocessed_states.pop()
            dfa_transitions[current_dfa_state] = {}

            for symbol in self.alphabet:
                if symbol == '':  # Skip epsilon transitions
                    continue
                next_states = set()
                for nfa_state in current_dfa_state:
                    next_states.update(self.transitions.get(nfa_state, {}).get(symbol, []))
                epsilon_closure_states = set()
                for state in next_states:
                    epsilon_closure_states.update(self.epsilon_closure(state))
                next_dfa_state = frozenset(epsilon_closure_states)

                if next_dfa_state not in dfa_states:
                    dfa_states.append(next_dfa_state)
                    unprocessed_states.append(next_dfa_state)

                dfa_transitions[current_dfa_state][symbol] = next_dfa_state

                if next_dfa_state & self.final_states:
                    dfa_final_states.add(next_dfa_state)

        return DFA(dfa_states, self.alphabet, dfa_transitions, dfa_start_state, dfa_final_states)

class DFA:
    def __init__(self, 
        states: set[int], 
        alphabet: set[str], 
        transitions: dict[frozenset[int], dict[str, frozenset[int]]],
        start_state: int, 
        final_states: set[int]
    ):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def accepts(self, string):
        """Check if the DFA accepts the given string."""
        current_state = self.start_state
        for symbol in string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions.get(current_state, {}).get(symbol)
            if current_state is None:
                return False
        return current_state in self.final_states