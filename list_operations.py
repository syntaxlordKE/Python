def main():
    # Step 1: Create an empty list
    my_list = []

    # Step 2: Append elements 10, 20, 30, 40
    my_list.extend([10, 20, 30, 40])
    print("After appending: ", my_list)

    # Step 3: Insert 15 at the 2nd position (index 1)
    my_list.insert(1, 15)
    print("After inserting 15: ", my_list)

    # Step 4: Extend with [50, 60, 70]
    my_list.extend([50, 60, 70])
    print("After extending: ", my_list)

    # Step 5: Remove the last element
    my_list.pop()
    print("After removing last element: ", my_list)

    # Step 6: Sort in ascending order
    my_list.sort()
    print("After sorting: ", my_list)

    # Step 7: Find index of 30
    index_30 = my_list.index(30)
    print("The index of 30 is:", index_30)

if __name__ == "__main__":
    main()
