#პროგრამა ჩაიფიქრებს რიცხვს 1-დან 100-მდე
#მოთამაშემ უნდა გამოიცნოს ეს რიცხვი
#თუ კომპიუტერის მიერ ჩაფიქრებული რიცხვი 5 ერთეული მეტია ან ნაკლებია იმ რიცხვზე რაც კომხმარებელმა შეიყვანა უნდა გამოვიტანოთ სიტყვა : ცხელა "hot"
#თუ 10 ერთეულით შორს არის მაშინ "warm"
# თუ საერთოდ არაა ახლოს მაშინ "cold"
#თუ გამოიცნო რიცხვი, მაშინ უნდა გამოვიტანოით რამდენი ცდა დასჭირდა

import random
computer_number = random.randint(1, 100)
steps = 0
while True:
    answer = int(input("Please input your number between 1-100: "))
    if answer<1 or answer>100:
        print("Please input the number the number in the right range!!")
        continue
    steps +=1
    if answer==computer_number:
        print("CONGRATS YOU HAVE FOUND THE RIGHT NUMBER",computer_number)
        print(f" Amount of steps: {steps}")
        break
    if answer in range(computer_number-5, computer_number+6):
        print("HOT")
        continue

    if answer in range(computer_number-10, computer_number+11):
        print("Warm")
        continue
    else:
        print("COLD")







