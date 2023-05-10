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



