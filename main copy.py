# streamlit에 쓸 파일
# ml은 colab
import streamlit as st


# st.title("MachineLearning")
# st.header("주식 예측 프로그램")

import tkinter as tk

# Tkinter 창 설정
root = tk.Tk()
root.title("Company Name Input")

# 라벨 추가
label = tk.Label(root, text="Enter Company Name:")
label.pack()

# 텍스트 입력창 추가
company_name_entry = tk.Entry(root)
company_name_entry.pack()

# 버튼 클릭 시 입력된 값을 출력하는 함수
def show_company_name():
    company_name = company_name_entry.get()
    print("Entered Company Name:", company_name)

# 버튼 추가
button = tk.Button(root, text="Submit", command=show_company_name)
button.pack()

# Tkinter 실행
root.mainloop()