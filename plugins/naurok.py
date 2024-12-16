from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

from pyrogram import Client, filters
from pyrogram.types import Message


async def replace_answer(answer: str) -> str:
    return answer\
        .replace('&nbsp', ' ')\
        .replace('<sup>2</sup> ;', '^2 ')\
        .replace('<sup>3</sup> ;', '^3 ')\
        .replace(' ;', '')


async def get_answers(url: str) -> str:
    if url.startswith('https://') or url.startswith('naurok.com'):
        None
    else:
        url = f'https://naurok.com.ua/test/join?gamecode={url}'

    driver = webdriver.Firefox()

    try:
        driver.get(url)

        sleep(1)

        name_field = driver.find_element(
            By.ID,
            'joinform-name'
        )
        name_field.clear()
        name_field.send_keys('asd')

        sleep(1)

        driver.find_element(
            By.TAG_NAME,
            'button'
        ).click()

        sleep(3)

        test_variants = driver.find_element(
            By.XPATH,
            "//div[contains(@class, 'test-options-grid')]"
        )
        test_variants.find_element(
            By.TAG_NAME,
            'div'
        ).click()

        sleep(5)

        driver.find_element(
            By.CLASS_NAME,
            'endSessionButton'
        ).click()

        sleep(7)

        quest_div = driver.find_element(
            By.CSS_SELECTOR,
            'div.homework-stats'
        )

        quest_blocks = quest_div.find_elements(
            By.CLASS_NAME,
            'homework-stat-options'
        )

        correct_answers = []

        for i in quest_blocks:
            answers = i.find_elements(
                By.CLASS_NAME,
                'homework-stat-option-line'
            )
            correct_answer_block = [
                i for i in answers if 'correct' in i.get_attribute('outerHTML')
            ][0]

            num = correct_answer_block.find_element(
                By.CSS_SELECTOR,
                'span'
            ).get_attribute('innerHTML')

            correct_answer = correct_answer_block.find_element(
                By.CSS_SELECTOR,
                'p'
            ).get_attribute('innerHTML')

            correct_answers.append([num, await replace_answer(correct_answer)])

        answer_text = ''

        for num, i in enumerate(correct_answers, start=1):
            answer_text += f'{num}: {i[0]}) {i[1]}\n'

        return answer_text
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()


@Client.on_message(
    filters.command(
        commands=['naurok'],
        prefixes=['.', '/']
    )
)
async def naurok(_, message: Message):
    answers = await get_answers(message.text.split()[-1])

    await message.reply(
        answers,
        quote=True
    )
