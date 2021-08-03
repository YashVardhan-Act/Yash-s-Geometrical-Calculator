# This Program Is A Geometrical Calculator. Here, You Can Calculate Area and Perimeter Of Various Shapes
# Author : Yash Vardhan
# copyright : Yash Vardhan
# Dont copy this program without asking

while True:
    # Printing The Instructions For User
    print("Enter A For Area")
    print("Enter P For Primeter")
    print("Enter Q To Quit")

    choice = str(input("Enter Your Choice: "))

    # Giving The Instructions To The Program

    if choice == 'Q':
        break
    elif choice == 'A':
        # Printing The User Instructions For Area
        print("Enter R For Rectangle")
        print("Enter S For Square")
        print("Enter ET For Equilateral Triangle")
        print("Enter IT For Isosceles Triangle")
        print("Enter ST For Scalene Triangle")
        print("Enter C1 For Circle Whose Vaue Of Pi Is Given 22/7")
        print("Enter C2 For Circle Whose Vaue Of Pi Is Given 3.14")

        choice_of_shapes = str(input("Enter The Shape: "))

        # Giving The Instruction To The Program That What To Do If The User Selects Area

        if choice_of_shapes == 'R':
            l = float(input("Enter The Length: "))
            b = float(input("Enter The Breadth: "))

            area = l*b
            print("The Area Of The Rectangle Is:", area)
        elif choice_of_shapes == 's':
            s = float(input("Enter The Shape: "))

            area_of_square = s*s
            print("The Area Of The Square Is:", area_of_square)
        elif choice_of_shapes == 'ET':
            s_of_ET = float(input("Enter The Side: "))

            area_of_ET = (s_of_ET*s_of_ET)*1.732/4
            print("The Area Of The Equilateral Triangle Is:", area_of_ET)
        elif choice_of_shapes == 'IT':
            b_of_IT = float(input("Enter The Base: "))
            h_of_IT = float(input("Enter The Height: "))

            area_of_IT = 1/2*(b_of_IT*h_of_IT)
            print("The Area Of Isosceles Triangle Is:", area_of_IT)
        elif choice_of_shapes =='ST':
            b_of_ST = float(input("Enter The Base: "))
            h_of_ST = float(input("Enter The Height: "))

            area_of_ST = 1/2*(b_of_ST*h_of_ST)
            print("The Area Of The Scalene Triangle Is:", area_of_ST)
        elif choice_of_shapes == 'C1':
            radius = float("Enter The Radius: ")

            area_of_C1 = 22/7*radius*radius
            print("The Area Of The Circle Is:", area_of_C1)
        elif choice == 'C2':
            radius2 = float("Enter The Radius")

            area_of_C2 = 3.14*radius2*radius2
        else:
            print("Invalid Shape")
    elif choice == 'P':
        # Givng The User Instructions For Perimeter
        print("Enter R For Rectangle")
        print("Enter S For Square")
        print("Enter ET For Equilateral Triangle")
        print("Enter IT For Isosceles Triangle")
        print("Enter ST For Scalene Triangle")
        print("Enter C1 For Circle Whose Value Of Pi Is Given 22/7")
        print("Enter C2 For Circle Whose Value Of Pi Is Given 3.14")

        # Giving The Instruction To The Program That What To Do If The User Selects Perimeter

        choice_of_shapes_perimeter = str(input("Enter The Choice: "))

        if choice_of_shapes_perimeter == 'R':
            lr = float(input("Enter The Length: "))
            br = float(input("Enter The Breadth"))

            perimeter = 2*(lr+br)
            print("The Perimeter Of The Rectangle Is:", perimeter)
        elif choice_of_shapes_perimeter == 'S':
            s_p = float(input("Enter The Side: "))

            perimeter_s = 4*s_p
            print("The Perimeter Of The Square Is:", perimeter_s)
        elif choice_of_shapes_perimeter == 'ET':
            s_ET = float(input("Enter The Side: "))

            perimeter_ET = 3*s_ET
            print("The Perimeter Of The Equilateral Triangle Is:", perimeter_ET)
        elif choice_of_shapes_perimeter == 'IT':
            s1 = float(input("Enter The First Side: "))
            s2 = float(input("Enter The Second Side: "))
            s3 = float(input("Enter The Third Side: "))

            perimeter_IT = s1+s2+s3
            print("The Perimeter Of The Isosceles Triangle Is:", perimeter_IT)
        elif choice_of_shapes_perimeter == 'ST':
            s1_ST = float(input("Enter The First Side: "))
            s2_ST = float(input("Enter The Second Side: "))
            s3_ST = float(input("Enter The Third Side: "))

            perimeter_ST = s1_ST+s2_ST+s3_ST
            print("The Perimeter Of The Scalene Triangle Is:", perimeter_ST)
        elif choice_of_shapes_perimeter == 'C1':
            r_perimeter = float(input("Enter The Radius: "))

            perimeter_C1 = 2*22/7*r_perimeter
            print("The Perimeter Of The Circle Is:", perimeter_C1)
        elif choice_of_shapes_perimeter == 'C2':
            r1_perimeter = float(input("Enter The Radius: "))

            perimeter_C2 = 2*3.14*r1_perimeter
            print("The Perimeter Of The Circle Is:", perimeter_C2)
        else:
            print("Invalid Shape")
    else:
        print("Invalid Choice")