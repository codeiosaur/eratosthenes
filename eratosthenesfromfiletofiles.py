from typing import Union

def eratosthenes(num:int,file:str) -> list:
    prime_attempts = []
    primes = []
    for i in range(2,num+1):
        if i not in prime_attempts:
            primes.append(i)
            for n in range(i**2,num+1,i):
                prime_attempts.append(n)
    with open(file, 'w') as file:
        for i in range(len(primes)):
            file.write(str(primes[i]) + '\n')
    return (primes)

def eratosthenesbool(num:int,file: Union[str,list],debug:bool) -> list:
    if debug == True:
        import time; start_time = time.time()
    primes = [True] * (num+1); primes[0] = False; primes[1] = False
    for i in range(2,num+1):
        if primes[i] == True:
            for n in range(i**2,num+1,i):
                primes[n] = False
    if type(file) == 'str':
        with open(file, 'w+') as f:
            for i in range(len(primes)):
                if primes[i] == True:
                    f.write(str(i) + '\n')
            if debug == True:
                length_of_file = len(f.readlines()) # NOTE: Only includes prime numbers. Ignores debug options
                exec_time = time.time() - start_time; f.write('# of primes: ' + str(length_of_file) + '\n'); f.write('Execution time: ' + str(exec_time))
        return (primes)
    else:
        for i in range(len(file)):
            current_file = file[i]
            with open(current_file, 'w+') as f:
                if i == 0:
                    for n in range(len(primes)//len(file)):
                        if primes[n] == True:
                            f.write(str(n) + '\n')
                else:
                    for m in range(((len(primes)//len(file))*i),((len(primes)//len(file))*(i+1))):
                        if primes[m] == True:
                            f.write(str(m) + '\n')
                if debug == True:
                    length_of_file = len(f.readlines()) # NOTE: Only includes prime numbers. Ignores debug options
                    exec_time = time.time() - start_time; f.write('# of primes: ' + str(length_of_file) + '\n'); file.write('Execution time: ' + str(exec_time))
        return (primes)


def find_prime(num:int,length:int) -> int:
    try:
        list = eratosthenesbool(length,'test.txt')
        return list[num]
    except IndexError:
        raise Exception('The prime you were accessing does not appear in the first ' + str(length) + ' #s. Please increase the length parameter.')

def isPrime(num) -> bool:
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

# Driver code:
cmds = None
while cmds != 'quit':
    cmds = input('Please enter a command.')
    if cmds == 'quit':
        break
    elif '.txt' in cmds:
        try:
            with open(cmds, 'r') as f:
                for i in f.readlines():
                    exec(i)
                print('All commands were executed successfully.')
        except (NameError, SyntaxError) as e:
            raise Exception('Invalid filename!')
    else:
        try:
            exec(cmds); print('The command executed successfully.')
        except (NameError, SyntaxError) as e:
            raise Exception('Invalid command!')