# eratosthenes
A collection of Python functions that deal with prime numbers using the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) and other algorithms.
## functions and what they do
```
eratosthenes(num, file) -> list/file
```
Takes an integer **num** and a single string filename **file** and prints all the prime numbers from 2 to num to file, while also returning them in list form.
In the file, the numbers are one per line, while in the return statement/stdout, the primes are in a list consisting of the prime integers found.
Due to speed and memory requirements, this function is deprecated. Use eratosthenesbool where possible.
```
eratosthenesbool(num, file:str/list[str], debug) -> list/file(s)
```
Takes the same arguments as eratosthenes, with an additional boolean **debug** that can be used to view execution time and the number of primes in the output file.
This function does the same thing as eratosthenes, with the following differences:
1. The function can write to multiple files by passing a list containing string filenames to file, dividing the primes evenly among them. For example, with a prime # list of length 1000, the function can write 250 prime #s to each of 4 files.
2. The prime number list the function returns contains boolean values instead of integers, reducing memory usage and execution time drastically.
```
find_prime(num, length)
```
Writes the first **length** primes to a file called 'test.txt'. Returns the **num**th prime if it occurs within the calculated values. If it does not occur, the function throws an exception.
```
isPrime(num)
```
Takes a positive integer for num and returns True if that integer is prime. Otherwise, returns False.
