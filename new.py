import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import pandas as pd


st.set_page_config(layout="centered", page_icon="🍜", page_title="IniMiePedas")




#Harga harga
#Makanan
hmiegorengpedas = 11000
hmiekuahpedas = 11000
hmiekuahsegar = 11000
hmieseblak = 11000
hmieayamgoreng = 11000

#Topping
hkerupukbawang = 1000
hnugget = 2000
hpangsitr = 2000
hpangsitg = 2000
hceker = 2000
hkerupukudang = 2000
hbaksoayam = 1000
hbaksoikan = 2000
hbaksoudang = 2000
hdimsum = 2000

#Minuman
hesteh = 3000
hestehk = 4000
hesus = 6000
hesust = 7000


selected = option_menu(
    menu_title = None,
    options = ["Home", "Cara memesan", "Kontak"],
    icons = ["house", "book", "envelope"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
    )
if selected == "Home":

    # Buat Judul
    st.markdown("<h1 style='text-align: center;'>INI MIE PEDAS</h1>", unsafe_allow_html=True)


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_iabttnbo.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # medium ; high
        height=300,
        width=None,
        key=None,
    )

    st.markdown("<h2 style='text-align: center; color: black;'>Silahkan Pilih Pesanan Anda 🍜</h1>", unsafe_allow_html=True)


    # Buat input duls
    # st.text_input itu buat masukin teks buat masukkin nama
    # st.number_input itu buat masukkin angka


    nama = st.text_input("Atas Nama")
    makanmana = st.radio(
        "Makan mana kak?",
        ('Disini', 'Bawa pulang'))

    if makanmana == 'Disini':
        meja = st.number_input("Meja berapa (1-12)", 1, 12)
    else:
        st.info("Anda memilih bawa pulang")


    st.markdown("##")
    st.markdown("##")
    st.markdown("##")
    st.write('-' * 100)


    col1, col2 = st.columns(2)
    with col1:
        st.success("Makanan")
        #Mie goreng pedas
        st.image("https://d1sag4ddilekf6.azureedge.net/compressed_webp/items/IDITE2020050907121874043/detail/menueditor_item_4def51a34c20408ab7c05eefd1da2bb7_1607659990742315735.webp", width=319)
        st.write("Rp 11.000")
        st.markdown("#")
        st.markdown("#")
        st.markdown("##")
        st.text("-----------------------------------------")

        #Mie kuah pedas
        st.image("https://d1sag4ddilekf6.azureedge.net/compressed_webp/items/IDITE2020050907110325852/detail/menueditor_item_a38b8ff252b14865abed69af3e21e836_1589008262887214749.webp", width=317)
        st.write("Rp 11.000")
        st.markdown("#")
        st.markdown("#")
        st.markdown("##")
        st.text("-----------------------------------------")



        #Mie kuah segar
        st.image("https://d1sag4ddilekf6.azureedge.net/compressed_webp/items/IDITE2020050907100593593/detail/menueditor_item_cefc969bab14469f9ec5108c0b80f0b9_1589008205212294087.webp", width=321)
        st.write("Rp 11.000")
        st.text("-----------------------------------------")



        #Mie seblak spesial
        st.image("https://d1sag4ddilekf6.azureedge.net/compressed_webp/items/IDITE2020050907142399707/detail/menueditor_item_b8a5ce81a6e84fd5809096a1f76a36e7_1589008462707742447.webp", width=317)
        st.write("Rp 11.000")
        st.markdown("#")
        st.markdown("#")
        st.markdown("##")
        st.text("-----------------------------------------")

        #Mie ayam goreng
        st.image("https://d1sag4ddilekf6.azureedge.net/compressed_webp/items/IDITE2020050907131855192/detail/menueditor_item_0d37748b48b44b06b7c261a0bfe84298_1589008398446055359.webp", width=321)
        st.write("Rp 11.000")
        st.text("-----------------------------------------")


        st.warning("Topping")
        kbawang = st.number_input("Kerupuk Bawang (Rp 1.000)", 0)
        nuget = st.number_input ("Nugget (Rp 2.000)", 0)
        pangsitr = st.number_input("Pangsit Rebus (Rp 2.000)", 0)
        pangsitg = st.number_input("Pangsit Goreng (Rp 2.000)", 0)
        ceker = st.number_input("Ceker Pedas (Rp 2.000)", 0)

        st.info("Minuman")
        st.image("https://d1sag4ddilekf6.azureedge.net/compressed_webp/items/IDITE2020050808303231685/detail/menueditor_item_179e7a6247ae451a8febe11b76d34422_1662446974570934973.webp", width=307)
        st.text("-----------------------------------------")
        st.image("https://d1sag4ddilekf6.azureedge.net/compressed_webp/items/IDITE2020050808313856027/detail/menueditor_item_a60872615b964c12b800d7b090b12d62_1588926698146092576.webp", width=305)
        st.text("-----------------------------------------")




    with col2:
        st.success("-")
        #Mie goreng pedas
        migoreng = st.number_input("Mie Goreng Pedas lvl 1", 0)
        migoreng2 = st.number_input("Mie Goreng Pedas lvl 2", 0)
        migoreng3 = st.number_input("Mie Goreng Pedas lvl 3", 0)
        migoreng4 = st.number_input("Mie Goreng Pedas lvl 4", 0)
        migoreng5 = st.number_input("Mie Goreng Pedas lvl 5", 0)


        st.markdown("#")
        st.text("-----------------------------------------")

        #Mie kuah pedas
        mikuah= st.number_input("Mie Kuah Pedas lvl 1", 0)
        mikuah2 = st.number_input("Mie Kuah Pedas lvl 2", 0)
        mikuah3 = st.number_input("Mie Kuah Pedas lvl 3", 0)
        mikuah4 = st.number_input("Mie Kuah Pedas lvl 4", 0)
        mikuah5 = st.number_input("Mie Kuah Pedas lvl 5", 0)
        st.markdown("#")
        st.text("-----------------------------------------")


        #Mie kuah segar
        mikuahsegar = st.number_input("Mie Kuah Segar", 0)
        st.text("*Tidak Pedas")

        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")

        st.text("-----------------------------------------")


        #Mie seblak spesial
        miseblak = st.number_input("Mie Seblak Spesial lvl 1", 0)
        miseblak2 = st.number_input("Mie Seblak Spesial lvl 2", 0)
        miseblak3 = st.number_input("Mie Seblak Spesial lvl 3", 0)
        miseblak4 = st.number_input("Mie Seblak Spesial lvl 4", 0)
        miseblak5 = st.number_input("Mie Seblak Spesial lvl 5", 0)

        st.markdown("#")
        st.text("-----------------------------------------")



        #Mie ayam goreng
        miayamgoreng = st.number_input("Mie Ayam Goreng", 0)
        st.text("*Saos diberikan setiap pembelian")

        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.text("-----------------------------------------")


        st.warning("-")
        kudang = st.number_input("Kerupuk Udang (Rp 1.500)", 0)
        bayam = st.number_input("Bakso Ayam (Rp 1.000)", 0)
        bikan = st.number_input("Bakso Ikan (Rp 2.000)", 0)
        budang = st.number_input("Bakso Udang (Rp 2.000)", 0)
        dimsum = st.number_input("Dimsum (Rp 2.000)", 0)


        st.info("-")
        esteh = st.number_input("Es Teh", 0)
        estehk = st.number_input("Es Teh Kampul", 0)

        st.markdown("##")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.text("-----------------------------------------")


        essusu = st.number_input("Es Susu Putih", 0)
        essusut = st.number_input("Es Tape Susu", 0)

        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.text("-----------------------------------------")


