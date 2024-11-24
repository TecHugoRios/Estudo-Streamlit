import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def sendemail(nome, titulo, mensagem, foto):
    sender = f"{nome}<user@demomailtrap.com>"
    receiver = "AquaSpy <hugoba532@gmail.com>"

    # Cria o e-mail com partes personalizadas
    msg = MIMEMultipart()
    msg['Subject'] = titulo
    msg['From'] = sender
    msg['To'] = receiver

    # Adiciona o texto ao e-mail
    body = f"Nome:\n {nome}\n\nMensagem:\n{mensagem}"
    msg.attach(MIMEText(body, 'plain'))

    # Adiciona a imagem como anexo
    if foto is not None:
        img = foto.read()
        image = MIMEImage(img)
        image.add_header('Content-Disposition', 'attachment', filename=foto.name)
        msg.attach(image)

    # Envia o e-mail
    with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
        server.starttls()
        server.login("api", "c669a11159c33ff4033285e892079063")
        server.sendmail(sender, receiver, msg.as_string())


# Interface Streamlit
with st.form("email_form"):
    st.write("Denuncie acúmulo de resíduo plástico na sua área.")

    nome = st.text_input("Nome")
    titulo = st.text_input("Título")
    mensagem = st.text_area("Mensagem")
    foto = st.file_uploader("Enviar foto", type=["png", "jpg", "jpeg"])

    submitted = st.form_submit_button("Enviar")

# Verifica se o formulário foi enviado
if submitted:
    if nome and mensagem and titulo and foto:  # Verifica se todos os campos estão preenchidos
        sendemail(nome, titulo, mensagem, foto)
        st.success("Email enviado com sucesso!")
        st.toast('Obrigado por ajudar o planeta!', icon='🎉')
        st.balloons()
    else:
        st.error("Por favor, preencha todos os campos e envie uma foto.")
