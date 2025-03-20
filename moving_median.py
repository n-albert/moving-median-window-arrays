def ArrayChallenge(arr):
  window_size = arr[0]
  data = arr[1:]
  medians = [] # empty list

  temp_list = []

  for i in range(1, len(arr)):
    if i < window_size:
      window = arr[1:i+1]
    else:
      window = arr[i-window_size+1:i+1]

    window.sort()

    # calculate median of list of numbers
    if len(window) % 2 == 0:
      median = (window[len(window)//2 - 1] + window[len(window)//2]) / 2
    else:
      median = window[len(window)//2]


    medians.append(int(median))


  # code goes here
  return ",".join(str(x) for x in medians)

test_cases = [[3, 1, 3, 5, 10, 6, 4, 3, 1],
              [8, 51, 3, 9],
              [6, 7, 8, 9, 1, 6, 5, 3]]

for test_case in test_cases:
    print("For the input array: ", test_case)
    print("The corresponding moving median array is: ", ArrayChallenge(test_case))

# keep this function call here if interested in user input
# print(ArrayChallenge(input()))