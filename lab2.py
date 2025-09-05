# Q1
# L = [11,12,13,14]
# (i)
# L.extend([50,60])
# print("After adding 50 and 60:",L)
# (ii)
# L.remove(11)
# L.remove(13)
# print("After removing 11 and 13:",L)
# (iii)
# L.sort()
# print("Sorted ascending:",L)
# (iv)
# L.sort(reverse=True)
# print("Sorted descending:",L)
# (v)
# print("Is 13 in list?", 13 in L)
# (vi)
# print("Length of list:",len(L))
# (vii)
# print("Sum of elements:",sum(L))
# (viii)
# print("Sum of odd numbers:", sum(x for x in L if x % 2 != 0))
# (ix)
# print("Sum of even numbers:",sum(x for x in L if x % 2 == 0))
# (x)
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0: return False
#     return True
# print("Sum of prime numbers:",sum(x for x in L if is_prime(x)))
# (xi)
# L.clear()
# print("After clearing:",L)
# (xii)
# del L


# Q2
# list = [11,24,69,78,52]
# total = 0
# for i in list:
#     total += i
# print("Final sum:",total)


# Q3
# list = [1,2,3,4,5]
# product = 1
# for i in list:
#     product *= i
# print("Product:",product)


# Q4
# arr= [[[ '*' for i in range(6)] for i in range(4)] for i in range(3)]
# print("Array:",arr)


# Q5
# D = {1:5.6,2:7.8,3:6.6,4:8.7,5:7.7}
# print("Initial dictionary:",D)
# (i)
# D[8] = 8.8
# print("After adding key 8:",D)
# (ii)
# D.pop(2)
# print("After removing key 2:",D)
# (iii)
# print("Is key 6 present?",6 in D)
# (iv)
# print("Length of dictionary:", len(D))
# (v)
# print("Sum of values:",sum(D.values()))
# (vi)
# D[3] = 7.1
# print("After updating key 3:",D)
# (vii)
# D.clear()
# print("After clearing:",D)


# Q6
# S1 = {10, 20, 30, 40, 50, 60}
# S2 = {40, 50, 60, 70, 80, 90}
# print("Initial S1:", S1)
# print("Initial S2:", S2)
# (i)
# S1.update([55, 66])
# print("After adding 55 and 66 to S1:",S1)
# (ii) 
# S1.discard(10)
# S1.discard(30)
# print("After removing 10 and 30 from S1:",S1)
# (iii) 
# print("Is 40 in S1?", 40 in S1)
# (iv) 
# union_set = S1.union(S2)
# print("Union of S1 and S2:", union_set)
# (v)
# intersection_set = S1.intersection(S2)
# print("Intersection of S1 and S2:", intersection_set)
# (vi)
# difference_set = S1.difference(S2)
# print("Difference of S1 and S2:", difference_set)


# Q7
# (i)
# import random
# import string
# print("100 Random Strings (Length 6-8):")
# for i in range(100):
#     length = random.randint(6,8)
#     rand_str = ''.join(random.choices(string.ascii_letters, k=length))
#     print(rand_str)
# (ii)
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print("Prime Numbers Between 600 and 800:")
# for num in range(600, 801):
#     if is_prime(num):
#         print(num)
# (iii)
# print("\nNumbers divisible by 7 and 9 between 100 and 1000:")
# for num in range(100, 1001):
#     if num % 7 == 0 and num % 9 == 0:
#         print(num)


# Q8
# exam_st_date = (11,12,2025)
# print(f"The examination will start from: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")


# Q9
# numbers = [10,23,45,66,75]
# for num in numbers:
#     if num % 5 == 0:
#         print("Numbers divisible by 5:",num)


# Q10
# num = int(input("Enter a number:"))
# is_even = num % 2 == 0
# print(f"The number {num} is", "Even" if is_even else "Odd")


# Q11
# sentence = "Emma is a good student. Emma writes clean code. Emma loves Python."
# word = "Emma"
# count = sentence.count(word)
# print(f"\nThe word '{word}' appears {count} times in the sentence.")


# Q12
# list1 = [1, 3, 5, 6, 8]
# list2 = [2, 4, 7, 9, 12]
# new_list = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
# print("New list with odd from list1 and even from list2:",new_list)


# Q13
# positions = [(2,3),(4,5),(6,7),(7,8)]
# even_positions = [pos for pos in positions if pos[0] % 2 == 0]
# print("Positions where the x-coordinate is even:",even_positions)

# Q14
# sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
# high_readings = [id for id, val in sensor_data.items() if val > 3.0]
# print("Sensor ID's>3.0:",high_readings)


# Q15
# commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
# commands_executed = {"MOVE", "TURN_LEFT", "STOP"}
# not_executed = commands_received - commands_executed
# print("Commands not executed",not_executed)

