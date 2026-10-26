if __name__ == " __main__ ":
    print (" Converter \n")
    print ("(1) Unidades metricas" ) 
    print ("(2) Unidades volumetricas ")

    op1 = int( input ("> "))

    if op1 == 1:
        print (" (1) mm- >km , (2) km - >mm")
        op2 = int ( input ("> "))
        
        if op2 == 1:
            x = float ( input ("mm = "))
            print (f"km = {x /1000} ")

        else :
            x = float ( input ("km = "))
            print (f"mm = {x *1000} ")

    elif op1 == 2:
            print (" Por implementar ")

    else :
            print ("Opção incorreta ")