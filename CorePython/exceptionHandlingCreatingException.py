

# three type exception 1)ZeroDivisionError,2) ValueError 3)Exception
a=1
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    print("hey",e)
except ValueError as e:
    print("hello",e)  
except Exception as e:
    print("hii",e)
finally:
    print("resource closed")          
print("ok")        