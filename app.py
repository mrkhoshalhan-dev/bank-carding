
print("*Bank card number checking script*")

card_number = input("Enter your card number : ") #در خط اول که اومدیم شماره کارت رو گرفتیم 
sum = 0 #قرره حاصل ضرب های بریزم توسش
for i in range(len(card_number)):
    if (i+1) % 2 == 0:
        result = int(card_number[i]) * 1
    else:
        if (int(card_number[i]) * 2) > 9:
            result = (int(card_number[i]) * 2) - 9
        else:
            result = int(card_number[i]) * 2
    sum += result

if sum % 10 == 0:
    print("Your card number is correct :)")
else:
    print("Your card number is incorrect :(")