
<<<<<<< HEAD

"""
создать функцию, которая принимает имя файла и выводит его расширение. Если
расширение у файла определить невзможно, выбросите исключение.
"""
def get_file_extension(file_name: str) -> str:
    """
    Возвращает расширение файла.
    Вызывает исключение, если расширение не удалось определить.

    :param file_name:
    :return:

    """
    dot_index = file_name.rfind(".")
    if 0 <= dot_index < len(file_name) - 1:
        return file_name[dot_index + 1:]
    raise Exception(f"Не удалось определить расширения файла \"{file_name}\"")


def execute_application():
    file_name = input("Введите имя файла с расширением: ")

    try:
        extension = get_file_extension(file_name)
        print(f"Файл \"{file_name}\" имеет расширение \"{extension}\"")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    execute_application()