from aiohttp import ClientSession
from asyncio import gather, run
from os import path, makedirs, getenv


async def download_image(session: ClientSession, url: str, save_path: str) -> None:
    async with session.get(url) as response:
        if response.status == 200:
            with open(save_path, 'wb') as file:
                file.write(await response.read())
            print(f"Изображение сохранено по пути: {save_path}")
        else:
            print(f"Ошибка загрузки изображения. Статус-код: {response.status}. Ссылка: {url}")


def read_file_to_list(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return lines


async def main(image_url: str):
    file_path = 'links.txt'
    lines_list = read_file_to_list(file_path)

    makedirs(path.dirname("./images/"), exist_ok=True)

    async with ClientSession() as session:
        for link in lines_list:
            image_name = link.replace("/", ".")[1:-1]
            await download_image(
                session=session,
                url=f"{image_url}{link[1:-1]}",
                save_path=f"./images/{image_name}",
            )


# Запускаем main с помощью asyncio
if __name__ == '__main__':
    minio_url = getenv('MINIO_URL')
    run(main(image_url=minio_url))
