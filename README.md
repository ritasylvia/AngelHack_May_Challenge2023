# AngelHack_May_Challenge2023
Monthly Code Challenge for AngelHack
# Challenge1:

John was visiting a friend one day who lived in an apartment, but the instructions that he
received were a bit confusing. When he arrives, he starts on the ground floor (floor 0) and
has to follow the instructions one character at a time.
A left arrow (<) means going up one floor, and a right arrow (>) means going down one floor

Which floor did he end up on?

## Solution:
#### Answer = 56
![image](https://user-images.githubusercontent.com/95111839/236300038-37687d0c-1888-44df-81a9-26fa9e0df26a.png)


# Challenge2:
### Who’s the fastest runner? (1 mark)
A group of friends wanted to know who is the fastest amongst them, and
decided to hold a running race.
It wasn’t fun just running, so they decided to go for a marathon. These guys are good, but
must rest occasionally to recover their energy.
Did I mention that these people are weird? They can only be running (always at their top
speed), or resting (not moving at all), and can only spend integer amounts of time in either
state.
Example case:
John can run 10 m/s for 6 seconds, but then must rest for 20 seconds
James can run 8 m/s for 8 seconds, but then must rest for 25 seconds
 In this case, John would have won if the race ended at 100 seconds.
Here are the descriptions of this group of friends:
1) John can run 10 m/s for 6 seconds, but then must rest for 20 seconds
2) James can run 8 m/s for 8 seconds, but then must rest for 25 seconds
3) Jenna can run 12 m/s for 5 seconds, but then must rest for 16 seconds
4) Josh can run 7 m/s for 7 seconds, but then must rest for 23 seconds
5) Jacob can run 9 m/s for 4 seconds, but then must rest for 32 seconds
6) Jerry can run 5 m/s for 9 seconds, but then must rest for 18 seconds
After 1234 seconds, what is the distance of the winning runner?

