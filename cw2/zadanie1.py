zmienna=5.0
if isinstance(zmienna,int)==True:
    print("Zmienna jest typu wartości całkowitej")
if isinstance(zmienna,str)==True:
    print("Zmienna jest tekstem")
if isinstance(zmienna,float)==True:
    print("Zmienna jest typu wartości rzeczywistej")
    if zmienna.is_integer()==True:
        print("Zmienna jest wartością całkowitą")
    else:
        print("Zmienna jest wartością rzeczywistą")