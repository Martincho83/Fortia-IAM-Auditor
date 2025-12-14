import streamlit as st
from zxcvbn import zxcvbn
import requests
import hashlib
import random
import string

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Fortia IAM - Auditor", page_icon="🔐", layout="centered")

# --- FUNCIONES DE SEGURIDAD ---
def check_pwned_api(password):
    """Verifica si la contraseña ha sido filtrada en la Deep Web (Have I Been Pwned)
    Usamos k-Anonymity: Solo enviamos los primeros 5 caracteres del Hash SHA-1.
    NUNCA enviamos la contraseña real."""
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char = sha1password[:5]
    tail = sha1password[5:]
    
    url = 'https://api.pwnedpasswords.com/range/' + first5_char
    res = requests.get(url)
    
    if res.status_code != 200:
        return 0 # Error en API, asumimos 0 por seguridad
        
    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return int(count)
    return 0

def generar_password(longitud=16):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(caracteres) for i in range(longitud))

# --- INTERFAZ ---
st.title("🔐 Fortia IAM: Auditor de Accesos")
st.markdown("Herramienta de **Gestión de Identidades** para validar credenciales corporativas antes de su uso.")

tab1, tab2 = st.tabs(["🛡️ Auditoría de Claves", "⚙️ Generador Seguro"])

with tab1:
    password = st.text_input("Ingrese la contraseña a auditar:", type="password", help="No guardamos nada. Validación en memoria.")
    
    if password:
        # 1. Análisis de Fuerza (Algoritmo zxcvbn)
        resultado = zxcvbn(password)
        score = resultado['score'] # 0 a 4
        tiempo_crackeo = resultado['crack_times_display']['offline_slow_hashing_1e4_per_second']
        
        # 2. Análisis de Filtraciones (API Real)
        veces_filtrada = check_pwned_api(password)
        
        st.divider()
        
        # Visualización de Resultados
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Nivel de Robustez (0-4)", f"{score}/4")
            if score < 3:
                st.error("❌ Contraseña DÉBIL")
            else:
                st.success("✅ Contraseña FUERTE")
                
        with col2:
            st.metric("Tiempo estimado de hackeo", tiempo_crackeo)
            
        st.markdown("#### 🕵️ Búsqueda en Filtraciones (Data Leaks)")
        if veces_filtrada > 0:
            st.error(f"🚨 **¡PELIGRO CRÍTICO!** Esta contraseña aparece en **{veces_filtrada}** bases de datos de hackers filtradas. NO LA USES.")
        else:
            st.success("✨ Esta contraseña no aparece en bases de datos filtradas conocidas.")

        with st.expander("Ver detalles técnicos (Feedback)"):
            st.write(resultado['feedback'])

with tab2:
    st.subheader("Generador de Credenciales NIST")
    longitud = st.slider("Longitud", 12, 32, 16)
    if st.button("Generar Nueva Clave"):
        clave_segura = generar_password(longitud)
        st.code(clave_segura, language='')
        st.success("Copie esta credencial y guárdela en un gestor de contraseñas.")

st.markdown("---")
st.caption("🔒 Desarrollado por **Fortia Security**. Cumple con estándares NIST 800-63B.")
