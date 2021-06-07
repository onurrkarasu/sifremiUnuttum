# Şifremi unuttum
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def sifreyiGetir(kullanici_adi):
    dosya=open("kullanicilar.txt","r")
    satirlar=dosya.readlines()

    for kullanici in satirlar:
        bolunmus=kullanici.split()
        k_adi=bolunmus[0]
        sifre=bolunmus[1]
        mail=bolunmus[2]
        if kullanici_adi==k_adi:
            sifreyi_mail_gonder(kullanici_adi=kullanici_adi,mail=mail,sifre=sifre)



def sifreyi_mail_gonder(kullanici_adi,mail,sifre):
    gonderici_mail="phponur1@gmail.com"
    mesaj_icerigi="""
                    Merhabalar {kullanici_adi};
                     Şifrenizi unutmuşsunuz ve {tarih} tarihinde  mailinize gönderilmesini talep ettiniz.
                     
                     Şifreniz {sifre} 
                  """
    mesaj=MIMEMultipart()
    mesaj["Suject"]="Şifreniz Gönderildi"
    mesaj["From"] =gonderici_mail
    mesaj["To"] =mail

    tarih_bugun=datetime.now()

    mesaj_formatlanmis=mesaj_icerigi.format(kullanici_adi=kullanici_adi,tarih=tarih_bugun.strftime("%d/%M/%Y %H:%M:%S"),sifre=sifre)

    mesaj.attach(MIMEText(mesaj_formatlanmis,"plain"))

    mail_servisi=smtplib.SMTP("smtp.gmail.com",587)
    mail_servisi.ehlo()
    mail_servisi.starttls()
    mail_servisi.login("phponur1@gmail.com","Krokeri123")
    mail_servisi.sendmail(gonderici_mail,mail,mesaj.as_string())
    mail_servisi.quit()
    print("Mail Gönderildi")


if __name__=="__main__":
    sifreyiGetir("onur2")
