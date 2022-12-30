# It is Exercise 3
# Create a program capable of disaplaying questions to the user like KBC
# Use list data type to store the questions and their right answers
# Display the final amount the person is taking home after playing the game


questions = ["What is the capital of India?", "Who is the king of fruits?",
             "What is the full form of PM in politics", "Who is the prime minister of India?"]
answers = ["New Delhi", "Mango", "Prime Minister", "Narendra Modi"]

stopper = True

while (stopper):
    key = input("Enter the key")
    if (key == "Stop"):
        stopper = False
    print("Yes")
