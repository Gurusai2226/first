linked_list = []
n = int(input("Enter number of elements in the list: "))
for _ in range(n):
    val = int(input("Enter element: "))
    linked_list.append(val)
def add_window(arr, start, end):
    return sum(arr[start:end])
def multiply_window(arr, start, end):
    product = 1
    for i in range(start, end):
        product *= arr[i]
    return product
window_size = int(input("Enter window size: "))
for i in range(len(linked_list) - window_size + 1):
    window_sum = add_window(linked_list, i, i + window_size)
    window_product = multiply_window(linked_list, i, i + window_size)
    print(f"Window elements: {linked_list[i:i+window_size]}")
    print(f"Sum: {window_sum}, Product: {window_product}")
    print("---")
