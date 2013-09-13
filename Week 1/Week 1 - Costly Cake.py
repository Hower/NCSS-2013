cake1 = input("Cake 1 side length (cm): ")
cake1Cost = float(input("Cake 1 cost ($): "))
cake2 = input("Cake 2 side length (cm): ")
cake2Cost = float(input("Cake 2 cost ($): "))
squared1, squared2 = float(cake1)**2, float(cake2)**2
perCm1, perCm2 = cake1Cost/squared1, cake2Cost/squared2
print("Cake 1 costs ${:.2f} per cm2 for {} cm2" \
    .format(perCm1, round(squared1)))
print("Cake 1 costs ${:.2f} per cm2 for {:.2f} cm2" \
    .format(perCm2, squared2), round(squared2, 2))
if perCm1 < perCm2:
    print("Get cake 1!")
elif perCm2 < perCm1:
    print("Get cake 2!")
else:
    print("Get either!")