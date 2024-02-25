# 指定した自然数より大きい素数を1つ表示するプログラム（by Python）

## 使い方

### int型で対応できる範囲の素数を計算する場合

1. calculate_prime_numbers.pyのコード中の「# 指定した自然数」の段落中の「input_number = 」の後ろの自然数を好きな自然数にする（この自然数より大きい素数が表示されることになる）
   ```python
   input_number =  3000000
   ```
2. ターミナルにて、calculate_prime_numbers.pyを実行する
   ```bash
   $ python calculate_prime_numbers.py
   ```
   表示結果
   ```
   3,000,000 (300万) よりも大きい素数: 3,000,017 (300万17), 入力桁数: 7桁, 素数桁数: 7桁
   実行時間: 0.00016秒
   ```

### 大きい桁数の素数を計算する場合

1. calculate_prime_numbers_with_decimal.pyのコード中の「# 指定した自然数」の段落中の「input_number = Decimal("」の後ろの自然数を好きな自然数に変更する（この自然数より大きい素数が表示されることになる）
   ```python
   input_number = Decimal("10000000000000000000")
   ```
2. その下の「getcontext().prec =」の後ろの値を「1」で指定した桁数より大きくする。（「1」の自然数の桁数が20桁なら21以上の値を指定する）
   ```python
   getcontext().prec = 21  # 精度を設定
   ```
3. ターミナルにて、calculate_prime_numbers_with_decimal.pyを実行する
   ```bash
   $ python calculate_prime_numbers_with_decimal.py
   ```
   表示結果
   ```
   10,000,000,000,000,000,000 (1000京) よりも大きい素数: 10,000,000,000,000,000,051 (1000京 51), 入力桁数: 20桁, 素数桁数: 20桁
   実行時間: 494.15581秒
   ```
