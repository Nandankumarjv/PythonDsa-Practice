def locate_cards(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1 
test = {
    'input': {
        'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'query': 7
    },
    'output': 3
}

tests = []
tests.append(test)

tests.append({
    'input': {'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'query': 10},
    'output': 0
})
tests.append({
    'input': {'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'query': 1},
    'output': 9
})
tests.append({
    'input': {'cards': [10, 9, 8, 8, 7, 5, 4, 3, 2, 1], 'query': 8},
    'output': 2
})
tests.append({
    'input': {'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'query': 0},
    'output': -1
})
tests.append({
    'input': {'cards': [10, 10, 8, 8, 6, 6, 4, 4, 4, 1], 'query': 8},
    'output': 2
})
tests.append({
    'input': {'cards': [10], 'query': 10},
    'output': 0
})
tests.append({
    'input': {'cards': [], 'query': 7},
    'output': -1
})

print("Running Automated Tests...\n" + "="*30)

for i, test_case in enumerate(tests):
    result = locate_cards(test_case['input']['cards'], test_case['input']['query'])
    is_correct = result == test_case['output']
    print(f"Test Case {i} Result: {result} | Expected: {test_case['output']} | Passed: {is_correct}")