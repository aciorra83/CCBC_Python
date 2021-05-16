# the code in the else block is always executed IF NO ERROR OCCURRED    

try:
    with open('input.txt', 'r') as myinputfile:
        for line in myinputfile:
            prin(line)
except FileNotFoundError:
    print('Whoops! File does not exist.')
except ValueError:
    print('A value error occurred.')
except Exception:
    print('Something unforseen happened.')
else:
    print('No error because file exists.')
print('Execution will continue to here.')

# EX 51: Implementing the 'Finally' keyword:
try:
    with open('input.txt', 'r') as myinputfile:
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print('Whoops! It ain\'t there bruh')
except ValueError:
    print('A value error happened.')
except Exception:
    print('I don\'t know what happened')
finally:
    print('I will ALWAYS show up')
print('This is the end of execution.')