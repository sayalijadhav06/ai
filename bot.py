def welcome():
    print("Hello! I am ShopBuddy, the customer assistant of this online store.")
    print("I can chat with you, play a small game and test your knowledge.")


def ask_name():
    name = input("What is your name? ")
    print("Nice to meet you, " + name + "!")
    return name


def guess_age():
    print("Let me guess your age.")
    print("Tell me the remainder when your age is divided by 3, 5 and 7.")
    remainder_3 = int(input("Remainder when divided by 3: "))
    remainder_5 = int(input("Remainder when divided by 5: "))
    remainder_7 = int(input("Remainder when divided by 7: "))
    age = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105
    print("Your age is " + str(age) + "!")


def count_numbers():
    limit = int(input("Enter a number and I will count up to it: "))
    for number in range(1, limit + 1):
        print(number)
    print("Done counting!")


def ask_questions():
    questions = [
        ("Which of these is available 24x7 without a break?\n1. Human agent\n2. Chatbot\n3. Shop manager", "2"),
        ("Which type of chatbot follows fixed rules?\n1. Rule-based\n2. AI-based\n3. Voice-based", "1"),
        ("What does a chatbot mainly do?\n1. Cook food\n2. Talk with users\n3. Repair phones", "2"),
    ]
    score = 0
    for question, correct_answer in questions:
        print(question)
        answer = input("Your answer (1/2/3): ")
        if answer == correct_answer:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong. The right answer is option " + correct_answer + ".")
    print("You scored " + str(score) + " out of " + str(len(questions)) + ".")


def main():
    welcome()
    name = ask_name()
    guess_age()
    count_numbers()
    ask_questions()
    print("Thank you for chatting with me, " + name + ". Goodbye!")


main()
