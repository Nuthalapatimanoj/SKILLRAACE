def flames_game(name1, name2):
    # Function to remove matching characters
    def remove_match_char(list1, list2):
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    list1[i] = list2[j] = ''
                    return list1, list2
        return list1, list2
    
    # Function to count remaining characters
    def count_remaining_chars(name1, name2):
        list1 = list(name1.lower().replace(" ", ""))
        list2 = list(name2.lower().replace(" ", ""))
        proceed = True
        while proceed:
            list1, list2 = remove_match_char(list1, list2)
            if '' in list1:
                list1.remove('')
            if '' in list2:
                list2.remove('')
            if '' not in list1 and '' not in list2:
                proceed = False
        return len(list1) + len(list2)

    # Calculate the number of remaining characters
    count = count_remaining_chars(name1, name2)

    # FLAMES logic
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    # Determine relationship
    relationship = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }

    return relationship[flames[0]]

# User inputs
name1 = input("Enter the Name1:")
name2 = input("Enter the Name2:")
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
