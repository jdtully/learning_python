#lowest number divisible  by 1_20
for num in range(1,1000000):    
    if num%20==0 and num%19==0 and num%18==0 and num%17==0:
                    if num%16==0:
                        if num%15==0:
                            if num%14==0:
                                if num%13==0:
                                    if num%12==0:
                                        if num%11==0:
                                            if num%10==0:
                                                if num%9==0:
                                                    print(num)