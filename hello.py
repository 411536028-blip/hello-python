print("Hello, world!")
# ANSI 顏色設定
RESET = "\033[0m"
BOLD = "\033[1m"

COLOR_GREEN = "\033[32m"   # 綠色：健康體位
COLOR_YELLOW = "\033[33m"  # 黃色：過重 / 體重過輕
COLOR_RED = "\033[31m"     # 紅色：輕度/中度/重度肥胖


def calculate_bmi():
    print("=== BMI 體重指數計算器 ===")
    
    try:
        height_cm = float(input("請輸入您的身高 (公分): "))
        weight_kg = float(input("請輸入您的體重 (公斤): "))
        
        if height_cm <= 0 or weight_kg <= 0:
            print(f"{COLOR_RED}錯誤：身高和體重必須大於 0！{RESET}")
            return

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        
        # 根據衛福部標準與嚴重程度進行顏色與分類對應
        if bmi < 18.5:
            category = "體重過輕"
            color = COLOR_YELLOW
        elif 18.5 <= bmi < 24:
            category = "健康體位 (正常)"
            color = COLOR_GREEN
        elif 24 <= bmi < 27:
            category = "過重"
            color = COLOR_YELLOW
        elif 27 <= bmi < 30:
            category = "輕度肥胖"
            color = COLOR_RED
        elif 30 <= bmi < 35:
            category = "中度肥胖"
            color = COLOR_RED
        else:
            category = "重度肥胖"
            color = f"{BOLD}{COLOR_RED}"  # 加粗紅字顯示最高警告 level
            
        print(f"\n您的 BMI 指數為：{BOLD}{bmi:.1f}{RESET}")
        print(f"身體狀況評估：{color}{category}{RESET}")
        
    except ValueError:
        print(f"{COLOR_RED}錯誤：請輸入有效的數字！{RESET}")

if __name__ == "__main__":
    calculate_bmi()
