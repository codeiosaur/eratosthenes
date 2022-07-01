# eratosthenes
A collection of Python functions that deal with prime numbers using the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) and other algorithms.
## functions and what they do
```
eratosthenes(num, file) -> list/file
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
Does the same thing as eratosthenes_bool, except that file cannot be a string and must be a list populated with string values. Also, the prime number array (before it's written to a file) is now a bitarray instead of a list populated with boolean values.(before it's written to a file) is now a bitarray instead of a list populated with boolean values.
```
find_prime(num, length) -> int
```
Writes the first **length** primes to a file called 'test.txt'. Returns the **num**th prime if it occurs within the calculated values. If it does not occur, the function throws an exception.
```
is_prime(num) -> bool
```
Takes a positive integer for num and returns True if that integer is prime. Otherwise, returns False.
```
file_name_gen(folder, end, file_num) -> list
```
Takes a string, integer and another integer for **folder**, **end** and **file_num** respectively. 
Creates **file_num** text files and names them primes-**starting_number**-**endingnumber**.txt in **folder**. 
starting_number and ending_number are both in scientific notation.
- The first file is primes-0.0e+00-**end/file_num**.txt. 
- The last file is called primes-**(file_num-1)×sep**-**end**.txt, where **sep** is (end/file_num) and the range that each file covers.

## Dependencies
- **eratosthenes_bool** and **eratosthenes_bitflip** import time from the standard library if debug is set to True.
- **eratosthenes_bool** also uses **Union** from the **typing module**, but this does not affect the program's execution.
- **eratosthenes_bitflip** additionally require the module **bitarray** regardless of passed arguments. That module can be downloaded [here](https://pypi.org/project/bitarray/) or by running `python -m pip install bitarray`, assuming the latest version of Python is used as of this writing.
- The other functions have no dependencies.