#Mie goreng pedas
    jmiepedas = (migoreng * hmiegorengpedas)
    jmiepedas2 = (migoreng2 * hmiegorengpedas)
    jmiepedas3 = (migoreng3 * hmiegorengpedas)
    jmiepedas4 = (migoreng4 * hmiegorengpedas)
    jmiepedas5 = (migoreng5 * hmiegorengpedas)

    tmipedas = jmiepedas + jmiepedas2 + jmiepedas3 + jmiepedas4 + jmiepedas5

#mie kuah pedas
    jmiekuah = (mikuah * hmiekuahpedas)
    jmiekuah2 = (mikuah2 * hmiekuahpedas)
    jmiekuah3 = (mikuah3 * hmiekuahpedas)
    jmiekuah4 = (mikuah4 * hmiekuahpedas)
    jmiekuah5 = (mikuah5 * hmiekuahpedas)

    tmikuah = jmiekuah + jmiekuah2 + jmiekuah3 + jmiekuah4 + jmiekuah5

#mie kuah segar
    jmiekuahsegar = (mikuahsegar * hmiekuahsegar)

#mie seblak spesial
    jmieseblak = (miseblak * hmieseblak)
    jmieseblak2 = (miseblak2 * hmieseblak)
    jmieseblak3 = (miseblak3 * hmieseblak)
    jmieseblak4 = (miseblak4 * hmieseblak)
    jmieseblak5 = (miseblak5 * hmieseblak)

    tmiseblak = jmieseblak + jmieseblak2 + jmieseblak3 + jmieseblak4 + jmieseblak5

