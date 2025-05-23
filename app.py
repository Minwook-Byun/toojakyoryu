import streamlit as st
import base64
from pathlib import Path

# --- 페이지 설정 ---
st.set_page_config(
    page_title="2025 사회서비스 투자 교류회",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 글로벌 스타일 및 CI 색상 정의 ---
PRIMARY_COLOR = "#8BC34A"
PRIMARY_COLOR_LIGHT = "#AED581"
PRIMARY_COLOR_DARK = "#689F38"
TEXT_COLOR_PRIMARY = "#212529"
TEXT_COLOR_SECONDARY = "#495057"
TEXT_COLOR_MUTED = "#6c757d"
BACKGROUND_COLOR_LIGHT_GRAY = "#f8f9fa"
BACKGROUND_COLOR_DARK_GRAY = "#292E33" # 더 세련된 어두운 배경색
WHITE_COLOR = "#FFFFFF"
BORDER_COLOR = "#e0e0e0" # 부드러운 테두리 색상
BOX_SHADOW_LIGHT = "0 4px 8px rgba(0, 0, 0, 0.05)"
BOX_SHADOW_MEDIUM = "0 6px 12px rgba(0, 0, 0, 0.1)"
BOX_SHADOW_DARK = "0 8px 16px rgba(0,0,0,0.15)"

HEADER_HEIGHT_PX = 70
GOOGLE_FORM_URL = "https://forms.gle/6vLUsvaa7XNtTLWz7"
NOTION_PAGE_URL = "https://socialservice.notion.site/2024-e8a776c6420b41819c77ef0c533bbb3b"

# --- 이미지 Base64 인코딩 함수 ---
def image_to_data_uri(file_path_str):
    file_path = Path(file_path_str)
    if not file_path.is_file(): return None
    try:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        ext = file_path.suffix.lower()
        mime_type = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
                     ".gif": "image/gif", ".svg": "image/svg+xml"}.get(ext, "application/octet-stream")
        return f"data:{mime_type};base64,{encoded_string}"
    except Exception: return None

LOGO_MOHW_DATA_URI = image_to_data_uri("mohw_logo.png")
LOGO_KSSI_DATA_URI = image_to_data_uri("kssi_logo.png")
LOGO_MYSC_DATA_URI = image_to_data_uri("mysc_logo.png") # KSIF -> MYSC 로고로 변경

# --- 고정 헤더, FAB 및 전역 스타일 ---
def inject_global_styles_and_header():
    logos_html = ""
    if LOGO_MOHW_DATA_URI: logos_html += f'<img src="{LOGO_MOHW_DATA_URI}" alt="보건복지부" class="header-logo">'
    else: logos_html += '<span class="header-logo-placeholder">보건복지부</span>'
    if LOGO_KSSI_DATA_URI: logos_html += f'<img src="{LOGO_KSSI_DATA_URI}" alt="중앙사회서비스원" class="header-logo">'
    else: logos_html += '<span class="header-logo-placeholder">중앙사회서비스원</span>'
    if LOGO_MYSC_DATA_URI: logos_html += f'<img src="{LOGO_MYSC_DATA_URI}" alt="엠와이소셜컴퍼니(MYSC)" class="header-logo header-logo-mysc">' # alt 텍스트 및 클래스명 변경
    else: logos_html += '<span class="header-logo-placeholder">엠와이소셜컴퍼니(MYSC)</span>'

    nav_items_data = [
        {"label": "행사소개", "id_target": "section-introduction"},
        {"label": "참가안내", "id_target": "section-participation-guide"},
        {"label": "세부일정", "id_target": "section-event-composition"},
        {"label": "연간일정", "id_target": "section-annual-schedule"},
        {"label": "신청방법", "id_target": "section-application-method"},
        {"label": "FAQ", "id_target": "section-faq"},
        {"label": "문의", "id_target": "section-contact"}
    ]
    nav_html_elements = "".join([f'<a href="#{item["id_target"]}" class="header-nav-item">{item["label"]}</a>' for item in nav_items_data])
    scroll_margin_selectors = ", ".join([f"#{item['id_target']}" for item in nav_items_data] + ["#section-hero"])

    global_styles = f"""
    <style>
        @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
        :root {{
            --primary-color: {PRIMARY_COLOR}; --primary-color-light: {PRIMARY_COLOR_LIGHT}; --primary-color-dark: {PRIMARY_COLOR_DARK};
            --text-primary: {TEXT_COLOR_PRIMARY}; --text-secondary: {TEXT_COLOR_SECONDARY}; --text-muted: {TEXT_COLOR_MUTED};
            --background-light-gray: {BACKGROUND_COLOR_LIGHT_GRAY}; --background-dark-gray: {BACKGROUND_COLOR_DARK_GRAY};
            --white-color: {WHITE_COLOR}; --border-color: {BORDER_COLOR};
            --box-shadow-light: {BOX_SHADOW_LIGHT}; --box-shadow-medium: {BOX_SHADOW_MEDIUM}; --box-shadow-dark: {BOX_SHADOW_DARK};
            --header-height: {HEADER_HEIGHT_PX}px;
            --border-radius-sm: 6px; --border-radius-md: 10px; --border-radius-lg: 16px; /* 좀 더 둥글게 */
        }}
        html {{ scroll-behavior: smooth; }}
        body, .stApp {{
            font-family: 'Pretendard', sans-serif !important;
            font-size: 16.5px; /* 기본 폰트 크기 미세 조정 */
            line-height: 1.7; /* 기본 줄간격 조정 */
            color: var(--text-primary);
            background-color: var(--white-color);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}
        {scroll_margin_selectors} {{ scroll-margin-top: calc(var(--header-height) + 30px) !important; }} /* 스크롤 마진 증가 */
        .section {{
            padding: 100px 25px;
            max-width: 1180px; /* 최대 너비 약간 증가 */
            margin-left: auto;
            margin-right: auto;
        }}
        .section-title {{
            font-size: 3rem; /* 타이틀 크기 증가 */
            font-weight: 700; /* Pretendard Bold */
            color: var(--text-primary);
            text-align: center;
            margin-bottom: 30px;
            line-height: 1.3;
            letter-spacing: -0.5px; /* 자간 미세 조정 */
        }}
        .section-subtitle {{ /* 요청 4 수정 */
            font-size: 1.3rem;
            color: var(--text-secondary);
            text-align: center;
            margin-bottom: 75px;
            width: 100%; /* 화면 full 너비 (부모 .section 내에서) */
            max-width: 100%; /* max-width 제거 효과 */
            margin-left: auto;
            margin-right: auto;
            line-height: 1.75;
        }}
        .fixed-header {{
            position: fixed; top: 0; left: 0; width: 100%;
            height: var(--header-height);
            background-color: rgba(255, 255, 255, 0.9); /* 투명도 약간 조정 */
            padding: 0 30px;
            border-bottom: 1px solid var(--border-color);
            z-index: 1000;
            display: flex; justify-content: center; align-items: center;
            box-sizing: border-box;
            backdrop-filter: blur(12px); /* 블러 효과 강화 */
            box-shadow: 0 4px 12px rgba(0,0,0,0.06); /* 그림자 스타일 변경 */
        }}
        .header-content {{
            display: flex; justify-content: space-between; align-items: center;
            width: 100%; max-width: 1200px; height: 100%;
        }}
        .header-logo-group {{ display: flex; align-items: center; gap: 18px; }}
        .header-logo {{ height: 34px; object-fit: contain; }}
        .header-logo-placeholder {{ font-size: 1.05rem; font-weight: 600; color: var(--text-muted); }}
        .header-nav {{ display: flex; align-items: center; }}
        .header-nav-item {{
            text-decoration: none; color: var(--text-secondary);
            font-size: 1.05rem; font-weight: 500;
            padding: 10px 20px;
            margin-left: 12px;
            border-radius: var(--border-radius-md);
            transition: color 0.25s ease, background-color 0.25s ease, transform 0.2s ease;
            position: relative;
        }}
        .header-nav-item:hover, .header-nav-item:focus {{
            color: var(--primary-color-dark);
            background-color: {PRIMARY_COLOR_LIGHT}55; /* 호버 배경색 투명도 추가 */
            transform: translateY(-2px);
        }}
        .header-nav-item::after {{
            content: '';
            position: absolute;
            width: 0;
            height: 3px; /* 밑줄 두께 증가 */
            bottom: 6px; /* 위치 조정 */
            left: 50%;
            transform: translateX(-50%);
            background-color: var(--primary-color-dark);
            border-radius: 2px; /* 밑줄 둥글게 */
            transition: width 0.35s ease;
        }}
        .header-nav-item:hover::after {{ width: 60%; }}
        .fab {{
            position: fixed; bottom: 35px; right: 35px; /* 위치 조정 */
            background: linear-gradient(145deg, var(--primary-color), var(--primary-color-dark)); /* 그라데이션 각도 변경 */
            color: var(--white-color) !important;
            padding: 18px 28px; /* 패딩 증가 */
            border-radius: 60px; /* 더 둥글게 */
            text-decoration: none;
            font-size: 1.1rem; font-weight: 600;
            box-shadow: 0 6px 20px rgba(139, 195, 74, 0.4); /* 그림자 색상 및 강도 조정 */
            z-index: 999;
            display: flex; align-items: center; gap: 12px;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* 트랜지션 효과 변경 */
        }}
        .fab:hover {{
            background: linear-gradient(145deg, var(--primary-color-dark), var(--primary-color));
            transform: translateY(-6px) scale(1.08); /* 호버 효과 강화 */
            box-shadow: 0 10px 25px rgba(104, 159, 56, 0.5);
        }}
        .fab .fab-icon {{ font-size: 1.4rem; }}
        div[data-testid="stAppViewContainer"] > section.main {{ padding-top: calc(var(--header-height) + 30px) !important; }}
        .custom-button {{
            display: inline-block;
            padding: 14px 32px; /* 버튼 패딩 조정 */
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.05rem; /* 버튼 폰트 크기 */
            transition: all 0.3s ease;
            border: 2px solid transparent;
            cursor: pointer;
            letter-spacing: 0.5px; /* 자간 추가 */
        }}
        .button-primary {{
            background-color: var(--primary-color);
            color: var(--white-color) !important;
            box-shadow: var(--box-shadow-light);
        }}
        .button-primary:hover {{
            background-color: var(--primary-color-dark);
            color: var(--white-color) !important;
            transform: translateY(-3px);
            box-shadow: var(--box-shadow-medium);
        }}
        .button-outline {{
            background-color: transparent;
            color: var(--primary-color-dark) !important;
            border-color: var(--primary-color-dark);
        }}
        .button-outline:hover {{
            background-color: var(--primary-color-dark);
            color: var(--white-color) !important;
            transform: translateY(-3px);
            box-shadow: var(--box-shadow-medium);
        }}

        @media (max-width: 992px) {{ .header-nav {{ display: none; }} .header-content {{ justify-content: center; }} }}
        @media (max-width: 576px) {{
            body, .stApp {{ font-size: 15.5px; }}
            .section {{ padding: 60px 20px; }}
            .section-title {{ font-size: 2.4rem; }}
            .section-subtitle {{ font-size: 1.15rem; margin-bottom: 50px;}}
            .fab {{ font-size: 1rem; padding: 15px 22px; bottom:25px; right:25px;}}
            .header-logo {{ height: 30px; }}
            .header-logo-placeholder {{ font-size: 1rem;}}
        }}
    </style>
    <div class="fixed-header"><div class="header-content"><div class="header-logo-group">{logos_html}</div><nav class="header-nav">{nav_html_elements}</nav></div></div>
    <a href="{GOOGLE_FORM_URL}" target="_blank" class="fab"><span class="fab-icon">📝</span> 참가 신청하기</a>
    """
    st.markdown(global_styles, unsafe_allow_html=True)

