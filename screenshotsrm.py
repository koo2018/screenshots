import os,shutil
from datetime import datetime, date, timedelta

screenshot_folder = 'Снимки экрана'

'''
Алгоритм:
Если на рабочем столе найдены файлы Снимков экрана более чем недельной давности,
то они отправляются в папку Снимки экрана, где раскладываются по годам и месяцам
'''


def main():
    desktop_path = os.environ['HOME'] + "/Desktop"

    if not os.path.isdir(desktop_path):
        print(f'Директория {desktop_path} не найдена')
        return 1

    files = dict()

    for file in os.listdir(desktop_path):
        if 'Снимок экрана' in file:
            cctime = datetime.utcfromtimestamp(os.stat(desktop_path + "/" + file).st_birthtime).strftime('%Y-%m-%d %H:%M:%S')
            files[file] = cctime

    files_to_store = dict()
    edge_day = str(date.today() - timedelta(days=20))

    for file in files:
        if files[file] < edge_day and not file.endswith('.icloud'):
            files_to_store[file] = files[file]

    if files_to_store:
        if not os.path.isdir(desktop_path+"/"+screenshot_folder):
            os.mkdir(desktop_path+"/"+screenshot_folder)

        for file in files_to_store:
            year = files_to_store[file][0:4]
            if not os.path.isdir(os.path.join(desktop_path,screenshot_folder,year)):
                os.mkdir(os.path.join(desktop_path,screenshot_folder,year))

            month = files_to_store[file][5:7]
            if not os.path.isdir(os.path.join(desktop_path,screenshot_folder,year,month)):
                os.mkdir(os.path.join(desktop_path,screenshot_folder,year,month))

            shutil.move(os.path.join(desktop_path,file), os.path.join(desktop_path,screenshot_folder,year,month))


if __name__ ==  '__main__':
    main()