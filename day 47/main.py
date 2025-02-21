import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.header import Header

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/",
    "DNT": "1"
}

def get_price():
    url = "https://www.amazon.com/dp/B075CYMYK6"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        # Verificar se não é página de bloqueio
        if "robot check" in response.text.lower():
            raise Exception("Bloqueado pela Amazon - Verificação de robô necessária")
            
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Seletor atualizado e verificação de elemento
        price_element = soup.select_one('span.a-price span.a-offscreen')
        
        if not price_element:
            raise ValueError("Elemento de preço não encontrado")
            
        price_text = price_element.get_text(strip=True)
        return float(price_text.split("$")[1].replace(",", ""))
        
    except Exception as e:
        print(f"Erro: {e}")
        return None

def send_email(price, link):
    try:
        subject = Header(f"🚨 Amazon Price Alert: ${price}", 'utf-8')
        body = f"""Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker
        Current Price: ${price}
        Link: {link}"""

        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = os.getenv("EMAIL_USER")
        msg['To'] = os.getenv("EMAIL_USER")
        msg['Subject'] = subject

        with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), 587) as connection:
            connection.starttls()
            connection.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))
            connection.sendmail(
                from_addr=os.getenv("EMAIL_USER"),
                to_addrs=os.getenv("EMAIL_USER"),
                msg=msg.as_string()
            )
        print("✅ E-mail enviado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    current_price = get_price()
    
    if current_price and current_price < 100:
        send_email(current_price, "https://www.amazon.com/dp/B075CYMYK6")
    elif current_price:
        print(f"Preço atual: ${current_price} (acima do limite)")
    else:
        print("Não foi possível obter o preço")