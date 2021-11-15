---
# Front matter
title: "Математические основы защиты информации и информационной безопасности.Лабораторная работа №1"
subtitle: "Шифры простой замены"
author: |
 Студент: Лесков Данила Валерьевич НФИмд-02-21  
 Преподаватель: Кулябов Дмитрий Сергеевич


# Generic otions
lang: ru-RU
toc-title: "Содержание"

# Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

# Pdf output format
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
### Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Misc options
indent: true
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Ознакомиться с шифрами простой замены на примере шифра Цезаря и Атбаш.

# Задание

1. Реализовать шифр Цезаря с произвольным ключом k;
2. Реализовать шифр Атбаш.

# Теоретическое введение

## Шифр Цезаря

Данный шифр замены позволяет зашифровать сообщение путем сдвига каждого символа сообщения на произвольный ключ `j`. Таким образом, можно вывести соотношение для [шифра Цезаря [1]](#список-литературы):

$$ T_{m}= {T^{j}}, j = 0,1, ... , m - 1, $$
$$ {T^{j}(a)} = (a + j) mod \ m, $$  

где $T_{m}$ --- циклическая подгруппа; $(a + j)mod \ m$ - операция нахождения остатка от целочисленного деления $a + j$ на $m$.

## Шифр Атбаш

Шифрование Атбаш - шифрование, правило замены которого строится из следующего соотношения:

$$ m − n + 1, $$  

где переменная $m$ - число букв в алфавите; $n$ - порядковый номер заданного символа.
Говоря по простому метод сдвига на порядковый номер буквы в алфавите.

Более подробно о шифрах см. в [@atbash;@caesar].


# Выполнение лабораторной работы

Для выполнения данной работы были описаны два метода: `caesar(message, shift)` для выполнения алгоритма шифрования Цезаря и `atbash(message)` для шифрования Атбаш. Первый метод принимает исходное сообщение и ключ смещения shift, а второй метод только сообщение. Оба метода возвращают зашифрованное сообщение. В качестве алфавита был выбран английский строчный алфавит, а для взаимодействия с ним была использована таблица ASCII (рис. [-@fig:1]).  

![Таблица ASCII](image/ASCII.gif){ #fig:1 width=70% }  

На языке python системные методы `ord()` и `chr()` преобразуют строковой символ в порядковый номер ASCII и обратно соответсвенно. Благодаря этим методам в данной лабораторной работе осуществляется работа со смещением символов строковых элементов.

Более подробно о таблице ASCII и методах работы с ней см. в [@ascii;@pythonim].

## Листинг кода

Программный код был написан на языке python.

```
FIRST_SYMBOL_ACII = 97
LAST_SYMBOL_ACII = 122
alphabet = {"en": 26}
IGNORE_SYMBOLS = " 1234567890-=./[]';<>*-+|?,!"


def caesar(message, shift):
    new_message = ""
    for symbol in message:
        if symbol in IGNORE_SYMBOLS:
            new_message += symbol
            continue
        new_symbol = chr(FIRST_SYMBOL_ACII +
                         ((ord(symbol) - FIRST_SYMBOL_ACII + shift)
                          % alphabet["en"]))
        new_message += new_symbol
    return new_message


def atbash(message):
    new_message = ""
    for symbol in message:
        if symbol in IGNORE_SYMBOLS:
            new_message += symbol
            continue
        new_symbol = chr(FIRST_SYMBOL_ACII +
                         LAST_SYMBOL_ACII -
                         ord(symbol))
        new_message += new_symbol
    return new_message


if __name__ == '__main__':
    while (True):
        code = int(input(
            "Нажмите: \n\t"
            "1 - для работы с шифром цезаря;\n\t"
            "2 - для работы с шифром атбаш;\n\t"
            "0 - для выхода из программы.\n"))
        if (code == 1):
            message = input("Введите сообщение: ")
            shift = int(input("Задайте сдвиг (от 1 до 25): "))
            result = caesar(message, shift)
            print("\nЗашифрованное сообщение (Шифр Цезаря):\n{}"
                  .format(result))
        elif (code == 2):
            message = input("Введите сообщение: ")
            result = atbash(message)
            print("\nЗашифрованное сообщение (Шифр Атбаш):\n{}"
                  .format(result))
        elif (code == 0):
            break
        else:
            print("Ошибка ввода!")

```

## Результаты и анализ выполнения

В результате работы программы производится шифрование методом Цезаря и Атбаш. Для взаимодействия пользователя с программой был организован вывод меню в консоль для выбора пользователем алгоритма шифрования. На рис. [-@fig:2] представлен сценарий выполнения программы шифрования Цезаря:

![Шифр Цезаря](image/output1.png){ #fig:2 width=70% }  

Как видно на рисунке выше, на вход поступает строка, выполняется сдвиг каждой буквы этой строки на 4 символа, а знаки препинания, в свою очередь, остаются без изменений.  
На рис. [-@fig:3] представлен сценарий работы программы, если пользователь выбирает шифрование Атбаш:

![Шифр Атбаш](image/output2.png){ #fig:3 width=70% }  

# Выводы

В ходе выполнения данной лабораторной работы было выполнено ознакомление с шифрами простой замены на примере шиффров Цезаря и Атбаш.  
В результате проделанной работы были реализованы методы шифрования Цезаря и Атбаш. Также были получены навыки работы с функциями преобразования строковых символов в таблицу ASCII.  
Как итог, поставленные цели и задачи были успешно достигнуты.

# Список литературы{.unnumbered}

::: {#refs}
:::