# It is Exercise 3
# Create a program capable of disaplaying questions to the user like KBC
# Use list data type to store the questions and their right answers
# Display the final amount the person is taking home after playing the game


questions = [
    ["What is the capital of India?", "New Delhi"],
    ["Who is the king of fruits?", "Mango"],
    ["What is the full form of PM in politics", "Prime Minister"],
    ["Who is the prime minister of India?", "Narendra Modi"]
]

priceMoney = [1000, 2000, 3000, 4000]
totalpmoney = 0
stopper = True
count = 0

print("Swagat, Aabhar, Abhinandan, Aap Khel rhe hai Kon Banega Crorepati")
while (count < len(questions)):
    while (stopper):
        for q in questions:
            pcount = 0
            print("Aapka Agla Sawal, ye rha aapke computer screen par")
            print(q[0])
            if (input("Aapke paas koi option nahi hai, kripaya apna jawab bataiye\n")
                    == q[1]):
                totalpmoney = totalpmoney + priceMoney[pcount]
                print(f"Badhai ho! Aap jeet chuke hain {totalpmoney} ₹")
                stopper = False
            else:
                print(
                    f"Galat Jawab! 😒, Aapki kul rashi jo aap ghar lekar jayenge yaha se wo hai {totalpmoney} ₹")
                break
            pcount += 1
    count += 1
