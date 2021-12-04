"""
Author: RoyTheKing-WangXia
email: aiart9759@gmail.com
Last-time-modified: Sat 4 Dec., 12:50
No comments are provided, sorry for that.

To start the program, simply start it in command line by type in:

    python main.py

Be sure to put word.txt at the same directory with the main.py
"""


import random
def readInFile(file_path):
    fr = open(file_path, "r")
    lines = fr.readlines()
    word_list = []
    word_dict = dict()

    for line in lines:
        line_list = line.split(",")
        pre_index = len(word_list)
        for i in range(len(line_list)):
            line_list[i] = line_list[i].strip("\n")
            word_list.append(line_list[i])
            list_in_dict = []
            for j in range(len(line_list)):
                if j != i:
                    list_in_dict.append(j+pre_index)
            if line_list[i] not in word_dict:
                word_dict[line_list[i]] = list_in_dict
            else:
                for k in list_in_dict:
                    word_dict[line_list[i]].append(k)
    return word_dict, word_list

def wordTest(word_dict, word_list, word_number, round_number):
    for m in range(round_number):
        random_word_list = [""] * word_number
        random_index_list = [0] * word_number
        for i in range(word_number):
            random_index_list[i] = i
        for i in range(word_number):
            temp_index = random_index_list[i]
            random_index = random.randint(0, word_number-1)
            random_index_list[i] = random_index_list[random_index]
            random_index_list[random_index] = temp_index
        random_word_index_list = [0] * word_number
        for j in range(word_number-1):
            a = random.randint(0, len(word_list)-1)
            while a in random_word_index_list:
                a = random.randint(0, len(word_list)-1)
            random_word_index_list[j] = a
            random_word_list[random_index_list[j]] = word_list[random_word_index_list[j]]
        select_word_pair_list = word_dict[word_list[random_word_index_list[0]]]
        random_word_pair_choice = random.randint(0, len(select_word_pair_list)-1)
        random_word_list[random_index_list[word_number-1]] = word_list[select_word_pair_list[random_word_pair_choice]]
        correct_answer = [random_index_list[word_number-1], random_index_list[0]]
        print("*" * 10 + " round " + str(m+1) + " " + "*"*10)
        for i in range(word_number):
            print(str(i) + ": " + random_word_list[i])
        ans = input("Your Ans: ").split(",")
        if int(ans[0]) == correct_answer[0] and int(ans[1]) == correct_answer[1] or int(ans[1]) == correct_answer[0] and int(ans[0]) == correct_answer[1]:
            print("Correct !!!\n")
        else:
            print("Wrong !!!\nCorrect Answer: ", correct_answer)
            print()

if __name__ == '__main__':
    word_dict, word_list = readInFile("word.txt")
    # Indicate the number of words in a set you want to test yourself (such as: 6)
    # Indicate the number of rounds you want to test yourself (scuh as: 10)
    wordTest(word_dict, word_list, 6, 10)