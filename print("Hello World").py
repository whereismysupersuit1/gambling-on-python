weight = float(input("Weight? "))
weight_type = input("Kilograms(K) or Lbs(L)? ")
if weight_type == "K":
    converted = 2.20 * weight
    print("weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("weight in Kilos: " + str(converted))
 