#mie ayam goreng
    jmieayamgoreng = (miayamgoreng * hmieayamgoreng)

#Topping
    jkbawang = (kbawang * hkerupukbawang)
    jnuget = (nuget * hnugget)
    jpangsitr = (pangsitr * hpangsitr)
    jpangsitg = (pangsitg * hpangsitg)
    jceker = (ceker * hceker)
    jkudang = (kudang * hkerupukudang)
    jbayam = (bayam * hbaksoayam)
    jbikan = (bikan * hbaksoikan)
    jbudang = (budang * hbaksoudang)
    jdimsum = (dimsum * hdimsum)

#Minuman
    jesteh = (esteh * hesteh)
    jestehk = (estehk * hestehk)
    jessusu = (essusu * hesus)
    jessusut = (essusut * hesust)

#Penjumlahan
    hitungmakanan = (tmipedas + tmikuah + jmiekuahsegar + tmiseblak + jmieayamgoreng)
    hitungtopping = (jkbawang + jnuget + jpangsitr + jpangsitg + jceker + jkudang +jbayam +jbikan + jbudang + jdimsum  )
    hitungminuman = ( jesteh + jestehk + jessusu + jessusut)

    st.write('-' * 100)


    if makanmana == 'Disini':

        st.write("Kak",nama, "Memilih Untuk Makan", makanmana, "Dengan Meja Nomor", meja)

    else:
        st.write("Kak", nama, "Memilih Untuk", makanmana, "Makanannya")

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_cvxx4oei.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # medium ; high
        height=200,
        width=None,
        key=None,
    )





