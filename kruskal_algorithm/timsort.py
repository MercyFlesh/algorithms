def _insert_sort(data, vert_edge):
	for i in range(1, len(data)):
		j = i - 1 
		temp = data[i]
		while data[j][vert_edge] > temp[vert_edge] and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = temp

	return data


def _merge_sort(left_arr, right_arr, vert_edge):
    merge_arr = []

    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0][vert_edge] < right_arr[0][vert_edge]:
            merge_arr.append(left_arr[0])
            left_arr = left_arr[1:]
        else:
            merge_arr.append(right_arr[0])
            right_arr = right_arr[1:]

    for i in range(len(left_arr)):
        merge_arr.append(left_arr[i])
       

    for j in range(len(right_arr)):
        merge_arr.append(right_arr[j])

    return merge_arr


def _minRunLength(n):
   flag = 0
   while (n >= 64):
     flag |= n & 1
     n >>= 1
   return n + flag


def Timsort(data, vert_edge):
    min_run = _minRunLength(len(data))
    
    if len(data) > 0:
        for i in range(0, len(data), min_run):
            data[i:i + min_run] =  _insert_sort(data[i:i + min_run], vert_edge)

        run = min_run

        while run < len(data):
            for i in range(0, len(data), run * 2):
                data[i : i + 2 * run] = _merge_sort(data[i: i + run], data[i + run: i + (run * 2)], vert_edge)
            run *= 2
    
    return data

