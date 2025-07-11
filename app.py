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
BACKGROUND_COLOR_DARK_GRAY = "#000000"
WHITE_COLOR = "#FFFFFF"
BORDER_COLOR = "#e0e0e0"
BOX_SHADOW_LIGHT = "0 4px 8px rgba(0, 0, 0, 0.05)"
BOX_SHADOW_MEDIUM = "0 6px 12px rgba(0, 0, 0, 0.1)"
BOX_SHADOW_DARK = "0 8px 16px rgba(0,0,0,0.15)"

HEADER_HEIGHT_PX = 70
# 실제 구글폼 링크로 변경해야 합니다.
GOOGLE_FORM_URL = "https://forms.gle/your_google_form_link_here" # 예시 링크
# 실제 노션 페이지 또는 파일 다운로드 링크로 변경해야 합니다.
NOTION_PAGE_URL = "https://www.example.com/downloads" # 예시 링크

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

# 로고 파일명을 실제 파일명으로 확인하고, 파일이 코드 실행 위치에 있거나 정확한 경로를 지정해야 합니다.
LOGO_MOHW_DATA_URI = image_to_data_uri("mohw_logo.png")
LOGO_KSSI_DATA_URI = image_to_data_uri("kssi_logo.png")
LOGO_MYSC_DATA_URI = image_to_data_uri("mysc_logo.png")

