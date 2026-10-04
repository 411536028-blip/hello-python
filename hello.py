print("Hello, world!")
def calculate_bmi():
    print("=== BMI 體重指數計算器 ===")
    
    try:
        # 取得使用者輸入
        height_cm = float(input("請輸入您的身高 (公分): "))
        weight_kg = float(input("請輸入您的體重 (公斤): "))
        
        # 驗證輸入數據數值是否正常
        if height_cm <= 0 or weight_kg <= 0:
            print("錯誤：身高和體重必須大於 0！")
            return

        # 計算 BMI：體重(公斤) / 身高(公尺)的平方
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        
        # 輸出 BMI 值（保留小數點後一位）
        print(f"\n您的 BMI 指數為：{bmi:.1f}")
        
        # 判斷體重狀態 (根據衛生福利部標準)
        if bmi < 18.5:
            category = "體重過輕"
        elif 18.5 <= bmi < 24:
            category = "健康體位 (正常)"
        elif 24 <= bmi < 27:
            category = "過重"
        elif 27 <= bmi < 30:
            category = "輕度肥胖"
        elif 30 <= bmi < 35:
            category = "中度肥胖"
        else:
            category = "重度肥胖"
            
        print(f"身體狀況評估：{category}")
        
    except ValueError:
        print("錯誤：請輸入有效的數字！")

# 執行程式
if __name__ == "__main__":
    calculate_bmi()
