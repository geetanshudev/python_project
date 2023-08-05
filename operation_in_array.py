A = eval(input("Enter List of array = "))
B = list(A)
print(B)


while True:
    ans = input("Do you want to apply any operation on array ? (Y or N):")
    if ans == 'Y':
        while True:
            ans1 = input("Enter \n 1 for Traversing \n 2 for Inserting new element\n 3 for Deleting new element\n 4 for remove specific element \n 5 for searching specific element in  array\n 6 for Merging two array \n 7 for sorting array")
            if ans1 == '1':
                for i in B:
                    print(i)
                
                break
            elif ans1 == '2':
                while True:
                    ans = input("do you want to add new element ? (Y or N):")
                    if ans == 'Y':
                        while True:
                            ans1 = input("do you really want to add an element (Y or N) : ")
                            if ans1 == 'Y':
                                new = eval(input("Enter new element = "))
                                B.append(new)
                            elif ans1 == 'N':
                                break
                    elif ans == 'N':
                        break
                    else:
                        print("Wrong input !! ")

                    print(B)
                    
            elif ans1 == '3':
                while True:
                    ans = input("do you want to delete last element ? (Y or N):")
                    if ans == 'Y':
                        while True:
                            ans1 = input("do you really want to delete last element (Y or N) : ")
                            if ans1 == 'Y':
                
                                B.pop()
                                print("\nLast element is deleted.")
                                print("\n only",len(B),"elements left")
                            elif ans1 == 'N':
                                break
                    elif ans == 'N':
                        break
                    else:
                        print("Wrong input !! ")
                        break

                    print(B)

            elif ans1 == '4':
                while True:
                    ans = input("do you want to delete specific element ? (Y or N):")
                    if ans == 'Y':
                        while True:
                            ans1 = input("do you really want to delete specific element (Y or N) : ")
                            if ans1 == 'Y':
                
                                kh = eval(input("enter element to  delete = "))
                                B.remove(kh)
                                print("element is deleted.")
                                print("only",len(B),"elements left")
                            elif ans1 == 'N':
                                break
                    elif ans == 'N':
                        break
                    else:
                        print("Wrong input !! ")

                    print(B)
                    
            
                    
            elif ans1 == '5':
                while True:
                    ans = input("do you want to search element ? (Y or N):")
                    if ans == 'Y':
                        while True:
                            ans1 = input("do you really want to search specific element (Y or N) : ")
                            if ans1 == 'Y':
                
                                kh = eval(input("enter element to search = "))
                                for i in B:
                                #print(i)
                                    if (kh != i):
                                        print("Result = There is no such element found")
                        
                    
                                    else:
                                        l = B.index(kh)
                                        print("Result = element founded !! in.",l,"of index.")
                                        break
                
                
               
                            elif ans1 == 'N':
                                break
                    elif ans == 'N':
                        break
                    else:
                        print("Wrong input !! ")
                        
            elif ans1 == '6':
                while True:
                    ans = input("do you want to add new List ? (Y or N):")
                    if ans == 'Y':
                        while True:
                            ans1 = input("do you really want to add new List (Y or N) : ")
                            if ans1 == 'Y':
                                newL = eval(input("Enter new List = "))
                                newLL = list(newL)
                                B.extend(newLL)
                            elif ans1 == 'N':
                                break
                    elif ans == 'N':
                        break
                    else:
                        print("Wrong input !! ")

                    print(B)
            elif ans1 == '7':
                while True:
                    ans = input("do you want to Sort a  List ? (Y or N):")
                    if ans == 'Y':
                        while True:
                            print("Unsorted array = ",B)
                            ans1 = input("Enter asc for ascending order or dsc for descending order : ")
                            if ans1 == 'asc':
                                B.sort()
                                print(B)
                                break
                            elif ans1 == 'dsc':
                                B.sort(reverse = True)
                                print(B)
                                break
                    elif ans == 'N':
                        break
                    else:
                        print("Wrong input !! ")
                
                
                        
                        

    elif ans == 'N':
        break
    else:
        print("Wrong input !! ")
        break
print("Thank you \nGood bye")
