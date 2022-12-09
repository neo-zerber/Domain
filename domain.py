import whois
import smtplib
from datetime import datetime
from email.mime.text import MIMEText    # for microsoft Outlook
from email.mime.multipart import MIMEMultipart # for microsoft Outlook


def get_domain_expiration_date(domains):
    domains_info = []   # list for add result

    for domain in domains:        
        expiration_date = whois.whois(domain).expiration_date  # grab expiration_date
        data = str(expiration_date)[0:10]   # grab only data
        if isinstance(expiration_date, list): # type checking and action
            days_diff = (expiration_date[0] - datetime.now()).days
        elif isinstance(expiration_date, datetime):
            days_diff = (expiration_date - datetime.now()).days
        elif isinstance(expiration_date, str):
            days_diff = (
                datetime.strptime(expiration_date[:-3], "%Y-%m-%d %H:%M:%S")
                - datetime.now()
            ).days
 
        else:
            print(f"Domain {domain}, wrong expiration_date={expiration_date} type={type(expiration_date)}") # if not domain assign -1
            days_diff = -1
        domains_info.append((domain, days_diff, data)) # add in list
        domains_info.sort(key=lambda x: x[1])  # sort by second value
    result = [(domain, f"{days} left", data) for domain, days, data in domains_info]

    return result

def send_email(message):
    sender = "Yevhen.Nikolskyi@com.ua"
    password = "*******"
    msg = MIMEMultipart()
    body = message1
    msg['From'] = sender
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server = smtplib.SMTP("mail.com", 465)
    server.starttls()

    try: 
        server.login(sender, password)
        server.sendmail(sender, "Yevhen.Nikolskyi@com.ua", f"Subject: Expiration Domains in DAYS!\n{text}")

        return "The massege send"
    except Exception as _ex:
        return f"{_ex}\nCheck your"

def main():
    print(send_email(message=message1))
    

if __name__ == "__main__":
    domains = ["dragon-capital.net", "dragon-capital.org", "dragon-capital.info", "TheDrgn.com", "ureh-pe.com", "ucpih.com", "nupeh.com", "dragon-capital.ua", "dccl.com.cy", "dragon-capital.cy", 
    "dragon-capital.com.ua", "dragon-capital.kiev.ua", "dragon.ua", "drakon.ua", "dcf.com.ua", "dragon-pm.com.ua", "o-r.com.ua", "green-hills.com.ua",
    "green-hills.ua", "new.green-hills.ua", "wgl.com.ua", "ces.org.ua", "premier-pm.com.ua", "prime-bc.com.ua", "eurasia-bc.com.ua",
    "piramida.ua", "nupeh-cz.com", "kmzindustries.ua", "variant-ab.com.ua", "vgardens.com.ua", "skypark.ua", "eco-tower.zp.ua", "horizon-park.com.ua", "aladdin.ua",
    "platinum-bc.com.ua", "victoriagardens.com.ua", "vg-offices.com", "viking-bc.com.ua", "grand-bc.com.ua", "obolon-plaza.com.ua", "pbpark.com.ua", "smartplaza-obolon.com.ua", "green-hills.fitness", "pampik.com.ua", "pampik.com", "pampik.kiev.ua", "e-distribution.com.ua", "parfums.ua", "parf.top", "m10.com.ua",
    "m-10.com.ua", "e-40.com.ua", "e40.com.ua", "borychiv.com.ua", "pravda.ua", "tablo.com.ua", "kievpravda.com.ua", "adnet.com.ua", "tabloid.com.ua", "tabloid.net.ua", "narodnapravda.com.ua", "tabloid.org.ua", "pravda.fm", "pravda.com", "pravda.com.ua",
    "epravda.com.ua", "greenleaf.com.ua", "rau.ua", "truskavetska.com.ua", "truskavetska.com", "ua-ua.org", "dilovyi-bc.com.ua", "obolon-residences.com.ua"]
    domains_info = get_domain_expiration_date(domains)
    message1 = ('\t\n'.join([str(item) for item in domains_info]))
    main()
