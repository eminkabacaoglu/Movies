# match case 3.10 sürümüyle geldi
quit_flag = 8
match quit_flag:
    case 1:
        print("Quitting")
        exit()
    case 2:
        print("System is on 2")
        exit()
    case 3:
        print("System is on 3")
        exit()  
    case _:
        print("hiççççç")
        exit()