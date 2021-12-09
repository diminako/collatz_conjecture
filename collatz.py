#  Collatz Conjecture - Hailstone Numbers
import matplotlib.pyplot as plt

def collatz_conjecture():
    num = int(input("What number do you want to test out? "))
    list = [num]
    answer = num
    count = 0
    while answer != 1:
        count += 1
        if answer % 2 == 1:
            answer = 3 * answer + 1
        else:
            answer = int(answer / 2)
        list.append(answer)

    return list


plt.plot(collatz_conjecture())
plt.show()

# def create_x_axis(list):
#     x_axis_list = []
#     for x in range(0, len(list)):
#         x_axis_list.append(x)
#     return x_axis_list
# x_axis([1,2,3,4])
# collatz_conjecture(5)