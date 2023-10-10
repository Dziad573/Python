'''stan_konta = input("Podaj stan konta ")
stan_konta = int(stan_konta)
#stan_konta = stan_konta + 2*750
print(stan_konta)'''

'''temperature = 16
czy = False
if temperature >= 10 and czy:
    print("Ciepło")
elif temperature >= -10 or czy == True:
    print("Zimno")
else:
    print("Bardzo zimno")'''

'''for i in range (1,10,2):
    if i == 5:
        break
    print("Numer:",i)'''

'''while temperature >= 10:
    print("temperatura:",temperature)
    temperature -=2'''

liczby = [1, 5, 4, 6, 3, 2, 4, 5]
'''liczby[2] = 99
print(liczby[2])'''


'''for i in range(len(liczby)):
    print(liczby[i], end=" ")'''

'''for liczba in liczby:
    print(liczba, end=" ")'''

'''for i, liczba in enumerate(liczby):
    if i%2 == 0 and liczba > 3:
        print(i, liczba)'''

for i, liczba in enumerate(liczby):
    #liczby[i] +=1
    liczby.append(33)
    liczby.extend([55, 66, 12])
    liczby.insert(0,8)

    liczby = sorted(liczby, reverse=False)
    liczby.pop()

    if 55 in liczby:
        print("Jest taka liczba")
    else:
        print("Nie ma takiej liczby")

    print(liczby)

    break

