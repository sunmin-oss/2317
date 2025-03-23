import pandas as pd
import numpy as np

# 假設我們有一個DataFrame存儲鴻海的歷史價格數據
# df = pd.read_csv('hon_hai_stock_data.csv')

# 這裡是一個示例DataFrame
data = {
    'Date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'Close': np.random.normal(loc=190, scale=10, size=100)  # 模擬的收盤價數據
}
df = pd.DataFrame(data)

# 定義窗口期（例如過去一年的交易日）
window_period = 252  # 大約一年

# 計算突破次數
breakout_level = 200
breakout_count = np.sum(df['Close'] > breakout_level)

# 計算總交易日數
total_days = len(df)

# 計算突破機率
breakout_probability = breakout_count / total_days

print(f"突破{breakout_level}元的機率：{breakout_probability:.2%}")