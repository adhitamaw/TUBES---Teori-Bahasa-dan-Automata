ribbon =  input("PERULANGAN WHILE - DO : ").split()
angka = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
indecrements = ["++", "--"]
variabel = ["a", "b", "c"]
inequality = [">=", "<=", "<", ">"] 
operator = ["+", "-", "*", "/"]
EOS=False
error = 0

if ribbon[0]=="int":
    if ribbon[1] in variabel:
        error = 1
        if ribbon[2] == '=':
            error = 2
            if ribbon[3] in angka:
                error = 3
                if ribbon[4] == ';':
                    error = 4
                    if ribbon[5] == 'do':
                        error = 5
                        if ribbon[6] == '{':
                            error = 6
                            if ribbon[7] in variabel:
                                error = 7
                                if ribbon[8] == '=':
                                    error = 8
                                    if ribbon[9] in variabel:
                                        error = 9
                                        if ribbon[10] in operator:
                                            error = 10
                                            if ribbon[11] in angka:
                                                error = 11
                                                if ribbon[12] == ';':
                                                    error = 12
                                                    if ribbon[13] in variabel:
                                                        error = 13
                                                        if ribbon[14] in indecrements:
                                                            error = 14
                                                            if ribbon[15] == ';':
                                                                error = 15
                                                                if ribbon[16] == '}':
                                                                    error = 16
                                                                    if ribbon[17] == 'while':
                                                                        error = 17
                                                                        if ribbon[18] == '(':
                                                                            error = 18
                                                                            if ribbon[19] in variabel:
                                                                                error = 19
                                                                                if ribbon[20] in inequality:
                                                                                    error = 20
                                                                                    if ribbon[21] in angka:
                                                                                        error = 21
                                                                                        if ribbon[22] == ')':
                                                                                            error = 22
                                                                                            if ribbon[23] == ';':
                                                                                                EOS=True
                                                                                                
if EOS==True:                                
    print("Input in Correct!, it reach 25th state")
else:
    print("terdapat kesalahan pada state", error+2)
