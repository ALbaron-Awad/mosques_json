from json import *


data = load(open("mosques.json"))


def insert_mosques():
        name = input("\nأدخل اسم المسجد :")
        x_coordinates = input("\nأدخل خطوط الطول  :")
        # data.append({"x_coordinates": x})
        y_coordinates = input("\nأدخل خطوط العرض  :")
        # data.append({"y_coordinates": y})
        r = input("\nأدخل البلاغ :")
        # data.append({"report": r})
        data.append({
            "name": name,
            "L_coordinates": x_coordinates,
            "W_coordinates": y_coordinates,
            "report": r
        })
        file = open("mosques.json", "w+")
        file.write(dumps(data))
        file.close()


def display_mosques():
    for x in data:
        print(x)


def delete_mosques():
    display_mosques()
    name = input("\nأدخل أسم المسجد لكي يحدف :")
    for x in data:
        if x["name"] == name:
            data.remove(x)
            print("تم حدف مسجد  ", name)
        else:
            print("الرجاء التأكد من الأسم ")
            file = open("mosques.json", "w+")
            file.write(dumps(data))
            file.close()


def main():
    while True:
        print("\033[H\033[J")
        ask = int(input('\n------------------------------------------\n'
                        'أدخل رقم (1)لإضافة مسجد جديد '
                        '\nأدخل رقم (2) لحذف مسجد '
                        '\n أدخل رقم (3) لعرض المساجد المسجلة'
                        '\n\n~~~~~~~~من فضلك أدخل أختيارك~~~~~~\n\n'))
        if ask == 1:
            insert_mosques()
        elif ask == 2:
            delete_mosques()
        elif ask == 3:
            display_mosques()
        else:
            print('خطأ, الرجاء التأكد من أختيارك !')
            exit()


main()

