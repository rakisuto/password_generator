import random
import string
import logging


def generate_password(
    length,
    only_lowercase=False,
    include_uppercase=False,
    include_numbers=False,
    include_symbols=False,
):
    password = ""
    try:
        # チェックボックスの条件に基づいて適切な文字列を作成する
        chars = ""
        if only_lowercase:
            chars += string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += string.punctuation

        # パスワードの文字数に応じて指定された長さでランダムに生成する
        password = "".join(random.choices(chars, k=length))

        return password

    except ValueError as e:
        # 例外が発生した場合の処理
        logger = logging.getLogger(__name__)
        logger.error("Error occurred while generating password: %s", str(e))
        return None
