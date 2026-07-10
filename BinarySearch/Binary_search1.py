def rotate_list(num):
    low,high=0,len(num)-1
    while low<=high:
        mid=(low+high)//2
        mid_number=num[mid]
        if mid>0 and num[mid]<num[mid-1]:
            return mid
        elif mid>0 and num[mid]>num[-1]:
            low=mid+1
        else:
            high=mid-1
    return 0
tests=[]
tests.append({
    'input':{
        'nums':[4,5,6,1,2,3]
    },
    'output':3
})
tests.append({
    'input':{
        'nums':[3,4,5,6,1,2]
    },
    'output':4
})
tests.append({
    'input':{
        'nums':[1,2,3,4,5,6]
    },
    'output':0
})
tests.append({
    'input':{
        'nums':[3,1,2]
    },
    'output':1
})
tests.append({
    'input':{
        'nums':[]
    },
    'output':0
})
tests.append({
    'input':{
        'nums':[4]
    },
    'output':0
})
tests.append({
    'input':{
        'nums':[2,3,4,5,6,1]
    },
    'output':5
})
for i,test_case in enumerate(tests):
    result=rotate_list(test_case['input']['nums'])
    is_correct=result==test_case['output']
    print(f"test case {i}:output {result} expected output :{test_case['output']}||passed:{is_correct}")
