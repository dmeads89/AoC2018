## day 2 of advent of code but in python

fileinput = open("day2-input.txt", "r")

count_2times = 0
count_3times = 0

for line in fileinput:
    ## into the per line block

    matching_2times = False
    matching_3times = False

    for index_of_prime, prime_char in enumerate(line):
        ## so we are starting to loop over the chars in the line and holding th index of the item
        ## we will use the index of the item to remove itself from the new list

        transformed_line = line[:index_of_prime] + line[(index_of_prime + 1):]

        matching_chars = []

        for comparison_char in transformed_line:
            if comparison_char == prime_char:
                ## then we have a match
                previously_in_match = False

                print(f"{comparison_char} does match {prime_char}")

                for previously_matched_char in matching_chars:
                    if comparison_char == previously_matched_char['character']:
                        previously_matched_char['count'] += 1
                        previously_in_match = True

                        print(f"found matching char: comparison char: {comparison_char}, previously matched char: {previously_matched_char}")
                    
                    ## now we test to see if this is the first time this character has ever been matched

                if previously_in_match == False:
                    item = {
                        "character": comparison_char,
                        "count": 1
                    }

                    print(f"Adding first char to match: {comparison_char}")
                    
                    matching_chars.append(item)
        
        ## line should be evaluated now so need to check for occurence of 2s and 3s in dict count fields

        if matching_chars != []:
            print(f"printing matching chars: {matching_chars}")

        for item in matching_chars:
            if item['count'] == 2:
                matching_2times = True
            elif item['count'] == 3:
                matching_3times = True

    if matching_2times == True:
        count_2times += 1


    if matching_3times == True:
        count_3times += 1

checksum = count_2times * count_3times

print(f"Count for 2 times is: {count_2times}")

print(f"Count for 3 times is: {count_3times}")

print(f"Check sum is: {checksum}")


    