##Solution:
#### Answer = Jenna: 3540m
![image](https://user-images.githubusercontent.com/95111839/236635363-de105379-dbad-4c1d-a778-edcfdea3a913.png)

![image](https://user-images.githubusercontent.com/95111839/236635316-ee346646-11df-4148-83a5-d48d4b9c815b.png)

# Challenge3:
Given an integer string, create all integer permutations of its digits. Determine if there is a
permutation whose integer value is evenly divisible by 7, i.e. (permutation value) mod 7 = 0.
For example, the possible permutations of 789 are p = {789, 798, 879, 897, 978, 987}. Of
these values, p[1] and p[5] is divisible by 7 because 879 mod 7 = 0 and 987 mod 7 = 0.
Their average is (798 + 987) / 2 = 892.5
What you’ll need to do is determine if any of the permutations of 1867 are divisible by 7, and
if so, what is the average between the smallest and largest permutation? Decimals are
allowed.

## Solution
#### Answer = 5152.0
![image](https://user-images.githubusercontent.com/95111839/236912831-99f93a49-1be9-45a1-b47b-30447137c111.png)

![image](https://user-images.githubusercontent.com/95111839/236912365-36c71026-a964-4592-90c1-a6b4e741c3ab.png)

# Challenge4:
A group of workers gathered to complete a task. Each worker has an efficiency rating. They will be grouped in pairs so an even number of workers are required. The cost of a pair is the absolute difference of the efficiencies assigned to the workers. The cost of the task is the
sum of the costs of all pairs formed. There are an odd number of workers to choose from, so one worker will not be paired. Select the worker to exclude so the task's cost is minimized. Given n workers and efficiency for each worker, find a configuration of the workers such that the cost of the task is the minimum possible. Return the minimum cost as the answer. 
First Example
Efficiency = [1, 2, 4]
The first worker has an efficiency of 1, the second worker has an efficiency of 2, and the last worker has an efficiency of 4. If we excluded the first worker (1) and pair the second (2) and last worker (4), the cost is |2 -4| = 2 If we excluded the second worker (2), and pair the first and last worker instead, the cost is |1- 4| = 3. If we excluded the last worker (4), the cost is |1 - 2| = 1
Thus, the minimum cost is 1.

Task
What is the minimum cost of this array of efficiencies:
[1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

## Solution
#### Answer = 475
![image](https://github.com/ritasylvia/AngelHack_May_Challenge2023/assets/95111839/98cb0032-6849-4122-845f-9560e907e3e0)
![image](https://github.com/ritasylvia/AngelHack_May_Challenge2023/assets/95111839/6f544412-8bbb-48a4-b347-938b5deabfc5)

# Challenge5:
You are tasked with designing a variable-length decoding algorithm for a given set of bit strings.A variable-length code is an encoding mechanism where each symbol can be represented by a number of bits that varies from symbol to symbol.For example, 'a' could be epresented by '01', 'b' by '01', 'c' by '10', etc. This kind of encoding is useful in situations where some symbols appear more frequently than others, and hence, it makes sense to assign fewer bits to more frequent symbols. 
Your task is to write a function
decode(encoded: str, codebook: Dict[str, str]) -> str
which takes an encoded string and a codebook, and returns the original string. The function
should return an error if the encoded string is not a valid encoding according to the
codebook.
Let's consider this codebook:
{'a': '00',
'b': '01',
'c': '10',
'd': '1100',
'e': '1101',
'f': '1110',
'g': '111100',
'h': '111101',
'i': '111110',
'j': '1111110000',
'k': '1111110001',
'l': '1111110010',
'm': '1111110011',
'n': '1111110100',
'o': '1111110101',
'p': '1111110110',
'q': '1111110111',
'r': '1111111000',
's': '1111111001',
't': '1111111010',
'u': '1111111011',
'v': '1111111100',
'w': '1111111101',
'x': '1111111110',
'y': '1111111111',
'z': '11111111110000',
' ': '11111111110001'}
Example
decode('0110', codebook) should return 'bc'.
What is the decoded phrase for this string?
“11111011111111110001111111001011111101011111111100110111111111110001001111110100111100110111111100101111010010111111000111111111110001101111110101110011011111111111000110111101001111110010111111001011011111110100111100110111111111110001011101100011111110111111111001110111111111110001111110111111101011111111110001111110111111100111111111110001111011111110111111110100111111111100010011111101001100111111111100011101111111111010111110111111101011111011111101001111001111111111000100111111010011001111111111000111111011111111110001110011111011111110011111110010111110111111000111011111111111000111111110101111011101111111111100011111111101111111010111111110001100111111111100011111111111000111111111110001111111101011110100111111101011111111110001001111110110111111011011010011111110001111111001111111111100011111101111110100111111111100011111111010111101110111111111110001111111011011110111111110000011111110011101”
P.S. Use your best judgement to get the proper final answer - the answer should make
sense and be readable!

## Solution
I sort the codebook in descending order such that longer pairs are accounted for first before shorther pairs. With this, ' ' is seleced on the iteration befor 'yab'. When I had recurring space, I replaced the middle space with 'yab' 
#### Answer: i love angelhack code challenge because it is fun and exciting and i dislike the word yab that appears in the phrase
![image](https://github.com/ritasylvia/AngelHack_May_Challenge2023/assets/95111839/f100f4b7-1dfb-4d88-bf79-4a0d7d10e37f)
![image](https://github.com/ritasylvia/AngelHack_May_Challenge2023/assets/95111839/49d9a1bc-0196-4864-bfc4-667f33f54932)


# Challenge5:
Question 6: How many steps are needed to disconnect the string? (5marks)
A secure communication network has been compromised and the cyber security team must restore its security. The network, series, is represented as a series of nodes identified using lowercase English letters. The nodes must be disconnected in order to remove the threat. In a single operation, any number of adjacent nodes identified by the same character can be disconnected. Find the minimum number of operations required to disconnect all the nodes and secure the network.
Example
Suppose we have a series that goes "aabbaa". To remove the string entirely, you’d first have to get rid of “bb” to get “aaaa” and then you can remove “aaaa”. You can remove the first “aa” to get “bbaa” but it means you’d need to spend another two moves to remove “bb” and then “aa”. In this case, the minimum number of moves required to delete the entire series is 2.
Another example
Suppose we have another series that goes “aabbbcccaacccaa”. What’s the minimum number of moves required for this? You can remove the middle “aa” first to get “aabbbccccccaa” and then remove “cccccc” to get “aabbbaa”, and then you remove the “bbb” and subsequently “aaaa” to delete the entire series. 
Boom, 4 moves.

What is the minimum number of steps required to delete this series:
“kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor

## Solution
#### Answer: 90
![image](https://github.com/ritasylvia/AngelHack_May_Challenge2023/assets/95111839/88f1d643-6ad8-41f3-bd5e-38d8e773fcb8)

![image](https://github.com/ritasylvia/AngelHack_May_Challenge2023/assets/95111839/6225d815-5ca4-4fb4-956b-eccfaba00bc8)




