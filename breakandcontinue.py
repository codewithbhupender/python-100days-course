for i in range(12):
    if i+1==8:
        continue
    if i==10:
        break
    print("5 X ",i+1," = ",5*(i+1))
print("End of the loop")