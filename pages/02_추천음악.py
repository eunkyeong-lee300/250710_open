import streamlit as st

st.set_page_config(page_title="MBTI 여행+책+음악 추천", page_icon="🎶", layout="centered")

st.title("✈️ MBTI로 떠나는 여행 + 책 + 음악 추천")
st.markdown("당신의 MBTI에 따라 어울리는 여행지, 책, 그리고 여행의 감성을 더해줄 음악까지 🎶 함께 추천해드립니다.")
st.markdown("---")

mbti_list = [
    'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
    'ISTP', 'ISFP', 'INFP', 'INTP',
    'ESTP', 'ESFP', 'ENFP', 'ENTP',
    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
]

selected_mbti = st.selectbox("🎯 당신의 MBTI는?", mbti_list)

recommendations = {
    "INFP": {
        "places": [
            ("아이슬란드 🇮🇸", "자연과 고요함 속에서 내면의 이야기를 들을 수 있어요."),
            ("피렌체, 이탈리아 🎨", "예술과 낭만이 가득한 도시는 INFP의 상상력을 자극해요."),
            ("통영, 대한민국 🎣", "바다와 예술이 만나는 도시, 조용한 감성 여행에 딱이에요.")
        ],
        "book": ("『여행의 이유』 – 김영하 ✍️", "작가의 철학과 삶을 따라가며 자신의 감정을 돌아보기에 좋아요."),
        "music": ("김사월 - '비밀' 🎵", "감성적인 분위기와 고요한 여행길에 어울리는 곡입니다.", "https://www.youtube.com/watch?v=bknnRQOUp4o")
    },
    "ESTP": {
        "places": [
            ("바르셀로나, 스페인 ⚽", "에너지 넘치고 활동적인 도시가 ESTP에 잘 맞아요."),
            ("호놀룰루, 하와이 🏄", "모험과 자유로운 분위기를 만끽할 수 있어요."),
            ("도쿄, 일본 🎮", "빠르고 다채로운 환경에서 끝없이 새로운 것을 경험할 수 있어요.")
        ],
        "book": ("『인간 본성에 대하여』 – 스티븐 핑커 📘", "논리적이고 도전적인 사고를 즐기는 ESTP에게 적합한 책이에요."),
        "music": ("Dua Lipa - 'Physical' 💃", "에너지 넘치는 여행길에 어울리는 팝 트랙입니다.", "https://www.youtube.com/watch?v=9HDEHj2yzew")
    },
    "INFJ": {
        "places": [
            ("산토리니, 그리스 🇬🇷", "고요한 바다와 하얀 마을에서 내면 성찰을 할 수 있어요."),
            ("아바나, 쿠바 🎷", "복잡하지 않지만 독특한 문화에서 영감을 받을 수 있어요."),
            ("지베르니, 프랑스 🌸", "모네의 정원이 있는 이곳은 예술 감성을 자극해요.")
        ],
        "book": ("『어떻게 살 것인가』 – 유시민 📖", "깊이 있는 성찰과 인간에 대한 고민을 담아 INFJ의 철학적 사고에 어울려요."),
        "music": ("Sigur Rós - 'Samskeyti' 🌫", "산토리니의 해질녘처럼 고요하고 서정적인 분위기입니다.", "https://www.youtube.com/watch?v=CVZqBuHi6zA")
    },
    "ENTP": {
        "places": [
            ("베를린, 독일 🎧", "변화를 즐기고 새로운 문화를 탐색하는 ENTP에게 이상적인 도시예요."),
            ("시애틀, 미국 ☕", "기술과 창의성이 어우러진 도시에서 활발한 아이디어 교류가 가능해요."),
            ("홍콩, 중국 🌆", "혼잡함 속에서도 질서를 찾아내는 두뇌 싸움이 즐거워요.")
        ],
        "book": ("『크리에이티브 클래스』 – 리처드 플로리다 💡", "도시, 창의성, 혁신을 좋아하는 ENTP에게 자극을 줍니다."),
        "music": ("Imagine Dragons - 'On Top of the World' 🕺", "밝고 다이내믹한 여행길에 기분을 끌어올려주는 곡이에요.", "https://www.youtube.com/watch?v=w5tWYmIOWGk")
    }
    # 다른 유형도 동일하게 추가 가능
}

if selected_mbti:
    st.subheader(f"🌟 {selected_mbti} 유형을 위한 맞춤 여행 추천")

    if selected_mbti in recommendations:
        data = recommendations[selected_mbti]
        
        st.markdown("### 🧳 여행지")
        for place, reason in data["places"]:
            st.markdown(f"- **{place}**  \n  👉 {reason}")
        
        st.markdown("### 📚 책 추천")
        book_title, book_reason = data["book"]
        st.markdown(f"- **{book_title}**  \n  📖 {book_reason}")
        
        st.markdown("### 🎧 여행 음악")
        music_title, music_reason, music_url = data["music"]
        st.markdown(f"- **{music_title}**  \n  🎶 {music_reason}")
        st.markdown(f"[유튜브에서 듣기 ▶️]({music_url})")

    else:
        st.warning("이 MBTI 유형은 아직 준비 중입니다. 곧 업데이트할게요!")

    st.balloons()
