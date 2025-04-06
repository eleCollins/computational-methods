
class NFA:
    """
    Represents a Nondeterministic Finite Automaton (NFA), including support for epsilon transitions.

    Attributes:
        states (set[int]): Set of states in the NFA.
        alphabet (set[str]): Set of input symbols (excluding epsilon).
        transitions (dict[int, dict[str, list[int]]]): 
            Transition function mapping each state to a dictionary that maps symbols 
            (including epsilon '') to a list of reachable states.
        start_state (int): Initial state of the NFA.
        final_states (set[int]): Set of accepting states.
    """
    def __init__(
        self, 
        states: set[int], 
        alphabet: set[str],  
        transitions: dict[int, dict[str, list[int]]], 
        start_state: int,  
        final_states: set[int]):
        """
        Initializes the NFA with its components.

        Args:
            states (set[int]): All states in the NFA.
            alphabet (set[str]): The input alphabet (excluding epsilon '').
            transitions (dict): The transition table.
            start_state (int): The starting state.
            final_states (set[int]): The set of accepting states.
        """
        
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def epsilon_closure(self, state):
        """
        Computes the epsilon closure of a given state.

        The epsilon closure is the set of all states reachable from the given
        state using only epsilon (empty string) transitions.

        Args:
            state (int): The state to compute the epsilon closure for.

        Returns:
            set[int]: The epsilon closure of the state.
        """
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
        """
        Converts this NFA into an equivalent DFA using the subset construction algorithm.

        This includes handling epsilon transitions during state expansion.

        Returns:
            DFA: A deterministic finite automaton equivalent to this NFA.
        """
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
    """
    Represents a Deterministic Finite Automaton (DFA).

    Attributes:
        states (set[frozenset[int]]): Set of DFA states (each is a frozenset of NFA states).
        alphabet (set[str]): Set of input symbols.
        transitions (dict[frozenset[int], dict[str, frozenset[int]]]): DFA transition function.
        start_state (frozenset[int]): Start state of the DFA.
        final_states (set[frozenset[int]]): Set of accepting states.
    """
    def __init__(self, 
        states: set[int], 
        alphabet: set[str], 
        transitions: dict[frozenset[int], dict[str, frozenset[int]]],
        start_state: int, 
        final_states: set[int]):
        """
        Initializes the DFA with its components.

        Args:
            states (set[frozenset[int]]): DFA states.
            alphabet (set[str]): DFA input symbols.
            transitions (dict): Transition function.
            start_state (frozenset[int]): Start state.
            final_states (set[frozenset[int]]): Accepting states.
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def accepts(self, string):
        """
        Determines if the DFA accepts the given input string.

        Args:
            string (str): The input string to evaluate.

        Returns:
            bool: True if the string is accepted by the DFA, False otherwise.
        """
        current_state = self.start_state
        for symbol in string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions.get(current_state, {}).get(symbol)
            if current_state is None:
                return False
        return current_state in self.final_states