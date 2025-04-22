import streamlit as st

# 국가 정보 데이터 설정
country_data = {
    "대한민국": {
        "capital": "서울",
        "population": "51,780,579 명",
        "languages": "한국어"
    },
    "미국": {
        "capital": "워싱턴 D.C.",
        "population": "331,002,651 명",
        "languages": "영어"
    },
    "프랑스": {
        "capital": "파리",
        "population": "65,273,511 명",
        "languages": "프랑스어"
    },
    "일본": {
        "capital": "도쿄",
        "population": "126,476,461 명",
        "languages": "일본어"
    },
    "영국": {
        "capital": "런던",
        "population": "67,886,011 명",
        "languages": "영어"
    },
    "독일": {
        "capital": "베를린",
        "population": "83,783,942 명",
        "languages": "독일어"
    },
    "중국": {
        "capital": "베이징",
        "population": "1,439,323,776 명",
        "languages": "중국어"
    },
    "인도": {
        "capital": "뉴델리",
        "population": "1,380,004,385 명",
        "languages": "힌디어, 영어"
    },
    "브라질": {
        "capital": "브라질리아",
        "population": "212,559,417 명",
        "languages": "포르투갈어"
    },
    "러시아": {
        "capital": "모스크바",
        "population": "145,912,025 명",
        "languages": "러시아어"
    },
    "캐나다": {
        "capital": "오타와",
        "population": "37,742,154 명",
        "languages": "영어, 프랑스어"
    },
    "호주": {
        "capital": "캔버라",
        "population": "25,499,884 명",
        "languages": "영어"
    },
    "이탈리아": {
        "capital": "로마",
        "population": "60,244,639 명",
        "languages": "이탈리아어"
    },
    # 필요한 경우 추가 국가를 여기에 추가할 수 있습니다.
}

# Streamlit 앱 제목
st.title("🌏국가 정보 조회기")

# 국가 선택 옵션
country_selected = st.selectbox("🎉국가를 선택하세요:", list(country_data.keys()))

# 선택된 국가 정보 표시
if country_selected:
    capital = country_data[country_selected]["capital"]
    population = country_data[country_selected]["population"]
    languages = country_data[country_selected]["languages"]

    st.subheader(f"{country_selected} 정보")
    st.write(f"**🎯수도**: {capital}")
    st.write(f"**🪆인구**: {population}")
    st.write(f"**✒️사용 언어**: {languages}")
