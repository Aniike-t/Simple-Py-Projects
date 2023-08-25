import matplotlib.pyplot as plt
import pickle
import os

#try if file available or make the values 0/null
try:
  with open("data.pkl", "rb") as f:
    dict, tran, y = pickle.load(f)
# public variables
except FileNotFoundError:
  dict = {}
  tran = []
  y = []

n=0

while n != 8:
  total = 0
  k = True

  # Menu
  n = int(
    input(
      "Menu\n1.Add Item to inventory\n2.Add or Reduce Quantity to an item\n3.Buy\n4.Show Inventory, Quantity, Prices And Total Cost\n5.Remove Item\n6.Transaction History And Graph\n7.Update Price\n8.Exit\n\n"
    ))

  # Add Item if present add quantity
  if n == 1:

  # If Item Present
    nameF = input("\nEnter Name of Fruit : ")
    if nameF in dict:
      choice = input("Item already exists, do you want to add quantity? (Y/N) : ")
      if choice == 'Y':
        addQ = int(input("Enter Quantity to add : "))
        dict[nameF][0] += addQ
        print("Quantity Added\n")
        tran.append(['UpdateQuantity', nameF, 'AddedQuantity :' + str(addQ)])
        for key, value in dict.items():
          total += value[0]*value[1]
        y.append(total)
      if choice == 'N':
        print("Item Not Added\n")
      else:
        print("Please make a valid choice")
  # Add Item if !present
    else:
      price = int(input("Enter Price : "))
      quantity = int(input("Enter Quantity : "))
      dict[nameF] = [quantity, price]
      print("Item Added\n")
      tran.append(['AddedItem', nameF, 'Quantity: ' + str(quantity), 'Price: ' + str(price)])
      for key, value in dict.items():
        total = total + value[0] * value[1]
      y.append(total)


  # Add Quantity
      
  elif n == 2:
    nameF = input("\nEnter Name of Fruit : ")
    if nameF in dict:
        choice = int(input("\n1. Add Quantity\n2. Reduce Quantity\n"))
        if choice == 1:
          addQ = int(input("Enter Quantity to add : "))
          dict[nameF][0] += addQ
          print("\nQuantity Added\n")
          st1 = 'AddedQuantity :'
        if choice == 2 :
          addQ = int(input("\nEnter Quantity to be reduced : "))
          if dict[nameF][0] < addQ:
            print("\n\tNot Enough Inventory\t\n")
            k= False
          else:
            dict[nameF][0] -= addQ
            st1 = 'ReducedQuantity :'
            print("\nQuantity Reduced\n")
            k= True
        else:
          print("\nEnter a valid option\n")
        if (choice == 1 or (choice == 2 and k)):
          for key,values in dict.items():
            total += values[0]*values[1]
          y.append(total)
          tran.append(['UpdateQuantity', nameF, st1 + str(addQ)])
    else:
      print("\n\tItem Not Found\t\n")
      
  #buy
  elif n == 3:
    print("\n\t\tFruits Available \n")
    for key,i in dict.items():
      print("\nFruit: ", key, " Quantity: ", i[0], " Price: ", i[1], "\n")
    nameF = input("\nEnter Name of Fruit : ")
    if nameF in dict:
      buyQ = int(input("\nEnter Quantity to buy : "))
      if dict[nameF][0] < buyQ:
        print("\nNot Enough Quantity\n")
      else:
        dict[nameF][0] -= buyQ
        print("\nTotal Cost : ", buyQ * dict[nameF][1])
        print("\nItem Bought\n")
        for i in dict.values():
            total = total + i[0] * i[1]
        y.append(total)
        tran.append([
          'Buying', nameF, 'CostBought ' + str(buyQ * dict[nameF][1]),
            'Quantity:' + str(-1 * buyQ)
          ])
    else:
      print("\nItem Not Found\n")

  # Inventory and Total Cost
  elif n == 4:
    total = 0
    print("\nInventory And Total Cost: \n")
    if len(dict) !=0 :
      for key,i in dict.items():
        print("\nFruit: ", key, " Quantity: ", i[0], " Price: ", i[1], "\n")
      for i in dict.values():
        total +=  i[0] * i[1]
      print('\ntotal cost of inventory : ', total, "\n")
      total = 0
    else:
      print("\nInventory is empty.\n")

  # Del key or remove quantity
  elif n == 5:
    nameF = input("\nEnter Name of Fruit : ")
    for key, value in dict.items():
      if key == nameF:
        del dict[key]
        print("\nItem Deleted\n")
        tran.append(['DELETION', nameF])
        total = 0
        for i in dict.values():
          total +=  i[0] * i[1]
        y.append(total)
        break
    else:
      print("\nItem Not Found\n")

  # Exit
  elif n == 8:
    choice = input("\nWould You Like To Save The Current State ?\n ( Y to save, N to None, D to Delete prev saved file ) : ")
    if choice == 'Y':
      with open("data.pkl", "wb") as f:
        pickle.dump([dict, tran, y], f)
    elif choice == 'D':
      try:
        os.remove("data.pkl")
      except FileNotFoundError:
        pass
    else:
      pass
    print("\n\t\t\tExit\t\t\t\n")

  # Transaction history And Graph
  elif n == 6:
    print('\nTransaction History:\t', tran, '\n\n')
    print('\nTotal Cost list :', y)
    choice = input("\nTotal-Cost Graph ? (Y?N) ")
    if len(y) != 0 and choice == 'Y':
      x = [i for i in range(1, len(y) + 1)]
      plt.plot(x, y,marker = 'o', markerfacecolor = 'r')
      plt.xlabel('Timespan')
      plt.ylabel('Price')
      plt.title('Buy-Sell Graph')
      plt.show()
    elif choice == 'N':
      print("\nExited Prompt\n")
    else:
      print("\n\t\t\tNOT ENOUGH DATA AVAILABLE\n")

  #Update Price
  elif n == 7:
    if len(dict) == 0:
      print('\nEmpty Inventory\n')
      break
    nameF = input("\nEnter Name of Fruit : ")
    if nameF in dict:
      print('\nPrevious Price: ', dict[nameF][1])
      newP = int(input("Enter updated price : "))
      dict[nameF][1] = newP
      print("\nPrice Updated\n")
      tran.append(['UpdatePrice', nameF, 'UpdatedPrice: ' + str(newP)])
      for i in dict.values():
        total +=  i[0] * i[1]
      y.append(total)
    else:
      print("\nItem Not Found\n")

  # invalid input
  else:
    print("Invalid Input\n")