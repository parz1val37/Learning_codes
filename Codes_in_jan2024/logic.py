# import random

# inputs = 100

# def odd_even():
#     player1 = []
#     player2 = []


#     for i in range(inputs):
#         player1.append(random.randint(1,5))
#         player2.append(random.randint(1,5))

#     odd_times = 0

#     for i in range(len(player1)):
#         if (player1[i] + player2[i]) % 2 == 1:
#             odd_times += 1
    
#     return odd_times

# result = []

# for i in range(5000):
#     result.append(odd_even())


# individual_result = []

# for i in range(len(result)):
#     individual_result.append((result[i]/inputs)*100)

# counter = 0
# for i in individual_result:
#     counter += i
    
# final_res = counter/len(individual_result)

# # print(f'Times iterated: {len(individual_result)} \n Attempts per input: {inputs} \n\n Probability of getting an odd number is: {final_res} \n\n Probability of getting an even number is: {100-final_res}')


# print(final_res)
