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
    assert type(num) == int, "Error: data type of num must be int!"; assert type(debug) == bool, "Error: data type of debug must be bool!"
    if type(file) == list:
        if all(type(i) is str for i in file) == False:
            raise TypeError("Error: all filenames in list file must be type str!")
    else:
        assert type(file) == str, "Error: data type of file must be str/list!"
    if debug == True:
        import time; start_time = time.time()
    primes = [True] * (num+1); primes[0] = False; primes[1] = False
    for i in range(2,num+1):
        if primes[i] == True:
            for n in range(i**2,num+1,i):
                primes[n] = False
    if type(file) == str:
        with open(file, 'w+') as f:
            for i in range(len(primes)):
                if primes[i] == True:
                    f.write(str(i) + '\n')
        if debug == True:
            with open(file, 'r') as f:
                length_of_file = len(f.readlines()) # NOTE: Only includes prime numbers. Ignores debug options
            with open(file, 'a+') as f:
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
                with open(current_file, 'r') as f:
                    length_of_file = len(f.readlines()) # NOTE: Only includes prime numbers. Ignores debug options
                with open(current_file, 'a+') as f:
                    exec_time = time.time() - start_time; f.write('# of primes: ' + str(length_of_file) + '\n'); f.write('Execution time: ' + str(exec_time))
        return (primes)

def eratosthenesbitflip(num:int,file: list[str],debug:bool) -> list:
    import bitarray
    # lines 64-69: anti-user error catching code
    # lines 70-74: actual sieve
    assert type(num) == int, "Error: data type of num must be int!"; assert type(debug) == bool, "Error: data type of debug must be bool!"
    assert type(file) == list, "Error: data type of file must be list!"
    if all(type(i) is str for i in file) == False: # Checks if even a single file name is not a string
        raise TypeError("Error: all filenames in list file must be data type str!")
    if debug == True:
        import time; start_time = time.time()
    primes = bitarray.bitarray(num+1); primes.setall(1); primes[0:2] = 0 # initialize prime number array
    for i in range(2,num+1):
        if primes[i] == 1:
            for n in range(i**2,num+1,i):
                primes[n] = 0
    for i in range(len(file)):
        current_file = file[i]
        with open(current_file, 'w+') as f:
            if i == 0:
                for n in range(len(primes)//len(file)): # optimize
                    if primes[n] == 1:
                        f.write(str(n) + '\n')
            else:
                for m in range(((len(primes)//len(file))*i),((len(primes)//len(file))*(i+1))):
                    if primes[m] == 1:
                        f.write(str(m) + '\n')
        if debug == True:
            with open(current_file, 'r') as f:
                length_of_file = len(f.readlines()) # NOTE: Only includes prime numbers. Ignores debug options
            with open(current_file, 'a+') as f:
                exec_time = time.time() - start_time; f.write('# of primes: ' + str(length_of_file) + '\n'); f.write('Execution time: ' + str(exec_time))
    return (primes)

def find_prime(num:int,length:int) -> int:
    try:
        if isinstance(num, int) == False or isinstance(length, int) == False:
            raise TypeError("One of the passed parameters is not of type 'int'!")
        list = eratosthenesbitflip(length,'test.txt',False)
        return list[num]
    except IndexError as e:
        raise IndexError('The prime you were accessing does not appear in the first ' + str(length) + ' #s. Please increase the length parameter.') from e

def isPrime(num) -> bool:
    if not isinstance(num, int):
        raise TypeError("num should be of type 'int'!")
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def file_name_gen(folder:str, end:int, file_num:int) -> list:
    file_list = []; sep = end/file_num
    for i in range(1,file_num+1):
        num_1 = str("{:e}".format((i-1)*sep)); num_2 = str("{:e}".format(i*sep)) # Get scientific numbers, exponent and all!
        num_1 = num_1.split('e'); num_1_exp = 'e' + num_1[1]; num_1_dec = num_1[0] # split into two parts: the exponenent and the power, called num_1_exp and num_1_dec respectively.
        num_2 = num_2.split('e'); num_2_exp = 'e' + num_2[1]; num_2_dec = num_2[0]
        num_1_dec = num_1_dec.rstrip("0"); num_2_dec = num_2_dec.rstrip("0") # remove all trailing zeroes from number
        
        if num_1_dec[-1] == '.': # adds trailing zeroes to avoid rogue trailing decimal points
            num_1_dec += '0'
        if num_2_dec[-1] == '.':
            num_2_dec += '0'
        file_name = f"{folder}/primes-{num_1_dec}{num_1_exp}-{num_2_dec}{num_2_exp}.txt"; file_list.append(file_name) # file name formatting
        f = open(file_name,'w+'); f.close() # the file creation bit; creates a blank file
    return file_list

# Driver code
if __name__ == '__main__':
    cmds = None
    while cmds != 'quit':
        cmds = input('Please enter a command.')
        if cmds == 'quit':
            break
        if '.txt' not in cmds[:12]:
            try:
                exec(cmds); print('The command executed successfully.')
            except (NameError, SyntaxError) as e:
                raise Exception('Invalid command!')
        else:
            try:
                with open(cmds, 'r') as f:
                    for i in f.readlines():
                        exec(i)
                    print('All commands were executed successfully.')
            except (NameError, SyntaxError) as e:
                raise Exception('Invalid filename!')