def check_location(cards,query,mid):
    mid_number=cards[mid]
    if cards[mid]==query:
        if mid-1>=0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'
        
    elif cards[mid]<query:
        return 'left'
    else:
        return 'right'

def Binary_search(cards,query):
    low,high=0,len(cards)-1
    while low<=high:
        mid=(low+high)//2
        mid_number=cards[mid]
        print("low:",low,"high:",high,"mid:",mid,"number:",mid_number)
        result=check_location(cards,query,mid)
        if result=='found':
            return mid
        elif result=='left':
            high=mid-1
        else:
            low=mid+1
    return-1

tests = []


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
    result = Binary_search(test_case['input']['cards'], test_case['input']['query'])
    is_correct = result == test_case['output']
    print(f"Test Case {i} Result: {result} | Expected: {test_case['output']} | Passed: {is_correct}")    