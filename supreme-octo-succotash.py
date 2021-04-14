from tkinter import *
import time


def update():
    global str_lbl_time
    global begin
    global count_errors
    global text

    if begin is None:
        str_lbl_time.set("Начните печатать")
    else:
        time_ = time.time() - begin
        str_lbl_time.set("Время с начала: " + str(round(time.time() - begin, 1)) +
                         "\nКоличество ошибок: " + str(count_errors) +
                         "\nПроцент ошибок: " + str(count_errors * 100 / (count_correct_clicks + count_errors)) +
                         "\nКоличество символов в минуту: " + str(count_correct_clicks * 60 / time_))
    root.after(100, update)


def pf(event):
    global count_correct_clicks
    global begin
    global count_errors
    global text
    global number_line
    global number_symbol

    # мы нажали какую-то специальную клавишу
    if event.char == "":
        return

    # костль для \n
    if event.char == chr(13):
        event.char = "\n"

    # первое нажатие, начинаем отсчет времени
    if begin is None:
        begin = time.time()

    print(ord(event.char), ord(text[count_correct_clicks]))
    # проверяем правильно ли мы нажали кнопку
    if event.char == text[count_correct_clicks]:
        # красим в зеленый то, что написали без ошибок и в желтый, если ошиблись в этой букве
        if "errors" in progress_view.tag_names():
            progress_view.tag_delete("errors")
            progress_view.tag_add("fixed", str(number_line) + "." + str(number_symbol), str(number_line) + "." + str(number_symbol + 1))
            progress_view.tag_config("fixed", background="yellow", foreground="blue")
            print("test")
        else:
            progress_view.tag_add("true", str(number_line) + "." + str(number_symbol), str(number_line) + "." + str(number_symbol + 1))
            progress_view.tag_config("true", background="green", foreground="blue")

        count_correct_clicks += 1
        number_symbol += 1
        if event.char == "\n":
            number_line += 1
            number_symbol = 0
    else:
        count_errors += 1
        # красим в красный ошибку то, что написали
        progress_view.tag_add("errors", str(number_line) + "." + str(number_symbol), str(number_line) + "." + str(number_symbol + 1))
        progress_view.tag_config("errors", background="red", foreground="blue")

    # проверяем, что написали весь тест
    if count_correct_clicks == len(text):
        print(time.time() - begin)
        err = count_errors
        sentence = text
        print(err, "ошибок")
        print(err * 100 / (len(sentence) + err), "процент ошибок")
        time_ = time.time() - begin
        print(time_, "время печати")
        print(len(sentence) * 60 / time_, "колчичество символов в минуту")
        print(len(sentence.split()) * 60 / time_, "количество слов в минуту")
        exit(0)


number_line = 1
number_symbol = 0
count_errors = 0
begin = None
text = "Дядя у тебя шиза. (почти басня про Зайца и Волка)\n\nПриходит однажды Волк к Зайцу и говорит. Слышь заяц ты " \
       "декартач написал? Заяц ответил Волку, что написал. А Волк сказал, а надо было не декартач. Вот так Заяц и " \
       "стал царем зверей, потому что с шизой можно все что захочешь.\n\nAuris enim placitum est in Latine!"
count_correct_clicks = 0

root = Tk()
progress_view = Text(root)
progress_view.insert(INSERT, text)

progress_view.pack()
print(progress_view["state"])

progress_view["state"] = "disable"

root.bind("<Key>", pf)

# progress_view.bind()


str_lbl_time = StringVar()
lbl_time = Label(root, textvariable=str_lbl_time)
lbl_time.pack()
#lbl_time.grid(column=1, row=0)
root.after(100, update)

root.mainloop()