# --- 1. 히어로 섹션 ---
def display_hero_section():
    first_event_date = "2025년 6월 25일(수)"
    first_event_theme = "국민의 삶의 질을 높이는 AI 사회서비스"
    application_deadline = "2025년 6월 9일(금)"
    hero_html = f"""
    <style>
        /* ... (기존 #section-hero, .hero-bg-elements, .bg-shape, @keyframes float, .hero-content-wrapper, .hero-main-title, .hero-subtitle-text, .hero-key-info 스타일은 이전과 동일하게 유지) ... */
        /* 히어로 섹션의 다른 스타일들은 이전 답변의 최종 버전을 유지합니다. */
        /* 여기서는 CTA 버튼과 관련된 스타일만 변경/추가합니다. */
        #section-hero {{
            background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, {PRIMARY_COLOR_DARK} 100%);
            min-height: 80vh; display: flex; flex-direction: column;
            align-items: center; justify-content: center; text-align: center;
            padding: calc(var(--header-height) + 70px) 25px 70px 25px;
            position: relative; overflow: hidden; color: var(--white-color);
        }}
        #section-hero .hero-bg-elements {{
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            overflow: hidden; z-index: 0;
        }}
        #section-hero .bg-shape {{
            position: absolute; background: rgba(255,255,255,0.08);
            border-radius: 50%; opacity: 0.7; filter: blur(12px);
        }}
        #section-hero .shape1 {{ top: -100px; left: -80px; width: 300px; height: 300px; animation: float 13s infinite ease-in-out; }}
        #section-hero .shape2 {{ bottom: -120px; right: -100px; width: 400px; height: 400px; border-radius: 55% 45% 70% 30% / 40% 60% 40% 60%; animation: float 16s infinite ease-in-out 2.5s; }}
        #section-hero .shape3 {{ top: 15%; right: 5%; width: 180px; height: 180px; animation: float 11s infinite ease-in-out 1.5s; opacity: 0.5; }}

        @keyframes float {{
            0% {{ transform: translateY(0px) rotate(0deg) scale(1); opacity: 0.6; }}
            50% {{ transform: translateY(-25px) rotate(20deg) scale(1.1); opacity: 0.8; }}
            100% {{ transform: translateY(0px) rotate(0deg) scale(1); opacity: 0.6; }}
        }}
        .hero-content-wrapper {{
            position: relative; z-index: 1; max-width: 900px;
        }}
        .hero-main-title {{
            font-size: 3.8rem; font-weight: 800;
            color: var(--white-color); line-height: 1.3; margin-bottom: 25px;
            text-shadow: 3px 3px 12px rgba(0,0,0,0.4);
            animation: fadeInDown 1s ease-out forwards;
        }}
        .hero-subtitle-text {{
            font-size: 1.4rem; color: rgba(255,255,255,0.95);
            line-height: 1.8; margin-bottom: 40px;
            animation: fadeInUp 1s ease-out 0.3s forwards; opacity:0;
            max-width: 750px; margin-left: auto; margin-right: auto;
        }}
        .hero-key-info {{
            background-color: rgba(255,255,255,0.98);
            color: var(--text-primary); padding: 30px 35px;
            border-radius: var(--border-radius-md); margin: 0 auto 30px auto;
            display: block; width: fit-content; max-width: 90%;
            box-shadow: var(--box-shadow-medium); text-align: left;
            animation: fadeInUp 1s ease-out 0.5s forwards; opacity:0;
            border-left: 6px solid {PRIMARY_COLOR_DARK};
        }}
        .hero-key-info h3 {{
            font-size: 1.3rem; font-weight: 700; color: {PRIMARY_COLOR_DARK};
            margin-top: 0; margin-bottom: 20px; text-align: center;
            border-bottom: 2px solid {PRIMARY_COLOR_LIGHT}; padding-bottom: 15px;
        }}
        .hero-key-info p {{
            margin: 14px 0; font-size: 1.1rem; font-weight: 500;
            color: var(--text-secondary);
        }}
        .hero-key-info .info-label {{
            font-weight: 600; color: {PRIMARY_COLOR_DARK};
            min-width: 90px; display: inline-block;
        }}
        .hero-key-info .deadline {{ font-weight: 700; color: #C62828; }}

        .hero-cta-button-container {{
            display: block; margin-top: 10px; /* key-info와 버튼 사이 간격 조정됨 */
            animation: popIn 0.8s ease-out 0.8s forwards; opacity:0;
        }}

        /* 요청 1: 히어로 CTA 버튼 새 디자인 */
        .hero-cta-button.custom-button {{ /* .custom-button 클래스를 활용하여 기본 구조는 가져오되, 히어로 전용으로 덮어쓰기 */
            background: linear-gradient(145deg, {PRIMARY_COLOR_DARK}, {PRIMARY_COLOR});
            color: var(--white-color) !important;
            padding: 18px 40px; /* 기존 패딩 유지 또는 약간 조정 */
            font-size: 1.25rem; /* 폰트 크기 조정 */
            font-weight: 700; /* Pretendard Bold */
            border-radius: 50px;
            text-decoration: none;
            border: none; /* 테두리 제거 */
            box-shadow: 0 5px 15px rgba(0,0,0,0.2), 0 3px 8px {PRIMARY_COLOR_DARK}99; /* 그림자 변경 */
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* 부드러운 트랜지션 */
            display: inline-flex; /* 아이콘과 텍스트 정렬 위해 */
            align-items: center;
            gap: 10px; /* 아이콘과 텍스트 간격 */
            letter-spacing: 0.5px;
        }}
        .hero-cta-button.custom-button:hover {{
            background: linear-gradient(145deg, {PRIMARY_COLOR}, {PRIMARY_COLOR_DARK});
            transform: translateY(-4px) scale(1.03); /* 호버 효과 강화 */
            box-shadow: 0 8px 20px rgba(0,0,0,0.25), 0 5px 12px {PRIMARY_COLOR_DARK}CC;
            color: var(--white-color) !important; /* 호버 시 글자색 유지 */
            border: none; /* 호버 시 테두리 불필요 */
        }}
        .hero-cta-button .cta-icon {{ /* 버튼 내 아이콘 예시 */
            font-size: 1.3em;
            line-height: 1; /* 아이콘 수직 정렬 도움 */
        }}

        @keyframes fadeInDown {{ from {{ opacity: 0; transform: translateY(-50px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        @keyframes fadeInUp {{ from {{ opacity: 0; transform: translateY(50px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        @keyframes popIn {{ 0% {{ opacity: 0; transform: scale(0.6); }} 70% {{ opacity: 1; transform: scale(1.05); }} 100% {{ opacity: 1; transform: scale(1); }} }}

        @media (max-width: 768px) {{
            .hero-main-title {{ font-size: 2.8rem; }}
            .hero-subtitle-text {{ font-size: 1.2rem; margin-bottom:30px; }}
            .hero-key-info {{ padding: 25px; margin-bottom:25px; }}
            .hero-key-info h3 {{ font-size: 1.2rem; }}
            .hero-key-info p {{ font-size: 1rem; }}
            .hero-cta-button.custom-button {{ font-size: 1.1rem; padding: 16px 35px; }}
            #section-hero {{ min-height: 75vh; }}
        }}
    </style>
    <section id="section-hero">
        <div class="hero-bg-elements">
            <div class="bg-shape shape1"></div>
            <div class="bg-shape shape2"></div>
            <div class="bg-shape shape3"></div>
        </div>
        <div class="hero-content-wrapper">
            <h1 class="hero-main-title">2025 사회서비스 투자 교류회</h1>
            <p class="hero-subtitle-text">사회서비스 기업, 투자자, 그리고 유관기관의 만남.<br>혁신적인 사회서비스의 성장과 투자를 연결하는 네트워킹의 장입니다.</p>
        </div>
        <div class="hero-key-info">
            <h3>✨ 제1회 투자 교류회 안내 ✨</h3>
            <p><span class="info-label">일시:</span> {first_event_date}</p>
            <p><span class="info-label">주제:</span> {first_event_theme}</p>
            <p><span class="info-label">신청마감:</span> <span class="deadline">{application_deadline}</span></p>
        </div>
        <div class="hero-cta-button-container">
             <a href="#section-application-method" class="hero-cta-button custom-button">
                <span class="cta-icon">🚀</span> 참가 신청 바로가기
             </a>
        </div>
    </section>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

# --- 2. 행사 소개 및 목적 ---
def display_introduction_section():
    intro_html = f"""
    <style>
        #section-introduction {{ background-color: var(--white-color); }}
        .intro-grid-container {{
            display: grid; grid-template-columns: 1fr; gap: 60px; 
            align-items: center;
        }}
        /* 요청 2: .intro-text-content 내부 요소들 중앙 정렬 */
        .intro-text-content {{ text-align: center; }}
        .intro-text-content h3 {{
            font-size: 2.2rem; font-weight: 700;
            color: var(--primary-color-dark); margin-bottom: 30px; line-height: 1.4;
            letter-spacing: -0.3px;
            /* text-align: center; 이미 부모에서 적용 */
        }}
        .intro-text-content p {{
            font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 22px; line-height: 1.85;
            /* text-align: center; 이미 부모에서 적용 */
            max-width: 700px; /* 중앙 정렬 시 가독성을 위해 p 태그 너비 제한 가능 */
            margin-left: auto;
            margin-right: auto;
        }}
        .intro-text-content p em {{ /* em 태그는 block 이므로 margin auto로 중앙 정렬 */
            color: var(--text-muted); font-style: normal; display: block;
            margin-top: 18px; font-size: 0.95rem; 
            background-color: {BACKGROUND_COLOR_LIGHT_GRAY}; padding: 10px 15px; border-radius: var(--border-radius-sm);
            max-width: 600px; /* 너비 제한 */
            margin-left: auto;
            margin-right: auto;
        }}
        .intro-image-placeholder {{
            background-color: var(--background-light-gray); border-radius: var(--border-radius-lg);
            min-height: 400px; display: flex; align-items: center; justify-content: center;
            font-size: 1.3rem; color: var(--text-muted);
            box-shadow: var(--box-shadow-light); overflow: hidden;
            border: 1px solid var(--border-color);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }}
        .intro-image-placeholder:hover {{ transform: scale(1.03); box-shadow: var(--box-shadow-medium); }}
        .intro-image-placeholder img {{ width: 100%; height: 100%; object-fit: cover; }}
        
        .organizers-section {{ /* 이 부분은 .intro-text-content 밖에 있으므로, text-align: center는 이미 적용됨 */
            margin-top: 80px; text-align: center; padding-top: 60px;
            border-top: 1px solid var(--border-color);
        }}
        .organizers-section h4 {{
            font-size: 1.8rem; color: var(--text-primary); margin-bottom: 40px; font-weight: 600;
        }}
        .organizer-logos-flex {{
            display: flex; justify-content: center; align-items: center;
            gap: 40px; flex-wrap: wrap;
        }}
        .organizer-logo-item {{ 
            width: 180px; height: 60px; display: flex;
            justify-content: center; align-items: center;
        }}
        .organizer-logo-item img {{ 
            max-width: 100%; max-height: 100%; object-fit: contain;
            opacity: 0.8; transition: opacity 0.3s ease, transform 0.3s ease;
        }}
        .organizer-logo-item img:hover {{ opacity: 1; transform: scale(1.05); }}
    </style>
    <section id="section-introduction" class="section">
        <h2 class="section-title">사회서비스 투자, 연결을 넘어 성장으로</h2>
        <p class="section-subtitle">
            국민의 삶의 질을 높이는 혁신적인 사회서비스 기업과<br>
            지속 가능한 성장을 지원하는 투자자 및 유관기관을 연결하여 사회적 가치와 경제적 성과를 함께 창출합니다.
        </p>
        <div class="intro-grid-container">
            <div class="intro-text-content">
                <h3>투자와 협력의 기회를 창출하는 플랫폼</h3>
                <p>「2025 사회서비스 투자 교류회」는 사회서비스 분야의 혁신 기업들이 투자 유치 기회를 확대하고, 투자자 및 유관기관과의 긴밀한 네트워킹을 통해 실질적인 성장을 도모할 수 있도록 마련된 연결의 장입니다. 보건복지부, 중앙사회서비스원, 그리고 엠와이소셜컴퍼니(MYSC)가 함께합니다.</p>
                <p>다양한 사회서비스 기업을 발굴하고 임팩트 투자 연계를 통해 기업의 스케일업을 지원하며, 궁극적으로 국민 모두에게 고품질의 사회서비스가 제공될 수 있는 건강한 생태계 조성을 목표로 합니다.</p>
                <p><em>본 투자 교류회는 2023년부터 시작되어 연간 4-5회 개최되며 사회서비스 투자 생태계 활성화에 기여하고 있습니다.</em></p>
                 <div class="organizers-section">
                    <h4>주최 및 주관</h4>
                    <div class="organizer-logos-flex">
                        <div class="organizer-logo-item">{f'<img src="{LOGO_MOHW_DATA_URI}" alt="보건복지부">' if LOGO_MOHW_DATA_URI else ""}</div>
                        <div class="organizer-logo-item">{f'<img src="{LOGO_KSSI_DATA_URI}" alt="중앙사회서비스원">' if LOGO_KSSI_DATA_URI else ""}</div>
                        <div class="organizer-logo-item">{f'<img src="{LOGO_MYSC_DATA_URI}" alt="엠와이소셜컴퍼니(MYSC)">' if LOGO_MYSC_DATA_URI else ""}</div>
                    </div>
                </div>
            </div>
            <div class="intro-image-placeholder">
                <span>대표 이미지 또는 네트워킹 장면 (예시)</span>
            </div>
        </div>
    </section>
    """
    st.markdown(intro_html, unsafe_allow_html=True)

# --- 3. 참가 안내 (신청 대상) ---
def display_participation_guide_section():
    guide_html = f"""
    <style>
        #section-participation-guide {{ background-color: var(--background-light-gray); }}
        
        .participation-layout-wrapper {{ /* 전체 레이아웃을 감싸는 컨테이너 */
            display: flex;
            flex-direction: column;
            align-items: center; /* 중앙 정렬 */
            gap: 50px; /* 행 간의 간격 및 원과의 간격 */
        }}

        .guide-card-row {{ /* 카드 행을 위한 래퍼 */
            display: grid;
            grid-template-columns: 1fr; /* 기본 1열 */
            gap: 30px;
            width: 100%; /* 부모 너비에 맞춤 */
            max-width: 900px; /* 행의 최대 너비 (카드 2개 배치시 적절하게) */
        }}
        @media (min-width: 768px) {{ /* 태블릿 이상에서 2열 */
            .guide-card-row {{ grid-template-columns: repeat(2, 1fr); }}
        }}

        .guide-card {{
            background-color: var(--white-color);
            border-radius: var(--border-radius-lg); padding: 35px;
            box-shadow: var(--box-shadow-light);
            border: 1px solid var(--border-color);
            border-bottom: 5px solid var(--primary-color-light);
            transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
            display: flex; flex-direction: column;
        }}
        .guide-card:hover {{
            transform: translateY(-10px) scale(1.02);
            box-shadow: var(--box-shadow-dark);
            border-bottom-color: var(--primary-color-dark);
        }}
        .guide-card-title {{
            font-size: 1.7rem; font-weight: 700; color: var(--primary-color-dark);
            margin-bottom: 18px; display: flex; align-items: center;
        }}
        .guide-card-title .title-icon {{
            font-size: 2rem; margin-right: 15px; color: var(--primary-color);
        }}
        .guide-card-description {{
            font-size: 1rem; color: var(--text-secondary); margin-bottom: 28px;
            line-height: 1.75; flex-grow: 1;
        }}
        .guide-card ul {{ list-style-type: none; padding-left: 0; margin: 0; margin-top: auto; }}
        .guide-card li {{
            font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 12px;
            padding-left: 28px; position: relative; line-height: 1.65;
        }}
        .guide-card li::before {{
            content: '✔'; color: var(--primary-color); position: absolute;
            left: 0; font-weight: bold; font-size: 1.2em;
        }}
        
        .central-motif-wrapper {{ /* 원형 모티프 래퍼는 그대로 유지 */
            text-align: center;
            position: relative;
            padding: 20px 0; /* 상하 패딩 추가하여 카드 행과 자연스러운 간격 */
            width: 100%; /* 전체 너비 차지 */
        }}
        .central-circle-motif {{
            width: 200px; /* 원 크기 증가 */
            height: 200px;
            background: linear-gradient(145deg, {PRIMARY_COLOR_LIGHT}, {PRIMARY_COLOR_DARK}); /* 그라데이션 조정 */
            border-radius: 50%;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            color: var(--white-color);
            font-size: 1.6rem; /* 폰트 크기 조정 */
            font-weight: 700; /* 폰트 굵게 */
            text-align: center; line-height: 1.35;
            box-shadow: 0 0 0 8px rgba(255,255,255,0.7), /* 내부 흰색 테두리 */
                        0 0 0 16px {PRIMARY_COLOR}99,  /* 외부 주조색 테두리 (투명도) */
                        0 10px 30px rgba(0,0,0,0.2); /* 그림자 */
            margin: 0 auto;
            animation: pulseEffect 2.8s infinite ease-in-out;
            position: relative; z-index: 1;
            transform-style: preserve-3d; /* 입체감 위한 준비 */
        }}
        .central-circle-motif span {{ 
            letter-spacing: 1.5px; /* 자간 조정 */
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3); /* 텍스트 그림자 */
        }}

        @keyframes pulseEffect {{
            0% {{ transform: scale(0.94); box-shadow: 0 0 0 8px rgba(255,255,255,0.6), 0 0 0 16px {PRIMARY_COLOR}77, 0 8px 25px rgba(0,0,0,0.15);}}
            50% {{ transform: scale(1); box-shadow: 0 0 0 10px rgba(255,255,255,0.8), 0 0 0 20px {PRIMARY_COLOR}AA, 0 12px 35px rgba(0,0,0,0.25);}}
            100% {{ transform: scale(0.94); box-shadow: 0 0 0 8px rgba(255,255,255,0.6), 0 0 0 16px {PRIMARY_COLOR}77, 0 8px 25px rgba(0,0,0,0.15);}}
        }}

        @media (max-width: 767px) {{ /* 모바일에서는 카드 1열, 원 크기 조정 */
             .guide-card-row {{ max-width: 450px; /* 1열일 때 카드 최대 너비 */}}
            .central-circle-motif {{ width: 160px; height: 160px; font-size: 1.4rem; }}
        }}
        @media (max-width: 576px) {{
            .guide-card-title {{ font-size: 1.5rem; }}
            .guide-card-description {{ font-size: 0.95rem; }}
            .guide-card li {{ font-size: 0.9rem; }}
        }}
    </style>
    <section id="section-participation-guide" class="section">
    <h2 class="section-title">참가 안내</h2>
    <p class="section-subtitle">사회서비스 투자 교류회에 참여하여 기업의 성장과 네트워킹 기회를 넓히세요.<br>다양한 유형으로 참여가 가능합니다.</p>

    <div class="participation-layout-wrapper">
        <div class="guide-card-row">
            <div class="guide-card ir-presentation">
                <h3 class="guide-card-title"><span class="title-icon">📢</span> IR 발표 기업</h3>
                <p class="guide-card-description">IR 발표를 통해 투자 유치 기회 확대를 필요로 하는 사회서비스 기업 (회차별 10~12개사)</p>
                <ul><li>IR 발표기업은 투자 유치가 가능한 <strong>‘주식회사’</strong> 형태로 기업 IR 자료 필요</li></ul>
            </div>
            <div class="guide-card">
                <h3 class="guide-card-title"><span class="title-icon">📰</span> 홍보테이블 운영 기업</h3>
                <p class="guide-card-description">기업의 비즈니스 모델(BM) 홍보 및 투자자·유관기관과의 네트워킹을 희망하는 사회서비스 기업 (회차별 5~7개사)</p>
                <ul><li>운영 가능한 테이블만 준비되며, 관련 홍보자료는 참여기업에서 별도 준비</li></ul>
            </div>
        </div>
        <div class="central-motif-wrapper">
            <div class="central-circle-motif">
                <span>투자<br>교류회</span>
            </div>
        </div>
        <div class="guide-card-row">
            <div class="guide-card">
                <h3 class="guide-card-title"><span class="title-icon">🤝</span> 투자자 밋업 기업</h3>
                <p class="guide-card-description">라운드 테이블 미팅에 참여하여 투자자(VC)와의 투자 상담 및 밋업을 희망하는 사회서비스 기업 (회차별 8개사)</p>
                <ul>
                    <li>라운드 테이블 미팅(16:00~17:20)에 참여하여 투자자와 1:1 투자 상담 진행</li>
                    <li>밋업 전 참석하여 행사 참관 가능</li>
                </ul>
            </div>
            <div class="guide-card">
                <h3 class="guide-card-title"><span class="title-icon">👀</span> 참관 및 네트워킹</h3>
                <p class="guide-card-description">사회서비스 투자 교류회 참관 및 네트워킹을 희망하는 기업 또는 기관</p>
                <ul><li>별도 신청 절차는 '신청 방법' 섹션 또는 공지사항을 참고해주십시오.</li></ul>
            </div>
        </div>
    </div> </section>
    """
    st.markdown(guide_html, unsafe_allow_html=True)


# --- 4. 세부 행사 일정 (예시) --- (디자인 고도화 적용)
def display_event_composition_section():
    # detailed_schedule 데이터는 이제 HTML 내부에 직접 작성됩니다.
    composition_html = f"""
    <style>
        #section-event-composition {{
            background-color: {BACKGROUND_COLOR_LIGHT_GRAY};
            font-family: 'Pretendard', sans-serif;
        }}
        .timeline-wrapper {{
            max-width: 900px; margin: 0 auto; position: relative; padding: 30px 0;
        }}
        .timeline-wrapper::before {{
            content: ''; position: absolute; top: 0; left: 50px; bottom: 0; width: 4px;
            background: linear-gradient(to bottom, {PRIMARY_COLOR_LIGHT}, {PRIMARY_COLOR});
            border-radius: 2px; z-index: 0;
        }}
        .timeline-item {{
            display: flex; position: relative; margin-bottom: 40px;
            animation: itemFadeInUp 0.6s ease-out forwards; opacity: 0;
        }}
        .timeline-item:last-child {{ margin-bottom: 0; }}
        .timeline-icon-wrapper {{
            position: absolute; left: 50px; top: 0; transform: translateX(-50%);
            z-index: 2; display: flex; align-items: center; justify-content: center;
        }}
        .timeline-icon {{
            width: 60px; height: 60px; background-color: var(--white-color); color: {PRIMARY_COLOR_DARK};
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-size: 2rem; box-shadow: 0 0 0 5px {PRIMARY_COLOR_LIGHT}BB, var(--box-shadow-medium);
            border: 2px solid var(--white-color);
        }}
        .timeline-content-card {{
            margin-left: 100px; background-color: var(--white-color); padding: 25px 30px;
            border-radius: var(--border-radius-lg); box-shadow: var(--box-shadow-dark);
            flex: 1; border-left: 5px solid {PRIMARY_COLOR}; position: relative;
            transition: transform 0.35s ease, box-shadow 0.35s ease;
        }}
        .timeline-content-card:hover {{
            transform: scale(1.03) translateX(5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.22);
        }}
        .timeline-content-card::before {{
            content: ""; position: absolute; top: 20px; left: -10px;
            border-top: 10px solid transparent; border-bottom: 10px solid transparent;
            border-right: 10px solid {PRIMARY_COLOR};
        }}
        .time-duration-badge {{
            display: inline-block; font-size: 0.9rem;
            font-weight: 700; color: var(--white-color); background-color: {PRIMARY_COLOR_DARK};
            padding: 6px 14px; border-radius: 25px; margin-bottom: 18px;
        }}
        .item-title-text {{
            font-size: 1.5rem; font-weight: 700; color: var(--text-primary);
            margin-top: 0; margin-bottom: 14px;
        }}
        .item-details-text {{
            font-size: 1.05rem; color: var(--text-secondary);
            line-height: 1.75; margin: 0;
        }}
        @keyframes itemFadeInUp {{
            from {{ opacity:0; transform: translateY(35px); }}
            to {{ opacity:1; transform: translateY(0); }}
        }}
        @media (max-width: 768px) {{
            .timeline-wrapper::before {{ left: 30px; }}
            .timeline-icon-wrapper {{ left: 30px; }}
            .timeline-icon {{ width: 50px; height: 50px; font-size: 1.8rem; }}
            .timeline-content-card {{ margin-left: 70px; padding: 20px 25px; }}
            .timeline-content-card::before {{ display:none; }}
            .item-title-text {{ font-size: 1.3rem; }}
            .item-details-text {{ font-size: 0.95rem; }}
        }}
    </style>
    <section id="section-event-composition" class="section">
        <h2 class="section-title">세부 행사 일정 (예시)</h2>
        <p class="section-subtitle">성공적인 투자 유치와 네트워킹을 위한 알찬 프로그램이<br>체계적인 시간 계획 하에 진행됩니다. (아래는 제1회 행사 기준 예시입니다.)</p>
        <div class="timeline-wrapper">
            <div class="timeline-item" style="animation-delay: 0s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">📝</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">13:00 - 13:30 (30분)</span>
                    <h4 class="item-title-text">참가자 등록 및 사전 네트워킹</h4>
                    <p class="item-details-text">행사장 도착, 명찰 수령 및 자료 확인, 자유로운 분위기 속 사전 교류의 시간입니다.</p>
                </div>
            </div>
            <div class="timeline-item" style="animation-delay: 0.1s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">🎉</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">13:30 - 14:10 (40분)</span>
                    <h4 class="item-title-text">개회식 및 사업 안내</h4>
                    <p class="item-details-text">개회 선언, 주최/주관기관 환영사 및 축사, 투자교류회 전반적인 사업 소개, 기념 단체 사진 촬영이 진행됩니다.</p>
                </div>
            </div>
            <div class="timeline-item" style="animation-delay: 0.2s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">🗣️</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">14:10 - 14:20 (10분)</span>
                    <h4 class="item-title-text">홍보 참여기업 소개</h4>
                    <p class="item-details-text">홍보 테이블을 운영하는 참여 기업들의 간략한 소개와 부스 위치 안내가 이루어집니다.</p>
                </div>
            </div>
            <div class="timeline-item" style="animation-delay: 0.3s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">🚀</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">14:20 - 14:55 (35분)</span>
                    <h4 class="item-title-text">IR 발표 (세션 1)</h4>
                    <p class="item-details-text">엄선된 사회서비스 기업들의 투자 유치 발표가 진행됩니다. (5개 기업, 기업당 7분 발표 및 Q&A)</p>
                </div>
            </div>
            <div class="timeline-item" style="animation-delay: 0.4s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">☕</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">14:55 - 15:10 (15분)</span>
                    <h4 class="item-title-text">네트워킹 브레이크 & 홍보부스 관람</h4>
                    <p class="item-details-text">참석자 간 자유로운 네트워킹과 함께 홍보 기업들의 부스를 둘러볼 수 있는 시간입니다.</p>
                </div>
            </div>
            <div class="timeline-item" style="animation-delay: 0.5s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">🚀</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">15:10 - 15:45 (35분)</span>
                    <h4 class="item-title-text">IR 발표 (세션 2)</h4>
                    <p class="item-details-text">계속해서 혁신적인 사회서비스 기업들의 IR 발표가 이어집니다. (5개 기업, 기업당 7분 발표 및 Q&A)</p>
                </div>
            </div>
            <div class="timeline-item" style="animation-delay: 0.6s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">🔄</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">15:45 - 16:00 (15분)</span>
                    <h4 class="item-title-text">네트워킹 브레이크 & 투자 매칭 준비</h4>
                    <p class="item-details-text">잠시 휴식을 취하며, 이어질 라운드 테이블 미팅을 위한 투자자-기업 간 매칭을 최종 점검합니다.</p>
                </div>
            </div>
            <div class="timeline-item" style="animation-delay: 0.7s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">🤝</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">16:00 - 17:20 (80분)</span>
                    <h4 class="item-title-text">라운드 테이블 미팅 (투자자 밋업)</h4>
                    <p class="item-details-text">사전 신청 및 매칭된 투자자와 기업 간의 1:1 심층 투자 상담 및 네트워킹이 진행됩니다. (세션별 순환)</p>
                </div>
            </div>
            <div class="timeline-item" style="animation-delay: 0.8s;">
                <div class="timeline-icon-wrapper"><div class="timeline-icon">🏁</div></div>
                <div class="timeline-content-card">
                    <span class="time-duration-badge">17:20 - 17:30 (10분)</span>
                    <h4 class="item-title-text">폐회 및 마무리 네트워킹</h4>
                    <p class="item-details-text">행사 주요 성과 요약 및 공지사항 전달 후, 자유로운 마무리 네트워킹 시간이 주어집니다.</p>
                </div>
            </div>
        </div>
    </section>
    """
    st.markdown(composition_html, unsafe_allow_html=True)

# --- 5. 2025년 투자 교류회 연간 일정 ---
def display_annual_schedule_section():
    # events_data는 이제 HTML 내부에 직접 작성됩니다.
    annual_schedule_html = f"""
    <style>
        #section-annual-schedule {{ background-color: var(--white-color); }}
        .event-schedule-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(330px, 1fr));
            gap: 40px;
        }}
        .event-schedule-card {{
            background-color: var(--white-color);
            border-radius: var(--border-radius-lg); padding: 35px;
            box-shadow: var(--box-shadow-medium); border: 1px solid var(--border-color);
            display: flex; flex-direction: column;
            transition: transform 0.35s ease, box-shadow 0.35s ease;
            animation: cardPopIn 0.5s ease-out forwards; opacity: 0;
            border-left: 5px solid {PRIMARY_COLOR_LIGHT};
        }}
        .event-schedule-card:hover {{
            transform: translateY(-12px); box-shadow: var(--box-shadow-dark);
            border-left-color: {PRIMARY_COLOR_DARK};
        }}
        .event-schedule-card .card-header {{
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 18px;
        }}
        .event-date-venue {{
            font-size: 0.95rem; font-weight: 600; color: var(--text-muted);
        }}
        .event-status {{
            font-size: 0.85rem; font-weight: 700; color: var(--white-color);
            padding: 6px 14px; border-radius: 25px;
        }}
        .event-theme {{
            font-size: 1.5rem; font-weight: 700; color: var(--primary-color-dark);
            margin-bottom: 15px; line-height: 1.45;
        }}
        .event-time {{
            font-size: 1rem; color: var(--text-secondary); margin-bottom: 18px;
            display: flex; align-items: center;
        }}
        .event-time .icon-time {{ margin-right: 10px; color: {PRIMARY_COLOR_DARK}; font-size: 1.1em; }}
        .event-details {{
            font-size: 1rem; color: var(--text-secondary); line-height: 1.75;
            margin-bottom: 30px; flex-grow: 1;
        }}
        .card-apply-button {{
            margin-top: auto; text-align: center; width: 100%;
            padding-top: 15px; padding-bottom: 15px; font-size: 1.05rem;
        }}
        @keyframes cardPopIn {{
            from {{ opacity: 0; transform: translateY(25px) scale(0.96); }}
            to {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}
        @media (max-width: 768px) {{
            .event-theme {{ font-size: 1.3rem; }}
            .event-details {{ font-size: 0.95rem; }}
        }}
    </style>
    <section id="section-annual-schedule" class="section">
        <h2 class="section-title">2025년 투자 교류회 연간 일정</h2>
        <p class="section-subtitle">올해 진행될 사회서비스 투자 교류회의 주요 일정과 주제를 확인하시고, 성장의 기회를 잡아보세요.</p>
        <div class="event-schedule-grid">
            <div class="event-schedule-card" style="animation-delay: 0s;">
                <div class="card-header">
                    <span class="event-date-venue">2025. 6. 25.(수) / 서울</span>
                    <span class="event-status" style="background-color:{PRIMARY_COLOR};">모집중</span>
                </div>
                <h3 class="event-theme">제1회: 국민의 삶의 질을 높이는 AI 사회서비스</h3>
                <p class="event-time"><strong><i class="icon-time">⏰</i> 시간:</strong> 13:30 ~ 17:30</p>
                <p class="event-details">AI 기술을 활용하여 사회서비스의 효율성과 접근성을 혁신하는 기업을 위한 투자 교류의 장입니다. (참석 규모: 약 80명 내외)</p>
                <a href="#section-application-method" class="card-apply-button custom-button button-primary">세부 정보 확인 및 신청</a>
            </div>
            <div class="event-schedule-card" style="animation-delay: 0.15s;">
                <div class="card-header">
                    <span class="event-date-venue">2025. 8월 예정 / 대전</span>
                    <span class="event-status" style="background-color:{PRIMARY_COLOR_DARK};">모집예정</span>
                </div>
                <h3 class="event-theme">제2회: 돌봄의 공백을 채우는 지역 상생 사회서비스</h3>
                <p class="event-time"><strong><i class="icon-time">⏰</i> 시간:</strong> 미정</p>
                <p class="event-details">지역 사회의 특성을 반영한 맞춤형 돌봄 서비스 및 지역사회 활성화에 기여하는 기업을 발굴합니다.</p>
                <a href="#section-application-method" class="card-apply-button custom-button button-primary">관련 정보 더보기</a>
            </div>
            <div class="event-schedule-card" style="animation-delay: 0.3s;">
                <div class="card-header">
                    <span class="event-date-venue">2025. 9. 9.(화) / aT센터 (서울 강남구)</span>
                    <span class="event-status" style="background-color:{PRIMARY_COLOR_DARK};">모집예정정</span>
                </div>
                <h3 class="event-theme">제3회: 국민의 삶을 HEAL하는 사회서비스</h3>
                <p class="event-time"><strong><i class="icon-time">⏰</i> 시간:</strong> 미정</p>
                <p class="event-details">정신건강, 웰니스, 치유 프로그램 등 국민의 정서적, 신체적 건강 증진을 위한 사회서비스 기업을 지원합니다.</p>
                <a href="#section-application-method" class="card-apply-button custom-button button-primary">관련 정보 더보기</a>
            </div>
        </div>
    </section>
    """
    st.markdown(annual_schedule_html, unsafe_allow_html=True)


# --- 6. 신청 방법 ---
def display_application_method_section():
    application_note = "※ 교류회 주제 및 장소 여건에 따라 선착순 마감될 수 있으며, 선정 기업(기관) 별도 통보 예정" # 요청 2
    application_deadline_text = "2025년 6월 9일(금)까지"

    application_html = f"""
    <style>
        #section-application-method {{
            background-color: {BACKGROUND_COLOR_LIGHT_GRAY}; /* 배경색 변경 */
            text-align: center; padding-bottom: 100px;
        }}
        .application-content {{ max-width: 850px; margin: 0 auto; }} /* 너비 증가 */
        .application-step {{
            background-color: var(--white-color); /* 배경색 변경 */
            padding: 40px; /* 패딩 증가 */
            border-radius: var(--border-radius-lg);
            margin-bottom: 35px; /* 간격 증가 */
            box-shadow: var(--box-shadow-medium); /* 그림자 강화 */
            text-align: left;
            border-left: 6px solid {PRIMARY_COLOR};
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .application-step:hover {{
            transform: translateY(-8px); /* 효과 강화 */
            box-shadow: var(--box-shadow-dark);
        }}
        .application-step-title {{
            font-size: 1.6rem; /* 크기 증가 */
            font-weight: 700; color: {PRIMARY_COLOR_DARK};
            margin-bottom: 20px; /* 간격 증가 */
        }}
        .application-step p {{
            font-size: 1.1rem; /* 크기 증가 */
            color: var(--text-secondary); margin-bottom: 15px; /* 간격 증가 */
            line-height: 1.8;
        }}
        .application-step a.form-link {{
            color: {PRIMARY_COLOR_DARK}; font-weight: 600; text-decoration: none;
            background-color: {PRIMARY_COLOR_LIGHT}66; /* 배경 투명도 */
            padding: 10px 15px; /* 패딩 조정 */
            border-radius: var(--border-radius-sm);
            transition: background-color 0.25s ease, color 0.25s ease;
            display: inline-flex; align-items:center; gap: 8px; /* 아이콘과 텍스트 정렬 */
            margin-top: 8px;
        }}
        .application-step a.form-link:hover {{
            background-color: {PRIMARY_COLOR}; color: var(--white-color);
        }}
        .application-deadline-highlight {{
            font-size: 1.3rem; /* 크기 증가 */
            font-weight: 700; color: var(--white-color);
            background: linear-gradient(135deg, {PRIMARY_COLOR_DARK}, {PRIMARY_COLOR});
            padding: 20px 35px; /* 패딩 증가 */
            border-radius: var(--border-radius-md); display: inline-block;
            margin-top: 20px; margin-bottom: 45px; /* 간격 증가 */
            box-shadow: var(--box-shadow-dark);
        }}
        .download-area {{ margin-top: 55px; }}
        .download-links-title {{
            font-size: 1.5rem; /* 크기 증가 */
            font-weight: 600; color: var(--text-primary);
            margin-bottom: 35px; /* 간격 증가 */
            text-align:center;
        }}
        .download-links-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); /* 너비 조정 */
            gap: 30px; /* 간격 증가 */
            justify-content: center; max-width: 850px; /* 너비 증가 */
            margin: 0 auto;
        }}
        .download-link-button {{ /* 글로벌 .custom-button, .button-outline 활용 */
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            background-color: transparent;
            color: {PRIMARY_COLOR_DARK} !important;
            padding: 28px 20px; /* 패딩 증가 */
            border-radius: var(--border-radius-md); text-decoration: none;
            font-size: 1.05rem; /* 크기 증가 */
            font-weight: 600; border: 2px solid {PRIMARY_COLOR_DARK}; /* 테두리 색상 */
            box-shadow: none; /* 기본 그림자 제거 */
            transition: all 0.3s ease; text-align: center;
            min-height: 100px; /* 높이 증가 */
        }}
        .download-link-button:hover {{
            background-color: {PRIMARY_COLOR_DARK};
            color: var(--white-color) !important;
            border-color: {PRIMARY_COLOR_DARK};
            transform: translateY(-6px) scale(1.03);
            box-shadow: var(--box-shadow-medium);
        }}
        .download-link-button .icon {{
            font-size: 2.2em; /* 아이콘 크기 증가 */
            margin-bottom: 15px; /* 간격 증가 */
        }}
        .application-notice {{ /* 요청 2 문구 추가됨 */
            margin-top: 65px; padding: 30px; /* 패딩 증가 */
            background-color: var(--white-color); /* 배경색 변경 */
            border: 1px solid var(--border-color);
            border-left: 5px solid {TEXT_COLOR_MUTED};
            border-radius: var(--border-radius-md);
            font-size: 1rem; /* 크기 증가 */
            color: var(--text-muted); line-height: 1.8; /* 줄간격 증가 */
            text-align: left; max-width: 800px; /* 너비 증가 */
            margin-left: auto; margin-right: auto;
            box-shadow: var(--box-shadow-light);
        }}
        .application-notice strong {{ color: {PRIMARY_COLOR_DARK}; }}
        .application-notice p:last-child {{ margin-bottom: 0; }}

        @media (max-width: 600px) {{
            .download-links-grid {{ grid-template-columns: 1fr; }}
            .application-step-title {{ font-size: 1.4rem; }}
            .application-step p {{ font-size: 1.05rem; }}
            .application-deadline-highlight {{ font-size: 1.2rem; padding: 18px 25px; }}
            .application-notice {{ text-align: left; }} /* 모바일에서도 좌측 정렬 */
        }}
    </style>
    <section id="section-application-method" class="section">
        <h2 class="section-title">참가 신청 방법</h2>
        <p class="section-subtitle">간단한 절차를 통해 2025 사회서비스 투자 교류회에 참여를 신청하세요.</p>
        <div class="application-content">
            <div class="application-deadline-highlight">
                ✨ 참가 신청 마감: {application_deadline_text} ✨
            </div>
            <div class="application-step">
                <h3 class="application-step-title">Step 1: 참여 정보 확인 및 온라인 신청서 작성</h3>
                <p>IR발표, 홍보테이블 운영, 투자자 밋업 참여를 희망하시는 기업은 아래 '온라인 참가 신청하기' 버튼을 통해 신청 페이지로 이동 후, 기업 정보를 기재하고 제출합니다.</p>
                <p><a href="{GOOGLE_FORM_URL}" target="_blank" class="form-link">➡️ 온라인 참가 신청하기 (Google Form)</a></p>
            </div>
            <div class="application-step">
                <h3 class="application-step-title">Step 2: 제출 서류 준비 및 업로드/이메일 제출</h3>
                <p>참여 유형에 맞는 신청서 및 필요 서류를 아래에서 다운로드 받아 작성 후, 온라인 신청서 내 안내에 따라 업로드하거나 지정된 이메일로 제출해 주십시오.</p>
                <p><em>* 참관 및 네트워킹 참여 희망자는 별도 공지되는 이메일 주소 또는 신청 절차를 확인해주시기 바랍니다. (필요시 양식 다운로드)</em></p>
            </div>
            <div class="download-area">
                <p class="download-links-title">주요 신청 양식 다운로드</p>
                <div class="download-links-grid">
                    {f'<a href="{NOTION_PAGE_URL}" target="_blank" class="download-link-button"><span class="icon">📄</span>참가신청서<br>(발표기업용)</a>' if NOTION_PAGE_URL else ""}
                    {f'<a href="{NOTION_PAGE_URL}" target="_blank" class="download-link-button"><span class="icon">📄</span>참가신청서<br>(홍보기업용)</a>' if NOTION_PAGE_URL else ""}
                    {f'<a href="{NOTION_PAGE_URL}" target="_blank" class="download-link-button"><span class="icon">📄</span>개인정보<br>이용동의서</a>' if NOTION_PAGE_URL else ""}
                </div>
            </div>
            <div class="application-notice">
                <p><strong>[유의사항]</strong><br>{application_note}</p>
            </div>
        </div>
    </section>
    """
    st.markdown(application_html, unsafe_allow_html=True)

# --- 7. FAQ 섹션 --- (디자인 고도화)
def display_faq_section():
    faq_html = f"""
    <style>
        #section-faq {{ background-color: var(--white-color); }}
        .faq-intro {{
            max-width: 850px; /* 너비 증가 */
            margin: 0 auto 60px auto; /* 하단 마진 증가 */
            padding: 30px; /* 패딩 증가 */
            background-color: {BACKGROUND_COLOR_LIGHT_GRAY};
            border-radius: var(--border-radius-md);
            text-align: center;
            font-size: 1.05rem; /* 크기 증가 */
            color: var(--text-secondary);
            border-left: 6px solid {PRIMARY_COLOR}; /* 강조선 두껍게 */
            box-shadow: var(--box-shadow-light);
        }}
        .faq-intro p {{ margin-bottom: 12px; line-height: 1.75; }}
        .faq-intro p:last-child {{ margin-bottom: 0; }}

        .faq-list-container {{ max-width: 900px; margin: 0 auto; }} /* 너비 증가 */
        .faq-item {{
            background-color: var(--white-color);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            margin-bottom: 20px; /* 간격 증가 */
            transition: box-shadow 0.3s ease, border-color 0.3s ease;
            box-shadow: var(--box-shadow-light);
            overflow: hidden; /* 내부 요소 border-radius 적용 위해 */
        }}
        .faq-item:last-child {{ margin-bottom: 0; }}
        .faq-item[open] {{
            box-shadow: var(--box-shadow-medium);
            border-color: {PRIMARY_COLOR_DARK}; /* 열렸을 때 테두리 색상 변경 */
        }}
        .faq-item[open] .faq-question {{
            font-weight: 700; /* Pretendard Bold */
            color: {PRIMARY_COLOR_DARK};
            background-color: {PRIMARY_COLOR_LIGHT}44; /* 배경 투명도 조정 */
            /* border-bottom: 1px solid {PRIMARY_COLOR_LIGHT}; /* 답변과 구분선은 답변 영역의 border-top으로 통일 */
        }}
        .faq-question {{
            padding: 22px 30px; /* 패딩 증가 */
            font-size: 1.2rem; /* 크기 증가 */
            font-weight: 600; /* Pretendard SemiBold */
            color: var(--text-primary);
            cursor: pointer; outline: none; display: block;
            transition: background-color 0.25s ease, color 0.25s ease;
            position: relative;
        }}
        .faq-question:hover {{ background-color: {BACKGROUND_COLOR_LIGHT_GRAY}; }}
        .faq-question::marker, .faq-question::-webkit-details-marker {{ display: none; }}
        .faq-question::before {{ /* 커스텀 마커 (FontAwesome 아이콘 등으로 대체 가능) */
            content: '+'; /* 닫혔을 때 */
            position: absolute; right: 30px; top: 50%;
            transform: translateY(-50%) rotate(0deg);
            color: {PRIMARY_COLOR_DARK}; font-size: 1.5em; /* 아이콘 크기 */
            font-weight: 300; /* 가늘게 */
            transition: transform 0.3s ease, content 0.3s ease; /* content 트랜지션은 일반적으로 안됨, JS 필요 */
        }}
        .faq-item[open] .faq-question::before {{
            content: '−'; /* 열렸을 때 */
            transform: translateY(-50%) rotate(0deg); /* 회전 불필요 */
        }}
        .faq-answer {{
            padding: 25px 30px 30px 30px; /* 패딩 조정 (상단은 질문과 겹치지 않게) */
            font-size: 1.05rem; /* 크기 증가 */
            color: var(--text-secondary); line-height: 1.8;
            background-color: var(--white-color);
            border-top: 1px solid var(--border-color); /* 답변과 질문 구분선 */
        }}
        .faq-answer p {{ margin-bottom: 18px; }}
        .faq-answer p:last-child {{ margin-bottom: 0; }}
        .faq-answer a {{
            color: {PRIMARY_COLOR_DARK}; text-decoration: none; font-weight: 600;
            border-bottom: 2px solid {PRIMARY_COLOR_LIGHT}; /* 밑줄 스타일 변경 */
            padding-bottom: 1px;
            transition: color 0.2s ease, border-bottom-color 0.2s ease;
        }}
        .faq-answer a:hover {{ color: {PRIMARY_COLOR}; border-bottom-color: {PRIMARY_COLOR}; }}
    </style>
    <section id="section-faq" class="section">
        <h2 class="section-title">✅ 모집 FAQ (자주 묻는 질문)</h2>
        <div class="faq-intro">
            <p>❓ 궁금하신 질문을 클릭하시면 답변이 표시됩니다.</p>
            <p>모집 기간 중 수집 된 문의 사항 중 공유가 가능한 답변이 수시로 업데이트 됩니다.</p>
        </div>
        <div class="faq-list-container">
            <details class="faq-item">
                <summary class="faq-question">신청 가능한 ‘사회서비스 기업’은 어떤 곳인가요?</summary>
                <div class="faq-answer">
                    <p>‘사회서비스 기업’은 「사회서비스 이용 및 이용권 관리에 관한 법률」, 「사회보장기본법」에 따라 복지, 보건의료, 교육, 고용, 주거, 문화, 환경 등의 분야에서 상담, 재활, 돌봄, 정보의 제공, 관련 시설의 이용, 역량 개발, 사회참여 지원 등을 통해 국민 삶의 질이 향상되도록 지원하는’ 서비스를 제공하는 기업입니다.</p>
                </div>
            </details>
            <details class="faq-item">
                <summary class="faq-question">지원 신청서 양식은 어디서 다운로드 받을 수 있나요?</summary>
                <div class="faq-answer">
                    <p>본 페이지의 <a href="#section-application-method">신청 양식 다운로드 칸 내(클릭)</a> ‘[첨부1] 참가신청서’와 ‘[첨부2] 개인정보동의서’(총 2개 파일)에서 다운로드 가능합니다.</p>
                </div>
            </details>
            <details class="faq-item">
                <summary class="faq-question">최종 선정 팀 발표는 언제, 어떻게 되나요?</summary>
                <div class="faq-answer">
                    <p>심사 결과는 대표자 이메일 및 유선 연락을 통해 개별 통보되며, 1-2주 이내로 발표될 예정으로 선발 후 오리엔테이션이 진행될 예정입니다.</p>
                </div>
            </details>
            <details class="faq-item">
                <summary class="faq-question">‘소링아(소셜링크아카데미)’가 궁금해요!</summary>
                <div class="faq-answer">
                    <p>소링아(소셜링크아카데미)는 중앙사회서비스원이 주관하고, 엠와이소셜컴퍼니(MYSC)가 함께하는 사회서비스 기업의 투자 유치 역량 강화를 위한 사회서비스 전문 액셀러레이팅 프로그램입니다.</p>
                    <p>기업가치 고도화 및 투자 유치 역량 강화를 필요로 하는 혁신기술 또는 사회서비스 제공 기업을 대상으로 기본교육 및 심화교육을 제공하고 있습니다.</p>
                    <p>상세 내용은 아래 링크 참고 부탁드립니다. <a href="{NOTION_PAGE_URL if NOTION_PAGE_URL else '#'}" target="_blank">소링아에 대해서 자세히 보러 가기(클릭)</a></p>
                </div>
            </details>
        </div>
    </section>
    """
    st.markdown(faq_html, unsafe_allow_html=True)

# --- 8. 문의처 --- (요청 4: 기존 코드를 유지하되, 디자인 고도화)
def display_contact_section():
    contact_email = "social.link.academy@gmail.com"
    phone_number = "02-499-5111"
    operator_name = "프로그램 운영 사무국 (MYSC)"

    section_style = f"""
    <style>
        #section-contact {{
            padding: 100px 25px;
            background-color: var(--white-color); /* 요청 4: 흰색 배경 */
            color: var(--text-primary); /* 기본 텍스트 색상 변경 */
            font-family: 'Pretendard', sans-serif;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        /* 배경 장식 패턴 제거 또는 밝은 테마에 맞게 수정 */
        /* #section-contact::before {{ ... }} */

        #section-contact .content-wrapper {{
            position: relative; z-index: 1;
            max-width: 750px; margin: 0 auto;
        }}
        #section-contact .contact-section-title {{
            font-size: 3rem; font-weight: 700;
            color: var(--text-primary); /* 어두운 색으로 변경 */
            margin-bottom: 25px;
            text-shadow: none; /* 어두운 배경용 텍스트 그림자 제거 */
        }}
        #section-contact .contact-section-subtitle {{
            font-size: 1.3rem;
            color: var(--text-secondary); /* 어두운 색으로 변경 */
            margin-bottom: 60px; line-height: 1.8;
            max-width: 700px; margin-left: auto; margin-right: auto;
        }}
        .contact-card-styled {{
            background-color: var(--background-light-gray); /* 카드 배경은 밝은 회색으로 구분 */
            color: var(--text-primary);
            border-radius: var(--border-radius-lg);
            box-shadow: var(--box-shadow-medium); /* 그림자 조정 */
            padding: 50px; text-align: left;
            max-width: 600px; margin: 0 auto;
            border-top: 6px solid {PRIMARY_COLOR}; /* 상단 강조 테두리 유지 */
            position: relative;
        }}
        /* 카드 위 아이콘 장식 제거 또는 다른 스타일로 변경 */
        /* .contact-card-styled::before {{ ... }} */

        .contact-card-styled h3 {{
            font-size: 2em; font-weight: 600;
            color: {PRIMARY_COLOR_DARK};
            margin-top: 0; margin-bottom: 40px;
            text-align: center;
        }}
        .contact-card-styled p {{
            font-size: 1.2em;
            color: var(--text-secondary); /* 어두운 색으로 변경 */
            line-height: 1.9; margin-bottom: 28px;
            display: flex; align-items: center;
        }}
        .contact-card-styled p:last-child {{ margin-bottom: 0; }}
        .contact-card-styled .icon {{
            margin-right: 20px; font-size: 1.8em;
            color: {PRIMARY_COLOR_DARK}; /* 아이콘 색상 유지 */
            width: 40px; text-align: center;
        }}
        .contact-card-styled strong {{ color: var(--text-primary); font-weight: 600; }}
        .contact-card-styled a {{
            color: {PRIMARY_COLOR_DARK}; /* 링크 색상 유지 */
            text-decoration: none; font-weight: 600;
            border-bottom: 2px solid {PRIMARY_COLOR_LIGHT};
            padding-bottom: 3px;
            transition: color 0.25s ease, border-bottom-color 0.25s ease;
        }}
        .contact-card-styled a:hover {{
            color: {PRIMARY_COLOR};
            border-bottom-color: {PRIMARY_COLOR};
        }}
        @media (max-width: 768px) {{
            #section-contact .contact-section-title {{ font-size: 2.4rem; }}
            #section-contact .contact-section-subtitle {{ font-size: 1.15rem; margin-bottom: 45px; }}
            .contact-card-styled h3 {{ font-size: 1.7em; margin-bottom:35px; }}
            .contact-card-styled p {{ font-size: 1.1em; }}
            .contact-card-styled {{ padding: 40px; }}
        }}
    </style>
    <section id="section-contact">
        <div class="content-wrapper">
            <h2 class="contact-section-title">문의하기</h2>
            <p class="contact-section-subtitle">궁금한 점이 있으시면 언제든지 문의해주세요.<br>행사 운영사무국에서 신속하게 답변드리겠습니다.</p>
            <div class="contact-card-styled">
                <h3>{operator_name}</h3>
                <p><span class="icon">✉️</span><strong>이메일:</strong> <a href="mailto:{contact_email}">{contact_email}</a></p>
                <p><span class="icon">📞</span><strong>연락처:</strong> <a href="tel:{phone_number.replace('-', '')}">{phone_number}</a></p>
            </div>
        </div>
    </section>
    """
    st.markdown(section_style, unsafe_allow_html=True)

# --- 푸터 ---
def display_footer():
    # 요청 3: "한국사회투자" -> "엠와이소셜컴퍼니(MYSC)"
    footer_html = f"""
    <style>
        .page-footer {{
            background-color: var(--background-dark-gray);
            color: var(--text-muted); padding: 70px 25px; /* 패딩 증가 */
            text-align: center; font-size: 1rem; /* 폰트 크기 조정 */
            line-height: 1.75;
            border-top: 1px solid #444; /* 상단 구분선 */
        }}
        .footer-logo-container {{
            margin-bottom: 35px; display: flex;
            justify-content: center; align-items: center;
            gap: 35px; flex-wrap: wrap;
        }}
        /* 요청 5: 로고 크기 강제 적용 */
        .footer-logo-item {{
            width: 170px; /* 각 로고 아이템의 너비 */
            height: 55px; /* 각 로고 아이템의 높이 */
            display: flex; justify-content: center; align-items: center;
        }}
        .footer-logo-item img {{
            max-width: 100%; max-height: 100%;
            object-fit: contain; opacity: 0.65; /* 기본 투명도 조정 */
            filter: grayscale(50%) brightness(150%); /* 톤앤매너 약간 조정 */
            transition: opacity 0.3s ease, filter 0.3s ease, transform 0.3s ease;
        }}
         .footer-logo-item img:hover {{
            opacity: 1; filter: grayscale(0%) brightness(100%);
            transform: scale(1.05);
        }}
        .footer-logo-item span {{ opacity: 0.65; font-weight: 500; }}
        .footer-links {{ margin: 30px 0; }}
        .footer-links a {{
            color: var(--text-muted); text-decoration: none;
            margin: 0 18px; transition: color 0.2s ease, text-decoration 0.2s ease;
            padding-bottom: 4px; border-bottom: 1px solid transparent;
        }}
        .footer-links a:hover {{
            color: var(--primary-color-light); border-bottom-color: var(--primary-color-light);
        }}
        .footer-copyright {{
            margin-top: 25px; font-size: 0.9rem; /* 폰트 크기 */
            color: rgba(255,255,255,0.55);
        }}
         .footer-copyright strong {{ color: rgba(255,255,255,0.75); }}
    </style>
    <footer class="page-footer">
        <div class="footer-logo-container">
            <div class="footer-logo-item">{f'<img src="{LOGO_MOHW_DATA_URI}" alt="보건복지부">' if LOGO_MOHW_DATA_URI else "<span>보건복지부</span>"}</div>
            <div class="footer-logo-item">{f'<img src="{LOGO_KSSI_DATA_URI}" alt="중앙사회서비스원">' if LOGO_KSSI_DATA_URI else "<span>중앙사회서비스원</span>"}</div>
            <div class="footer-logo-item">{f'<img src="{LOGO_MYSC_DATA_URI}" alt="엠와이소셜컴퍼니(MYSC)">' if LOGO_MYSC_DATA_URI else "<span>엠와이소셜컴퍼니(MYSC)</span>"}</div>
        </div>
        <div class="footer-links">
        </div>
        <p class="footer-copyright">© 2025 사회서비스 투자 교류회 운영사무국. All Rights Reserved.<br>본 투자교류회는 <strong>보건복지부, 중앙사회서비스원, 엠와이소셜컴퍼니(MYSC)</strong>가 함께합니다.</p>
    </footer>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

# ===============================================
# === 메인 실행 로직 ===
# ===============================================
def main():
    inject_global_styles_and_header()
    display_hero_section()
    display_introduction_section()
    display_participation_guide_section()
    display_event_composition_section()
    display_annual_schedule_section()
    display_application_method_section()
    display_faq_section()
    display_contact_section()
    display_footer()

if __name__ == "__main__":
    main()
