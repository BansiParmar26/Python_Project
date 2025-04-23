def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    answer = int(input("Enter the number of your answer: "))
    if options[answer - 1] == correct_answer:
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is: {correct_answer}\n")

def kbc_game():
    questions = [
        ("Which is the smallest continent by area?", ["Asia", "Africa", "Europe", "Australia"], "Australia"),
        ("What is the capital of India?", ["Mumbai", "New Delhi", "Kolkata", "Chennai"], "New Delhi"),
        ("Who is known as the 'Father of the Nation' in India?", ["Jawaharlal Nehru", "Subhas Chandra Bose", "Mahatma Gandhi", "Bhagat Singh"], "Mahatma Gandhi"),
        ("Which is the longest river in the world?", ["Ganga", "Amazon", "Nile", "Yangtze"], "Nile"),
        ("Which is the currency of Japan?", ["Yuan", "Yen", "Ringgit", "Won"], "Yen"),
        ("What is the largest mammal in the world?", ["Elephant", "Shark", "Blue Whale", "Giraffe"], "Blue Whale"),
        ("Which element has the chemical symbol 'O'?", ["Oxygen", "Osmium", "Ozone", "Oganesson"], "Oxygen"),
        ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Leonardo da Vinci"),
        ("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "South Korea", "Thailand"], "Japan"),
        ("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter")
    ]
    
    for question, options, correct_answer in questions:
        ask_question(question, options, correct_answer)

if __name__ == "__main__":
    kbc_game()
