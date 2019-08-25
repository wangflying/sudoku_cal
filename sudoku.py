import sys

data_init1 = [
    9, 0, 0, 2, 7, 8, 1, 0, 0,
    0, 0, 1, 0, 3, 0, 2, 4, 9,
    0, 0, 3, 0, 0, 0, 0, 0, 0,
    0, 3, 0, 8, 0, 0, 0, 0, 0,
    0, 0, 7, 0, 0, 0, 5, 0, 0,
    0, 0, 0, 0, 0, 4, 0, 3, 0,
    0, 0, 0, 0, 0, 0, 3, 0, 0,
    5, 7, 8, 0, 4, 0, 9, 0, 0,
    0, 0, 4, 5, 1, 6, 0, 0, 7
]
data_init = [
    0,0,6,0,0,7,0,0,9,
    8,0,0,0,3,0,1,0,0,
    9,0,0,6,0,5,0,3,0,
    0,0,3,0,0,0,0,1,8,
    0,0,0,9,0,1,0,0,0,
    2,1,0,0,0,0,6,0,0,
    0,6,0,7,0,3,0,0,1,
    0,0,9,0,2,0,0,0,4,
    7,0,0,8,0,0,5,0,0
]
modify_flag = False


def print_data_init():
    global data_init
    for j in range(0,81):
        sys.stdout.write(str(data_init[j]))
        if (j+1) % 27 == 0:
            print('\n')
        elif (j+1) % 9 == 0:
            print('')
        elif (j+1) % 3 == 0:
            sys.stdout.write('\t')
        else:
            sys.stdout.write(' ')

def select_set(i):
    global data_init
    global modify_flag
    # print(i)
    if data_init[i] != 0:
        return [data_init[i]]
    tmp_list = []
    tmp_list2 = []
    base_pos = i/9 * 9
    for k in range(0,9):
        pos = base_pos + k
        if i != pos and data_init[pos] != 0:
            tmp_list.append(data_init[pos])
    base_pos = i%9
    for k in range(0, 9):
        pos = 9*k + base_pos
        if i != pos and data_init[pos] != 0:
            tmp_list.append(data_init[pos])
    for k in range(0,9):
        pos = i/9/3*9*3 + i%9/3*3 + k/3*9 + k%3
        if i != pos and data_init[pos] != 0:
            tmp_list.append(data_init[pos])
    # print(tmp_list)
    for j in range(1,10):
        if j not in tmp_list:
            tmp_list2.append(j)
            
    if len(tmp_list2) == 1:
        data_init[i] = tmp_list2[0]
        # print_data_init
        modify_flag = True
        return [data_init[i]]
    elif len(tmp_list2) == 0:
        print("error1")
        return []
    else:
        return tmp_list2

def sort_one():
    global modify_flag
    global data_init
    modify_flag = False
    for i in range(0, 81):
        if data_init[i] != 0:
            continue
        
        can_selected = select_set(i)
        if len(can_selected) == 1:
            continue
        elif len(can_selected) == 0:
            print('error2')
            return 1
        else:
            for data in can_selected:
                other_select = False
                for k in range(0, 9):
                    pos = i/9/3*9*3 + i%9/3*3 + k/3*9 + k%3
                    if i != pos: # and data_init[pos] == 0:
                        other_avai_set = select_set(pos)
                        if data in other_avai_set:
                            other_select = True
                            break
                if other_select == False:
                    data_init[i] = data
                    # print('xxx:')
                    # print_data_init()
                    modify_flag = True
                    break
        #print(data_init)
    # print("after one iteration:")
    # print_data_init()
    
def fill():
    global data_init
    global modify_flag
    print_data_init()
    modify_flag = True
    while(0 in data_init):
       if modify_flag == True:
           sort_one() 
       else:
           print('donot do')
           print_data_init()
           exit(1)
    print('finish')
    print_data_init()

    
fill()