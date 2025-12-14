
# 🔐 Fortia IAM: Auditor de Identidad y Accesos

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red)
![Security](https://img.shields.io/badge/Security-NIST_800--63B-orange)
![API](https://img.shields.io/badge/API-HaveIBeenPwned-green)

> **Herramienta de Gestión de Identidades (IAM)** para la validación de credenciales corporativas y prevención de fugas de datos.  
> *Desarrollado por Martincho83.*

---

## 📋 Descripción

El 81% de las brechas de seguridad en empresas se deben a contraseñas débiles o reutilizadas. **Fortia IAM** es una solución diseñada para auditar la robustez de las credenciales antes de que sean asignadas a los empleados.

Utiliza algoritmos de entropía y consultas a bases de datos de filtraciones reales para garantizar que ninguna contraseña comprometida sea utilizada en la organización.

### 🚀 Demo en Vivo
👉 **[ACCEDER A LA APLICACIÓN](https://fortia-iam-auditor-qr5cne6nkjpg2qtnovpsta.streamlit.app/)**

---

## 🛡️ Funcionalidades Técnicas

1.  **Auditoría de Fortaleza (zxcvbn):**
    *   Utiliza el algoritmo desarrollado por Dropbox para medir la entropía real de una clave.
    *   Estima el tiempo que tardaría un ataque de fuerza bruta en romperla.

2.  **Verificación de Filtraciones (Data Leaks):**
    *   Conexión vía API con la base de datos *Have I Been Pwned* (más de 11 mil millones de cuentas filtradas).
    *   **Privacidad (k-Anonymity):** Implementación segura que **NUNCA** envía la contraseña real a la nube. Solo se envían los primeros 5 caracteres del hash SHA-1, garantizando anonimato total.

3.  **Generador NIST:**
    *   Creación de credenciales aleatorias criptográficamente seguras cumpliendo normativas internacionales.

---

## 🛠️ Tecnologías

*   **Python 3.9**
*   **Streamlit** (Frontend)
*   **Requests** (Consumo de API REST)
*   **Hashlib** (Criptografía SHA-1)

---

## 👨‍💻 Autor

**[Martincho83](https://github.com/Martincho83)** 
