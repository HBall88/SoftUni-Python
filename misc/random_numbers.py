import random
print(f'-Добре дошли при врачката Марулия.')
print(f'Какво ще желаете?')
print(f'')
print(f'-Искам да стана врач. Какво трябва да направя?')
print(f'')
print(f'-Попаднал си на правилното място. Трябва да преминеш поредица специални тестове. Съгласен ли си?')
print(f'')
answer=input(f'-Въведи отговор - да или не! ')
if answer=="не":
    print(f'')
    print('-Явно все пак не си готов да се докажеш. Усъвършенствай уменията си и се върни пак когато си сигурен в себе си.')
    print(f'')
if answer=="да":
    print(f'')
    print(f'-Страхотно! За целта трябва да минеш през 2 теста! Първият е с числа. Готов ли си?')
    print(f'')
    print(f'-Никога не съм бил по-готов!')
    print(f'')
    print(f'-За целите на първия ти тест ще си намисля няколко на брой числа от 1 до 10, ти трябва да познаеш кои са.')
    print(f'За твое улеснение, ти избираш колко числа да познаваш!')
    print(f'Е, колко числа искаш?')
    print(f'')
    count_numbers=int(input(f'-'))
    print(f'')
    print(f'-Добре, нека са {count_numbers}!')
    if count_numbers%2==0:
        print(f'За да преминеш изпитанието, трябва да уцелиш поне {count_numbers/2} числа!')
        needed_count=count_numbers/2
        guess_counter = 0
    else:
        print(f'За да преминеш изпитанието, трябва да уцелиш поне {count_numbers//2}!')
        needed_count = count_numbers // 2
        guess_counter = 0
    for _ in range(count_numbers):
        number=random.randint(1, 10)

        print(number) #махни този ред след тестовете

        print("")
        print("-Марулия намисли своето число! Сега е твой ред да познаваш!")
        print("")
        guess_number=int(input(f'-Хм... Казвам '))
        if guess_number==number:
            print(f'')
            print(f'-Поздравления! Ти уцели!')
            print(f'')
            guess_counter+=1
        else:
            print(f'')
            print(f'-За съжаление, ти не позна!')
            print(f'')
    if guess_counter >= needed_count:
        print(f'Честито! Ти премина първото изпитание! Започвам да надушвам враческите способности в теб!!!')

    elif guess_counter<needed_count:
        print(f'За съжаление, ти се провали. Но определено в теб има потенциал')
        print(f'Не спирай да го развиваш!')
        exit()

    print(f'')
    print(f'Поздравления за минатото първо изпитание. ')
    print(f'Но макар и да виждам, че си достоен, не съм напълно убедена! ')
    print(f'Трябва да минеш моя специален IQ тест, за да се докажеш напълно!')
    print(f'')
    print(f"-Давайте насам!")
    print(f"")
    questions=["Колко е 69*0?", "Коя е столицата на Китай?", "Къде се намира Айфеловата кула?", "Как се казвам?", "На колко години е човек, роден през 1942 г. (сега сме 2022 г.)", "Как се нарича писателят, чието име започва с Х, по средата има У и завършва на Й? Кажи за какво си мисля"]
    print(f'-Ще ти задам един единствен въпрос и за да минеш теста, трябва да му отговориш вярно! Готов?')
    print(f'')
    print(f'-Абсолютно!')
    q1=random.choice(questions)
    print(q1)
    if q1=="Колко е 69*0?":
        answer_needed=0
        answer_given=int(input("-"))
        if answer_given==answer_needed:
            print(f'')
            print(f'Успешно отговори на въпросa!')
            print(f'Честито, вече си врач при мен!')
            print(f'')
        else:
            print(f'')
            print(f'Eeee, това беше наистина на косъм. Нищо!')
            print(f'Определено в теб има потенциал. Не спирай да го развиваш!')
            exit()
    elif q1=="Коя е столицата на Китай?":
        answer_needed = "Пекин"
        answer_given = str(input("-"))
        if answer_given == answer_needed:
            print(f'')
            print(f'Успешно отговори на въпросa!')
            print(f'Честито, вече си врач при мен!')
            print(f'')
        else:
            print(f'')
            print(f'Eeee, това беше наистина на косъм. Нищо!')
            print(f'Определено в теб има потенциал. Не спирай да го развиваш!')
            exit()
    elif q1=="Къде се намира Айфеловата кула?":
        answer_needed = "Париж"
        answer_given = str(input("-"))
        if answer_given == answer_needed:
            print(f'')
            print(f'Успешно отговори на въпросa!')
            print(f'Честито, вече си врач при мен!')
            print(f'')
        else:
            print(f'')
            print(f'Eeee, това беше наистина на косъм. Нищо!')
            print(f'Определено в теб има потенциал. Не спирай да го развиваш!')
            exit()
    elif q1=="Как се казвам?":
        answer_needed = "Марулия"
        answer_given = str(input("-"))
        if answer_given == answer_needed:
            print(f'')
            print(f'Успешно отговори на въпросa!')
            print(f'Честито, вече си врач при мен!')
            print(f'')
        else:
            print(f'')
            print(f'Eeee, това беше наистина на косъм. Нищо!')
            print(f'Определено в теб има потенциал. Не спирай да го развиваш!')
            exit()
    elif q1=="На колко години е човек, роден през 1942 г. (сега сме 2022 г.)":
        answer_needed = 80
        answer_given = int(input("-"))
        if answer_given == answer_needed:
            print(f'')
            print(f'Успешно отговори на въпросa!')
            print(f'Честито, вече си врач при мен!')
            print(f'')
        else:
            print(f'')
            print(f'Eeee, това беше наистина на косъм. Нищо!')
            print(f'Определено в теб има потенциал. Не спирай да го развиваш!')
            exit()
    elif q1=="Как се нарича писателят, чието име започва с Х, по средата има У и завършва на Й? Кажи за какво си мисля":

        answer_needed = "За мръсни неща"
        answer_given = str(input("-"))
        if answer_given == answer_needed:
            print(f'')
            print(f'Успешно отговори на въпросa!')
            print(f'Честито, вече си врач при мен!')
            print(f'')
        else:
            print(f'')
            print(f'Eeee, това беше наистина на косъм. Нищо!')
            print(f'Определено в теб има потенциал. Не спирай да го развиваш!')
            exit()