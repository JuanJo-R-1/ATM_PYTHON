useful = ("pencil","eraser","rule","notebook","pen")
useful=[]
while True:
 print(useful)
 print("0. Pencil")
 print("1. eraser")
 print("2. rule")
 print("3. notebook")
 print("4. Pen")

 print("do you wanna add a new item?")
 input()
 if "yes":
      print("wich item do you wanna add?")
      useful.extend([input])
 elif "no":
      break