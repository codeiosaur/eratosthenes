from typing import Union
import time

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

def eratosthenes_bool(num:int,file: Union[str,list],debug:bool) -> list:
    assert type(num) == int, (f'Error: expected type int for num,'
                            f' type {type(num)} given')
    assert type(debug) == bool, (f'Error: expected type bool for debug,'
                            f' type {type(debug)} given')
    if type(file) == list:
        if all(type(i) is str for i in file) == False:
            raise TypeError('Error: all filenames in list must be type str!')
    else:
        assert type(file) == str, 'Error: file type must be str/list!'
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
                # NOTE: Only includes prime numbers. Ignores debug options
                length_of_file = len(f.readlines())
            with open(file, 'a+') as f:
                exec_time = time.time() - start_time
                f.write('# of primes: ' + str(length_of_file) + '\n')
                f.write('Execution time: ' + str(exec_time))
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
                    for m in range(((len(primes)//len(file))*i),
                                   ((len(primes)//len(file))*(i+1))):
                        if primes[m] == True:
                            f.write(str(m) + '\n')
            if debug == True:
                with open(current_file, 'r') as f:
                    # NOTE: Only includes prime numbers. Ignores debug options
                    length_of_file = len(f.readlines()) 
                with open(current_file, 'a+') as f:
                    exec_time = time.time() - start_time 
                    f.write('# of primes: ' + str(length_of_file) + '\n')
                    f.write('Execution time: ' + str(exec_time))
        return (primes)

def eratosthenes_bitflip(num:int,output: list[str],debug:bool) -> list:
    import bitarray
    # lines 64-69: anti-user error catching code
    # lines 70-74: actual sieve
    assert type(num) == int, (f'Error: expected type int for num,'
                            f' type {type(num)} given')
    assert type(debug) == bool, (f'Error: expected type bool for debug,'
                                f' type {type(debug)} given')
    assert type(output) == list, (f'Error: expected type list for file,'
                                f'type {type(output)} given')
    # Checks if even a single file name is not a string
    if all(type(i) is str for i in output) == False:
        raise TypeError('Error: all filenames in list must be data type str!')
    if debug == True:
        import time; start_time = time.time()
    primes = bitarray.bitarray(num+1)
    primes.setall(1); primes[0:2] = 0 # initialize prime number array
    for i in range(2,num+1):
        if primes[i] == 1:
            for n in range(i**2,num+1,i):
                primes[n] = 0
    for i in range(len(output)):
        current_file = output[i]
        with open(current_file, 'w+') as f:
            if i == 0:
                for n in range(len(primes)//len(output)): # optimize
                    if primes[n] == 1:
                        f.write(str(n) + '\n')
            else:
                for m in range(((len(primes)//len(output))*i),
                               ((len(primes)//len(output))*(i+1))):
                    if primes[m] == 1:
                        f.write(str(m) + '\n')
        if debug == True:
            with open(current_file, 'r') as f:
                # NOTE: Only includes prime numbers. Ignores debug options
                length_of_file = len(f.readlines())
            with open(current_file, 'a+') as f:
                exec_time = time.time() - start_time
                f.write('# of primes: ' + str(length_of_file) + '\n')
                f.write('Execution time: ' + str(exec_time))
    return (primes)

def dd_eratosthenes(start:int,num:int,infile:list[str],outfile:str) -> list: 
    # a list of output files is not required 
    # Optimize Lines 107-113 and 117-124
    # Add in-sieve sieving?
    import bitarray
    assert type(start) == int, (f'Error: expected type int for start,'
                                f' type {type(start)} given')
    assert type(num) == int, (f'Error: expected type int for num,'
                                f' type {type(num)} given')
    assert type(infile) == list, (f'Error: expected type list for infile,' 
                                f' type {type(infile)} given')
    assert type(outfile) == str, (f'Error: expected type str for outfile,' 
                                f' type {type(outfile)} given')
    # FIXME: Fix an edge case where if start**2 < num, 
    # Some numbers are misidentified as prime when they are actually composite. 
    # An assertion has been added to prevent this until a fix has been found.
    try:
        assert start**2 > num
    except AssertionError:
        raise NotImplementedError(f'A bug for number ranges like {start**2}'
                                f' through {num} exists!'
                                f' Please select another range instead.')

    for name in range(len(infile)):
        if isinstance(infile[name], str) == False:
            raise TypeError(f'Error: expected type str for all infile elements'
                            f', type {type(infile[name])}'
                            f' given for element {name} of infile')
    with open(infile[-1],'r') as f:
        for line in f:
            pass
        very_last_input_num = line # last line of last file
    # initialize prime number array
    primes = bitarray.bitarray(1 for i in range(num-start))

    for i in range(len(infile)):
        curr_i_file = infile[i] # current input file
        with open(curr_i_file, 'r') as f:
            for line in f:
                content = int(line.rstrip()) # Sanitize the line to remove \n
                for j in range(len(primes)):
                    # NOTE: Write input # to sieve of eratosthenes. Optimize
                    if (j+start) % content == 0:
                        primes[j] = 0

    # FIXME: See line 100
    # if (start**2 <= num): #If start**2 < num, run normal sieve and file read.
    #     for i in range(len(primes)):
    #         if primes[i] == 1:
    #             if i == 0:
    #                 for n in range((start)**2, num+1):
    #                     pass # Implement edge case if 1st # is prime
    #             else:
    #                 for n in range((i+start)**2,num+1,i):
    #                     primes[(n-start)] = 0 # TEST THIS

    with open(outfile, 'w+') as f:
        for i in range(len(primes)):
            if primes[i] == 1:
                f.write(str(i+start) + '\n')
    return (primes)

def find_prime(num:int,length:int) -> int:
    try:
        if isinstance(num, int) == False or isinstance(length, int) == False:
            raise TypeError('A passed parameter is not of type "int"!')
        list = eratosthenes_bitflip(length,['test.txt'],False)
        return list[num]
    except IndexError as e:
        raise IndexError('The prime you were accessing does not appear in the' 
                         'first ', + str(length) + 
                         ' #s. Please increase the length parameter.') from e

def is_prime(num) -> bool:
    if not isinstance(num, int):
        raise TypeError('num should be of type "int"!')
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def file_name_gen(folder:str, end:int, file_num:int) -> list:
    file_list = []; sep = end/file_num
    for i in range(1,file_num+1):
        # Get scientific numbers, exponent and all
        num_1 = str('{:e}'.format((i-1)*sep))
        num_2 = str('{:e}'.format(i*sep))

        num_1 = num_1.split('e')
        num_1_exp = 'e' + num_1[1] # exponent part of num
        num_1_dec = num_1[0] # decimal part of num

        num_2 = num_2.split('e')
        num_2_exp = 'e' + num_2[1]
        num_2_dec = num_2[0]
        # remove all trailing zeroes to prevent rogue decimal points
        num_1_dec = num_1_dec.rstrip('0')
        num_2_dec = num_2_dec.rstrip('0')
        # adds trailing zeroes to avoid rogue trailing decimal points
        if num_1_dec[-1] == '.':
            num_1_dec += '0'
        if num_2_dec[-1] == '.':
            num_2_dec += '0'
        # file name formatting
        file_name = f'{folder}/primes-{num_1_dec}{num_1_exp} \
            -{num_2_dec}{num_2_exp}.txt'
        file_list.append(file_name) # file name formatting
        # creates a blank file
        f = open(file_name,'w+'); f.close()
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