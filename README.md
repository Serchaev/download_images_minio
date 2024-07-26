# Описание проекта

Этот проект предназначен для скачивания изображений из минио по ссылкам из БД. Он включает в себя скрипт `main.py`, который обрабатывает данные, указанные в файле `links.txt`, и сохраняет результаты в папке `images`.

## Установка и запуск

Чтобы запустить проект, выполните следующие шаги:

1. **Склонируйте репозиторий:**

   ```bash
   git clone <url репозитория>
   cd <название репозитория>
   ```
   

2. **Создайте виртуальное окружение:**

   ```bash
   python -m venv venv
   ```
   

3. **Активируйте виртуальное окружение:**
 
    - В Windows:
       ```bash
       venv\Scripts\activate
       ```
 
    - В macOS и Linux::
       ```bash
       source venv/bin/activate
       ```
   

4. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```
   

5. **Создайте файл links.txt. Добавьте нужные ссылки в файл.**
   

5. **Запустите скрипт:**

   ```bash
   MINIO_URL=<link> python main.py
   ```

## Результаты
После выполнения скрипта результаты будут сохранены в папке "images".
