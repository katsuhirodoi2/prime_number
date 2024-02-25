import time
import locale
from decimal import Decimal, getcontext

def find_prime_larger_than(number):
    num = number + Decimal(1)  # 指定した自然数よりも大きい数から開始する
    while True:
        is_prime = True
        for i in range(2, int(num.sqrt()) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            return num
        num += 1

def kanji_number(number):
    digits = ["", "万", "億", "兆", "京", "垓", "𥝱", "穣", "溝", "澗", "正", "載", "極", "恒河沙", "阿僧祇", "那由他", "不可思議", "無量大数"]
    digit_groups = []
    while number > 0:
        number, remainder = divmod(number, 10000)
        digit_groups.append(remainder)
    kanji_representation = ""
    for i, digit_group in enumerate(digit_groups):
        if digit_group == 0:
            continue
        digit_str = str(digit_group)
        if kanji_representation:
            kanji_representation = " " + kanji_representation
        kanji_representation = digit_str + digits[i] + kanji_representation
    return kanji_representation

# 指定した自然数
input_number = Decimal("10000000000000000000")
getcontext().prec = 21  # 精度を設定
start_time = time.time()
prime_number = find_prime_larger_than(input_number)
end_time = time.time()

# カンマ区切りの表示
locale.setlocale(locale.LC_NUMERIC, 'ja_JP.UTF-8')
formatted_input_number = locale.format_string('%d', input_number, grouping=True)
formatted_prime_number = locale.format_string('%d', prime_number, grouping=True)

# 漢数字で表示
kanji_input_number = kanji_number(int(input_number))
kanji_prime_number = kanji_number(int(prime_number))

# 左側の数字の桁数を計算
input_digits = len(str(int(input_number)))
prime_digits = len(str(int(prime_number)))

print(f"{formatted_input_number} ({kanji_input_number}) よりも大きい素数: {formatted_prime_number} ({kanji_prime_number}), 入力桁数: {input_digits}桁, 素数桁数: {prime_digits}桁")
print(f"実行時間: {end_time - start_time:.5f}秒")