# --- 고정 헤더, FAB 및 전역 스타일 ---
def inject_global_styles_and_header():
    logos_html = ""
    if LOGO_MOHW_DATA_URI: logos_html += f'<img src="{LOGO_MOHW_DATA_URI}" alt="보건복지부" class="header-logo">'
    else: logos_html += '<span class="header-logo-placeholder">보건복지부</span>'
    if LOGO_KSSI_DATA_URI: logos_html += f'<img src="{LOGO_KSSI_DATA_URI}" alt="중앙사회서비스원" class="header-logo">'
    else: logos_html += '<span class="header-logo-placeholder">중앙사회서비스원</span>'
    if LOGO_MYSC_DATA_URI: logos_html += f'<img src="{LOGO_MYSC_DATA_URI}" alt="엠와이소셜컴퍼니(MYSC)" class="header-logo header-logo-mysc">'
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
            --border-radius-sm: 6px; --border-radius-md: 10px; --border-radius-lg: 16px;
        }}
        html {{ scroll-behavior: smooth; }}
        body, .stApp {{
            font-family: 'Pretendard', sans-serif !important;
            font-size: 16.5px; line-height: 1.7; color: var(--text-primary);
            background-color: var(--white-color);
            -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;
        }}
        {scroll_margin_selectors} {{ scroll-margin-top: calc(var(--header-height) + 30px) !important; }}
        .section {{ padding: 100px 25px; max-width: 1180px; margin-left: auto; margin-right: auto; }}
        .section-title {{ font-size: 3rem; font-weight: 700; color: var(--text-primary); text-align: center; margin-bottom: 30px; line-height: 1.3; letter-spacing: -0.5px; }}
        .section-subtitle {{ font-size: 1.3rem; color: var(--text-secondary); text-align: center; margin-bottom: 75px; width: 100%; max-width: 100%; margin-left: auto; margin-right: auto; line-height: 1.75; }}
        .fixed-header {{
            position: fixed; top: 0; left: 0; width: 100%; height: var(--header-height);
            background-color: rgba(255, 255, 255, 0.9); padding: 0 30px;
            border-bottom: 1px solid var(--border-color); z-index: 1000;
            display: flex; justify-content: center; align-items: center; box-sizing: border-box;
            backdrop-filter: blur(12px); box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        }}
        .header-content {{ display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 1200px; height: 100%; }}
        .header-logo-group {{ display: flex; align-items: center; gap: 18px; }}
        .header-logo {{ height: 34px; object-fit: contain; }}
        .header-logo-placeholder {{ font-size: 1.05rem; font-weight: 600; color: var(--text-muted); }}

        /* === 내비게이션 스타일 수정 시작 === */
        /* 내비게이션 링크들을 담는 컨테이너 */
        .header-nav {{
            display: flex;
            align-items: center;
            gap: 8px; /* 각 링크 사이의 간격을 일정하게 조정 (margin 대신 사용) */
        }}

        /* 개별 내비게이션 링크 아이템 */
        .header-nav-item {{
            position: relative;
            text-decoration: none;
            color: var(--text-secondary);
            font-size: 1.05rem;
            font-weight: 500;
            padding: 10px 18px;
            border-radius: var(--border-radius-md);
            transition: color 0.25s ease, background-color 0.25s ease;
        }}

        /* 마우스를 올리거나 포커스(키보드 탭 등) 됐을 때의 스타일 */
        .header-nav-item:hover, .header-nav-item:focus {{
            color: var(--primary-color-dark);
            background-color: rgba(139, 195, 74, 0.1); /* 매우 투명한 강조 배경색 */
            outline: none;
        }}

        /* 링크 하단에 나타나는 애니메이션 바(bar) */
        .header-nav-item::after {{
            content: '';
            position: absolute;
            bottom: 0;          /* 링크 아이템의 가장 아래쪽에 위치 */
            left: 0;
            right: 0;
            margin: auto;       /* left, right, margin:auto 조합으로 수평 중앙 정렬 */
            width: 0;           /* 기본 너비는 0 (숨겨진 상태) */
            height: 3px;        /* 바의 두께 */
            background: var(--primary-color);
            border-radius: 3px 3px 0 0; /* 위쪽 모서리만 둥글게 */
            transition: width 0.3s ease-in-out; /* 너비가 변할 때 부드러운 애니메이션 */
        }}

        /* 링크에 마우스를 올렸을 때 ::after 요소의 너비를 변경 */
        .header-nav-item:hover::after {{
            width: 80%; /* 링크 너비의 80%만큼 바가 나타남 */
        }}
        /* === 내비게이션 스타일 수정 끝 === */

        .fab {{
            position: fixed; bottom: 35px; right: 35px;
            background: linear-gradient(145deg, var(--primary-color), var(--primary-color-dark));
            color: var(--white-color) !important; padding: 18px 28px; border-radius: 60px;
            text-decoration: none; font-size: 1.1rem; font-weight: 600;
            box-shadow: 0 6px 20px rgba(139, 195, 74, 0.4); z-index: 999;
            display: flex; align-items: center; gap: 12px;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }}
        .fab:hover {{
            background: linear-gradient(145deg, var(--primary-color-dark), var(--primary-color));
            transform: translateY(-6px) scale(1.08); box-shadow: 0 10px 25px rgba(104, 159, 56, 0.5);
        }}
        .fab .fab-icon {{ font-size: 1.4rem; }}
        div[data-testid="stAppViewContainer"] > section.main {{ padding-top: calc(var(--header-height) + 30px) !important; }}
        .custom-button {{
            display: inline-block; padding: 14px 32px; border-radius: 50px; text-decoration: none;
            font-weight: 600; font-size: 1.05rem; transition: all 0.3s ease;
            border: 2px solid transparent; cursor: pointer; letter-spacing: 0.5px;
        }}
        .button-primary {{ background-color: var(--primary-color); color: var(--white-color) !important; box-shadow: var(--box-shadow-light); }}
        .button-primary:hover {{ background-color: var(--primary-color-dark); color: var(--white-color) !important; transform: translateY(-3px); box-shadow: var(--box-shadow-medium); }}
        .button-outline {{ background-color: transparent; color: var(--primary-color-dark) !important; border-color: var(--primary-color-dark); }}
        .button-outline:hover {{ background-color: var(--primary-color-dark); color: var(--white-color) !important; transform: translateY(-3px); box-shadow: var(--box-shadow-medium); }}

        /* --- 참가 신청 방법 - 제출 서류 안내 스타일 --- */
        .required-docs-section {{
            background-color: var(--white-color); padding: 30px; border-radius: var(--border-radius-md);
            margin-bottom: 30px; box-shadow: var(--box-shadow-light); text-align: left;
            border-left: 5px solid {PRIMARY_COLOR_LIGHT};
        }}
        .required-docs-section h4 {{ /* Step 2 제목 */
            font-size: 1.6rem; font-weight: 700; color: {PRIMARY_COLOR_DARK}; 
            margin-bottom: 25px; text-align: center;
        }}
        .required-docs-section h5 {{ /* 각 참가 유형 제목 */
            font-size: 1.2rem; font-weight: 600; color: var(--text-primary); 
            margin-top: 20px; margin-bottom: 10px;
        }}
        .required-docs-section ul {{
            list-style-type: disc; padding-left: 20px; margin-bottom: 15px; 
            font-size: 1.05rem; color: var(--text-secondary);
        }}
        .required-docs-section li {{ margin-bottom: 8px; }}
        .required-docs-section hr {{ 
            margin: 25px 0; border: 0; border-top: 1px solid var(--border-color);
        }}
        .required-docs-section p.notice {{ /* 하단 안내 문구 */
            font-size: 0.95rem; color: var(--text-muted); margin-top: 15px; line-height: 1.6;
        }}


        @media (max-width: 992px) {{ 
            .header-nav {{ display: none; }} 
            .header-content {{ justify-content: center; }} 
            /* 참가 안내 카드 3개를 태블릿에서는 1줄 또는 2줄+1줄로 조정 필요시 */
            #section-participation-guide .guide-card-row {{ grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }}
        }}
        @media (max-width: 767px) {{ /* 모바일 */
             #section-participation-guide .guide-card-row {{ grid-template-columns: 1fr; }}
        }}
        @media (max-width: 576px) {{
            body, .stApp {{ font-size: 15.5px; }}
            .section {{ padding: 60px 20px; }} .section-title {{ font-size: 2.4rem; }}
            .section-subtitle {{ font-size: 1.15rem; margin-bottom: 50px;}}
            .fab {{ font-size: 1rem; padding: 15px 22px; bottom:25px; right:25px;}}
            .header-logo {{ height: 30px; }} .header-logo-placeholder {{ font-size: 1rem;}}
        }}
    </style>
    <div class="fixed-header"><div class="header-content"><div class="header-logo-group">{logos_html}</div><nav class="header-nav">{nav_html_elements}</nav></div></div>
    <a href="https://forms.gle/HLUu8cwfU4STHgF16" target="_blank" class="fab"><span class="fab-icon">📝</span> 참가 신청하기</a>
    """
    st.markdown(global_styles, unsafe_allow_html=True)

# --- 1. 히어로 섹션 ---
def display_hero_section():
    first_event_date = "2025년 8월 4일(월) 13:30"
    first_event_theme = "돌봄의 공백을 채우는 지역 상생 사회서비스"
    application_deadline = "2025년 7월 21일(월) 오후 6시까지(기한 엄수)"

    hero_catchphrase_html = """
        <p style="font-size: 1.5rem; margin-bottom: 0.5em;">사회서비스 기업-투자자-유관기관 연결의 장!</p>
        <p style="font-size: 1.5rem; margin-bottom: 1.5em;">투자 유치 및 홍보를 위한 기회의 장!</p>
    """
    hero_cta_button_text = "🚀 참가 신청 바로가기"

    # (히어로 섹션 HTML 및 내부 CSS는 이전 답변과 동일하게 유지 - 구조 변경 없음)
    hero_html = f"""
    <style>
        #section-hero {{
            background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, {PRIMARY_COLOR_DARK} 100%);
            min-height: 80vh; display: flex; flex-direction: column;
            align-items: center; justify-content: center; text-align: center;
            padding: calc(var(--header-height) + 70px) 25px 70px 25px;
            position: relative; overflow: hidden; color: var(--white-color);
        }}
        #section-hero .hero-bg-elements {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; z-index: 0; }}
        #section-hero .bg-shape {{ position: absolute; background: rgba(255,255,255,0.08); border-radius: 50%; opacity: 0.7; filter: blur(12px); }}
        #section-hero .shape1 {{ top: -100px; left: -80px; width: 300px; height: 300px; animation: float 13s infinite ease-in-out; }}
        #section-hero .shape2 {{ bottom: -120px; right: -100px; width: 400px; height: 400px; border-radius: 55% 45% 70% 30% / 40% 60% 40% 60%; animation: float 16s infinite ease-in-out 2.5s; }}
        #section-hero .shape3 {{ top: 15%; right: 5%; width: 180px; height: 180px; animation: float 11s infinite ease-in-out 1.5s; opacity: 0.5; }}
        @keyframes float {{ 0% {{ transform: translateY(0px) rotate(0deg) scale(1); opacity: 0.6; }} 50% {{ transform: translateY(-25px) rotate(20deg) scale(1.1); opacity: 0.8; }} 100% {{ transform: translateY(0px) rotate(0deg) scale(1); opacity: 0.6; }} }}
        .hero-content-wrapper {{ position: relative; z-index: 1; max-width: 900px; }}
        .hero-main-title {{ font-size: 3.8rem; font-weight: 800; color: var(--white-color); line-height: 1.3; margin-bottom: 25px; text-shadow: 3px 3px 12px rgba(0,0,0,0.4); animation: fadeInDown 1s ease-out forwards; }}
        .hero-catchphrase-container {{
            font-size: 1.4rem; color: rgba(255,255,255,0.95);
            line-height: 1.8; margin-bottom: 40px;
            animation: fadeInUp 1s ease-out 0.3s forwards; opacity:0;
            max-width: 750px; margin-left: auto; margin-right: auto;
        }}
        .hero-key-info {{
            background-color: rgba(255,255,255,0.98); color: var(--text-primary); padding: 30px 35px;
            border-radius: var(--border-radius-md); margin: 0 auto 30px auto;
            display: block; width: fit-content; max-width: 90%;
            box-shadow: var(--box-shadow-medium); text-align: left;
            animation: fadeInUp 1s ease-out 0.5s forwards; opacity:0;
            border-left: 6px solid {PRIMARY_COLOR_DARK};
        }}
        .hero-key-info h3 {{ font-size: 1.3rem; font-weight: 700; color: {PRIMARY_COLOR_DARK}; margin-top: 0; margin-bottom: 20px; text-align: center; border-bottom: 2px solid {PRIMARY_COLOR_LIGHT}; padding-bottom: 15px; }}
        .hero-key-info p {{ margin: 14px 0; font-size: 1.1rem; font-weight: 500; color: var(--text-secondary); }}
        .hero-key-info .info-label {{ font-weight: 600; color: {PRIMARY_COLOR_DARK}; min-width: 90px; display: inline-block; }}
        .hero-key-info .deadline {{ font-weight: 700; color: #C62828; }}
        .hero-cta-button-container {{ display: block; margin-top: 10px; animation: popIn 0.8s ease-out 0.8s forwards; opacity:0; }}
        .hero-cta-button.custom-button {{
            background: linear-gradient(145deg, {PRIMARY_COLOR_DARK}, {PRIMARY_COLOR});
            color: var(--white-color) !important; padding: 18px 40px; font-size: 1.25rem; font-weight: 700;
            border-radius: 50px; text-decoration: none; border: none;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2), 0 3px 8px {PRIMARY_COLOR_DARK}99;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: inline-flex; align-items: center; gap: 10px; letter-spacing: 0.5px;
        }}
        .hero-cta-button.custom-button:hover {{
            background: linear-gradient(145deg, {PRIMARY_COLOR}, {PRIMARY_COLOR_DARK});
            transform: translateY(-4px) scale(1.03);
            box-shadow: 0 8px 20px rgba(0,0,0,0.25), 0 5px 12px {PRIMARY_COLOR_DARK}CC;
        }}
        .hero-cta-button .cta-icon {{ font-size: 1.3em; line-height: 1; }}
        @keyframes fadeInDown {{ from {{ opacity: 0; transform: translateY(-50px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        @keyframes fadeInUp {{ from {{ opacity: 0; transform: translateY(50px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        @keyframes popIn {{ 0% {{ opacity: 0; transform: scale(0.6); }} 70% {{ opacity: 1; transform: scale(1.05); }} 100% {{ opacity: 1; transform: scale(1); }} }}
        @media (max-width: 768px) {{
            .hero-main-title {{ font-size: 2.8rem; }}
            .hero-catchphrase-container {{ font-size: 1.2rem; margin-bottom:30px; }}
            .hero-key-info {{ padding: 25px; margin-bottom:25px; }}
            .hero-key-info h3 {{ font-size: 1.2rem; }} .hero-key-info p {{ font-size: 1rem; }}
            .hero-cta-button.custom-button {{ font-size: 1.1rem; padding: 16px 35px; }}
            #section-hero {{ min-height: 75vh; }}
        }}
    </style>
    <section id="section-hero">
        <div class="hero-bg-elements"> <div class="bg-shape shape1"></div> <div class="bg-shape shape2"></div> <div class="bg-shape shape3"></div> </div>
        <div class="hero-content-wrapper">
            <h1 class="hero-main-title">2025 사회서비스 투자 교류회</h1>
            <div class="hero-catchphrase-container">{hero_catchphrase_html}</div>
        </div>
        <div class="hero-key-info">
            <h3>✨ 제2회 투자 교류회 안내 ✨</h3>
            <p><span class="info-label">일시:</span> {first_event_date}</p>
            <p><span class="info-label">주제:</span> {first_event_theme}</p>
            <p><span class="info-label">신청마감:</span> <span class="deadline">{application_deadline}</span></p>
            <p><span class="info-label"></span>장소: 대전테크노파크 디스테이션 10층 <span class="deadline"></span></p>
        </div>
        <div class="hero-cta-button-container">
            <a href="https://forms.gle/HLUu8cwfU4STHgF16" class="hero-cta-button custom-button">
                {hero_cta_button_text}
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
        .intro-grid-container {{ display: grid; grid-template-columns: 1fr; gap: 60px; align-items: center; }}
        .intro-text-content {{ text-align: center; }}
        /* 옮겨진 문단 스타일 */
        .intro-text-content .moved-paragraph {{
            font-style: italic;
            color: var(--text-muted);
            background-color: #f0f0f0; /* 이전 코드의 #f0f0f0 유지 또는 var(--background-light-gray) 사용 가능 */
            padding: 15px;
            border-radius: var(--border-radius-sm); /* 8px 대신 글로벌 변수 사용 */
            text-align: center;
            max-width: 700px;
            margin: 30px auto; /* 위아래 간격 및 중앙 정렬 */
        }}
        .intro-text-content h3 {{ font-size: 2.2rem; font-weight: 700; color: var(--primary-color-dark); margin-bottom: 30px; line-height: 1.4; letter-spacing: -0.3px; }}
        .intro-text-content p {{ font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 22px; line-height: 1.85; max-width: 700px; margin-left: auto; margin-right: auto; }}
        .intro-image-placeholder {{ background-color: var(--background-light-gray); border-radius: var(--border-radius-lg); min-height: 400px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; color: var(--text-muted); box-shadow: var(--box-shadow-light); overflow: hidden; border: 1px solid var(--border-color); transition: transform 0.4s ease, box-shadow 0.4s ease; }}
        .intro-image-placeholder:hover {{ transform: scale(1.03); box-shadow: var(--box-shadow-medium); }}
        .intro-image-placeholder img {{ width: 100%; height: 100%; object-fit: cover; }}
        .organizers-section {{ margin-top: 80px; text-align: center; padding-top: 60px; border-top: 1px solid var(--border-color); }}
        .organizers-section h4 {{ font-size: 1.8rem; color: var(--text-primary); margin-bottom: 40px; font-weight: 600; }}
        .organizer-logos-flex {{ display: flex; justify-content: center; align-items: center; gap: 40px; flex-wrap: wrap; }}
        .organizer-logo-item {{ width: 180px; height: 60px; display: flex; justify-content: center; align-items: center; }}
        .organizer-logo-item img {{ max-width: 100%; max-height: 100%; object-fit: contain; opacity: 0.8; transition: opacity 0.3s ease, transform 0.3s ease; }}
        .organizer-logo-item img:hover {{ opacity: 1; transform: scale(1.05); }}
    </style>
    <section id="section-introduction" class="section">
        <div class="intro-grid-container">
            <div class="intro-text-content">
                <h3>투자와 협력의 기회를 창출하는 플랫폼</h3>
                <p>보건복지부, 중앙사회서비스원, 그리고 엠와이소셜컴퍼니(MYSC)가 함께 하는 <br> 2025 사회서비스 투자 교류회는 사회서비스 분야의 혁신 기업들이 투자 유치 기회를 확대하고,  <br> 투자자 및 유관기관과의 긴밀한 네트워킹을 통해 실질적인 성장을 도모할 수 있도록 마련된 <br> 연결의 장입니다.</p>
                <p>다양한 사회서비스 기업을 발굴하고 임팩트 투자 연계를 통해  기업의 스케일업을 지원하며,<br> 궁극적으로 국민 모두에게 고품질의 사회서비스가 제공될 수 있는 <br> 건강한 생태계 조성을 목표로 합니다.</p>
                 <div class="organizers-section">
                     <div class="organizer-logos-flex">
                         <div class="organizer-logo-item">{f'<img src="{LOGO_MOHW_DATA_URI}" alt="보건복지부">' if LOGO_MOHW_DATA_URI else ""}</div>
                         <div class="organizer-logo-item">{f'<img src="{LOGO_KSSI_DATA_URI}" alt="중앙사회서비스원">' if LOGO_KSSI_DATA_URI else ""}</div>
                         <div class="organizer-logo-item">{f'<img src="{LOGO_MYSC_DATA_URI}" alt="엠와이소셜컴퍼니(MYSC)">' if LOGO_MYSC_DATA_URI else ""}</div>
                     </div>
                 </div>
            </div>
        </div>
    </section>
    """
    st.markdown(intro_html, unsafe_allow_html=True)
# --- 3. 참가 안내 (신청 대상) ---
def display_participation_guide_section():
    # 사용자 요청: 3개 카드 병렬 배치, 중앙 모티프 삭제
    guide_html = f"""
    <style>
        #section-participation-guide {{ background-color: var(--background-light-gray); }}
        .participation-layout-wrapper {{
            display: flex; flex-direction: column; align-items: center; gap: 0px; /* gap 제거 또는 조정 */
        }}
        .guide-card-row {{ /* 이제 하나의 row가 카드를 담도록 수정 */
            display: grid;
            grid-template-columns: 1fr; /* 모바일 기본 1열 */
            gap: 30px;
            width: 100%;
            max-width: 1100px; /* 카드 배치 위해 너비 조정 */
            margin-top: 50px; /* 위 subtitle과의 간격 */
        }}
        @media (min-width: 768px) {{ /* 태블릿 */
            .guide-card-row {{ grid-template-columns: repeat(2, 1fr); }} /* 태블릿부터 2열로 표시 */
        }}
        /* .guide-card, .guide-card-title 등 기존 스타일은 유지 */
        .guide-card {{
            background-color: var(--white-color); border-radius: var(--border-radius-lg); padding: 35px;
            box-shadow: var(--box-shadow-light); border: 1px solid var(--border-color);
            border-bottom: 5px solid var(--primary-color-light);
            transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
            display: flex; flex-direction: column; min-height: 250px; /* 카드 높이 일관성 */
        }}
        .guide-card:hover {{ transform: translateY(-10px) scale(1.02); box-shadow: var(--box-shadow-dark); border-bottom-color: var(--primary-color-dark); }}
        .guide-card-title {{ font-size: 1.7rem; font-weight: 700; color: var(--primary-color-dark); margin-bottom: 18px; display: flex; align-items: center; }}
        .guide-card-title .title-icon {{ font-size: 2rem; margin-right: 15px; color: var(--primary-color); }}
        .guide-card-description {{ font-size: 1rem; color: var(--text-secondary); margin-bottom: 28px; line-height: 1.75; flex-grow: 1; }}
        .guide-card ul {{ list-style-type: none; padding-left: 0; margin: 0; margin-top: auto; }}
        .guide-card li {{ font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 12px; padding-left: 28px; position: relative; line-height: 1.65; }}
        .guide-card li strong {{ font-weight: 700; color: var(--text-primary);}} /* 강조 스타일 */
        .guide-card li::before {{ content: '✔'; color: var(--primary-color); position: absolute; left: 0; font-weight: bold; font-size: 1.2em; }}
    </style>
    <section id="section-participation-guide" class="section">
        <h2 class="section-title">참가 유형</h2>
        <div class="participation-layout-wrapper">
            <div class="guide-card-row"> 
                <div class="guide-card ir-presentation">
                    <h3 class="guide-card-title"><span class="title-icon">📢</span> IR 발표 기업</h3>
                    <p class="guide-card-description">IR 발표를 통해 투자 유치 기회 확대를 필요로 하는 사회서비스 기업</p>
                </div>
                <div class="guide-card">
                    <h3 class="guide-card-title"><span class="title-icon">📰</span> 홍보테이블 운영 기업</h3>
                    <p class="guide-card-description">홍보테이블을 통해 기업의 비즈니스 모델/임팩트 홍보 투자자·유관기관과의 네트워킹을 희망하는 사회서비스 기업</p>
              </div> 
  *행사 참관을 희망하는 경우 별도 신청이 필요하며, 중앙사회서비스원 홈페이지 공지사항을 통해 신청 방법 확인
    </section>
    """
    st.markdown(guide_html, unsafe_allow_html=True)

#밋업 기업 주석 처리 
       # <div class="guide-card">
         # <h3 class="guide-card-title"><span class="title-icon">🤝</span> 투자자 밋업 기업</h3>
         # <p class="guide-card-description">라운드 테이블 미팅(16:00~17:20)에 <br> 참가하여 투자자와의 1:1 투자 상담 및 <br> 밋업을 희망하는 사회서비스 기업</p>
     #   </div>

# --- 4. 세부 행사 일정 (예시) ---
def display_event_composition_section():
    # (세부 행사 일정 HTML 및 내부 CSS는 이전 답변과 동일하게 유지 - 구조 변경 없음, 내부 텍스트만 PPT에 맞게 수정됨)
    composition_html = f"""
    <style>
        #section-event-composition {{ background-color: {BACKGROUND_COLOR_LIGHT_GRAY}; font-family: 'Pretendard', sans-serif; }}
        .timeline-wrapper {{ max-width: 900px; margin: 0 auto; position: relative; padding: 30px 0; }}
        .timeline-wrapper::before {{ content: ''; position: absolute; top: 0; left: 50px; bottom: 0; width: 4px; background: linear-gradient(to bottom, {PRIMARY_COLOR_LIGHT}, {PRIMARY_COLOR}); border-radius: 2px; z-index: 0; }}
        .timeline-item {{ display: flex; position: relative; margin-bottom: 40px; animation: itemFadeInUp 0.6s ease-out forwards; opacity: 0; }}
        .timeline-item:last-child {{ margin-bottom: 0; }}
        .timeline-icon-wrapper {{ position: absolute; left: 50px; top: 0; transform: translateX(-50%); z-index: 2; display: flex; align-items: center; justify-content: center; }}
        .timeline-icon {{ width: 60px; height: 60px; background-color: var(--white-color); color: {PRIMARY_COLOR_DARK}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; box-shadow: 0 0 0 5px {PRIMARY_COLOR_LIGHT}BB, var(--box-shadow-medium); border: 2px solid var(--white-color); }}
        .timeline-content-card {{ margin-left: 100px; background-color: var(--white-color); padding: 25px 30px; border-radius: var(--border-radius-lg); box-shadow: var(--box-shadow-dark); flex: 1; border-left: 5px solid {PRIMARY_COLOR}; position: relative; transition: transform 0.35s ease, box-shadow 0.35s ease; }}
        .timeline-content-card:hover {{ transform: scale(1.03) translateX(5px); box-shadow: 0 15px 40px rgba(0,0,0,0.22); }}
        .timeline-content-card::before {{ content: ""; position: absolute; top: 20px; left: -10px; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-right: 10px solid {PRIMARY_COLOR}; }}
        .time-duration-badge {{ display: inline-block; font-size: 0.9rem; font-weight: 700; color: var(--white-color); background-color: {PRIMARY_COLOR_DARK}; padding: 6px 14px; border-radius: 25px; margin-bottom: 18px; }}
        .item-title-text {{ font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin-top: 0; margin-bottom: 14px; }}
        .item-details-text {{ font-size: 1.05rem; color: var(--text-secondary); line-height: 1.75; margin: 0; }}
        @keyframes itemFadeInUp {{ from {{ opacity:0; transform: translateY(35px); }} to {{ opacity:1; transform: translateY(0); }} }}
        @media (max-width: 768px) {{ .timeline-wrapper::before {{ left: 30px; }} .timeline-icon-wrapper {{ left: 30px; }} .timeline-icon {{ width: 50px; height: 50px; font-size: 1.8rem; }} .timeline-content-card {{ margin-left: 70px; padding: 20px 25px; }} .timeline-content-card::before {{ display:none; }} .item-title-text {{ font-size: 1.3rem; }} .item-details-text {{ font-size: 0.95rem; }} }}
    </style>
    <section id="section-event-composition" class="section">
        <h2 class="section-title">세부 행사 일정</h2>
        <div class="timeline-wrapper">
            <div class="timeline-item" style="animation-delay: 0s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">📝</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">13:00 - 13:30 (30분)</span> <h4 class="item-title-text">참가자 등록 및 사전 네트워킹</h4> <p class="item-details-text">행사장 도착, 명찰 수령 및 자료 확인, 자유로운 분위기 속 사전 교류의 시간입니다.</p> </div> </div>
            <div class="timeline-item" style="animation-delay: 0.1s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🎉</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">13:30 - 14:10 (40분)</span> <h4 class="item-title-text">개회식 및 사업 안내</h4> <p class="item-details-text">개회 선언, 주최/주관기관 환영사 및 축사, 투자 교류회 사업 소개, 기념 단체 사진 촬영이 진행됩니다.</p> </div> </div>
            <div class="timeline-item" style="animation-delay: 0.2s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🗣️</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">14:10 - 14:20 (10분)</span> <h4 class="item-title-text">홍보 기업 소개</h4> <p class="item-details-text">홍보 테이블을 운영하는 참가가 기업들의 간략한 소개와 부스 위치 안내가 이루어집니다.</p> </div> </div>
            <div class="timeline-item" style="animation-delay: 0.3s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🚀</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">14:20 - 14:55 (35분)</span> <h4 class="item-title-text">IR 발표 (세션 1)</h4> <p class="item-details-text"> 사회서비스 기업들의 투자 유치 발표가 진행됩니다. (5개 기업, 기업당 7분 발표. Q&A는 없으며 이후 라운드 테이블에서 상세한 상담이 이뤄집니다.)</p> </div> </div>
            <div class="timeline-item" style="animation-delay: 0.4s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">☕</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">14:55 - 15:10 (15분)</span> <h4 class="item-title-text">네트워킹 브레이크 & 홍보 테이블 관람</h4> <p class="item-details-text">참석자 간 자유로운 네트워킹과 함께 홍보 기업들을 둘러볼 수 있는 시간입니다.</p> </div> </div>
            <div class="timeline-item" style="animation-delay: 0.5s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🚀</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">15:10 - 15:45 (35분)</span> <h4 class="item-title-text">IR 발표 (세션 2)</h4> <p class="item-details-text"> 사회서비스 기업들의 투자 유치 발표가 진행됩니다. (5개 기업, 기업당 7분 발표. Q&A는 없으며 이후 라운드 테이블에서 상세한 상담이 이뤄집니다.)</p> </div> </div>
            <div class="timeline-item" style="animation-delay: 0.6s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🔄</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">15:45 - 16:00 (15분)</span> <h4 class="item-title-text">네트워킹 브레이크 & 투자 매칭 준비</h4> <p class="item-details-text">잠시 휴식을 취하며, 이어질 라운드 테이블 미팅을 위한 투자자-기업 간 매칭을 최종 준비하고 홍보테이블 기업의 부스를 관람합니다.</p> </div> </div>
            <div class="timeline-item" style="animation-delay: 0.7s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🤝</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">16:00 - 17:20 (80분)</span> <h4 class="item-title-text">라운드 테이블 미팅 (투자자 밋업)</h4> <p class="item-details-text">사전 신청 및 매칭된 투자자와 기업 간의 1:1 심층 투자 상담 및 네트워킹이 진행됩니다. (세션별 순환)</p> </div> </div>
            <div class="timeline-item" style="animation-delay: 0.8s;"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🏁</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">17:20 - 17:30 (10분)</span> <h4 class="item-title-text">폐회 및 마무리 네트워킹</h4> <p class="item-details-text">폐회와 함께 자유로운 마무리 네트워킹 시간이 주어집니다.</p> </div> </div>
        </div>
    </section>
    """
    st.markdown(composition_html, unsafe_allow_html=True)

# --- 5. 2025년 투자 교류회 연간 일정 ---
# --- 5. 2025년 투자 교류회 연간 일정 ---
def display_annual_schedule_section():
    STATUS_COLOR_SCHEDULED = TEXT_COLOR_MUTED
    event3_details = "복지, 보건·의료, 교육, 고용, 주거, 문화, 환경의 분야에서 국민의 삶을 HEAL하는 사회서비스 기업을 지원합니다."
    # (연간 일정 HTML 및 내부 CSS는 이전 답변과 동일하게 유지 - 구조 변경 없음, 내부 텍스트만 PPT에 맞게 수정됨)
    annual_schedule_html = f"""
    <style>
        #section-annual-schedule {{ background-color: var(--white-color); }}
        .event-schedule-grid {{ display: grid; grid-template-columns: 1fr; gap: 35px; }}
        @media (min-width: 768px) {{ .event-schedule-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
        @media (min-width: 1024px) {{ .event-schedule-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
        .event-schedule-card {{ background-color: var(--white-color); border-radius: var(--border-radius-lg); padding: 30px 25px; box-shadow: var(--box-shadow-light); border: 1px solid var(--border-color); display: flex; flex-direction: column; transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out; animation: cardPopIn 0.5s ease-out forwards; opacity: 0; min-height: 430px; }}
        .event-schedule-card:hover {{ transform: translateY(-8px); box-shadow: var(--box-shadow-dark); border-color: {PRIMARY_COLOR}; }}
        .event-schedule-card.card-disabled-look {{ opacity: 0.8; background-color: {BACKGROUND_COLOR_LIGHT_GRAY}; }}
        .event-schedule-card.card-disabled-look:hover {{ transform: translateY(-4px); box-shadow: var(--box-shadow-medium); border-color: var(--border-color); }}
        .event-schedule-card .card-header {{ display: flex; flex-direction: column; align-items: center; text-align: center; margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid var(--border-color); }}
        .event-date-venue {{ font-size: 1rem; font-weight: 600; color: var(--text-primary); margin-bottom: 10px; text-align: center ; }}
        .event-status {{ font-size: 0.88rem; font-weight: 700; color: var(--white-color); padding: 7px 16px; border-radius: 20px; }}
        .event-theme {{ font-size: 1.5rem; font-weight: 700; color: var(--primary-color-dark); margin-bottom: 18px; line-height: 1.4; font-style: normal !important; text-align: center; min-height: calc(1.4em * 2 * 1.4); }} /* 테마 2줄 확보 */
        .event-time {{ font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 20px; display: flex; align-items: center; justify-content: center; }}
        .event-time .icon-time-emoji {{ margin-right: 8px; color: {PRIMARY_COLOR_DARK}; font-size: 1.1em; }}
        .event-details {{ font-size: 0.9rem; color: var(--text-secondary); line-height: 1.65; margin-bottom: 25px; flex-grow: 1; text-align: center; min-height: calc(1.65em * 3); }} /* 설명 3줄 확보 */
        .card-apply-button {{ margin-top: auto; text-align: center; width: 100%; padding-top: 14px; padding-bottom: 14px; font-size: 1rem; }}
        .custom-button.button-disabled {{ background-color: #d8d8d8 !important; color: #888888 !important; border-color: #d8d8d8 !important; box-shadow: none !important; pointer-events: none; cursor: not-allowed; }}
        .custom-button.button-disabled:hover {{ background-color: #d8d8d8 !important; transform: none !important; box-shadow: none !important; }}
        @keyframes cardPopIn {{ from {{ opacity: 0; transform: translateY(20px) scale(0.98); }} to {{ opacity: 1; transform: translateY(0) scale(1); }} }}
        @media (max-width: 1023px) and (min-width: 768px) {{ .event-schedule-grid {{ grid-template-columns: repeat(2, 1fr); }} .event-schedule-card {{ min-height: 450px; }} }}
        @media (max-width: 767px) {{ .event-schedule-grid {{ grid-template-columns: 1fr; }} .event-theme {{ font-size: 1.35rem; min-height: calc(1.4em * 2 * 1.35); }} .event-details {{ font-size: 0.9rem; min-height: calc(1.65em * 4);}} .event-schedule-card {{ padding: 25px; min-height: auto; }} }}
    </style>
    <section id="section-annual-schedule" class="section">
        <h2 class="section-title">2025년 투자 교류회 연간 일정</h2>
        <div class="event-schedule-grid">
            <div class="event-schedule-card card-disabled-look" style="animation-delay: 0s;">
                <div class="card-header"> <span class="event-status" style="background-color:{STATUS_COLOR_SCHEDULED};">모집 마감</span> </div>
                <h3 class="event-theme">제1회: 국민의 삶의 질을 높이는 AI 사회서비스</h3>
                <span class="event-date-venue">2025. 6. 25.(수) / 서울</span>
                <p class="event-details">AI 기술을 활용하여 사회서비스의 효율성과<br> 접근성을 혁신하는 기업을 위한 투자 교류의 장입니다. (참석 규모: 약 80명 내외)</p>
                <a href="#" class="card-apply-button custom-button button-disabled">모집 마감</a>
            </div>
            <div class="event-schedule-card" style="animation-delay: 0.15s;">
                <div class="card-header"> <span class="event-status" style="background-color:{PRIMARY_COLOR};">모집중</span> </div>
                <h3 class="event-theme">제2회: 돌봄의 공백을 채우는 지역 상생 사회서비스</h3>
                <p class="event-time"><span class="event-date-venue">2025. 8. 4.(월) / 대전테크노파크 디스테이션 10층 </span> </p>
                <p class="event-details">지역 사회의 특성을 반영한 맞춤형 돌봄 서비스 및 지역사회 활성화에 기여하는 <br> 기업을 발굴합니다.</p>
                <a href="#section-application-method" class="card-apply-button custom-button button-primary">세부 정보 확인 및 신청</a>
            </div>
            <div class="event-schedule-card card-disabled-look" style="animation-delay: 0.3s;">
                <div class="card-header"> <span class="event-status" style="background-color:{STATUS_COLOR_SCHEDULED};">모집예정</span> </div>
                <h3 class="event-theme">제3회: 국민의 삶을 HEAL하는 사회서비스</h3>
                <p class="event-time"><strong>2025. 9. 9.(화) / aT센터</strong></p>
                <p class="event-details">{event3_details}</p>
                <a href="#section-application-method" class="card-apply-button custom-button button-disabled">향후 모집 예정</a>
            </div>
        </div>
    </section>
    """
    st.markdown(annual_schedule_html, unsafe_allow_html=True)

# --- 6. 참가 신청 방법 ---
def display_application_method_section():
    application_note = "※ 교류회 주제 및 장소 여건에 따라 선착순 마감될 수 있으며, 선정 기업(기관) 별도 통보 예정"
    application_deadline_text = "2025년 6월 9일(금)까지"

    # 사용자 요청: 제출 서류 안내 부분 스타일 적용되도록 수정
    # 클래스명 required-docs-section 으로 통일하고, 해당 클래스에 대한 스타일은 inject_global_styles_and_header 함수 내 CSS에 정의함.
    required_docs_html = f"""
    <div class="required-docs-section">
        <h4>Step 2: 참가 유형별 제출 서류 안내</h4>
        <div>
            <h5>📢 IR 발표 기업</h5>
            <span>발표 기업의 경우 향후 발표 영상이 제작되어 중앙사회서비스원 유튜브에 업로드될 예정입니다</span>
            <ul>
                <li>참가신청서 (발표기업용)</li>
                <li>기업 IR 자료(발표 시간 7분, 질의응답 3분)</li>
                <li>사업자등록증 사본</li>
                <li>개인정보 수집·이용 동의서</li>

            </ul>
            <hr>
            <h5>📰 홍보테이블 운영 기업</h5>
            <ul>
                <li>참가신청서 (홍보기업용)</li>
                <li>기업 IR 자료</li>
                <li>기업 정보 자료 (홍보물 제작에 필요한 기본 정보)</li>
                <li>사업자등록증 사본</li>
                <li>개인정보 수집·이용 동의서</li>
            </ul>
            <hr>
            <h5>🤝 투자자 밋업 기업</h5>
            <ul>
                <li>참가신청서 (해당 시, 또는 온라인 신청으로 갈음)</li>
                <li>기업 IR 자료</li>
                <li>사업자등록증 사본</li>
                <li>개인정보 수집·이용 동의서</li>
            </ul>
            <p class="notice">* 행사 참관을 희망하는 경우 별도 신청 필요하며, 중앙사회서비스원 홈페이지 공지사항을 통해 신청 방법 확인</p>
        </div>
    </div>
    """

    # (참가 신청 방법 HTML 및 내부 CSS는 이전 답변과 유사하게 유지, required_docs_html 삽입 위치 및 스타일 조정)
    application_html = f"""
    <style>
        #section-application-method {{ background-color: {BACKGROUND_COLOR_LIGHT_GRAY}; text-align: center; padding-bottom: 100px; }}
        .application-content {{ max-width: 850px; margin: 0 auto; }}
        .application-step {{ background-color: var(--white-color); padding: 40px; border-radius: var(--border-radius-lg); margin-bottom: 35px; box-shadow: var(--box-shadow-medium); text-align: left; border-left: 6px solid {PRIMARY_COLOR}; transition: transform 0.3s ease, box-shadow 0.3s ease; }}
        .application-step:hover {{ transform: translateY(-8px); box-shadow: var(--box-shadow-dark); }}
        .application-step-title {{ font-size: 1.6rem; font-weight: 700; color: {PRIMARY_COLOR_DARK}; margin-bottom: 20px; }}
        .application-step p {{ font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 15px; line-height: 1.8; }}
        .application-step a.form-link {{ color: {PRIMARY_COLOR_DARK}; font-weight: 600; text-decoration: none; background-color: {PRIMARY_COLOR_LIGHT}66; padding: 10px 15px; border-radius: var(--border-radius-sm); transition: background-color 0.25s ease, color 0.25s ease; display: inline-flex; align-items:center; gap: 8px; margin-top: 8px; }}
        .application-step a.form-link:hover {{ background-color: {PRIMARY_COLOR}; color: var(--white-color); }}
        .application-deadline-highlight {{
            font-size: 1.3rem; font-weight: 700; color: var(--white-color);
            background: linear-gradient(135deg, {PRIMARY_COLOR_DARK}, {PRIMARY_COLOR});
            padding: 20px 35px; border-radius: var(--border-radius-md); display: inline-block;
            margin-top: 0px; margin-bottom: 45px;
            box-shadow: var(--box-shadow-dark);
        }}
        .download-area {{ margin-top: 35px; }} /* 제출서류 안내 섹션과의 간격 조정 */
        .download-links-title {{ font-size: 1.5rem; font-weight: 600; color: var(--text-primary); margin-bottom:0px; text-align:center; }}
        .download-links-span {{ font-size: 0.8rem; font-weight: 400; color: var(--text-primary); margin-bottom:100px; text-align:center; }}
        .download-links-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 30px; justify-content: center; max-width: 200px; margin-bottom:100px; margin: 0 auto; }}
        .download-link-button {{ display: flex; flex-direction: column; align-items: center; justify-content: center; background-color: transparent; color: {PRIMARY_COLOR_DARK} !important; padding: 28px 20px; border-radius: var(--border-radius-md); text-decoration: none; font-size: 1.05rem; font-weight: 600; border: 2px solid {PRIMARY_COLOR_DARK}; box-shadow: none; transition: all 0.3s ease; text-align: center; min-height: 100px; }}
        .download-link-button:hover {{ background-color: {PRIMARY_COLOR_DARK}; color: var(--white-color) !important; border-color: {PRIMARY_COLOR_DARK}; transform: translateY(-6px) scale(1.03); box-shadow: var(--box-shadow-medium); }}
        .download-link-button .icon {{ font-size: 2.2em; margin-bottom: 15px; }}
        .application-notice {{ margin-top: 65px; padding: 30px; background-color: var(--white-color); border: 1px solid var(--border-color); border-left: 5px solid {TEXT_COLOR_MUTED}; border-radius: var(--border-radius-md); font-size: 1rem; color: var(--text-muted); line-height: 1.8; text-align: left; max-width: 800px; margin-left: auto; margin-right: auto; box-shadow: var(--box-shadow-light); }}
        .application-notice strong {{ color: {PRIMARY_COLOR_DARK}; }}
        .application-notice p:last-child {{ margin-bottom: 0; }}
        @media (max-width: 600px) {{ .download-links-grid {{ grid-template-columns: 1fr; }} .application-step-title {{ font-size: 1.4rem; }} .application-step p {{ font-size: 1.05rem; }} .application-deadline-highlight {{ font-size: 1.2rem; padding: 18px 25px; }} .application-notice {{ text-align: left; }} }}
    </style>
     <section id="section-application-method" class="section">
        <h2 class="section-title">참가 신청 방법</h2>
        <div class="application-content">
            <div class="application-deadline-highlight">
                2회차 참가 신청 마감: 7월 21일(월) 오후 6시까지(시간 엄수)
            </div>
            <div class="application-step">
                <h3 class="application-step-title">Step 1: 참가 유형 확인 & 온라인 신청서 작성</h3>
                <p> <strong>IR발표, 홍보테이블 운영, 투자자 밋업 </strong> 참가를 희망하시는 기업은 아래 '온라인 참가 신청하기' 버튼을 통해 <br> 신청 페이지로 이동 후, 참가 유형을 확인하고 온라인 신청서 작성</p>
                <p><a href="https://forms.gle/HLUu8cwfU4STHgF16" target="_blank" class="form-link">➡️ 온라인 참가 신청하기 (Google Form)</a></p>
            </div>
            <div class="application-step">
                <h3 class="application-step-title">Step 2: 제출 서류 준비 및 업로드</h3>
                <p>'참가신청서 및 개인정보 동의서' 다운로드 및 작성 후 참가 유형별 제출 서류와 함께 온라인 신청서에 업로드</p>
            </div>
             <div class="download-area">
                <p class="download-links-title">주요 신청 양식 다운로드</p>
                 <span class="download-links-span">참가 유형별 참가신청서 1부와 개인정보 이용동의서 1부를 구글폼에 제출 부탁드립니다</span>
                <div class="download-links-grid">
                    {f'<a href="https://drive.google.com/uc?export=download&id=1sUNcIjQd6uCCc8qHdhqZjKGIvExhMsil" target="_blank" class="download-link-button"><span class="icon">📄</span>신청서식<br>(공통)</a>' if NOTION_PAGE_URL else ""}
                </div>
            </div>
             <div class="required-docs-section"> 
            <h4>Step 2: 참가 유형별 제출 서류 안내</h4>
            <div>
                <h5>📢 IR 발표 기업</h5>
                <ul>
                    <li>참가신청서 및 개인정보 동의서(상단 서식)</li>
                    <li>기업 IR 자료 (발표 : 7분)</li>
                    <li>사업자등록증 사본</li>
                </ul>
                <hr>
                <h5>📰 홍보테이블 운영 기업</h5>
                <ul>
                    <li>참가신청서 및 개인정보 동의서(상단 서식)</li>
                    <li>기업 IR 자료 (VC 밋업용)</li>
                    <li>홍보물 제작에 필요한 기본 정보</li>
                    <li>사업자등록증 사본</li>
                </ul>
             <p class="notice">* 참관 및 네트워킹 참가가는 본 신청 페이지를 통하지 않으며, 별도 안내될 예정입니다.</p>
            </div>
        </div>
            <div>      
            <div class="application-notice">
                <p><strong>[유의사항]</strong><br>{application_note}</p>
            </div>
        </div>
    </section>
    """
    st.markdown(application_html, unsafe_allow_html=True)

# --- 7. FAQ 섹션 ---
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
                    <p>‘사회서비스 기업’은 「사회보장기본법」 제3조 제4호에 따라 복지, 보건의료, 교육, 고용, 주거, 문화, 환경 등의 분야에서 상담, 재활, 돌봄, 정보의 제공, 관련 시설의 이용, 역량 개발, 사회참여 지원 등을 통해 국민 삶의 질이 향상되도록 서비스를 제공하는 기업입니다.</p>
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
                    <p>상세 내용은 아래 링크 참고 부탁드립니다. <a href="https://sociallink3.streamlit.app/" target="_blank">소링아에 대해서 자세히 보러 가기(클릭)</a></p>
                </div>
            </details>
        </div>
    </section>
    """
    st.markdown(faq_html, unsafe_allow_html=True)

# --- 8. 문의처 ---
def display_contact_section():
    contact_email = "kcpassinvest@gmail.com"
    phone_number = "02-499-5111"
    operator_name = "프로그램 운영 사무국 (MYSC)"
    # (문의처 HTML 및 내부 CSS는 이전 답변과 동일하게 유지 - 구조 변경 없음)
    section_style = f"""
    <style>
        #section-contact {{ padding: 100px 25px; background-color: var(--white-color); color: var(--text-primary); font-family: 'Pretendard', sans-serif; text-align: center; position: relative; overflow: hidden; }}
        #section-contact .content-wrapper {{ position: relative; z-index: 1; max-width: 750px; margin: 0 auto; }}
        #section-contact .contact-section-title {{ font-size: 3rem; font-weight: 700; color: var(--text-primary); margin-bottom: 25px; text-shadow: none; }}
        #section-contact .contact-section-subtitle {{ font-size: 1.3rem; color: var(--text-secondary); margin-bottom: 60px; line-height: 1.8; max-width: 700px; margin-left: auto; margin-right: auto; }}
        .contact-card-styled {{ background-color: var(--background-light-gray); color: var(--text-primary); border-radius: var(--border-radius-lg); box-shadow: var(--box-shadow-medium); padding: 50px; text-align: left; max-width: 600px; margin: 0 auto; border-top: 6px solid {PRIMARY_COLOR}; position: relative; }}
        .contact-card-styled h3 {{ font-size: 2em; font-weight: 600; color: {PRIMARY_COLOR_DARK}; margin-top: 0; margin-bottom: 40px; text-align: center; }}
        .contact-card-styled p {{ font-size: 1.2em; color: var(--text-secondary); line-height: 1.9; margin-bottom: 28px; display: flex; align-items: center; }}
        .contact-card-styled p:last-child {{ margin-bottom: 0; }}
        .contact-card-styled .icon {{ margin-right: 20px; font-size: 1.8em; color: {PRIMARY_COLOR_DARK}; width: 40px; text-align: center; }}
        .contact-card-styled strong {{ color: var(--text-primary); font-weight: 600; }}
        .contact-card-styled a {{ color: {PRIMARY_COLOR_DARK}; text-decoration: none; font-weight: 600; border-bottom: 2px solid {PRIMARY_COLOR_LIGHT}; padding-bottom: 3px; transition: color 0.25s ease, border-bottom-color 0.25s ease; }}
        .contact-card-styled a:hover {{ color: {PRIMARY_COLOR}; border-bottom-color: {PRIMARY_COLOR}; }}
        @media (max-width: 768px) {{ #section-contact .contact-section-title {{ font-size: 2.4rem; }} #section-contact .contact-section-subtitle {{ font-size: 1.15rem; margin-bottom: 45px; }} .contact-card-styled h3 {{ font-size: 1.7em; margin-bottom:35px; }} .contact-card-styled p {{ font-size: 1.1em; }} .contact-card-styled {{ padding: 40px; }} }}
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
    # (푸터 HTML 및 내부 CSS는 이전 답변과 동일하게 유지 - 로고 가시성 개선 시도됨)
    footer_html = f"""
    <style>
        .page-footer {{ background-color: var(--background-dark-gray); color: var(--text-muted); padding: 70px 25px; text-align: center; font-size: 1rem; line-height: 1.75; border-top: 1px solid #444; }}
        .footer-logo-container {{ margin-bottom: 35px; display: flex; justify-content: center; align-items: center; gap: 35px; flex-wrap: wrap; }}
        .footer-logo-item {{ width: 170px; height: 55px; display: flex; justify-content: center; align-items: center; }}
        .footer-logo-item img {{ max-width: 100%; max-height: 100%; object-fit: contain; opacity: 0.9; filter: brightness(150%) contrast(110%); transition: opacity 0.3s ease, filter 0.3s ease, transform 0.3s ease; }}
        .footer-logo-item img:hover {{ opacity: 1; filter: brightness(100%) contrast(100%); transform: scale(1.05); }}
        .footer-links {{ margin: 30px 0; }}
        .footer-links a {{ color: var(--text-muted); text-decoration: none; margin: 0 18px; transition: color 0.2s ease, text-decoration 0.2s ease; padding-bottom: 4px; border-bottom: 1px solid transparent; }}
        .footer-links a:hover {{ color: var(--primary-color-light); border-bottom-color: var(--primary-color-light); }}
        .footer-copyright {{ margin-top: 25px; font-size: 0.9rem; color: rgba(255,255,255,0.55); }}
        .footer-copyright strong {{ color: rgba(255,255,255,0.75); }}
    </style>
    <footer class="page-footer">
        <div class="footer-logo-container">
            <div class="footer-logo-item">{f'<img src="{LOGO_MOHW_DATA_URI}" alt="보건복지부">' if LOGO_MOHW_DATA_URI else "<span>보건복지부</span>"}</div>
            <div class="footer-logo-item">{f'<img src="{LOGO_KSSI_DATA_URI}" alt="중앙사회서비스원">' if LOGO_KSSI_DATA_URI else "<span>중앙사회서비스원</span>"}</div>
            <div class="footer-logo-item">{f'<img src="{LOGO_MYSC_DATA_URI}" alt="엠와이소셜컴퍼니(MYSC)">' if LOGO_MYSC_DATA_URI else "<span>엠와이소셜컴퍼니(MYSC)</span>"}</div>
        </div>
        <div class="footer-links"></div>
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