girls=int(input("τα κοριτσια στο τμημα ειναι:"))
boys=int(input("τα αγορια στο τμημα ειναι :"))
school=girls+boys
persentboys=(boys*100)/school
persentgirls=100-persentboys
print("το ποσοστο της ταξης για τα αγορια ειναι: {}%".format(persentboys))
print("το ποσοστο της ταξης για τα κοριτσια ειναι: {} %".format(persentgirls))