#NOTA
#NOTA MAKANAN
    st.text("Pesanan anda =")
    #MIE GORENG PEDAS
    if migoreng >= 1:
        st.write("Mie Goreng Pedas lvl 1_________", migoreng, "@Rp 11.000 = ____Rp", jmiepedas)

    if migoreng2 >= 1:
        st.write("Mie Goreng Pedas lvl 2_________", migoreng2, "@Rp 11.000 = ____Rp", jmiepedas2)

    if migoreng3 >= 1:
        st.write("Mie Goreng Pedas lvl 3_________", migoreng3, "@Rp 11.000 = ____Rp", jmiepedas3)

    if migoreng4 >= 1:
        st.write("Mie Goreng Pedas lvl 4_________", migoreng4, "@Rp 11.000 = ____Rp", jmiepedas4)

    if migoreng5 >= 1:
        st.write("Mie Goreng Pedas lvl 5_________", migoreng5, "@Rp 11.000 = ____Rp", jmiepedas5)


    #MIE KUAH PEDAS
    if mikuah >= 1:
        st.write("Mie Kuah Pedas lvl 1___________", mikuah, "@Rp 11.000 = ____Rp", jmiekuah)

    if mikuah2 >= 1:
        st.write("Mie Kuah Pedas lvl 2___________", mikuah2, "@Rp 11.000 = ____Rp", jmiekuah2)

    if mikuah3 >= 1:
        st.write("Mie Kuah Pedas lvl 3___________", mikuah3, "@Rp 11.000 = ____Rp", jmiekuah3)

    if mikuah4 >= 1:
        st.write("Mie Kuah Pedas lvl 4___________", mikuah4, "@Rp 11.000 = ____Rp", jmiekuah4)

    if mikuah5 >= 1:
        st.write("Mie Kuah Pedas lvl 5___________", mikuah5, "@Rp 11.000 = ____Rp", jmiekuah5)


    #MIE KUAH SEGAR
    if mikuahsegar >= 1:
        st.write("Mie Kuah Segar_______________", mikuahsegar, "@Rp 11.000 = ____Rp", jmiekuahsegar)

    #MIE SEBLAK SPESIAL
    if miseblak >= 1:
        st.write("Mie Seblak Spesial lvl 1_________", miseblak, "@Rp 11.000 = ____Rp", jmieseblak)

    if miseblak2 >= 1:
        st.write("Mie Seblak Spesial lvl 2_________", miseblak2, "@Rp 11.000 = ____Rp", jmieseblak2)

    if miseblak3 >= 1:
        st.write("Mie Seblak Spesial lvl 3_________", miseblak3, "@Rp 11.000 = ____Rp", jmieseblak3)

    if miseblak4 >= 1:
        st.write("Mie Seblak Spesial lvl 4_________", miseblak4, "@Rp 11.000 = ____Rp", jmieseblak4)

    if miseblak5 >= 1:
        st.write("Mie Seblak Spesial lvl 5_________", miseblak5, "@Rp 11.000 = ____Rp", jmieseblak5)

        #MIE AYAM GORENG
    if miayamgoreng >= 1:
        st.write("Mie Ayam Goreng______________", miayamgoreng, "@Rp 11.000 = ____Rp", jmieayamgoreng)


#TOPPING
    #KERUPUK BAWANG
    if kbawang >= 1:
        st.write("Kerupuk Bawang______________", kbawang, "@Rp 1.000 = _____Rp", jkbawang)

    #NUGGET
    if nuget >= 1:
        st.write("Nugget______________________", nuget, "@Rp 2.000 = _____Rp", jnuget)

    #Pangsit Rebus
    if pangsitr >= 1:
        st.write("Pangsit Rebus________________", pangsitr, "@Rp 2.000 = _____Rp", jpangsitr)

    #Pangsit Goreng
    if pangsitg >= 1:
        st.write("Pangsit Goreng_______________", pangsitg, "@Rp 2.000 = _____Rp", jpangsitg)

    #Ceker Pedas
    if ceker >= 1:
        st.write("Ceker Pedas_________________", ceker, "@Rp 2.000 = _____Rp", jceker)

    #Kerupuk Udang
    if kudang >= 1:
        st.write("Kerupuk Udang______________", kudang, "@Rp 2.000 = _____Rp", jkudang)

    #Bakso ayam
    if bayam >= 1:
        st.write("Bakso Ayam_________________", bayam, "@Rp 1.000 = _____Rp", jbayam)

    #Bakso Ikan
    if bikan >= 1:
        st.write("Bakso Ikan__________________", bikan, "@Rp 2.000 = _____Rp", jbikan)

    #Bakso Udang
    if budang >= 1:
        st.write("Bakso Udang________________", budang, "@Rp 2.000 = _____Rp", jbudang)

