def vacuum_cleaner(percept):
    state = percept
    if state['A'] == 'Dirty':
        print("Clean A")
        state['A'] = 'Clean'
    elif state['A'] == 'Clean' and state['B'] == 'Dirty':
        print("Move Right to B")
        print("Clean B")
        state['B'] = 'Clean'
    elif state['A'] == 'Clean' and state['B'] == 'Clean':
        print("All rooms are clean")
    return state

rooms = {'A': 'Dirty', 'B': 'Dirty'}
print("Initial State:", rooms)
rooms = vacuum_cleaner(rooms)
rooms = vacuum_cleaner(rooms)
rooms = vacuum_cleaner(rooms)
print("Final State:", rooms)
