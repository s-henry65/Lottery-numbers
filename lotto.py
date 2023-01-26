import random

again = 'y'
while again == 'y':
    print('\nA) Generate random numbers')
    print('B) Test your numbers')
    print('C) Quit')
    game = (input('\nSelection: '))

    # GENERATE RANDOM NUMBERS
    if game == 'a' or game == 'A':
        num_dict = {}
        draw_count = 1
        numbers = int(input('\nEnter the amount of numbers: '))
        draw = int(input('\nEnter the number of draws: '))
        print()
        print('Results')
        while draw_count <= draw:
            counter = 1
            num_draw = []
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48 ]
            while counter <= numbers:
                pick = (random.choice(nums))
                num_dict[pick] = num_dict.get(pick, 0) + 1
                num_draw.append(pick)
                nums.remove(pick)
                counter += 1
            print(f'Draw {draw_count} ',sorted(num_draw))
            draw_count += 1
        sorted_values = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
        sorted_keys = sorted(num_dict.items(), key=lambda x:x[0])
        print('\nSorted by times drawn (number, draws)')
        print(sorted_values)
        print('\nSorted by number (number, draws)')
        print(sorted(sorted_keys))
        again = input('\nPlay again? (y or n): ')

    # TEST USER NUMBER
    elif game == 'B' or game == 'b':
        match_count = 0
        pick3 = 0
        pick4 = 0
        pick5 = 0
        pick6 = 0
        num_pick = []
        num_pick = [int(x) for x in input('\nEnter six numbers (1-49): ').split()]
        num_dict = {}
        draw_count = 1
        draw = int(input('\nEnter the number of draws: '))
        match_num = int(input('\nEnter the amount of number matches to show (1-6): '))
        print()
        while draw_count <= draw:
            counter = 1
            num_draw = []
            num_match = []
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48 ]
            while counter <= 6:
                pick = (random.choice(nums))
                num_dict[pick] = num_dict.get(pick, 0) + 1
                num_draw.append(pick)
                for num in num_pick:
                    if num == pick:
                        num_match.append(pick)
                nums.remove(pick)
                counter += 1
            if len(num_match) == 3:
                pick3 += 1
            if len(num_match) == 4:
                pick4 += 1
            if len(num_match) == 5:
                pick5 += 1
            if len(num_match) == 6:
                pick6 += 1
            if len(num_match) >= match_num:
                match_count += 1
                print(f'\nDraw {draw_count} ',sorted(num_draw))
                print(len(num_match), 'Match: ' ,sorted(num_match))
                
            draw_count += 1
        sorted_values = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
        sorted_keys = sorted(num_dict.items(), key=lambda x:x[0])
        print()
        print(match_count, 'Total Matches ', pick3,'3-Matches ', pick4,'4-Matches ', pick5,'5-Matches ', pick6,'6-Matches')
        print('\nSorted by times drawn (number, draws)')
        print(sorted_values)
        print('\nSorted by number (number, draws)')
        print(sorted(sorted_keys))
        again = input('\nPlay again? (y or n): ')
    else:
        break 
print('\nGood Bye')