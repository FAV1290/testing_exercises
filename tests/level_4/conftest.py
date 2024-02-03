import os
import typing
import pytest
import configparser
from random import choice, sample, randint

from functions.level_4.two_students import Student


@pytest.fixture
def student_objects() -> typing.Callable:
    def create_student_objects(quantity: int, target_tg_name: str | None = '@@') -> list[Student]:
        first_names = ['John', 'Jane', 'Ann', 'Kate', 'Matt', 'Jack', 'Sam', 'Emma', 'Mia']
        last_names = ['Smith', 'Brown', 'Garcia', 'Wilson', 'Lopez', 'Moore', 'Clark', 'Nguyen']
        tg_names = [
            'fav1290', 'Sergey_IlinVBG', 'justatrade',
            'shpakdev', 'equalat', 'sanyajedi',
            'melevir', 'Zse117', 'vukitvik',
        ]
        tg_name = lambda x: choice(['@', '']) + choice(tg_names) if x == '@@' else x
        return [Student(choice(first_names), choice(last_names), tg_name(target_tg_name))
            for _ in range(quantity)]
    
    return create_student_objects


@pytest.fixture
def txt_file_with_fixed_lines_quantity() -> typing.Callable:
    filepath = 'count_lines_in_test' + str(randint(100000, 999999)) + '.txt'
    def create_text_file(lines: int, number_sign_lines: int = 0) -> str:
        number_sign_lines = lines if number_sign_lines > lines else number_sign_lines
        number_sign_lines_indexes = sample(range(lines), k=number_sign_lines)
        with open(filepath, 'w') as file_handler:
            for line_index in range(lines):
                if line_index in number_sign_lines_indexes:
                    prefix = ' ' * randint(0, 5) + '#'
                else:
                    prefix = ''
                file_handler.write(prefix + str(line_index) + '\n')
        return filepath
    
    yield create_text_file
    os.remove(filepath)


@pytest.fixture
def config_file() -> typing.Callable:
    filepath = 'fetch_app_config_field' + str(randint(100000, 999999)) + '.ini'
    def create_config_file(section_name: str, contents: typing.Mapping[str, str]) -> str:
        config = configparser.ConfigParser()
        config.add_section(section_name)
        for key, value in contents.items():
            config.set(section_name, key, value)
        with open(filepath, 'w') as config_file_handler:
            config.write(config_file_handler)
        return filepath
        
    yield create_config_file
    os.remove(filepath)
