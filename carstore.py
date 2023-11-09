import pandas as  pd

import matplotlib.pyplot as plt

f=pd.read_csv("newcars.csv")
txt="********NEW CARS DEALERSHIP********"
txt2='******WELCOME******'
y=txt2.center(125)
x=txt.center(125)
print(x)
print(y)
print("\n")
print("MAIN MENU")
def buyer():
        print("Hope you're having a nice day!!\nHow may we assist you?")
        stop="y"
        while stop=="y":
                print("1.View all vehicles\n2.Choose Company\n3.Budget\n4.Minimum Mileage\n5.Sort by price")
                ui=int(input("What would you like to do:"))
                if ui==1:
                        print(f)
                        f.plot(kind="bar" ,x="model",y="price")
                        plt.show()

                elif ui==2:
                        all_comp=(f["company"].unique())
                        for i in all_comp:
                            print(i)
                        comp=input("Which company's cars would you like to see:")
                        for row in f.iterrows():
                            if row['company']==comp:
                                print(row['model'])
                                
                elif ui==3:
                    budget=int(input("Enter maximum Budget:"))
                    for row in f.iterrows():
                            if row['price']<=budget:
                                print(row['company'],row['model'])
                                

                elif ui==4:
                    min_mi=float(input("Enter Minimum Mileage: "))
                    for row in f.iterrows():
                            if row['mpg']>=min_mi:
                                print(row['company'],row['model'])
                                
                                
                elif ui==5:
                    print(f.sort_values('price'))
                ask=input("Do you want to Continue (y/n)")
                stop=ask
                
                if stop =="n":
                    
                    print("Thankyou For Visiting! Hope to see you again")


def sales():
        print("Hope you're having a nice day!!\nHow may we assist you?")
        stop="y"
        while stop=="y":
            print("1.Update car price\n2.new car\n3.car sold\n4.View all cars.")
            ui=int(input("What would you like to do:"))
            if ui==1:
                car_name=input("car name:")
                new_price=int(input("new price:"))
                f.loc[f["model"]==car_name,"price"]=new_price
                print("Price Updated Successfully!!")
            elif ui==2:
                sno=int(input("S.no:"))
                company=input("company:")
                model=input("model name:")
                mpg=float(input("mpg:"))
                cyl=int(input("cyl:"))
                disp=float(input("disp:"))
                hp=int(input("hp:"))
                bootspace=int(input("bootspace(L):"))
                fuel=float(input("fuel capacity(gallons):"))
                camera=input("reverse cameras:")
                speakers=int(input("number of speakers:"))
                gear=int(input("number of gears:"))
                price=int(input("price:"))

                new_car=[sno,company,model,mpg,cyl,disp,hp,bootspace,fuel,camera,speakers,gear,price]
                        
                
                f.loc["new"]=new_car
                print("Car has been successfully added!!")
                print(f)

            elif ui==3:
                model=input("Enter Model sold:")
                index=f[f["model"]==model].index.values
                f.drop(index,axis=0,inplace=True)
                print("DataSet updated.",model,"has been removed.")
            
            elif ui==4:
                print(f)
                f.plot(kind="bar",x="model",y="price")
                plt.show()
            ask=input("Do you want to continue(y/n)")
            stop=ask
            if ask=="n":
                print("Thankyou For Visiting! Hope to see you again")
            
stop="n"
while stop=="n":
    user=input("Are you a customer or salesman: ")
    if user=="customer":
            buyer()
    elif user =="salesman":
            sales()

    else :
            print("invalid input")
            
    ask=input("Would you like to exit the app? (y/n)")
    stop=ask
print("Thankyou For Visiting! Hope to see you again")
