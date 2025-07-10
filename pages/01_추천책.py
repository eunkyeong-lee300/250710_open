import streamlit as st

st.set_page_config(page_title="MBTI 여행+책 추천", page_icon="📖", layout="centered")

st.title("📍 MBTI로 떠나는 여행지 & 책 추천")
st.markdown("당신의 **MBTI**에 따라 딱 맞는 여행지 3곳과 ✨여행 중 읽기 좋은 책 1권✨을 추천해드려요!")
st.markdown("---")

mbti_list = [
    'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
    'ISTP', 'ISFP', 'INFP', 'INTP',
    'ESTP', 'ESFP', 'ENFP', 'ENTP',
    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
]

selected_mbti = st.selectbox("✏️ 당신의 MBTI를 선택하세요", mbti_list)

# 여행지 + 책 추천
recommendations = {
    "INFP": {
        "places": [
            ("아이슬란드 🇮🇸", "자연과 고요함 속에서 내면의 이야기를 들을 수 있어요."),
            ("피렌체, 이탈리아 🎨", "예술과 낭만이 가득한 도시는 INFP의 상상력을 자극해요."),
            ("통영, 대한민국 🎣", "바다와 예술이 만나는 도시, 조용한 감성 여행에 딱이에요.")
        ],
        "book": ("『여행의 이유』 – 김영하 ✍️", "작가의 철학과 삶을 따라가며, 자신의 감정을 돌아보기에 좋은 책입니다.")
    },
    "ESTP": {
        "places": [
            ("바르셀로나, 스페인 ⚽", "에너지 넘치고 활동적인 도시가 ESTP에 잘 맞아요."),
            ("호놀룰루, 하와이 🏄", "모험과 자유로운 분위기를 만끽할 수 있어요."),
            ("도쿄, 일본 🎮", "빠르고 다채로운 환경에서 끝없이 새로운 것을 경험할 수 있어요.")
        ],
        "book": ("『인간 본성에 대하여』 – 스티븐 핑커 📘", "다채로운 인간 행동의 원리를 탐구하는 책으로, 논리적이고 도전적인 사고를 즐기는 ESTP에게 적합해요.")
    },
    "INFJ": {
        "places": [
            ("산토리니, 그리스 🇬🇷", "고요한 바다와 하얀 마을에서 내면 성찰을 할 수 있어요."),
            ("아바나, 쿠바 🎷", "복잡하지 않지만 독특한 문화에서 영감을 받을 수 있어요."),
            ("지베르니, 프랑스 🌸", "모네의 정원이 있는 이곳은 예술 감성을 자극해요.")
        ],
        "book": ("『어떻게 살 것인가』 – 유시민 📖", "깊이 있는 성찰과 인간에 대한 고민을 담아 INFJ의 철학적 사고에 잘 어울려요.")
    },
    "ENTP": {
        "places": [
            ("베를린, 독일 🎧", "변화를 즐기고 새로운 문화를 탐색하는 ENTP에게 이상적인 도시예요."),
            ("시애틀, 미국 ☕", "기술과 창의성이 어우러진 도시에서 활발한 아이디어 교류가 가능해요."),
            ("홍콩, 중국 🌆", "혼잡함 속에서도 질서를 찾아내는 두뇌 싸움이 즐거워요.")
        ],
        "book": ("『크리에이티브 클래스』 – 리처드 플로리다 💡", "도시, 창의성, 혁신을 좋아하는 ENTP에게 탁월한 자극을 줍니다.")
    },
    # 다른 유형들도 동일한 방식으로 추가 가능
}

if selected_mbti:
    st.subheader(f"🌍 {selected_mbti} 유형을 위한 맞춤 추천")

    if selected_mbti in recommendations:
        # 여행지 추천
        st.markdown("### ✈️ 추천 여행지")
        for place, reason in recommendations[selected_mbti]["places"]:
            st.markdown(f"- **{place}**  \n  👉 {reason}")
        
        # 책 추천
        st.markdown("### 📚 여행 중 읽기 좋은 책")
        book_title, book_reason = recommendations[selected_mbti]["book"]
        st.markdown(f"- **{book_title}**  \n  📖 {book_reason}")
    else:
        st.info("아직 이 유형에 대한 데이터가 준비되지 않았어요. 곧 업데이트될 예정입니다.")

    st.balloons()  # 풍선 효과
