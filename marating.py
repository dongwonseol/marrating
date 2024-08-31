import streamlit as st
import pandas as pd
import datetime

# Streamlit 페이지 설정
st.set_page_config(page_title="마린이 - 2024 마라톤 대회 정보 및 기록 관리", layout="wide")

# 스타일 정의
st.markdown(
    """
    <style>
    body {
      font-family: 'Noto Sans KR', sans-serif;
      background-color: #f0f8ff;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }
    header {
      text-align: center;
      background-color: #4169e1;
      color: white;
      padding: 20px;
      border-radius: 10px;
      margin-bottom: 20px;
    }
    h1 {
      margin: 0;
      font-size: 2.5em;
    }
    .record-form {
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown(
    """
    <div class="container">
      <header>
        <h1>마린이</h1>
        <p>2024 마라톤 대회 정보 및 기록 관리</p>
      </header>
    </div>
    """,
    unsafe_allow_html=True
)

# Sample Marathon Data
marathons = [
    {"date": "2024-03-17", "name": "서울국제마라톤", "location": "서울", "distance": "42.195km"},
    {"date": "2024-04-14", "name": "벚꽃마라톤", "location": "경주", "distance": "42.195km"},
    {"date": "2024-05-19", "name": "부산국제마라톤", "location": "부산", "distance": "42.195km"},
    {"date": "2024-09-08", "name": "춘천마라톤", "location": "춘천", "distance": "42.195km"},
    {"date": "2024-10-20", "name": "제주마라톤", "location": "제주", "distance": "42.195km"},
    {"date": "2024-11-03", "name": "광주마라톤", "location": "광주", "distance": "42.195km"}
]

# Marathon Schedule Section
st.header("2024년 마라톤 대회 일정")
df_marathons = pd.DataFrame(marathons)
st.table(df_marathons)

# Participant Management Section
st.header("참가 희망자 명단")
participants = []

with st.form("participant_form", clear_on_submit=True):
    participant_name = st.text_input("이름")
    selected_marathon = st.selectbox("대회 선택", df_marathons["name"])
    submit_button = st.form_submit_button("참가 신청")

    if submit_button and participant_name and selected_marathon:
        participants.append({
            "name": participant_name,
            "marathon": selected_marathon,
            "date": df_marathons[df_marathons["name"] == selected_marathon]["date"].values[0]
        })

if participants:
    st.table(pd.DataFrame(participants))

# Personal Record Section
st.header("개인 마라톤 기록")
with st.form("record_form", clear_on_submit=True):
    record_5k = st.number_input("5km 기록 (분)", min_value=0)
    record_10k = st.number_input("10km 기록 (분)", min_value=0)
    record_15k = st.number_input("15km 기록 (분)", min_value=0)
    record_21k = st.number_input("21km 기록 (분)", min_value=0)
    record_full = st.number_input("풀코스 기록 (분)", min_value=0)
    record_submit = st.form_submit_button("기록 저장")

    if record_submit:
        st.write(f"5km: {record_5k}분, 10km: {record_10k}분, 15km: {record_15k}분, 21km: {record_21k}분, 풀코스: {record_full}분")

# Weather Music Recommendation Section
st.header("날씨에 맞는 추천 노래")

weather = ["맑음", "비", "흐림"][datetime.datetime.now().hour % 3]  # 단순히 시간을 이용해 날씨 선택
music_by_weather = {
    "맑음": {"title": "Walking on Sunshine", "artist": "Katrina and The Waves"},
    "비": {"title": "Set Fire to the Rain", "artist": "Adele"},
    "흐림": {"title": "The Sound of Silence", "artist": "Simon & Garfunkel"}
}

music = music_by_weather[weather]
st.write(f"현재 날씨: {weather}")
st.write(f"추천 노래: {music['title']} - {music['artist']}")
