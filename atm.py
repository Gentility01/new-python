code = '*606#'
enter_code = input('yello... enter your code: ')

if enter_code != code:
    print('invalid code for MTN')
else:
    borrow = int(input('enter the amount you want to borro: '))
    if borrow >=50 and borrow <=500:
        print(f' yellow you have borrowed {borrow}, succesfully')
    elif borrow <50:
        print('you cant borrw any amount bellow 50')
    elif borrow > 500:
        print(' you cant borrow more than 500')
    else:
        print('you cant so this')
    
    