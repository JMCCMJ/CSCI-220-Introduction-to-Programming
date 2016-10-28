def main():
    a = 3
    ans = (input("what is ans?" ))
    
    if ans == '':
        print("cheat")
        return False
    ans_num = int(ans)
    if ans_num == 3:
        print("yay")
    
    else:
        print('loser')
        
x = main()
print(x)
