import random
import string


def generate_password(length, conditions):
    # パスワード生成のロジックを実装する
    password = ""

    # チェックボックスの条件に基づいて適切な文字列を作成する
    chars = ""
    if "only_lowercase" in conditions:
        chars += string.ascii_lowercase
    if "include_uppercase" in conditions:
        chars += string.ascii_uppercase
    if "include_numbers" in conditions:
        chars += string.digits
    if "include_symbols" in conditions:
        chars += string.punctuation

    # パスワードの文字数に応じて指定された長さでランダムに生成する
    password = "".join(random.choices(chars, k=length))

    return password
