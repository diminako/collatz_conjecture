#  Collatz Conjecture - Hailstone Numbers
def collatz_conjecture(num):
    if num == 1:
        print("the end of the loop is 1.")
    list = []
    answer = num
    count = 0
    while answer != 1:
        if answer % 2 == 1:
            answer = 3 * answer + 1
            count += 1
            list.append(answer)
        else:
            answer = answer / 2
            count += 1
            list.append(answer)

    plot_numbers(count, list)

def plot_numbers(count, list):
    print(f"Count: {count}")
    print(f"List: {list}")
    print(f"List: {len(list)}")


collatz_conjecture(137)