from itertools import combinations

file_name="puzzle.txt"
f_lines=[]

fH=open(file_name)
f_lines=fH.readlines()
fH.close()

total_press = 0

for line in f_lines:
    line = line.strip()
    lineP = line.split(' ')
    # Obstain the INPUT data from the lines
    str_L=""
    lst_B=[]
    lst_J=[]
    # For each line:
    # Split using space i.e. ' '
    #  - First part -> lights string (except '[' in front and ']' at back)
    #  - Middle string -> buttons (each having '(' in front and ')' at back)
    #    - needing str -> int conversion 
    #  - Last part us the JOLTAGE string (except '{' in front and '}' at back)
    lineL = lineP[0]
    lineB = lineP[1:-1] # string with all buttons
    lineJ = lineP[-1][1:-1]
    # Get the light string : TARGET light state
    str_L = lineL[1:-1]
    # Get all the buttons as list-of-int
    for str_b in lineB:
        #str_b = str_b[1:-1] # remove '(' and ')'
        #int_b = [int(s) for s in str_b.split(',')]
        lst_B.append(str_b) #int_b)
    # Get all Joltage
    lst_J=[int(s) for s in lineJ.split(',')]

    print("Testing for light status:" + str_L)
    def check_target_lights_str_using_buttons_comb(lst_b_comb):
        is_matched = 0

        for b_comb in lst_b_comb:
            str_r = "\nLight from buttons " + str(b_comb) + " :"
            # create the init light_dict to initialize before each button press
            light_dict={} 
            for r in range(len(str_L)):
                light_dict[r] = '.'
            for b_string in b_comb:
                button_w_connections = [int(s) for s in b_string[1:-1].split(',')]
                for connection in button_w_connections:
                    if light_dict[connection] == '#':
                        light_dict[connection] = '.'
                    else:
                        light_dict[connection] = '#'
            light_str = ""
            for k,c in light_dict.items():
                light_str += c
            str_r += light_str + ":"
            if light_str == str_L:
                is_matched = 1
                str_r += "Matched"
                break
            else:
                str_r += "UnMatched"
                pass
            #print('\t' + str_r)
        return is_matched
    def get_min_pressed_buttons_for_light_state():
        # create the possible combinations of the buttons
        # Each combination input will have one or more of the switches
        # So iterate of the the list of switches using the 
        
        r_pressed = 0
        # iterate for each possible combinations with  one, two, thee ... to all buttons
        for r in range(1, len(lst_B) + 1):
            # combination of 'r' buttons (from 1 to all) ; break when target reached
            r_pressed = r
            buttons_comb = list(combinations(lst_B, r))
            if check_target_lights_str_using_buttons_comb(buttons_comb):
                break
        print("Min Press for line:",r_pressed)
        return r_pressed

    total_press += get_min_pressed_buttons_for_light_state()
    print("\n\nTOTAL PRES:", total_press)
