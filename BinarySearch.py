def locate_cards(cards,query):
    lo,hi=0,len(cards)-1
    while lo<=hi:
        mid=(lo+hi)//2
        mid_num=cards[mid]
        print("lo:",lo,"hi:",hi,"Mid:",mid,"mid_num:",mid_num)
        if cards[mid]==query:
            return mid
        elif cards[mid]<query:
            hi=mid-1
        elif cards[mid]>query:
            lo=mid+1
    return -1

tests=[]
tests.append({
    'input':{
        'cards':[10,9,8,7,6,5,4,3,2,1],
        'query':7
    },
    'output':3
})
tests.append({
    'input':{
        'cards':[10,9,8,7,6,5,4,3,2,1],
        'query':10
    },
    'output':0
})
tests.append({
    'input':{
        'cards':[10,9,8,7,6,5,4,3,2,1],
        'query':1
    },
    'output':9
})
tests.append({
    'input':{
        'cards':[9],
        'query':9
    },
    'output':0
})
tests.append({
    'input':{
        'cards':[],
        'query':8
    },
    'output':-1
})
tests.append({
    'input':{
        'cards':[10,10,8,8,7,7,5,5,5,3,3,2,1,1],
        'query':7
    },
    'output':4
})
tests.append({
    'input':{
        'cards':[10,9,6,6,6,5,4,3,2,1],
        'query':6
    },
    'output':2
})
for i,test_case in enumerate(tests):
    result=locate_cards(test_case['input']['cards'],test_case['input']['query'])
    is_correct=result==test_case['output']
    print(f"test case{i}:result:{result} Expected:{test_case['output']}| Passed:{is_correct}")