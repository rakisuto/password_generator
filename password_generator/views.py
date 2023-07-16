from django.shortcuts import render
from .password_gen import generate_password


def password_generator(request):
    if request.method == "POST":
        # フォームからの入力を取得
        password_length = int(request.POST.get("password_length"))  # 文字数
        only_lowercase = bool(request.POST.get("only_lowercase"))  # 英字(小文字のみ)
        include_uppercase = bool(request.POST.get("include_uppercase"))  # 英字(大含む)
        include_numbers = bool(request.POST.get("include_numbers"))  # 数字含む
        include_symbols = bool(request.POST.get("include_symbols"))  # 記号含む

        # パスワードを生成
        password = generate_password(
            password_length,
            only_lowercase=only_lowercase,
            include_uppercase=include_uppercase,
            include_numbers=include_numbers,
            include_symbols=include_symbols,
        )

        # テンプレートにパスワードを渡してレンダリング
        return render(
            request, "password_generator/password.html", {"password": password}
        )

    return render(request, "password_generator/index.html")


def index(request):
    return render(request, "password_generator/index.html")
