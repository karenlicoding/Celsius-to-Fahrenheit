celsius = input("請輸入華氏溫度:")
celsius = float(celsius)
if celsius:
    fahrenheit = celsius * 9 / 5 + 32
    print(f"你輸入的溫度華氏{celsius}度是攝氏{fahrenheit}度")
else:
    print("請輸入溫度")