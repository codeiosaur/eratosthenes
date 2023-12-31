# eratosthenes
A collection of Python functions that deal with prime numbers using the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) and other algorithms.
## Functions
```
eratosthenes(num:int, file:str) -> list/file
```
Takes an integer **num** and a single string filename **file** and writes all the prime numbers in the range 2 through num to file, while also returning them in list form.
In the file, the numbers are one per line, while in the return statement/stdout, the primes are in a list consisting of the prime integers found.
Due to speed and memory requirements, this function is deprecated. Use eratosthenesbool where possible.

```
eratosthenes_bool(num:int, file:str/list[str], debug:bool) -> list/file(s)
```
Takes the same arguments as eratosthenes, with an additional boolean **debug** that can be used to view execution time and the number of primes in the output file.
This function does the same thing as eratosthenes, with the following differences:
1. The function can write to multiple files by passing a list containing string filenames to file, dividing the primes evenly among them. For example, with a prime # list of length 1000, the function can write 250 prime #s to each of 4 files.
2. The prime number list the function returns contains boolean values instead of integers, reducing memory usage and execution time drastically.
3. Has assertions to ensure the passed arguments are the proper type.

```
eratosthenes_bitflip(num:int, file:list[str], debug:bool) -> list/file(s)
```
Does the same thing as eratosthenes_bool, except that file cannot be a string and must be a list populated with string values. Also, the prime number array (before it's written to a file) is now a bitarray instead of a list populated with boolean values.
```
dderatosthenes(start:int, num:int,inputfile:list[str], outputfile:str) -> list/file(s)
```
Acts like eratosthenes_bitflip but reads from input files in addition to writing to an output file. The function sieves positive integers from start through num.
While this function is much slower than eratosthenes_bitflip due to I/O operations, the nature of the function means that memory usage is drastically reduced because the function only stores a part of a larger array at any time.

### Usage Example 
To calculate the primes up to 10^11 without running out of memory:
1. Choose a list size (e.g. 10^10) that is as big as your memory can handle.
2. Use `file_name_gen(folder_name, 10^11, 10^11/list size)` if you want to generate file names.
3. Run `eratosthenes_bitflip(list size, **first item of your file list here in list form**, False)`.
4. For the second array, run `dderatosthenes(list size, 2\*list size, 'first file in your file list' in a list, 'second file in your file list' by itself).`
5. For subsequent arrays, run the previous command, except increment the first two parameters by list size. For the last two parameters, replace 'first' with 'second' and so on.

Steps 4 and 5 can be done through the use of a for loop.
While this can seem convoluted, this is done intentionally to give as much granular control as possible.
```
find_prime(num:int, length:int) -> int
```
Writes the first **length** primes to a file called 'test.txt'. Returns the **num**th prime if it occurs within the calculated values. If it does not occur, the function throws an exception.

```
is_prime(num:int) -> bool
```
Takes a positive integer for num and returns True if that integer is prime. Otherwise, returns False.

```
file_name_gen(folder:str, end:int, file_num:int) -> list
```
Takes a string and two integers for **folder**, **end** and **file_num** respectively. 
Creates **file_num** text files and names them primes-**starting_number**-**endingnumber**.txt in **folder**. 
starting_number and ending_number are both in scientific notation.
- The first file is primes-0.0e+00-**end/file_num**.txt. 
- The last file is called primes-**(file_num-1)×sep**-**end**.txt, where **sep** is (end/file_num) and the range that each file covers.

## Dependencies
- **eratosthenes_bool** and **eratosthenes_bitflip** import time from the standard library if debug is set to True.
- **eratosthenes_bool** also uses **Union** from **typing**, but this does not affect the program's execution.
- **eratosthenes_bitflip** and **dderatosthenes** additionally require the module **bitarray** regardless of passed arguments. That module can be downloaded [here](https://pypi.org/project/bitarray/) or by running `python -m pip install bitarray`, assuming the latest version of Python is used as of this writing.
- The other functions have no dependencies.

## Future Plans
Generally, I have no plans to update eratosthenes or other explicitly deprecated commands, but if people ask, I will deliver. I will also respond to pull requests.
**eratosthenes_bitflip** and **dd_eratosthenes** can be improved, both in execution time and ease of use. 
Currently my plans with these two functions are to optimize execution time as much as possible (first file and I/O operations, second saving CPU time), and then packaging them into different forms. 
These ideas for forms include a function that uses **multiprocessing**, a module on [pypi](https://pypi.org/) and a self-contained command line package executable from a standard terminal.
These plans are uncertain, but they are my plans for the future.
Edit: This will likely no longer be maintained. I might edit this in the future, but I will organize this in a new repo.
