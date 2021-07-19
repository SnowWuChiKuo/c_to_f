# 攝氏('C)轉換成華氏('F)程式

# 讓使用者輸入攝氏溫度
# 然後印出華氏溫度

celsius = input('請輸入攝氏溫度: ')
celsius = float(celsius)
fahrenheit = 9 / 5 * celsius + 32
print('華氏溫度為: ',fahrenheit)