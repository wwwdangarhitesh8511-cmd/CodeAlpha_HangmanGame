def play_hangman():
    words = ["python", "coding", "intern", "screen", "laptop"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("🎮 Hangman ગેમમાં તમારું સ્વાગત છે!")
    while incorrect_guesses < max_attempts:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("શબ્દ:", display_word.strip())
        if "_" not in display_word:
            print(f"\n🎉 અભિનંદન! સાચો શબ્દ '{secret_word}' હતો!")
            break

        guess = input("એક અક્ષર લખો: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ માત્ર એક અક્ષર લખો.\n")
            continue
        if guess in guessed_letters:
            print(f"⚠️ '{guess}' અક્ષર પહેલેથી લખાઈ ગયો છે.\n")
            continue

        guessed_letters.append(guess)
        if guess in secret_word:
            print(f"✅ સરસ! '{guess}' શબ્દમાં છે.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ ખોટો અક્ષર! બાકી તક: {max_attempts - incorrect_guesses}\n")

    if incorrect_guesses == max_attempts:
        print(f"😢 ગેમ પૂરી! સાચો શબ્દ '{secret_word}' હતો.")

if __name__ == "__main__":
    play_hangman()


