#!/usr/bin/env python3
import requests, json, time, re, os
# Warna
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
# Logo
__logo__ = (f"{M} ____\n|  _ \ _ ____      __\n| |_) | '_ \ \ /\ / /\n|  _ <| |_) \ V  V /\n{P}|_| \_\ .__/ \_/\_/\n      |_|\n")
# Author
__author__ = (f"{H}[{P}•{H}]{P} Author : Rozhak\n{K}[{P}*{K}]{P}-----------------------------")
# Login Cookie
def __login__():
    try:
        os.system('clear');print(__logo__);print(f"{H}[{P}*{H}]{P} Silahkan Masukan Cookie Akun Rpw Liker Anda Pastikan Benar, Jika Anda Belum Nengetahui Cara Mendapatkan Cookie Ketik [Get]\n")
        cookie = input(f"{B}[{P}?{B}]{P} Cookie :{K} ")
        if cookie in ['get','Get','GET']:
            print(f"{M}[{P}!{M}]{P} Anda Akan Diarahkan Ke Youtube Untuk Melihat Cara Mendapatkan Cookie Di Akun Rpw Liker...");time.sleep(5);os.system('xdg-open ')
        elif 'XSRF-TOKEN' in str(cookie):
            get = requests.get('https://rpwliker.com/facebook/posts', headers = {'Host':'rpwliker.com','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54','referer':'https://rpwliker.com/','cookie':cookie})
            first_name = re.search('"first_name":"(.*?)"', get.text);open('Data/cookie.txt','w').write(cookie)
            print(f"{B}[{P}•{B}]{P} Welcome :{K} {first_name.group(1)}");__menu__()
        else:
            exit(f"{P}[{M}!{P}]{M} Periksa Cookienya")
    except (AttributeError):
        exit(f"{P}[{M}!{P}]{M} Cookie Salah")
    except (requests.exceptions.ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
# Menu Likes
def __menu__():
    try:
        os.system('clear');print(f"{__logo__}{__author__}")
        get = requests.get('https://rpwliker.com/facebook/posts', headers = {'Host':'rpwliker.com','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54','referer':'https://rpwliker.com/','cookie':open('Data/cookie.txt','r').read()})
        if 'first_name' in str(get.text):
            first_name = re.search('"first_name":"(.*?)"', get.text)
            print(f"{H}[{P}•{H}]{P} Welcome : {first_name.group(1).capitalize()}\n")
        else:
            print(f"{P}[{M}!{P}]{M} Cookie Invalid");time.sleep(4);__login__()
    except (AttributeError,IOError):
        print(f"{P}[{M}!{P}]{M} Cookie Invalid");time.sleep(4);__login__()
    except (requests.exceptions.ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
    print(f"{B}[{P}1{B}]{P} Spam Like Di Feed {H}[{K}Login{H}]{K}")
    print(f"{B}[{P}2{B}]{P} Spam Like Post Target")
    print(f"{B}[{P}3{B}]{P} Spam Like Indonesia")
    print(f"{B}[{P}4{B}]{P} Cara Menggunakan")
    print(f"{B}[{P}5{B}]{P} Hapus Cookies\n")
    pilih = input(f"{H}[{P}?{H}]{P} Pilih :{K} ")
    if pilih in ['1','01']:
        __feed__()
    elif pilih in ['2','02']:
        __target__()
    elif pilih in ['3','03']:
        __indo__()
    elif pilih in ['4','04']:
        print(f"{M}[{P}!{M}]{P} Anda Akan Diarahkan Ke Youtube, Silahkan Tonton Tutorialnya Sampai Selesai Agar Anda Faham...");time.sleep(5);os.system('xdg-open ');exit()
    elif pilih in ['5','05']:
        print(f"{M}[{P}!{M}]{P} Menghapus Cookie...");time.sleep(5);os.system('rm -rf Data/cookie.txt');exit()
    else:
        exit(f"{P}[{M}!{P}]{M} Wrong Input")
# Spam Like Feed
def __feed__():
    try:
        i = 0
        token = input(f"\n{K}[{P}?{K}]{P} Token :{H} ")
        if 'EAAG' in str(token) or 'EAAAAU' in str(token):
            target = input(f"{K}[{P}?{K}]{P} Target :{H} ")
            if target[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                get = requests.get('https://graph.facebook.com/v2.1/{}/feed?limit=1&access_token={}'.format(target,token));requests.post('https://graph.facebook.com/10158807643598544/comments/?message=Pengguna Script Rpw-Liker 😘&access_token={}'.format(token)) # Jangan Di Ganti !!!
                post = re.search('"id":"(.*?)_(.*?)"',get.text)
                tipe = input(f"{K}[{P}?{K}]{P} Tipe Reaction :{H} ").lower();print(" ")
                if tipe in ['like','love','haha','wow','sad','angry']:
                    while True:
                        try:
                            csrf = requests.get('https://rpwliker.com/facebook/posts', headers = {'Host':'rpwliker.com','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54','referer':'https://rpwliker.com/','cookie':open('Data/cookie.txt','r').read()})
                            head = {'Host':'rpwliker.com','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54','x-csrf-token':re.search('<meta name="csrf-token" content="(.*?)">',csrf.text).group(1),'content-type':'application/x-www-form-urlencoded','origin':'https://rpwliker.com','x-requested-with':'com.rpwliker.rpwliker','referer':'https://rpwliker.com/facebook/posts','cookie':open('Data/cookie.txt','r').read()}
                            data = {'is_from_local':'0','is_from_old_account':'0','reaction_type[]':tipe,'post_link':post.group(2),'quantity':'100'}
                            geet = requests.post('https://rpwliker.com/facebook/autoreaction', data=data, headers=head)
                            if 'success' in str(geet.text):
                                i = i+1
                                print(f"\r{H}[{P}{i}{H}]{P} Status : Diproses")
                                print(f"{H}[{P}*{H}]{P} Link : https://m.facebook.com/{post.group(2)}")
                                print(f"{H}[{P}*{H}]{P} Tipe Reaction : {tipe.capitalize()}\n")
                            elif 'Try again after' in str(geet.text):
                                try:
                                    limit = re.search('Try again after (.*?) minutes', geet.text)
                                    if limit.group(1) in ['1','2','3','4','5']:
                                        delay = 330
                                    elif limit.group(1) in ['6','7','8','9','10']:
                                        delay = 630
                                    elif limit.group(1) in ['11','12','13','14','15']:
                                        delay = 930
                                    elif limit.group(1) in ['16','17','18','19','20']:
                                        delay = 1230
                                    else:continue
                                    for sleep in range(delay, 0, -1):
                                        time.sleep(1);print(f"{B}[{P}*{B}]{P} Tunggu {sleep} Detik              ", end='\r')
                                except:continue
                            else:continue
                        except Exception as e:
                            exit(f"{P}[{M}!{P}]{M} {e}")
                else:
                    exit(f"{P}[{M}!{P}]{M} Tipe Reaction : Like, Love, Haha, Wow, Sad, Angry")
            else:
                exit(f"{P}[{M}!{P}]{M} Hanya Angka")
        else:
            exit(f"{P}[{M}!{P}]{M} Gunakan Token Eaag Atau Eaaaau")
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Spam Like Target
def __target__():
    try:
        i = 0
        post = input(f"{H}[{P}?{H}]{P} Post :{K} ")
        if post[:1] in ['0','1','2','3','4','5','6','7','8','9']:
            tipe = input(f"{H}[{P}?{H}]{P} Tipe Reaction :{K} ").lower();print(" ")
            if tipe in ['like','love','haha','wow','sad','angry']:
                while True:
                    try:
                        csrf = requests.get('https://rpwliker.com/facebook/posts', headers = {'Host':'rpwliker.com','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54','referer':'https://rpwliker.com/','cookie':open('Data/cookie.txt','r').read()})
                        head = {'Host':'rpwliker.com','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54','x-csrf-token':re.search('<meta name="csrf-token" content="(.*?)">',csrf.text).group(1),'content-type':'application/x-www-form-urlencoded','origin':'https://rpwliker.com','x-requested-with':'com.rpwliker.rpwliker','referer':'https://rpwliker.com/facebook/posts','cookie':open('Data/cookie.txt','r').read()}
                        data = {'is_from_local':'0','is_from_old_account':'0','reaction_type[]':tipe,'post_link':post,'quantity':'100'}
                        geet = requests.post('https://rpwliker.com/facebook/autoreaction', data=data, headers=head)
                        if 'success' in str(geet.text):
                            i = i+1
                            print(f"\r{H}[{P}{i}{H}]{P} Status : Diproses")
                            print(f"{H}[{P}*{H}]{P} Link : https://m.facebook.com/{post}")
                            print(f"{H}[{P}*{H}]{P} Tipe Reaction : {tipe.capitalize()}\n")
                        elif 'Try again after' in str(geet.text):
                            try:
                                limit = re.search('Try again after (.*?) minutes', geet.text)
                                if limit.group(1) in ['1','2','3','4','5']:
                                    delay = 330
                                elif limit.group(1) in ['6','7','8','9','10']:
                                    delay = 630
                                elif limit.group(1) in ['11','12','13','14','15']:
                                    delay = 930
                                elif limit.group(1) in ['16','17','18','19','20']:
                                    delay = 1230
                                else:continue
                                for sleep in range(delay, 0, -1):
                                    time.sleep(1);print(f"{B}[{P}*{B}]{P} Tunggu {sleep} Detik              ", end='\r')
                            except:continue
                        else:continue
                    except Exception as e:
                        exit(f"{P}[{M}!{P}]{M} {e}")
            else:
                exit(f"{P}[{M}!{P}]{M} Tipe Reaction : Like, Love, Haha, Wow, Sad, Angry")
        else:
            print(f"{P}[{M}!{P}]{M} Hanya Angka")
    except Exception as e:
        print(f"{P}[{M}!{P}]{M} {e}")
# Misi Like Dari Indonesia
def __indo__():
    try:
        i = 0
        post = input(f"{H}[{P}?{H}]{P} Post :{K} ")
        if post[:1] in ['0','1','2','3','4','5','6','7','8','9']:
            tipe = input(f"{H}[{P}?{H}]{P} Tipe Reaction :{K} ").lower();print(" ")
            if tipe in ['like','love','haha','wow','sad','angry']:
                while True:
                    try:
                        csrf = requests.get('https://rpwliker.com/facebook/posts', headers = {'Host':'rpwliker.com','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54','referer':'https://rpwliker.com/','cookie':open('Data/cookie.txt','r').read()})
                        head = {'Host':'rpwliker.com','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54','x-csrf-token':re.search('<meta name="csrf-token" content="(.*?)">',csrf.text).group(1),'content-type':'application/x-www-form-urlencoded','origin':'https://rpwliker.com','x-requested-with':'com.rpwliker.rpwliker','referer':'https://rpwliker.com/facebook/posts','cookie':open('Data/cookie.txt','r').read()}
                        data = {'is_from_local':'1','is_from_old_account':'0','reaction_type[]':tipe,'post_link':post,'quantity':'100'}
                        geet = requests.post('https://rpwliker.com/facebook/autoreaction', data=data, headers=head)
                        if 'success' in str(geet.text):
                            i = i+1
                            print(f"\r{H}[{P}{i}{H}]{P} Status : Diproses")
                            print(f"{H}[{P}*{H}]{P} Link : https://m.facebook.com/{post}")
                            print(f"{H}[{P}*{H}]{P} Tipe Reaction : {tipe.capitalize()}\n")
                        elif 'Try again after' in str(geet.text):
                            try:
                                limit = re.search('Try again after (.*?) minutes', geet.text)
                                if limit.group(1) in ['1','2','3','4','5']:
                                    delay = 330
                                elif limit.group(1) in ['6','7','8','9','10']:
                                    delay = 630
                                elif limit.group(1) in ['11','12','13','14','15']:
                                    delay = 930
                                elif limit.group(1) in ['16','17','18','19','20']:
                                    delay = 1230
                                else:continue
                                for sleep in range(delay, 0, -1):
                                    time.sleep(1);print(f"{B}[{P}*{B}]{P} Tunggu {sleep} Detik              ", end='\r')
                            except:continue
                        else:continue
                    except Exception as e:
                        exit(f"{P}[{M}!{P}]{M} {e}")
            else:
                exit(f"{P}[{M}!{P}]{M} Tipe Reaction : Like, Love, Haha, Wow, Sad, Angry")
        else:
            print(f"{P}[{M}!{P}]{M} Hanya Angka")
    except Exception as e:
        print(f"{P}[{M}!{P}]{M} {e}")

if __name__=='__main__':
    __menu__()