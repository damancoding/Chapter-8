# Amanda Manirambona
# Saddle_Points
# 3/22/2014
def create_3d_list_1(x,y,z):
        lst=[]
        for i in range(x):
                lst_2d=[]
                for j in range(y):
                        lst_1d=[]
                        for k in range(z):
                                lst_1d.append("#" * 7)
                        lst_2d.append(lst_1d)
                lst.append(lst_2d)
        return lst    
def main():
    x = int(input("Input how many rows for x: "))
    y = int(input("Input how many times you want to repeat x for y: "))
    z = int(input("Input what you want inside of x for z: "))
    output_1 = create_3d_list_1(x,y,z)
    for board in output_1:
        for row in board:
            print(row)
main()
create_3d_list_1(x,y,z)
