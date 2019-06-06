#This Code Was Created By Utkarsh Yadav on 
#         29th March 2017 at 22:49 IST
# this code uses a function to convert numbers into text
# feel free to report any bugs or request some additions
# you are allowed to modify the code and use in your projects
# untill this header is not removed
# this program has limitations as it can only translate to an extent
# it can translate upto (10^64 -1) 


def num2text(dat):
    
    #input inspection
    #added support for -ve numbers &added limit 31 jan 2018 23:13

    if(dat>pow(10,64)-1):
        print ("Input Out of range")
        exit()
    elif(dat<0):
        print ("Invalid Input \n converting to positive number")
        dat=dat*(-1)
    
    #default declaration  in case they are not used and are needed to print
    quintillion=""
    quadrillion=""
    sextillion=""
    septillion=""
    octillion =""
    nonillion =""
    decillion =""
    undecillion =""
    duodecillion =""
    tredecillion =""
    quattuordecillion =""
    quindecillion =""
    sexdecillion =""
    septemdecillion =""
    octodecillion =""
    novemdecillion =""
    vigintillion=""
    billions = ""
    trillions =""
    millions = ""
    thousands=""
    hundreds=""
    tens=""
    units=""
    nums=""


    if(dat%100>10 and dat%100<20):   #checks weather the number lies between 10 or 20 to assign special names
        nums=toteens(dat)
        dat =dat - (dat % 100)
    else:  # gives normal names to  upto two digit numbers excluding 11 12 13 14 15 16 17 18 19
        units = tounits(dat)
        dat = dat - (dat % 10)
        tens = totens(dat)
        dat = dat - (dat % 100)
        
        
    # general form of naming for numbers greater than 99 this function uses itself for comples repedted naming
    if (dat > 99):
        if (((dat % 1000) / 100) != 0):
            hundreds = num2text((dat % 1000) / 100) + " Hundred "
        dat = dat - (dat % 1000)


    if (dat > 999):
        if (((dat % 1000000) / 1000) != 0):
            thousands = num2text((dat % 1000000) / 1000) + " Thousand, "
        dat = dat - (dat % 1000000)

    if (dat > 999999):
        if (((dat % 1000000000) / 1000000) != 0):
            millions = num2text((dat % 1000000000) / 1000000) + " Million, "
        dat = dat - (dat % 1000000000)

    if (dat > 999999999):
        if (((dat % 1000000000000) / 1000000000) != 0):
            billions = num2text((dat % 1000000000000) / 1000000000) + " Billion, "
        dat = dat - (dat % 1000000000000)

    if (dat > 999999999999):
        if (((dat % 1000000000000000) / 1000000000000) != 0):
            trillions = num2text((dat % 1000000000000000) / 1000000000000) + " Trillion, "
        dat = dat - (dat % 1000000000000000)

    if (dat > 999999999999999):
        if (((dat % 1000000000000000000) / 1000000000000000) != 0):
            quadrillion = num2text((dat % 1000000000000000000) / 1000000000000000) + " Quadrillion, "
        dat = dat - (dat % 1000000000000000000)

    if (dat > 999999999999999999):
        if (((dat % 1000000000000000000000) / 1000000000000000000) != 0):
            quintillion = num2text((dat % 1000000000000000000000) / 1000000000000000000) + " Quintillion, "
        dat = dat - (dat % 1000000000000000000000)

    if (dat > 999999999999999999999):
        if (((dat % 1000000000000000000000000) / 1000000000000000000000) != 0):
            sextillion = num2text((dat % 1000000000000000000000000) / 1000000000000000000000) + " Sextillion, "
        dat = dat - (dat % 1000000000000000000000000)

    if (dat > 999999999999999999999999):
        if (((dat % 1000000000000000000000000000) / 1000000000000000000000000) != 0):
            septillion = num2text((dat % 1000000000000000000000000000) / 1000000000000000000000000) + " Septillion, "
        dat = dat - (dat % 1000000000000000000000000000)

    if (dat > 999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000) / 1000000000000000000000000000) != 0):
            octillion = num2text(
                (dat % 1000000000000000000000000000000) / 1000000000000000000000000000) + " Octillion, "
        dat = dat - (dat % 1000000000000000000000000000000)

    if (dat > 999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000) / 1000000000000000000000000000000) != 0):
            nonillion = num2text(
                (dat % 1000000000000000000000000000000000) / 1000000000000000000000000000000) + " Nonillion, "
        dat = dat - (dat % 1000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000) / 1000000000000000000000000000000000) != 0):
            decillion = num2text(
                (dat % 1000000000000000000000000000000000000) / 1000000000000000000000000000000000) + " Decillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000) / 1000000000000000000000000000000000000) != 0):
            undecillion = num2text((
                                   dat % 1000000000000000000000000000000000000000) / 1000000000000000000000000000000000000) + " Undecillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000) != 0):
            duodecillion = num2text((
                                    dat % 1000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000) + " Duodecillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000) != 0):
            tredecillion = num2text((dat % 1000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000) + " Tredecillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000) != 0):
            quattuordecillion = num2text((dat % 1000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000) + " Quattuordecillion, "
    dat = dat - (dat % 1000000000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000) != 0):
            quindecillion = num2text((dat % 1000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000) + " Quindecillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000) != 0):
            sexdecillion = num2text((dat % 1000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000) + " Sexdecillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000000) != 0):
            septemdecillion = num2text((dat % 1000000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000000) + " Septemdecillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000000000) != 0):
            octodecillion = num2text((dat % 1000000000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000000000) + " Octodecillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000000000000) != 0):
            novemdecillion = num2text((dat % 1000000000000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000000000000) + " Novemdecillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000000000000000000000000)

    if (dat > 999999999999999999999999999999999999999999999999999999999999999):
        if (((dat % 1000000000000000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000000000000000) != 0):
            vigintillion = num2text((dat % 1000000000000000000000000000000000000000000000000000000000000000) / 1000000000000000000000000000000000000000000000000000000000000) + " Vigintillion, "
        dat = dat - (dat % 1000000000000000000000000000000000000000000000000000000000000000)
    #returns the name to either the function itself or the user
    return (vigintillion + novemdecillion + octodecillion + septemdecillion + sexdecillion + quindecillion + quattuordecillion + tredecillion + duodecillion  + undecillion + decillion + nonillion + octillion + septillion + sextillion + quintillion + quadrillion + trillions + billions + millions + thousands +hundreds +  tens + units + nums)


#this function is used to give special names to number between 10 and 20
def toteens(dat):
    dat=dat%100
    if (dat==11.0 or dat==11):
        num="Eleven"
    elif (dat==12.0 or dat==12):
        num="Twelve"
    elif (dat==13.0 or dat==13):
        num="Thirteen"
    elif (dat==14.0 or dat==14):
        num="Fourteen"
    elif (dat==15.0 or dat==15):
        num="Fifteen"
    elif (dat==16.0 or dat==16):
        num="Sixteen"
    elif (dat==17.0 or dat==17):
        num="Seventeen"
    elif (dat==18.0 or dat==18):
        num="Eighteen"
    elif (dat==19.0 or dat==19):
        num="Nineteen"
    return( num )



#general purpose naming of number at unit place is completed hear
def tounits(dat):
    pof=""
    unit=dat%10
    if( unit == 1.0 or unit == 1 ):
        pof = "One"
    elif ( unit == 2.0 or unit == 2):
        pof = "Two"
    elif ( unit == 3.0 or unit == 3):
        pof = "Three"
    elif ( unit == 4.0 or unit == 4):
        pof = "Four"
    elif ( unit == 5.0 or unit == 5):
        pof = "Five"
    elif ( unit == 6.0 or unit == 6):
        pof = "Six"
    elif ( unit == 7.0 or unit == 7):
        pof = "Seven"
    elif ( unit == 8.0 or unit == 8):
        pof = "Eight"
    elif ( unit == 9.0 or unit == 9):
        pof = "Nine"
    elif ( unit == 0.0 or unit == 0):      #Zero added on 28 jan 2018 12:51
        pof = "Zero"
    return( pof )


# general purpose naming of numbers at tens place is completed hear
def totens(dat):
    pof=""
    unit=dat%100
    if(unit == 10):
        pof = "Ten"
    elif (unit == 20):
        pof = "Twenty "
    elif (unit == 30):
        pof = "Thirty "
    elif (unit == 40):
        pof = "Fourty "
    elif (unit == 50):
        pof = "Fivety "
    elif (unit == 60):
        pof = "Sixty "
    elif (unit == 70):
        pof = "Seventy "
    elif (unit == 80):
        pof = "Eightty "
    elif (unit == 90):
        pof = "Ninety "
    return( pof )


if __name__ == "__main__":
    inp=input("Enter Number : ")
    X=int(inp,10)

    print("\n" + "\n The Number " + inp + " is called "+num2text(X)+ "\n")
    input("PRESS ENTER TO EXIT")
