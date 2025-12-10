from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from recommend_problem import recommend_problem

load_dotenv()

llm = ChatGoogleGenerativeAI(
  model = "gemini-2.5-flash-lite",
  temperature = 0.6
)

st.title("Problem Solving 랜덤 문제 추천 랭체인")

platform = st.radio("플랫폼 선택", ["백준", "프로그래머스", "SWEA"], index = None)

if platform == "백준":
  level = st.radio("난이도 선택", ["브론즈", "실버", "골드", "플래티넘", "다이아몬드", "루비"], index = None)
elif platform == "프로그래머스":
  level = st.radio("난이도 선택", [0, 1, 2, 3, 4, 5], index = None)
elif platform == "SWEA":
  level = st.radio("난이도 선택", ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"], index = None)
  
response = None  
  
recommend_button = st.button("랜덤 문제 추천", type = "primary", disabled=(platform == None or level == None or response != None))  
  
if recommend_button:
  with st.spinner("문제 찾는 중..."):
    try:
      response = recommend_problem(llm, platform, level)
      st.write(response)
    except Exception as e:
      st.error(f"예외 발생: {e}")
    
if (response != None):
  reset_button = st.button("리셋", type="secondary")
  if reset_button:
    platform = None
    level = None
    response_content = None