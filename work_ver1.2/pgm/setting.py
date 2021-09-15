#
# 初期設定
#
# 観測期間と予測期間の設定
# 予測期間：201812 ~ 201801
# 観測期間：201712 ~ 201701
# 
# 【注意事項】：消費税の増税
# 1997年に5％、2014年に8％と段階的に引き上げられ、"2019年10月には10％"
# ※微増は増税によるものかもしれない
# ※増税付近は駆け込み需要が上がる

# ---- 手動設定 ----- #
# 基準年月
kjn_ym = 201801
# 観測期間
n_month = 12
# 予測期間
p_month = 12

# ---- 自動設定 ----- #
# ライブラリ
import pandas as pd
from dateutil.relativedelta import relativedelta

# date型に変換
kjn_ym_dt = pd.to_datetime(str(kjn_ym)+'01')
ym_bef = {'ym_bef%s'% n: (kjn_ym_dt + relativedelta(months=-n)).strftime('%Y%m') for n in range(1, n_month+1)}
ym_aft = {'ym_aft%s'% n: (kjn_ym_dt + relativedelta(months=+n)).strftime('%Y%m') for n in range(0, p_month)}