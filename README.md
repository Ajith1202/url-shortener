# URL-Shortener
A simple url shortening service made using Django for both front-end and back-end (Using an algorithm which uses base 62 conversions for hashing) .

### ALGORITHM USED
The algorithm used in this project consists of 2 functions, namely **encode()** and **decode()** .
* **encode()**
  The purpose of the encode function is basically to take the input long URL, and shorten it .
  This can be achieved by using a 62-base system, i.e letters [a-z], [A-Z] and digits [0-9] .
  
  As soon as the user inputs the long URL, it is validated through a URL Validator built-in with Django, and then entered into the database with a unique ID associated with it.
  The **encode()** function takes this ID as input, and converts the same to a 62-base figure.( In my case, since I was using python, the 62-base figure was a list. )
  ```For eg: If the ID was 187, the 62-base figure corresponding to 187 would be [3, 1] .( This is achieved by the normal base-conversion method .)```
  It then maps each element of the 62-base figure into it's corresponding letter/digit in the 62-base system .
  ```For eg: In the above case, [3, 1] would be mapped to db .( Since 0 -> a, 1 -> b, 2 -> c ...26 -> z, 27 -> A ... 52 -> Z, 53 -> 0 ... 61 -> 9)```
  So, the **encode()** function returns the code. ( In this case, the code is 'db' .)
  
* **decode()** 
  The purpose of the decode function is simply to reverse the above process.
  ```For eg: In the above case, the encoded string is 'db'. The **decode()** function takes this encoded string as argument and returns the ID of the corresponding original URL```
  This is done by simply reverse-mapping the code to it's base-62 figure/list, and then converting that base-62 figure into it's decimal version( which is the required ID of the original URL .)
  
### EFFECTIVENESS OF THE ALGORITHM
  I used this algorithm since it incorporates and combines the processes of Hashing and Regex .
  Since this algorithm uses a base-62 conversion system, there could be as many as **560 Billion** unique possibilities for a code which is just **6 characters long!!!.**
  