#Minuman
    #Es teh
    if esteh >= 1:
        st.write("Es Teh_____________________", esteh, "@Rp 3.000 = _____Rp", jesteh)

    #Es teh Kampul
    if estehk >= 1:
        st.write("Es Teh Kampul______________", estehk, "@Rp 4.000 = _____Rp", jestehk)

    #Es susu
    if essusu >= 1:
        st.write("Es Susu Putih_______________", essusu, "@Rp 6.000 = _____Rp", jessusu)

    #Es susu
    if essusut >= 1:
        st.write("Es Susu Tape_______________", essusut, "@Rp 7.000 = _____Rp", jessusut)

    total = (hitungmakanan + hitungtopping + hitungminuman)
    st.write("----------------------------------------------------------------------------")


    if total >= 1:
        totalq = st.write("Total pembelian anda adalah______________________Rp", total)

        st.markdown("#")
        st.markdown("#")
        st.markdown("#")

        agree = st.checkbox('Saya sudah memastikan pesanan saya sudah benar, dan saya ingin memesan')

        if agree:
            uang = st.number_input("Masukkan nominal uang anda", 0)
            tbayar = st.button("Bayar")
            kembalian = uang - total
            if tbayar:
                if uang >= total:
                    st.success("Pembayaran berhasil")
                    st.markdown("#")

                    def load_lottieurl(url: str):
                        r = requests.get(url)
                        if r.status_code != 200:
                            return None
                        return r.json()


                    lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/temp/lf20_q6KowU.json")

                    st_lottie(
                        lottie_hello,
                        speed=1,
                        quality="high",
                        height=200
                    )

                    st.write("Kembalian anda adalah Rp", kembalian)


                else:
                    st.warning("Uang anda tidak cukup")
                    st.markdown("#")


                    def load_lottieurl(url: str):
                        r = requests.get(url)
                        if r.status_code != 200:
                            return None
                        return r.json()


                    lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_s2ezQQs32F.json")

                    st_lottie(
                        lottie_hello,
                        speed=1,
                        quality="high",
                        height=200
                    )




    else:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        noorder = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_tll0j4bb.json")

        st_lottie(
            noorder,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",  # medium ; high
            height=250,
            width=None,
            key=None,
        )
        st.warning("Anda belum memesan :(")



if selected == "Cara memesan":
    st.markdown("<h2 style='text-align: center; color: white;'>Bagaimana Caranya?</h1>", unsafe_allow_html=True)

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    howto = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_UlXgnV.json")

    st_lottie(
        howto,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # medium ; high
        height=250,
        width=None,
        key=None,
    )

    st.markdown("#")

    st.write("1. Isi nama anda untuk mendapatkan panggilan dari kasir apabila makanan sudah siap")
    st.write("2. Pilih makanan, topping, dan minuman yang diinginkan")
    st.write('3. Cek apakah makanan yang dipesan sudah benar dan centang "Saya sudah memastikan pesanan saya sudah benar, dan saya ingin memesan"')
    st.write("4. Pilih metode pembayaran anda")
    st.markdown("#")
    st.markdown("#")
    st.markdown("#")
    st.write("*Segera laporkan kasir apabila terdapat salah pesan atau kesalahan yang terjadi dalam aplikasi")


if selected == "Kontak":
    st.markdown("<h2 style='text-align: center; color: white;'>Kami Selalu Mendengarkan Anda</h1>", unsafe_allow_html=True)
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    kontak = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_zhwxnxsj.json")

    st_lottie(
        kontak,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # medium ; high
        height=250,
        width=None,
        key=None,
    )


    st.text("Whatsapp   : 0815-1929-2601            (Widiya)")
    st.text("E-mail     : elfiramulia@gmail.com     (Elfira)")
    st.text("Instagram  : inimiepedas")





