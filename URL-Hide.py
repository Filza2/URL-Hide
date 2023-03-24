import random,re,os
from requests import get,post


#Hide The URL for social engineering

def header():
    os.system("cls" if os.name=='nt' else "clear");print('''
██╗   ██╗██████╗ ██╗         ██╗  ██╗██╗██████╗ ███████╗
██║   ██║██╔══██╗██║         ██║  ██║██║██╔══██╗██╔════╝
██║   ██║██████╔╝██║         ███████║██║██║  ██║█████╗  
██║   ██║██╔══██╗██║         ██╔══██║██║██║  ██║██╔══╝  
╚██████╔╝██║  ██║███████╗    ██║  ██║██║██████╔╝███████╗
 ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝                                  
                         
             By @TweakPY - @vv1ck                               
''')


def short(url):
    try:
        r=post('https://is.gd/create.php',headers={'Host': 'is.gd','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded'},data=f'url={url}&shorturl=&opt=0')
        try:short_url=re.findall('''<a id="qrlabel" onclick="load_qrcode('(.*?)'); return false" href="https://chart.apis.google.com/chart?cht=qr&amp;chs=100x100&amp;choe=UTF-8&amp;chld=H|0&amp;chl=(.*?)">Give me this URL as a QR code</a>''',r.text)[0][2]
        except:pass
        if 'https://is.gd/' in r.text:return str(short_url).split('https://')[1]
        else:
            r=post('https://da.gd/',headers={'Host': 'da.gd','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded'},data=f'url={url}&shorturl=')
            try:short_url=re.findall('<a href="(.*?)" style="color: #888; font-family: monospace;">(.*?)</a>',r.text)[0][1]
            except:pass
            if 'https://da.gd/' in r.text:return str(short_url).split('https://')[1]
            else:
                r=get(f'https://tinyurl.com/api-create.php?url={url}')
                if 'https://tinyurl.com/' in r.text:return str(r.text).split('https://')[1]
                else:return 'Error'
    except Exception as e:return 'Error'
    
def url_check(url):
    try:
        url==str(url).strip()
        if url=='':return 0
        elif url==None:return 0
        else:
            if 'https://' in url:return 1
            elif 'http://' in url:return 1
            else:return 0
    except:return 0

def hide_url(website):
    header()
    random_charts=''.join(random.choice('0ab1cd2ef3gh4ij5kl6mn7op8qr9st10uv0wx4yz1AB2C4DE0F05GHI4JKLM0NO4PQ0RSTU4VWXYZ') for _ in range(10))
    url=input("- Enter The URL : ");header()
    link=short(url)
    if int(url_check(url))==0:exit('- Error, url not valid !\n')
    else:
        if link=='Error':exit('- Error !\n')
        else:
            if website in ['youtube','spotify','instagram','facebook']:
                if website in ['youtube','spotify']:sub='video'
                elif website=='instagram':sub='photo'
                elif website=='facebook':sub='profile'
                print(f"- Your URL is : https://www.{website}.com-{sub}-{random_charts}@{link}")
            elif website in ['google','nytimes','github']:
                if website=='github':
                    print(f"- Your URL is : https://{website}.com-{random_charts}@{link}")
                else:
                    print(f"- Your URL is : https://www.{website}.com-{random_charts}@{link}")
            else:
                exit(404)

def Core():
    header()
    website=int(input('''
1 - Google
2 - Youtube
3 - Instagram
4 - Facebook
5 - Spotify
6 - New York Times
7 - Github
\nEnter The Number : '''))
    if website==1:hide_url('google')
    elif website==2:hide_url('youtube')
    elif website==3:hide_url('Instagram')
    elif website==4:hide_url('Facebook')
    elif website==5:hide_url('Spotify')
    elif website==6:hide_url('nytimes')
    elif website==7:hide_url('github')
    else:exit(404)
    
    
Core();print('\n')