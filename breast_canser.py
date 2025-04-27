import pickle
import joblib
import numpy as np
import streamlit as st

# load save model
model = joblib.load('random_search.sav')


# Tambahkan CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    /* Frame untuk seluruh aplikasi */
    .main-frame {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        padding: 20px;
        background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
        z-index: -1;
    }
    
    /* Mengatur tampilan utama */
    .stApp {
        background-color: #ffffff; /* Warna putih */
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        width: calc(100vw - 40px);
        height: calc(100vh - 40px);
        margin: 0;
        overflow: auto;
        position: relative;
        border: 15px solid #ffffff; /* Bingkai putih */
        outline: 1px solid #e0e0e0; /* Garis tipis sebagai aksen */
    }

    /* Kontainer utama */
    .block-container {
        padding: 2rem;
        max-width: 800px;
        margin: auto;
        background-color: #ffffff;
        border-radius: 8px;
    }

    /* Header */
    h1, h2, h3, h4, h5, h6 {
        color: #212529;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
        margin-bottom: 1.5rem;
    }

    /* Label teks */
    label {
        font-weight: bold;
        color: #333333;
        font-size: 18px;
        margin-bottom: 0.5rem;
        display: block;
    }

    /* Teks utama */
    body, p, div, span {
        color: #212529;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
    }

    /* Gaya tombol */
    .stButton>button {
        background-color: #007bff;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        display: block;
        margin: 1rem auto;
        width: fit-content;
    }

    /* Efek hover tombol */
    .stButton>button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    /* Kotak input */
    .stTextInput>div>div>input {
        border: 2px solid #e0e0e0;
        border-radius: 8px;
        padding: 12px;
        font-size: 16px;
        background-color: #ffffff;
        transition: border-color 0.3s ease;
    }

    .stTextInput>div>div>input:focus {
        border-color: #007bff;
        box-shadow: 0 0 0 2px rgba(0,123,255,0.2);
    }

    /* Checkbox & Radio button */
    .stCheckbox, .stRadio {
        font-size: 18px;
        color: #212529;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin: 5px 0;
    }

    /* Gaya utama Selectbox */
    .stSelectbox div[data-baseweb="select"] {
        border: 2px solid #e0e0e0 !important;
        border-radius: 8px !important;
    }

    .stSelectbox div[data-baseweb="select"] * {
        color: #212529 !important;
        font-size: 18px !important;
        font-family: 'Arial', sans-serif !important;
    }

    /* Gaya untuk daftar dropdown */
    .stSelectbox div[data-baseweb="popover"] {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
    }

    /* Gaya untuk setiap opsi dalam dropdown */
    .stSelectbox div[data-baseweb="option"] {
        color: #212529 !important;
        background-color: #ffffff !important;
        padding: 12px !important;
        font-size: 18px !important;
    }

    /* Gaya hover pada opsi dropdown */
    .stSelectbox div[data-baseweb="option"]:hover {
        background-color: #f8f9fa !important;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .stApp {
            width: 100vw;
            height: 100vh;
            padding: 1rem;
            border: none;
            border-radius: 0;
        }
        
        .block-container {
            padding: 1rem;
        }
    }
    </style>
    
    <div class="main-frame"></div>
""", unsafe_allow_html=True)
# Inisialisasi session state untuk melacak halaman
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Navigasi antara halaman
if st.session_state.page == "Home":
    st.title("Selamat Datang di Aplikasi Prediksi Kanker Payudara!")
    st.write("""
        Aplikasi ini dirancang untuk membantu Anda dalam memprediksi penyakit kanker payudara berdasarkan berbagai faktor kesehatan.
        
        **Fitur Utama:**
        - Input data kesehatan seperti umur, ukuran tumor, dan grade tumor.
        - Prediksi penyakit kanker payudara menggunakan model machine learning yang andal.
        
        Silakan klik tombol di bawah ini untuk memulai prediksi Anda!
    """)

    # Tombol untuk navigasi ke halaman prediksi
    if st.button("Mulai Prediksi"):
        st.session_state.page = "Prediksi"

elif st.session_state.page == "Prediksi":
    st.title('Prediksi Penyakit Kanker Payudara')

    # Tata letak dua kolom besar
    col_left, col_right = st.columns(2)

    with col_left:
        age = st.number_input('Age', step=2, min_value=0)
        race = st.selectbox('Race (White : 0, Black : 1, Other : 2', [0, 1, 2])
        martial_status = st.selectbox('Martial Status (Married : 0, Divorced : 1, Single : 2, Widowed : 3, Separated : 4)', [0, 1, 2, 3, 4])
        t_stage = st.selectbox('T Stage (T1 : 0, T2 : 1, T3 : 2, T4 : 3)', [0, 1, 2, 3])
        n_stage = st.selectbox('N Stage (N1 : 0, N2 : 1, N3 : 2', [0, 1, 2])
        th_stage = st.selectbox('6th Stage (IIA : 0, IIIA : 1, IIIC : 2, IIB : 3, IIIB : 4)', [0, 1, 2, 3, 4])
        differentiate = st.selectbox('Differentiate (Poorly differentiated : 0, Moderately differentiated : 1, Well differentiated : 2, Undifferentiated : 3)', [0, 1, 2, 3])
    with col_right:
        grade = st.selectbox('Grade (1 : 1, 2 : 2, 3 : 3, IV : 4, Anaplastic : 5)', [1, 2, 3, 4, 5])
        a_stage = st.selectbox('A Stage (Regional : 0, Distant : 1)', [0, 1])
        tumor_size = st.number_input('Tumor Size', step=2, min_value=0)
        estrogen_status = st.selectbox('Estrogen Status (Positive : 0, Negative : 1)', [0, 1])
        progesterone_status = st.selectbox('Progesterone Status (Positive : 1, Negative : 0)', [1, 0])
        regional_node_examined = st.number_input('Regional Node Examined', step=2, min_value=0)
        Reginol_Node_Positive = st.number_input('Regional Node Positive', step=2, min_value=0)
        Survival_Months = st.number_input('Survival Months', step=2, min_value=0)
        

    # Code untuk prediksi
    cancer_diagnosis = ''

    # Membuat tombol prediksi
    if st.button('Prediksi Penyakit Kanker Payudara'):
        cancer_diagnosis_prediction = model.predict([[age, race, martial_status, t_stage, n_stage, 
                                            th_stage, differentiate, grade, a_stage, 
                                            tumor_size, estrogen_status, progesterone_status, regional_node_examined
                                            , Reginol_Node_Positive, Survival_Months  ]])
        
        if cancer_diagnosis_prediction[0] == 0:
            cancer_diagnosis = 'Kemungkinan Hidup 60%'
        else:
            cancer_diagnosis = 'Kemungkinan Mati 60%'

    st.success(cancer_diagnosis)

    # Tombol kembali ke halaman Home
    if st.button("Kembali ke Home"):
        st.session_state.page = "Home"
