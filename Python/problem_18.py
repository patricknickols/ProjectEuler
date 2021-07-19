triangle ='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

rows = triangle.split("\n")
for i in range(len(rows)):
    rows[i] = rows[i].split(" ")
    for j in range(len(rows[i])):
        rows[i][j] = int(rows[i][j])

def previous_reachable(start_row, start_index):
    if start_index > 0 and start_index < start_row:
        return ((start_row - 1, start_index), (start_row - 1, start_index - 1))
    elif start_index == 0:
        return (None, (start_row - 1, start_index))
    elif start_index == start_row:
        return ((start_row - 1, start_index - 1), None)

pre_computed = {(0,0) : 75}

def max_going_up(row_number, row_index):
    if (row_number, row_index) in pre_computed:
        return pre_computed[(row_number, row_index)]
    else:
        option_1 = previous_reachable(row_number, row_index)[0]
        option_2 = previous_reachable(row_number, row_index)[1]
        if option_1 is None:
            answer = rows[row_number][row_index] + max_going_up(option_2[0], option_2[1])
        elif option_2 is None:
            answer = rows[row_number][row_index] + max_going_up(option_1[0], option_1[1])
        else:
            answer = rows[row_number][row_index] + max(max_going_up(option_1[0], option_1[1]), max_going_up(option_2[0], option_2[1]))
        pre_computed[(row_number, row_index)] = answer
        return answer

def main():
    max_so_far = 0
    for index in range(len(rows[14])):
        max_so_far = max(max_so_far, max_going_up(14, index))
    print(max_so_far)

if __name__ == "__main__":
    main()
