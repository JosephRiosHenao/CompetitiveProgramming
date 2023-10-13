def div(nums): 
    try: 
        return int(int(nums[0])/int(nums[1])) 
    except ZeroDivisionError as e:
        return"Error Code: integer division or modulo by zero"
    except ValueError as e: 
        return "Error Code: "+str(e) 
[print(div(input().split())) for _ in range(int(input()))] 
