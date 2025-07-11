import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="2025 사회서비스 투자 교류회",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

GOOGLE_FORM_URL = "https://forms.gle/7tPQ2fEykJKYBtzi7"

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

def file_to_data_uri(file_path_str):
    try:
        file_path = Path(file_path_str)
        if not file_path.is_file():
            return None
        
        with open(file_path, "rb") as file:
            encoded_string = base64.b64encode(file.read()).decode()
        
        mime_type = "application/x-hwp"
        
        return f"data:{mime_type};base64,{encoded_string}"
    except Exception as e:
        st.error(f"파일 처리 중 오류 발생: {e}")
        return None

LOGO_MOHW_DATA_URI = image_to_data_uri("mohw_logo.png")
LOGO_KSSI_DATA_URI = image_to_data_uri("kssi_logo.png")
LOGO_MYSC_DATA_URI = image_to_data_uri("mysc_logo.png")

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
        .header-nav {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
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
        .header-nav-item:hover, .header-nav-item:focus {{
            color: var(--primary-color-dark);
            background-color: rgba(139, 195, 74, 0.1);
            outline: none;
        }}
        .header-nav-item::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            margin: auto;
            width: 0;
            height: 3px;
            background: var(--primary-color);
            border-radius: 3px 3px 0 0;
            transition: width 0.3s ease-in-out;
        }}
        .header-nav-item:hover::after {{
            width: 80%;
        }}
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
        .required-docs-section {{
            background-color: var(--white-color); padding: 30px; border-radius: var(--border-radius-md);
            margin-bottom: 30px; box-shadow: var(--box-shadow-light); text-align: left;
            border-left: 5px solid {PRIMARY_COLOR_LIGHT};
        }}
        .required-docs-section h4 {{
            font-size: 1.6rem; font-weight: 700; color: {PRIMARY_COLOR_DARK};
            margin-bottom: 25px; text-align: center;
        }}
        .required-docs-section h5 {{
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
        .required-docs-section p.notice {{
            font-size: 0.95rem; color: var(--text-muted); margin-top: 15px; line-height: 1.6;
        }}
        @media (max-width: 992px) {{
            .header-nav {{ display: none; }}
            .header-content {{ justify-content: center; }}
            #section-participation-guide .guide-card-row {{ grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }}
        }}
        @media (max-width: 767px) {{
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
    <a href="{GOOGLE_FORM_URL}" target="_blank" class="fab"><span class="fab-icon">📝</span> 참가 신청하기</a>
    """
    st.markdown(global_styles, unsafe_allow_html=True)

def display_hero_section():
    first_event_date = "2025년 8월 4일(월) 13:30"
    first_event_theme = "돌봄의 공백을 채우는 지역 상생 사회서비스"
    application_deadline = "2025년 7월 21일(월) 오후 6시까지(기한 엄수)"

    hero_catchphrase_html = """
        <p style="font-size: 1.5rem; margin-bottom: 0.5em;">사회서비스 기업-투자자-유관기관 연결의 장!</p>
        <p style="font-size: 1.5rem; margin-bottom: 1.5em;">투자 유치 및 홍보를 위한 기회의 장!</p>
    """
    hero_cta_button_text = "🚀 참가 신청 바로가기"

    hero_html = f"""
    <style>
        #section-hero {{
            background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, {PRIMARY_COLOR_DARK} 100%);
            min-height: 80vh; display: flex; flex-direction: column;
            align-items: center; justify-content: center; text-align: center;
            padding: calc(var(--header-height) + 70px) 25px 70px 25px;
            position: relative; overflow: hidden; color: var(--white-color);
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
    </style>
    <section id="section-hero">
        <div class="hero-content-wrapper">
            <h1 class="hero-main-title">2025 사회서비스 투자 교류회</h1>
            <div class="hero-catchphrase-container">{hero_catchphrase_html}</div>
        </div>
        <div class="hero-key-info">
            <h3>✨ 제2회 투자 교류회 안내 ✨</h3>
            <p><span class="info-label">일시:</span> {first_event_date}</p>
            <p><span class="info-label">주제:</span> {first_event_theme}</p>
            <p><span class="info-label">신청마감:</span> <span class="deadline">{application_deadline}</span></p>
            <p><span class="info-label">장소:</span> 대전테크노파크 디스테이션 10층</p>
        </div>
        <div class="hero-cta-button-container">
            <a href="{GOOGLE_FORM_URL}" target="_blank" class="custom-button button-primary" style="padding: 18px 40px; font-size: 1.25rem; font-weight: 700;">
                {hero_cta_button_text}
            </a>
        </div>
    </section>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

def display_introduction_section():
    intro_html = f"""
    <style>
        .intro-text-content h3 {{ font-size: 2.2rem; font-weight: 700; color: var(--primary-color-dark); margin-bottom: 30px; line-height: 1.4; letter-spacing: -0.3px; }}
        .intro-text-content p {{ font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 22px; line-height: 1.85; max-width: 700px; margin-left: auto; margin-right: auto; }}
        .organizers-section {{ margin-top: 80px; text-align: center; padding-top: 60px; border-top: 1px solid var(--border-color); }}
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

def display_participation_guide_section():
    guide_html = f"""
    <style>
        #section-participation-guide {{ background-color: var(--background-light-gray); }}
        .participation-layout-wrapper {{
            display: flex; flex-direction: column; align-items: center; gap: 0px;
        }}
        .guide-card-row {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 30px;
            width: 100%;
            max-width: 1100px;
            margin-top: 50px;
        }}
        @media (min-width: 768px) {{
            .guide-card-row {{ grid-template-columns: repeat(2, 1fr); }}
        }}
        .guide-card {{
            background-color: var(--white-color); border-radius: var(--border-radius-lg); padding: 35px;
            box-shadow: var(--box-shadow-light); border: 1px solid var(--border-color);
            border-bottom: 5px solid var(--primary-color-light);
            transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
            display: flex; flex-direction: column; min-height: 250px;
        }}
        .guide-card:hover {{ transform: translateY(-10px) scale(1.02); box-shadow: var(--box-shadow-dark); border-bottom-color: var(--primary-color-dark); }}
        .guide-card-title {{ font-size: 1.7rem; font-weight: 700; color: var(--primary-color-dark); margin-bottom: 18px; display: flex; align-items: center; }}
        .guide-card-title .title-icon {{ font-size: 2rem; margin-right: 15px; color: var(--primary-color); }}
        .guide-card-description {{ font-size: 1rem; color: var(--text-secondary); margin-bottom: 28px; line-height: 1.75; flex-grow: 1; }}
        .participation-notice {{
            text-align: center;
            margin-top: 40px;
            color: var(--text-muted);
            font-size: 1rem;
        }}
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
            </div>
            <p class="participation-notice">*행사 참관을 희망하는 경우 별도 신청이 필요하며, 중앙사회서비스원 홈페이지 공지사항을 통해 신청 방법 확인</p>
        </div>
    </section>
    """
    st.markdown(guide_html, unsafe_allow_html=True)

def display_event_composition_section():
    composition_html = f"""
    <style>
        #section-event-composition {{ background-color: {BACKGROUND_COLOR_LIGHT_GRAY}; }}
        .timeline-wrapper {{ max-width: 900px; margin: 0 auto; position: relative; padding: 30px 0; }}
        .timeline-wrapper::before {{ content: ''; position: absolute; top: 0; left: 50px; bottom: 0; width: 4px; background: linear-gradient(to bottom, {PRIMARY_COLOR_LIGHT}, {PRIMARY_COLOR}); border-radius: 2px; z-index: 0; }}
        .timeline-item {{ display: flex; position: relative; margin-bottom: 40px; animation: itemFadeInUp 0.6s ease-out forwards; opacity: 0; }}
        .timeline-icon-wrapper {{ position: absolute; left: 50px; top: 0; transform: translateX(-50%); z-index: 2; }}
        .timeline-icon {{ width: 60px; height: 60px; background-color: var(--white-color); color: {PRIMARY_COLOR_DARK}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; box-shadow: 0 0 0 5px {PRIMARY_COLOR_LIGHT}BB, var(--box-shadow-medium); border: 2px solid var(--white-color); }}
        .timeline-content-card {{ margin-left: 100px; background-color: var(--white-color); padding: 25px 30px; border-radius: var(--border-radius-lg); box-shadow: var(--box-shadow-dark); flex: 1; border-left: 5px solid {PRIMARY_COLOR}; }}
        .time-duration-badge {{ display: inline-block; font-size: 0.9rem; font-weight: 700; color: var(--white-color); background-color: {PRIMARY_COLOR_DARK}; padding: 6px 14px; border-radius: 25px; margin-bottom: 18px; }}
        .item-title-text {{ font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin-top: 0; margin-bottom: 14px; }}
        .item-details-text {{ font-size: 1.05rem; color: var(--text-secondary); line-height: 1.75; margin: 0; }}
        @media (max-width: 768px) {{ .timeline-wrapper::before {{ left: 30px; }} .timeline-icon-wrapper {{ left: 30px; }} .timeline-icon {{ width: 50px; height: 50px; font-size: 1.8rem; }} .timeline-content-card {{ margin-left: 70px; padding: 20px 25px; }} .item-title-text {{ font-size: 1.3rem; }} .item-details-text {{ font-size: 0.95rem; }} }}
    </style>
    <section id="section-event-composition" class="section">
        <h2 class="section-title">세부 행사 일정</h2>
        <div class="timeline-wrapper">
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">📝</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">13:00 - 13:30 (30분)</span> <h4 class="item-title-text">참가자 등록 및 사전 네트워킹</h4> <p class="item-details-text">행사장 도착, 명찰 수령 및 자료 확인, 자유로운 분위기 속 사전 교류의 시간입니다.</p> </div> </div>
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🎉</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">13:30 - 14:10 (40분)</span> <h4 class="item-title-text">개회식 및 사업 안내</h4> <p class="item-details-text">개회 선언, 주최/주관기관 환영사 및 축사, 투자 교류회 사업 소개, 기념 단체 사진 촬영이 진행됩니다.</p> </div> </div>
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🗣️</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">14:10 - 14:20 (10분)</span> <h4 class="item-title-text">홍보 기업 소개</h4> <p class="item-details-text">홍보 테이블을 운영하는 참가가 기업들의 간략한 소개와 부스 위치 안내가 이루어집니다.</p> </div> </div>
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🚀</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">14:20 - 14:55 (35분)</span> <h4 class="item-title-text">IR 발표 (세션 1)</h4> <p class="item-details-text"> 사회서비스 기업들의 투자 유치 발표가 진행됩니다. (5개 기업, 기업당 7분 발표. Q&A는 없으며 이후 라운드 테이블에서 상세한 상담이 이뤄집니다.)</p> </div> </div>
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">☕</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">14:55 - 15:10 (15분)</span> <h4 class="item-title-text">네트워킹 브레이크 & 홍보 테이블 관람</h4> <p class="item-details-text">참석자 간 자유로운 네트워킹과 함께 홍보 기업들을 둘러볼 수 있는 시간입니다.</p> </div> </div>
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🚀</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">15:10 - 15:45 (35분)</span> <h4 class="item-title-text">IR 발표 (세션 2)</h4> <p class="item-details-text"> 사회서비스 기업들의 투자 유치 발표가 진행됩니다. (5개 기업, 기업당 7분 발표. Q&A는 없으며 이후 라운드 테이블에서 상세한 상담이 이뤄집니다.)</p> </div> </div>
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🔄</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">15:45 - 16:00 (15분)</span> <h4 class="item-title-text">네트워킹 브레이크 & 투자 매칭 준비</h4> <p class="item-details-text">잠시 휴식을 취하며, 이어질 라운드 테이블 미팅을 위한 투자자-기업 간 매칭을 최종 준비하고 홍보테이블 기업의 부스를 관람합니다.</p> </div> </div>
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🤝</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">16:00 - 17:20 (80분)</span> <h4 class="item-title-text">라운드 테이블 미팅 (투자자 밋업)</h4> <p class="item-details-text">사전 신청 및 매칭된 투자자와 기업 간의 1:1 심층 투자 상담 및 네트워킹이 진행됩니다. (세션별 순환)</p> </div> </div>
            <div class="timeline-item"> <div class="timeline-icon-wrapper"><div class="timeline-icon">🏁</div></div> <div class="timeline-content-card"> <span class="time-duration-badge">17:20 - 17:30 (10분)</span> <h4 class="item-title-text">폐회 및 마무리 네트워킹</h4> <p class="item-details-text">폐회와 함께 자유로운 마무리 네트워킹 시간이 주어집니다.</p> </div> </div>
        </div>
    </section>
    """
    st.markdown(composition_html, unsafe_allow_html=True)

def display_annual_schedule_section():
    STATUS_COLOR_SCHEDULED = TEXT_COLOR_MUTED
    event3_details = "복지, 보건·의료, 교육, 고용, 주거, 문화, 환경의 분야에서 국민의 삶을 HEAL하는 사회서비스 기업을 지원합니다."
    annual_schedule_html = f"""
    <style>
        .event-schedule-grid {{ display: grid; grid-template-columns: 1fr; gap: 35px; }}
        @media (min-width: 768px) {{ .event-schedule-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
        @media (min-width: 1024px) {{ .event-schedule-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
        .event-schedule-card {{ background-color: var(--white-color); border-radius: var(--border-radius-lg); padding: 30px 25px; box-shadow: var(--box-shadow-light); border: 1px solid var(--border-color); display: flex; flex-direction: column; min-height: 430px; }}
        .event-schedule-card .event-theme {{ font-size: 1.5rem; font-weight: 700; color: var(--primary-color-dark); margin-bottom: 18px; line-height: 1.4; min-height: calc(1.4em * 2 * 1.4); }}
        .event-schedule-card .event-details {{ font-size: 0.9rem; color: var(--text-secondary); line-height: 1.65; margin-bottom: 25px; flex-grow: 1; min-height: calc(1.65em * 3); }}
    </style>
    <section id="section-annual-schedule" class="section">
        <h2 class="section-title">2025년 투자 교류회 연간 일정</h2>
        <div class="event-schedule-grid">
            <div class="event-schedule-card">
                <div class="card-header"> <span class="event-status" style="background-color:{STATUS_COLOR_SCHEDULED};">모집 마감</span> </div>
                <h3 class="event-theme">제1회: 국민의 삶의 질을 높이는 AI 사회서비스</h3>
                <span class="event-date-venue">2025. 6. 25.(수) / 서울</span>
                <p class="event-details">AI 기술을 활용하여 사회서비스의 효율성과<br> 접근성을 혁신하는 기업을 위한 투자 교류의 장입니다. (참석 규모: 약 80명 내외)</p>
                <a href="#" class="custom-button button-disabled" style="margin-top: auto;">모집 마감</a>
            </div>
            <div class="event-schedule-card">
                <div class="card-header"> <span class="event-status" style="background-color:{PRIMARY_COLOR};">모집중</span> </div>
                <h3 class="event-theme">제2회: 돌봄의 공백을 채우는 지역 상생 사회서비스</h3>
                <p class="event-time"><span class="event-date-venue">2025. 8. 4.(월) / 대전테크노파크 디스테이션 10층 </span> </p>
                <p class="event-details">지역 사회의 특성을 반영한 맞춤형 돌봄 서비스 및 지역사회 활성화에 기여하는 <br> 기업을 발굴합니다.</p>
                <a href="#section-application-method" class="custom-button button-primary" style="margin-top: auto;">세부 정보 확인 및 신청</a>
            </div>
            <div class="event-schedule-card">
                <div class="card-header"> <span class="event-status" style="background-color:{STATUS_COLOR_SCHEDULED};">모집예정</span> </div>
                <h3 class="event-theme">제3회: 국민의 삶을 HEAL하는 사회서비스</h3>
                <p class="event-time"><strong>2025. 9. 9.(화) / aT센터</strong></p>
                <p class="event-details">{event3_details}</p>
                <a href="#" class="custom-button button-disabled" style="margin-top: auto;">향후 모집 예정</a>
            </div>
        </div>
    </section>
    """
    st.markdown(annual_schedule_html, unsafe_allow_html=True)

def display_application_method_section():
    application_note = "※ 교류회 주제 및 장소 여건에 따라 선착순 마감될 수 있으며, 선정 기업(기관) 별도 통보 예정"
    hwp_file_name = "(양식)2025년 제2회 사회서비스 투자 교류회 참가 신청서 및 개인정보 동의서.hwp"
    hwp_data_uri = file_to_data_uri(hwp_file_name)
    if hwp_data_uri:
        download_button_html = f'<a href="{hwp_data_uri}" download="{hwp_file_name}" class="download-link-button"><span class="icon">📄</span>신청서식<br>(공통)</a>'
    else:
        download_button_html = '<div style="color:red; text-align:center;">신청서식 파일을 찾을 수 없습니다.</div>'

    application_html = f"""
    <style>
        #section-application-method {{ background-color: {BACKGROUND_COLOR_LIGHT_GRAY}; text-align: center; padding-bottom: 100px; }}
        .application-content {{ max-width: 850px; margin: 0 auto; }}
        .application-step {{ background-color: var(--white-color); padding: 40px; border-radius: var(--border-radius-lg); margin-bottom: 35px; box-shadow: var(--box-shadow-medium); text-align: left; border-left: 6px solid {PRIMARY_COLOR}; }}
        .application-step-title {{ font-size: 1.6rem; font-weight: 700; color: {PRIMARY_COLOR_DARK}; margin-bottom: 20px; }}
        .download-area {{ margin-top: 35px; }}
        .download-links-title {{ font-size: 1.5rem; font-weight: 600; color: var(--text-primary); margin-bottom:0px; text-align:center; }}
        .download-links-span {{ font-size: 0.8rem; font-weight: 400; color: var(--text-primary); margin-bottom:20px; text-align:center; display:block; }}
        .download-links-grid {{ display: grid; grid-template-columns: 1fr; gap: 30px; justify-items: center; max-width: 200px; margin: 0 auto 100px; }}
        .download-link-button {{ display: flex; flex-direction: column; align-items: center; justify-content: center; background-color: transparent; color: {PRIMARY_COLOR_DARK} !important; padding: 28px 20px; border-radius: 10px; text-decoration: none; font-size: 1.05rem; font-weight: 600; border: 2px solid {PRIMARY_COLOR_DARK}; width: 100%; transition: all 0.3s ease; text-align: center; min-height: 100px; }}
        .download-link-button:hover {{ background-color: {PRIMARY_COLOR_DARK}; color: var(--white-color) !important; }}
        .download-link-button .icon {{ font-size: 2.2em; margin-bottom: 15px; }}
    </style>
     <section id="section-application-method" class="section">
         <div class="application-content">
             <div class="application-deadline-highlight">
                 2회차 참가 신청 마감: 7월 21일(월) 오후 6시까지(시간 엄수)
             </div>
             <div class="application-step">
                 <h3>Step 1: 참가 유형 확인 & 온라인 신청서 작성</h3>
                 <p> <strong>IR발표, 홍보테이블 운영 </strong> 참가를 희망하시는 기업은 아래 '온라인 참가 신청하기' 버튼을 통해 <br> 신청 페이지로 이동 후, 참가 유형을 확인하고 온라인 신청서 작성</p>
                 <a href="{GOOGLE_FORM_URL}" target="_blank" class="custom-button button-primary">➡️ 온라인 참가 신청하기</a>
             </div>
             <div class="application-step">
                 <h3>Step 2: 제출 서류 준비 및 업로드</h3>
                 <p>'참가신청서 및 개인정보 동의서' 다운로드 및 작성 후 참가 유형별 제출 서류와 함께 온라인 신청서에 업로드</p>
             </div>
              <div class="download-area">
                  <p class="download-links-title">주요 신청 양식 다운로드</p>
                   <span class="download-links-span">참가 유형별 참가신청서 1부와 개인정보 이용동의서 1부를 구글폼에 제출 부탁드립니다</span>
                   <div class="download-links-grid">
                       {download_button_html}
                   </div>
              </div>
               <div class="required-docs-section">
                 <h4>Step 2: 참가 유형별 제출 서류 안내</h4>
                 <div>
                     <h5>📢 IR 발표 기업</h5>
                     <ul>
                         <li>참가신청서 및 개인정보 동의서(상단 서식)</li>
                         <li>기업 IR 자료 (발표 7분, <strong>16:9 PDF 비율로 제출, 제출 후 수정 불가</strong>)</li>
                         <li>사업자등록증 사본</li>
                     </ul>
                     <hr>
                     <h5>📰 홍보테이블 운영 기업</h5>
                     <ul>
                         <li>참가신청서 및 개인정보 동의서(상단 서식)</li>
                         <li>기업 IR 자료 (라운드 테이블 시 VC 밋업용, 별도 비율 제한 없음)</li>
                         <li>홍보물 제작에 필요한 기본 정보</li>
                         <li>사업자등록증 사본</li>
                     </ul>
                  <p class="notice">* 참관 및 네트워킹 참가가는 본 신청 페이지를 통하지 않으며, 별도 안내될 예정입니다.</p>
                 </div>
             </div>
             <div class="application-notice">
                 <p><strong>[유의사항]</strong><br>{application_note}</p>
             </div>
         </div>
     </section>
    """
    st.markdown(application_html, unsafe_allow_html=True)

def display_faq_section():
    faq_html = f"""
    <style>
        #section-faq {{ background-color: var(--white-color); }}
        .faq-item {{ border: 1px solid var(--border-color); border-radius: var(--border-radius-md); margin-bottom: 20px; }}
        .faq-item[open] {{ border-color: {PRIMARY_COLOR_DARK}; }}
        .faq-item[open] .faq-question {{ font-weight: 700; color: {PRIMARY_COLOR_DARK}; background-color: {PRIMARY_COLOR_LIGHT}44; }}
        .faq-question {{ padding: 22px 30px; font-size: 1.2rem; font-weight: 600; cursor: pointer; position: relative; }}
        .faq-question::marker, .faq-question::-webkit-details-marker {{ display: none; }}
        .faq-question::before {{ content: '+'; position: absolute; right: 30px; top: 50%; transform: translateY(-50%); font-size: 1.5em; font-weight: 300; }}
        .faq-item[open] .faq-question::before {{ content: '−'; }}
        .faq-answer {{ padding: 25px 30px; font-size: 1.05rem; color: var(--text-secondary); line-height: 1.8; border-top: 1px solid var(--border-color); }}
        .faq-answer a {{ color: {PRIMARY_COLOR_DARK}; font-weight: 600; border-bottom: 2px solid {PRIMARY_COLOR_LIGHT}; }}
    </style>
    <section id="section-faq" class="section">
        <h2 class="section-title">✅ 모집 FAQ (자주 묻는 질문)</h2>
        <div class="faq-list-container" style="max-width: 900px; margin: 0 auto;">
            <details class="faq-item">
                <summary class="faq-question">신청 가능한 ‘사회서비스 기업’은 어떤 곳인가요?</summary>
                <div class="faq-answer">
                    <p>‘사회서비스 기업’은 「사회보장기본법」 제3조 제4호에 따라 복지, 보건의료, 교육, 고용, 주거, 문화, 환경 등의 분야에서 상담, 재활, 돌봄, 정보의 제공, 관련 시설의 이용, 역량 개발, 사회참여 지원 등을 통해 국민 삶의 질이 향상되도록 서비스를 제공하는 기업입니다.</p>
                </div>
            </details>
            <details class="faq-item">
                <summary class="faq-question">지원 신청서 양식은 어디서 다운로드 받을 수 있나요?</summary>
                <div class="faq-answer">
                    <p>본 페이지의 <a href="#section-application-method">신청 양식 다운로드 칸 내(클릭)</a>에서 다운로드 가능합니다.</p>
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
                    <p>상세 내용은 아래 링크 참고 부탁드립니다. <a href="https://sociallink3.streamlit.app/" target="_blank">소링아에 대해서 자세히 보러 가기(클릭)</a></p>
                </div>
            </details>
        </div>
    </section>
    """
    st.markdown(faq_html, unsafe_allow_html=True)

def display_contact_section():
    contact_email = "kcpassinvest@gmail.com"
    phone_number = "02-499-5111"
    operator_name = "프로그램 운영 사무국 (MYSC)"
    section_style = f"""
    <style>
        .contact-card-styled {{ background-color: var(--background-light-gray); border-radius: var(--border-radius-lg); box-shadow: var(--box-shadow-medium); padding: 50px; text-align: left; max-width: 600px; margin: 0 auto; border-top: 6px solid {PRIMARY_COLOR}; }}
        .contact-card-styled h3 {{ font-size: 2em; font-weight: 600; color: {PRIMARY_COLOR_DARK}; margin-bottom: 40px; text-align: center; }}
        .contact-card-styled p {{ font-size: 1.2em; line-height: 1.9; margin-bottom: 28px; display: flex; align-items: center; }}
        .contact-card-styled .icon {{ margin-right: 20px; font-size: 1.8em; color: {PRIMARY_COLOR_DARK}; width: 40px; text-align: center; }}
    </style>
    <section id="section-contact" class="section">
        <h2 class="section-title">문의하기</h2>
        <p class="section-subtitle">궁금한 점이 있으시면 언제든지 문의해주세요.<br>행사 운영사무국에서 신속하게 답변드리겠습니다.</p>
        <div class="contact-card-styled">
            <h3>{operator_name}</h3>
            <p><span class="icon">✉️</span><strong>이메일:</strong> <a href="mailto:{contact_email}">{contact_email}</a></p>
            <p><span class="icon">📞</span><strong>연락처:</strong> <a href="tel:{phone_number.replace('-', '')}">{phone_number}</a></p>
        </div>
    </section>
    """
    st.markdown(section_style, unsafe_allow_html=True)

def display_footer():
    footer_html = f"""
    <style>
        .page-footer {{ background-color: var(--background-dark-gray); color: var(--text-muted); padding: 70px 25px; text-align: center; font-size: 1rem; line-height: 1.75; }}
        .footer-logo-container {{ margin-bottom: 35px; display: flex; justify-content: center; align-items: center; gap: 35px; flex-wrap: wrap; }}
        .footer-logo-item img {{ max-width: 170px; max-height: 55px; object-fit: contain; opacity: 0.9; filter: brightness(150%) contrast(110%); }}
    </style>
    <footer class="page-footer">
        <div class="footer-logo-container">
            <div class="footer-logo-item">{f'<img src="{LOGO_MOHW_DATA_URI}" alt="보건복지부">' if LOGO_MOHW_DATA_URI else "<span>보건복지부</span>"}</div>
            <div class="footer-logo-item">{f'<img src="{LOGO_KSSI_DATA_URI}" alt="중앙사회서비스원">' if LOGO_KSSI_DATA_URI else "<span>중앙사회서비스원</span>"}</div>
            <div class="footer-logo-item">{f'<img src="{LOGO_MYSC_DATA_URI}" alt="엠와이소셜컴퍼니(MYSC)">' if LOGO_MYSC_DATA_URI else "<span>엠와이소셜컴퍼니(MYSC)</span>"}</div>
        </div>
        <p class="footer-copyright">© 2025 사회서비스 투자 교류회 운영사무국. All Rights Reserved.<br>본 투자교류회는 <strong>보건복지부, 중앙사회서비스원, 엠와이소셜컴퍼니(MYSC)</strong>가 함께합니다.</p>
    </footer>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

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