import fileinput
from typing import List


def main():
    for line in fileinput.input():

        image: List[str] = ['2'] * 150

        for i in range(0, len(line), 150):
            layer = line[i: i + 150]

            for j in range(150):
                if image[j] == '2':
                    image[j] = layer[j]

        for i in range(0, len(image), 25):
            row = image[i: i + 25]
            print("".join(row).replace('0', ' ').replace('1', '▮'))


if __name__ == '__main__':
    main()
