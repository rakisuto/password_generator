import string
import sys
import os

from django.test import TestCase
from .password_gen import generate_password


# プロジェクトのルートディレクトリへのパスを取得
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ルートディレクトリをPythonのモジュールの検索パスに追加
sys.path.append(BASE_DIR)


class PWG_TestCase(TestCase):
    def test_generate_password(self):
        length = 8
        conditions = ["only_lowercase", "include_symbols"]

        password = generate_password(length, conditions)

        self.assertEqual(len(password), length)
        self.assertTrue(any(char in string.ascii_lowercase for char in password))
        self.assertFalse(any(char in string.ascii_uppercase for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

        print(password)
