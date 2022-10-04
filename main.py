import streamlit as st
import time

st.title("streamlit 超入門")

# st.write("Show Image")

# img = Image.open("/Volumes/exssd/Dropbox/スクリーンショット/つなぐ/2022.3-0.png")
# st.image(img, caption="T", use_column_width=True)

st.write("プログレスバーの表示")
"start!!"

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f"Iteration {i+1}")
    bar.progress(i +1)
    time.sleep(0.01)

"Done!!"


left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ")
expander1.write(
    "問い合わせ内容を書く今日のご飯は何でしょうか私にはわかりませんうですね"
)
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ内容を書く")
expander3 = st.expander("問い合わせ")
expander3.write("問い合わせ内容を書く")



# option = st.selectbox(
#     "あなたが好きな数字をおしえてください。",
#     list(range(1, 11))
# )
# "あなたの好きな数字は、", option, "です。"


# text = st.text_input("あなたの趣味を教えて下さい。")
# "あなたの趣味：", text

# condition = st.slider("あなたの今の調子は？", 0, 100, 50)
# "コンディション", condition




# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=["a", "b", "c"]
# )

# st.dataframe(df)
# st.bar_chart(df)

# st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)

# st.table(df.style.highlight_max(axis=0))

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )

# st.map(df)
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""