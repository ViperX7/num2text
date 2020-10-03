# Copyright 2019 Utkarsh Yadav
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# This program has limitations as it can only translate to an extent
# it can translate upto (10^64 -1)


def num2text(dat, delimiter=", "):

    # input inspection

    if (dat > pow(10, 64) - 1):
        return "Input Out of range"
        
    elif (dat < 0):
        print("Invalid Input \n converting to positive number")
        dat = dat * (-1)

    # default declaration  in case they are not used and are needed to print
    quintillion = ""
    quadrillion = ""
    sextillion = ""
    septillion = ""
    octillion = ""
    nonillion = ""
    decillion = ""
    undecillion = ""
    duodecillion = ""
    tredecillion = ""
    quattuordecillion = ""
    quindecillion = ""
    sexdecillion = ""
    septemdecillion = ""
    octodecillion = ""
    novemdecillion = ""
    vigintillion = ""
    billions = ""
    trillions = ""
    millions = ""
    thousands = ""
    hundreds = ""
    tens = ""
    units = ""
    nums = ""

    # checks weather the number lies between 10 or 20 to assign special names
    if (dat % 100 > 10 and dat % 100 < 20):
        nums = toteens(dat)
        dat = dat - (dat % 100)
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
            thousands = num2text((dat % 1000000) / 1000) + \
                " Thousand" + delimiter
        dat = dat - (dat % 1000000)

    if (dat > 999999):
        if (((dat % 10**9) / 10**6) != 0):
            millions = num2text(
                (dat % 10**9) / 10**6) + " Million" + delimiter
        dat = dat - (dat % 10**9)

    if (dat > 999999999):
        if (((dat % 10**12) / 10**9) != 0):
            billions = num2text(
                (dat % 10**12) / 10**9) + " Billion" + delimiter
        dat = dat - (dat % 10**12)

    if (dat > 999999999999):
        if (((dat % 10**15) / 10**12) != 0):
            trillions = num2text((dat % 10**15) /
                                 10**12) + " Trillion" + delimiter
        dat = dat - (dat % 10**15)

    if (dat > 999999999999999):
        if (((dat % 10**18) / 10**15) != 0):
            quadrillion = num2text(
                (dat % 10**18) /
                10**15) + " Quadrillion" + delimiter
        dat = dat - (dat % 10**18)

    if (dat > 999999999999999999):
        if (((dat % 10**21) / 10**18) != 0):
            quintillion = num2text(
                (dat % 10**21) /
                10**18) + " Quintillion" + delimiter
        dat = dat - (dat % 10**21)

    if (dat > 999999999999999999999):
        if (((dat % 10**24) / 10**21) != 0):
            sextillion = num2text(
                (dat % 10**24) /
                10**21) + " Sextillion" + delimiter
        dat = dat - (dat % 10**24)

    if (dat > 999999999999999999999999):
        if (((dat % 10**27) / 10**24)
                != 0):
            septillion = num2text(
                (dat % 10**27) /
                10**24) + " Septillion" + delimiter
        dat = dat - (dat % 10**27)

    if (dat > 999999999999999999999999999):
        if (((dat % 10**30) /
             10**27) != 0):
            octillion = num2text(
                (dat % 10**30) /
                10**27) + " Octillion" + delimiter
        dat = dat - (dat % 10**30)

    if (dat > 999999999999999999999999999999):
        if (((dat % 10*33) /
             10**30) != 0):
            nonillion = num2text(
                (dat % 10**33) /
                10**30) + " Nonillion" + delimiter
        dat = dat - (dat % 10**33)

    if (dat > 999999999999999999999999999999999):
        if (((dat % 10**36) /
             10**33) != 0):
            decillion = num2text(
                (dat % 10**36) /
                10**33) + " Decillion" + delimiter
        dat = dat - (dat % 10**36)

    if (dat > 999999999999999999999999999999999999):
        if (((dat % 10**39) /
             10**36) != 0):
            undecillion = num2text(
                (dat % 10**39) /
                10**36
            ) + " Undecillion" + delimiter
        dat = dat - (dat % 10**39)

    if (dat > 999999999999999999999999999999999999999):
        if (((dat % 10**42) /
             10**39) != 0):
            duodecillion = num2text(
                (dat % 10**42) /
                10**39
            ) + " Duodecillion" + delimiter
        dat = dat - (dat % 10**42)

    if (dat > 999999999999999999999999999999999999999999):
        if (((dat % 10**45) /
             10**42) != 0):
            tredecillion = num2text(
                (dat % 10**45) /
                10**42
            ) + " Tredecillion" + delimiter
        dat = dat - (dat % 10**45)

    if (dat > 999999999999999999999999999999999999999999999):
        if (((dat % 10**48) /
             10**45) != 0):
            quattuordecillion = num2text(
                (dat % 10**48) /
                10**45
            ) + " Quattuordecillion" + delimiter
    dat = dat - (dat % 10**48)

    if (dat > 999999999999999999999999999999999999999999999999):
        if (((dat % 10**51) /
             10**48) != 0):
            quindecillion = num2text(
                (dat % 10**51) /
                10**48
            ) + " Quindecillion" + delimiter
        dat = dat - (dat % 10**51)

    if (dat > 999999999999999999999999999999999999999999999999999):
        if (((dat % 10**54) /
             10**51) != 0):
            sexdecillion = num2text(
                (dat % 10**54) /
                10**51
            ) + " Sexdecillion" + delimiter
        dat = dat - (dat %
                     10**54)

    if (dat > 999999999999999999999999999999999999999999999999999999):
        if (((dat % 10**57) /
             10**54) != 0):
            septemdecillion = num2text(
                (dat % 10**57)
                / 10**54
            ) + " Septemdecillion" + delimiter
        dat = dat - (dat %
                     10**57)

    if (dat > 999999999999999999999999999999999999999999999999999999999):
        if (((dat % 10**60)
             / 10**57) != 0):
            octodecillion = num2text(
                (dat %
                 10**60) /
                10**57
            ) + " Octodecillion" + delimiter
        dat = dat - (
            dat % 10**60)

    if (dat > 999999999999999999999999999999999999999999999999999999999999):
        if (((dat %
              10**63) /
             10**60) != 0):
            novemdecillion = num2text(
                (dat %
                 10**63)
                / 10**60
            ) + " Novemdecillion" + delimiter
        dat = dat - \
            (dat % 10**63)

    if (dat > 999999999999999999999999999999999999999999999999999999999999999):
        if (((dat %
              10**66)
             / 10**63)
                != 0):
            vigintillion = num2text((
                dat %
                10**66
            ) / 10**63
                                    ) + " Vigintillion" + delimiter
        dat = dat - \
            (dat % 10**66)
    # returns the name to either the function itself or the user
    num_name = (vigintillion + novemdecillion + octodecillion +
                septemdecillion + sexdecillion + quindecillion +
                quattuordecillion + tredecillion + duodecillion + undecillion +
                decillion + nonillion + octillion + septillion + sextillion +
                quintillion + quadrillion + trillions + billions + millions +
                thousands + hundreds + tens + units + nums)
    return num_name.strip(", ")


