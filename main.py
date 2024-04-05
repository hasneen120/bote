import requests,random

n='qwertyuioplkjhgfdsazxcvbnm1234567890_.zxcvbnmasertuiowm'
o = 0
while True:
	user = str(''.join(random.choice(n) for i in range(4)))
	
	url = 'https://z-p42.i.instagram.com/api/v1/users/check_username/'

	he = {
'X-Pigeon-Session-Id':'6879903a-c04c-48c7-b1de-4736ff9b8a58',
'X-Pigeon-Rawclienttime':'1712282630.407',
'X-IG-Connection-Speed':'-1kbps',
'X-IG-Bandwidth-Speed-KBPS':'-1.000',
'X-IG-Bandwidth-TotalBytes-B':'0',
'X-IG-Bandwidth-TotalTime-MS':'0',
'X-IG-VP9-Capable':'false',
'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
'X-IG-Connection-Type':'MOBILE(LTE)',
'X-IG-Capabilities':'3brTvw==',
'X-IG-App-ID':'567067343352427',
'User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 480dpi; 1080x2137; HUAWEI/HONOR; JSN-L22; HWJSN-H; kirin710; ar_AE; 161478664)',
'Accept-Language':'ar-AE, en-US',
'Cookie':'ig_direct_region_hint=ODN,57210829745,1743818616:01f71599dc79962f844536b8db267327f36a25a1d4b9261fc67ab518897ed1cf4ca822b2; ds_user_id=57210829745; mid=Zg9b2gABAAGHXqrQ8DY_9qy3NKD0; shbts=1712282629,57210829745,1743818629:01f7eb29a23bfb43c4e64b871f7219673c9cd07fd8ff608c58c2f858a7bf127d750983c5; sessionid=57210829745%3A1MfF1WRwPnE76i%3A17%3AAYdKaR1JwjZbsJqPz_zGahF74zBszobcJpI9sCPGvw; csrftoken=vXi5GufwKKZ9yBtUVD55BN4Iv7TBiYcs; shbid=1361,57210829745,1743818629:01f71471049dda9df8e68e793208a3bb1c472a2dfe586378e1e46fd39c61eb491eeef191; rur=LDC,57210829745,1743818629:01f70861b706c4b2b6bd1c07ad4cee4dc356d20dbab195d9365a6602adeae2c71082b7ee',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Accept-Encoding':'gzip, deflate',
'Host':'z-p42.i.instagram.com',
'X-FB-HTTP-Engine':'Liger',
'Connection':'keep-alive',
'Content-Length':'287',
}

	data = {"_csrftoken":"vXi5GufwKKZ9yBtUVD55BN4Iv7TBiYcs","username":user,"_uid":"57210829745","_uuid":"953cbaf2-e663-4126-bede-3e41ac2c502d"}

	rr = requests.post(url,headers=he,data=data).text
	print(rr)
	print('*'*40)
	o+=1
	print(f'The {o}')
	print('*'*40)
