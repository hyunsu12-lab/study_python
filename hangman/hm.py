import random
from hm_pic import games, final
from words import RandomWords

words = RandomWords()
random_word = words.get_random_word()

end_game = False
lives = 6
guess_list = []
random_word = random.choice(words)
print(random_word)

for letter in random_word:
    guess_list += "_"
print(guess_list)

while not end_game:
    user_input = input("알파벳을 입력해주세요.").lower()
    if user_input in guess_list:
        print("맞췄던 알파벳 입니다.")

    for index in range(len(random_word)):
        guess_letter = random_word[index]
        if guess_letter == user_input:
            guess_list[index] = guess_letter
            print(guess_list)
    if user_input not in guess_list:
        print("틀렸습니다")
        lives -= 1
        if lives == 0:
            end_game = True
            print("실패 했습니다.")
    if "_" not in guess_list:
        end_game = True
        print("이겼습니다.")
        print(games[lives])

print(guess_list)
print(final)