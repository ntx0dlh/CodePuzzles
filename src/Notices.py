"""
This coding puzzle was given to me by HackerRank.
(https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem)

The problem asks someone to write a function that will notify a customer whenever there is an expense that exceeds
double the median of the last d expenditures.
"""

def get_median(freq_arr: list[int], middle: int, middle2: int = None) -> list[float]:
    """
    Determines the median of a frequency array.  The median is the middle number.  If there are two middle numbers, the
    median is the average of both.
    :param freq_arr: A list of integers, each one represents an expenditure.
    :param middle: integer that represents the number of previous days to look back on, and determine the median.
    :param middle2: [Optional] integer that represents the second median, if the array has an even number of members.
    :return: a list of 2 integers.  Both will only hold a value is the array has an even number of members.  If it has
    an odd number of members, only the first value will contain a number.  It will return either [int, int] or
    [int, None].
    """
    med = 0
    med2 = 0
    count = -1
    count2 = -1
    if not middle2:  # Odd number of members in the array
        for i in range(len(freq_arr)):
            med += freq_arr[i]
            count += 1
            if med >= middle:
                break
    else:  # Even number of members in the array
        for i in range(len(freq_arr)):
            med += freq_arr[i]
            med2 += freq_arr[i]
            count += 1
            count2 += 1
            """
            Sometimes the two median values will be the same number, and sometimes they will not.  So, once the first
            median is found, the loop has to keep going to find the second one.
            """
            if med >= middle:
                for j in range(i + 1, len(freq_arr)):
                    if med2 >= middle2:
                        break  # break j loop
                    med2 += freq_arr[j]
                    count2 += 1
                break  # break i loop
    return [count, count2]


def activityNotifications(expenditure: list[int], d: int) -> int:
    """
    This function is designed to notify a customer if an expenditure is more than double the median of the "d" days
    prior.
    :param expenditure: A list of integers, each one represents an expenditure.
    :param d: integer that represents the number of previous days to look back on, and determine the median.
    :return: Returns and integer that represents the count of notices that was sent to the customer throughout the
    traversal of the expenditure list.
    """
    notices = 0
    ln = len(expenditure)
    if ln == 0:  # If there are no expenditures, there are no notices.
        return notices
    if d == ln:  # If d is the same as the length of the list of expenditures, there is no way to compare.
        print("d == len(expenditure), d: {d}, Exp: {expenditure}")
        return notices
    even_odd = 0 if d % 2 == 0 else 1
    middle = d // 2  # integer math
    """
    Setting up a frequency array to count how many times each number appears in the appears in the expenditure array, 
    from 0 to d-1.  The maximum any expenditure can be is $200, so the frequency array need only contain 201 members 
    (including zero). 
    """
    freq_arr = [0] * 201
    for exp in expenditure[:d]:
        freq_arr[exp] += 1

    with open('/Users/davidhill/PycharmProjects/CodingPuzzles/CodePuzzles/src/noticeOutput.txt', 'w') as file:
        for i in range(d, ln):
            if expenditure[i] > 0:  # An expenditure = zero will never return a notice.
                if even_odd == 0:  # If length of d is an even number
                    med = get_median(freq_arr, middle, middle + 1)
                    median = (med[0] + med[1]) / 2
                else:  # If length of d is an odd number
                    median = get_median(freq_arr, middle + 1)[0]
                notices += 1 if expenditure[i] >= median * 2 else 0

            # Update the frequency array.
            freq_arr[expenditure[(i - d)]] -= 1
            freq_arr[expenditure[i]] += 1

            file.write(f"i: {i}, d: {d}, exp[i]: {expenditure[i]}, median: {median}, notices: {notices}, added: "
                       f"{expenditure[i]},removed: {expenditure[(i - d)]}, expenditure: "
                       f"{str(expenditure[i-d: i-d+5]).replace(",", " ")}..."
                       f"{str(expenditure[i-5: i]).replace(",", " ")}\n")
    return notices


if __name__ == '__main__':
    file = open('/Users/davidhill/PycharmProjects/CodingPuzzles/CodePuzzles/src/noticeInput.txt', 'r')
    first_multiple_input = file.readline().split(' ')
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, file.readline().split()))
    result = activityNotifications(expenditure, d)
    print(str(result) + '\n')
