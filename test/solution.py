#открытие
def get_input():
    input_nk = []
    with open("input.txt", 'r') as file:
        for line in file:
            input_nk.append(int(line))

    return input_nk

#работа с цифрами,целочисленное деление,
def get_ten_degree(number):
    degree_ = 0
    while number != 0:
        number = number // 10
        degree_ += 1

    return degree_ - 1


def starts_with(number):
    return int(str(number)[0])

#упорядочение цифр,как в странной математике
def main():
    input_n, input_k = get_input()
    degree_n = get_ten_degree(input_n)
    degree_k = get_ten_degree(input_k)
    output = 0

    starts_n = starts_with(input_n)
    for i in range(1, starts_with(input_k)):
        if i < starts_n:
            output += int('1' * (degree_n + 1))
        elif i > starts_n:
            output += int('1' * degree_n)
        else:
            if degree_n != 0:
                output += int('1' * degree_n)
            output += input_n % (10 ** degree_n) + 1

    #подсчет + вывод в output
    if degree_k != 0:
        output += int('1' * degree_k)
    output += input_k % (10 ** degree_k) + 1

    print("Calculation completed successfully!")
    return output


if __name__ == "__main__":
    output_ = main()
    with open("output.txt", 'w') as f:
        f.write(str(output_))
