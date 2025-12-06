# script.rpy - starter script for Тени новой школы
label start:

    # Set up characters
    define b = Character("Беатрис", color="#c080ff")
    define g = Character("Гильберт", color="#80b3ff")
    define d = Character("Дилан", color="#ff8080")
    define s = Character("Стефани", color="#ffb380")
    define m = Character("Миа", color="#ff99cc")
    define k = Character("Крис", color="#ffcc80")
    define e = Character("Ева", color="#a6e3a1")
    define a = Character("Анна Петровна", color="#ffd580")

    scene bg school_hall with fade

    b "Сегодня первый день в новой школе... Меня зовут Беатрис."

    show gilbert neutral at right
    g "Привет. Ты в порядке?"

    menu:
        "Спасибо... Я испугалась.":
            $ gilbert_relation = 1
            b "Спасибо... Я была в ужасе."
            g "Нормально бояться. Главное — что они тебя больше не тронут."
        "Мне не нужна помощь.":
            $ gilbert_relation = 0
            b "Мне не нужна помощь."
            g "Я вмешался не потому, что считаю тебя слабой. Просто... так нельзя."
        "Почему ты вмешался?":
            $ gilbert_relation = 0
            b "Почему ты вмешался? Ты мог пострадать."
            g "Потому что так правильно."

    b "Конец демо. Спасибо за игру."

    return
