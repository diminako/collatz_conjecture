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

    print(list)
    return list

plt.title('Collatz Conjecture')
plt.ylabel('Range')
plt.xlabel('Amout of Calculations')

plt.plot(collatz_conjecture())
plt.show()