# this function is used to give special names to number between 10 and 20
def toteens(dat):
    dat = dat % 100
    if (dat == 11.0 or dat == 11):
        num = "Eleven"
    elif (dat == 12.0 or dat == 12):
        num = "Twelve"
    elif (dat == 13.0 or dat == 13):
        num = "Thirteen"
    elif (dat == 14.0 or dat == 14):
        num = "Fourteen"
    elif (dat == 15.0 or dat == 15):
        num = "Fifteen"
    elif (dat == 16.0 or dat == 16):
        num = "Sixteen"
    elif (dat == 17.0 or dat == 17):
        num = "Seventeen"
    elif (dat == 18.0 or dat == 18):
        num = "Eighteen"
    elif (dat == 19.0 or dat == 19):
        num = "Nineteen"
    return (num)


# general purpose naming of number at unit place is completed hear
def tounits(dat):
    pof = ""
    unit = dat % 10
    if (unit == 1.0 or unit == 1):
        pof = "One"
    elif (unit == 2.0 or unit == 2):
        pof = "Two"
    elif (unit == 3.0 or unit == 3):
        pof = "Three"
    elif (unit == 4.0 or unit == 4):
        pof = "Four"
    elif (unit == 5.0 or unit == 5):
        pof = "Five"
    elif (unit == 6.0 or unit == 6):
        pof = "Six"
    elif (unit == 7.0 or unit == 7):
        pof = "Seven"
    elif (unit == 8.0 or unit == 8):
        pof = "Eight"
    elif (unit == 9.0 or unit == 9):
        pof = "Nine"
    elif (dat == 0.0 or dat == 0):
        pof = "Zero"
    return (pof)


# general purpose naming of numbers at tens place is completed hear
def totens(dat):
    pof = ""
    unit = dat % 100
    if (unit == 10):
        pof = "Ten"
    elif (unit == 20):
        pof = "Twenty "
    elif (unit == 30):
        pof = "Thirty "
    elif (unit == 40):
        pof = "Fourty "
    elif (unit == 50):
        pof = "Fifty "
    elif (unit == 60):
        pof = "Sixty "
    elif (unit == 70):
        pof = "Seventy "
    elif (unit == 80):
        pof = "Eighty "
    elif (unit == 90):
        pof = "Ninety "
    return (pof)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--delimiter", help="choose the delimiter")
    parser.add_argument("Number", type=int)
    args = parser.parse_args()

    if args.Number:
        if args.delimiter:
            print(num2text(args.Number, delimiter=args.delimiter))
        else:
            print(num2text(args.Number))
