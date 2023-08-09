def delete_element(element, lst):
    try:
        lst.remove(element)
    except ValueError:
        print("Element not found in the list")

def print_list(lst):
    print("List:", end=' ')
    for item in lst:
        print(item, end=' ')
    print()  # Print a newline at the end

def main():
    list_len = int(input("Enter the length of the list: "))
    my_list = []

    for i in range(list_len):
        while True:
            try:
                num = int(input(f"Enter the {i+1}{['st', 'nd', 'rd'][min(i, 2)] if i < 3 else 'th'} number: "))
                my_list.append(num)
                break
            except ValueError:
                print("Wrong input")

    print_list(my_list)

    to_delete = int(input("Enter the element to delete from the list: "))
    delete_element(to_delete, my_list)

    print_list(my_list)

if __name__ == "__main__":
    main()
    