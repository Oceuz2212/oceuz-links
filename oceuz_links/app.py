import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="Oceuz | Official Links",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS avanzados (Dark Mode con branding Oceuz: #0A0A10 y morado #8B3DFF)
st.markdown("""
    <style>
    /* Ocultar barra superior y menú lateral de Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Fondo principal */
    .stApp {
        background-color: #0A0A10;
        color: #FFFFFF;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Contenedor del perfil */
    .profile-header {
        text-align: center;
        padding-top: 2rem;
        padding-bottom: 1.5rem;
    }
    
    .profile-avatar {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        border: 2px solid #8B3DFF;
        object-fit: cover;
        margin-bottom: 1rem;
        box-shadow: 0 0 15px rgba(139, 61, 255, 0.4);
    }
    
    .profile-title {
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 0.3rem;
        color: #FFFFFF;
    }
    
    .profile-bio {
        font-size: 0.95rem;
        color: #8B3DFF;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    
    /* Botones de enlaces */
    .link-card {
        display: block;
        width: 100%;
        background-color: #12121C;
        color: #FFFFFF !important;
        text-decoration: none !important;
        padding: 16px 20px;
        margin-bottom: 14px;
        border-radius: 12px;
        border: 1px solid rgba(139, 61, 255, 0.3);
        text-align: center;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.25s ease-in-out;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    
    .link-card:hover {
        background-color: #8B3DFF;
        border-color: #A366FF;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 61, 255, 0.5);
    }
    
    /* Pie de página */
    .footer-text {
        text-align: center;
        color: #555566;
        font-size: 0.8rem;
        margin-top: 2.5rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera del perfil
st.markdown("""streamlit run app.py
    <div class="profile-header">
        <h1 class="profile-title">OCEUZ</h1>
        <div class="profile-bio">Music Producer & Type Beats</div>
    </div>
""", unsafe_allow_html=True)

# Lista de Enlaces
# Sustituye las URLs por tus enlaces reales
links = [
    {"title": "🔥 Canal Roa Type Beats", "url": "https://youtube.com"},
    {"title": "🌌 Canal Juice WRLD Type Beats", "url": "https://youtube.com"},
    {"title": "💃 Canal Reggaeton Type Beats", "url": "https://youtube.com"},
    {"title": "🎷 Canal Funk / R&B Type Beats", "url": "https://youtube.com"},
    {"title": "🛒 Compra / Venta Beats (BeatStars)", "url": "https://beatstars.com"},
    {"title": "💬 Contacto Directo por Instagram", "url": "https://instagram.com"}
]

# Renderizar botones
for item in links:
    st.markdown(f"""
        <a href="{item['url']}" target="_blank" class="link-card">
            {item['title']}
        </a>
    """, unsafe_allow_html=True)

# Pie de página
st.markdown("""
    <div class="footer-text">
        © 2026 Oceuz. Todos los derechos reservados.
    </div>
""", unsafe_allow_html=True)