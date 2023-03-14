import requests
import json

def get_ids(src, category_id, offset = 0):
    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=c4bbe763d70b4622a52fd03b06e56ea2,sentry-sample_rate=0.5',
        '$cookie': '__lhash_=529f82a8549ca23012efbd5f66baf273; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_COOKIE=2500; MVID_CREDIT_AVAILABILITY=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MULTIOFFER=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _gid=GA1.2.983784629.1678366085; _ym_uid=1678366085446428891; _ym_d=1678366085; _ym_isad=2; partnerSrc=yandex; admitad_uid=; utm_term=; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; tmr_lvid=6d78e2060ad68f1c3f9b1407b94c1b28; tmr_lvidTS=1678366088799; advcake_track_id=4278882c-25af-7556-ed57-3db721b72934; advcake_session_id=9b62d7b6-3b05-51d1-6508-1ccf5ff1a974; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Flazernyi-printer-canon-lbp-2900-30065474%3Freff%3Dyan_tov_dD20_c20602_g206020201_m79%26utm_medium%3Dcpc%26utm_source%3Dyandex%26utm_campaign%3Dcn%3Amg_Regions_DSA_Feed%7Ccid%3A81741487%26utm_term%3D%26utm_content%3Dph%3A3276296%7Cre%3A3276296%7Ccid%3A81741487%7Cgid%3A5104492492%7Caid%3A13258961460%7Cadp%3Ano%7Cpos%3Aother1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A11285%7C%25D0%259B%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA-%25D0%259A%25D1%2583%25D0%25B7%25D0%25BD%25D0%25B5%25D1%2586%25D0%25BA%25D0%25B8%25D0%25B9%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs4MTc0MTQ4NzsxMzI1ODk2MTQ2MDt5YW5kZXgucnU6Z3VhcmFudGVl%26yclid%3D4207773662517657599; advcake_utm_partner=cn%3Amg_Regions_DSA_Feed%7Ccid%3A81741487; advcake_utm_webmaster=ph%3A3276296%7Cre%3A3276296%7Ccid%3A81741487%7Cgid%3A5104492492%7Caid%3A13258961460%7Cadp%3Ano%7Cpos%3Aother1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A11285%7C%25D0%259B%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA-%25D0%259A%25D1%2583%25D0%25B7%25D0%25BD%25D0%25B5%25D1%2586%25D0%25BA%25D0%25B8%25D0%25B9; advcake_click_id=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=8c5e3bfa-545d-4747-a0b9-a7591dd0dfd5; uxs_uid=a4e00090-be78-11ed-a227-45019dff26a7; flocktory-uuid=d777e599-eca1-4b20-a044-3d1ce7b3fcbb-6; adrdel=1; adrcid=Aif_ZOfJekZJzOSEr3yFjIA; afUserId=56211f06-c003-48b0-96f5-379630196453-p; AF_SYNC=1678366090006; cookie_ip_add=188.44.99.184; flacktory=no; BIGipServeratg-ps-prod_tcp80=1929698314.20480.0000; bIPs=2118529862; _sp_ses.d61c=*; MVID_GUEST_ID=22364990686; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=false; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; HINTS_FIO_COOKIE_NAME=2; searchType2=2; COMPARISON_INDICATOR=false; CACHE_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1929698314.20480.0000; SMSError=; authError=; __hash_=fccaa43959e917ca8aa2f6a0b52e8f7f; JSESSIONID=TtTqkJlJT18J7sMJ8byj1yVj54LsqQvpDLsnD4JPVrLBCfMtnvVb\\u00212003107617; MVID_ENVCLOUD=prod1; mindboxDeviceUUID=42142264-0aea-4b56-9772-6ba6139d89a6; directCrm-session=%7B%22deviceGuid%22%3A%2242142264-0aea-4b56-9772-6ba6139d89a6%22%7D; _dc_gtm_UA-1873769-1=1; _sp_id.d61c=4b45d5fa-0463-446e-95b1-4e8105af8232.1678366085.2.1678370286.1678366099.b87d013d-a6f9-4c72-9f0d-4ca8700be612.fb482c6f-c4df-4bef-a5c8-67d1ac270257.7bfefd93-1069-445e-9a87-7ebe0731cb9f.1678369252410.42; _ga=GA1.2.1952391252.1678366085; _dc_gtm_UA-1873769-37=1; tmr_detect=0%7C1678370291502; _ga_CFMZTSS5FM=GS1.1.1678369254.2.1.1678370310.0.0.0; _ga_BNX5WPP3YK=GS1.1.1678369254.2.1.1678370310.35.0.0',
        'referer': src,
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'c4bbe763d70b4622a52fd03b06e56ea2-bb222d21b1f46a12-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.4.778 Yowser/2.5 Safari/537.36',
        'x-set-application-id': 'e10f7264-3ca2-4030-bf22-6b7ba4d30d21',
    }

    params = (
        ('categoryId', category_id),
        ('offset', offset),
        ('limit', '24'),
        ('filterParams', 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ=='),
        ('doTranslit', 'true'),
    )

    cookies = {
        '__lhash_': '529f82a8549ca23012efbd5f66baf273',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_COOKIE': '2500',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MCLICK_NEW': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MULTIOFFER': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5'
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', headers=headers, params=params, cookies=cookies).json()
    return response["body"]["products"]

def get_data(products_ids):
    cookies = {
        '__lhash_': '529f82a8549ca23012efbd5f66baf273',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_COOKIE': '2500',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MCLICK_NEW': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MULTIOFFER': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_gid': 'GA1.2.983784629.1678366085',
        '_ym_uid': '1678366085446428891',
        '_ym_d': '1678366085',
        '_ym_isad': '2',
        'partnerSrc': 'yandex',
        'admitad_uid': '',
        'utm_term': '',
        '__SourceTracker': 'yandex__cpc',
        'admitad_deduplication_cookie': 'yandex__cpc',
        '__cpatrack': 'yandex_cpc',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'tmr_lvid': '6d78e2060ad68f1c3f9b1407b94c1b28',
        'tmr_lvidTS': '1678366088799',
        'advcake_track_id': '4278882c-25af-7556-ed57-3db721b72934',
        'advcake_session_id': '9b62d7b6-3b05-51d1-6508-1ccf5ff1a974',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Flazernyi-printer-canon-lbp-2900-30065474%3Freff%3Dyan_tov_dD20_c20602_g206020201_m79%26utm_medium%3Dcpc%26utm_source%3Dyandex%26utm_campaign%3Dcn%3Amg_Regions_DSA_Feed%7Ccid%3A81741487%26utm_term%3D%26utm_content%3Dph%3A3276296%7Cre%3A3276296%7Ccid%3A81741487%7Cgid%3A5104492492%7Caid%3A13258961460%7Cadp%3Ano%7Cpos%3Aother1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A11285%7C%25D0%259B%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA-%25D0%259A%25D1%2583%25D0%25B7%25D0%25BD%25D0%25B5%25D1%2586%25D0%25BA%25D0%25B8%25D0%25B9%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs4MTc0MTQ4NzsxMzI1ODk2MTQ2MDt5YW5kZXgucnU6Z3VhcmFudGVl%26yclid%3D4207773662517657599',
        'advcake_utm_partner': 'cn%3Amg_Regions_DSA_Feed%7Ccid%3A81741487',
        'advcake_utm_webmaster': 'ph%3A3276296%7Cre%3A3276296%7Ccid%3A81741487%7Cgid%3A5104492492%7Caid%3A13258961460%7Cadp%3Ano%7Cpos%3Aother1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A11285%7C%25D0%259B%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA-%25D0%259A%25D1%2583%25D0%25B7%25D0%25BD%25D0%25B5%25D1%2586%25D0%25BA%25D0%25B8%25D0%25B9',
        'advcake_click_id': '',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '8c5e3bfa-545d-4747-a0b9-a7591dd0dfd5',
        'uxs_uid': 'a4e00090-be78-11ed-a227-45019dff26a7',
        'flocktory-uuid': 'd777e599-eca1-4b20-a044-3d1ce7b3fcbb-6',
        'adrdel': '1',
        'adrcid': 'Aif_ZOfJekZJzOSEr3yFjIA',
        'afUserId': '56211f06-c003-48b0-96f5-379630196453-p',
        'AF_SYNC': '1678366090006',
        'cookie_ip_add': '188.44.99.184',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1929698314.20480.0000',
        'bIPs': '2118529862',
        'MVID_GUEST_ID': '22364990686',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'HINTS_FIO_COOKIE_NAME': '2',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'CACHE_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '1929698314.20480.0000',
        'SMSError': '',
        'authError': '',
        'JSESSIONID': 'TtTqkJlJT18J7sMJ8byj1yVj54LsqQvpDLsnD4JPVrLBCfMtnvVb!2003107617',
        '__hash_': 'e0fa6dc78c4b8476689d30a7939bd68f',
        '_sp_ses.d61c': '*',
        '_ga': 'GA1.2.1952391252.1678366085',
        '_sp_id.d61c': '4b45d5fa-0463-446e-95b1-4e8105af8232.1678366085.3.1678374184.1678370314.5822e9a6-1ee4-4a7d-bd9b-7f7e81e4dc9b.b87d013d-a6f9-4c72-9f0d-4ca8700be612.f4081809-9cc8-4c11-90c7-e6962f244e1c.1678374128883.83',
        'tmr_detect': '0%7C1678374186208',
        '_ga_CFMZTSS5FM': 'GS1.1.1678374129.3.1.1678374221.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1678374129.3.1.1678374222.60.0.0',
        'MVID_ENVCLOUD': 'prod1',
        'mindboxDeviceUUID': '42142264-0aea-4b56-9772-6ba6139d89a6',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2242142264-0aea-4b56-9772-6ba6139d89a6%22%7D',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '__lhash_=529f82a8549ca23012efbd5f66baf273; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_COOKIE=2500; MVID_CREDIT_AVAILABILITY=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MULTIOFFER=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _gid=GA1.2.983784629.1678366085; _ym_uid=1678366085446428891; _ym_d=1678366085; _ym_isad=2; partnerSrc=yandex; admitad_uid=; utm_term=; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; tmr_lvid=6d78e2060ad68f1c3f9b1407b94c1b28; tmr_lvidTS=1678366088799; advcake_track_id=4278882c-25af-7556-ed57-3db721b72934; advcake_session_id=9b62d7b6-3b05-51d1-6508-1ccf5ff1a974; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Flazernyi-printer-canon-lbp-2900-30065474%3Freff%3Dyan_tov_dD20_c20602_g206020201_m79%26utm_medium%3Dcpc%26utm_source%3Dyandex%26utm_campaign%3Dcn%3Amg_Regions_DSA_Feed%7Ccid%3A81741487%26utm_term%3D%26utm_content%3Dph%3A3276296%7Cre%3A3276296%7Ccid%3A81741487%7Cgid%3A5104492492%7Caid%3A13258961460%7Cadp%3Ano%7Cpos%3Aother1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A11285%7C%25D0%259B%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA-%25D0%259A%25D1%2583%25D0%25B7%25D0%25BD%25D0%25B5%25D1%2586%25D0%25BA%25D0%25B8%25D0%25B9%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs4MTc0MTQ4NzsxMzI1ODk2MTQ2MDt5YW5kZXgucnU6Z3VhcmFudGVl%26yclid%3D4207773662517657599; advcake_utm_partner=cn%3Amg_Regions_DSA_Feed%7Ccid%3A81741487; advcake_utm_webmaster=ph%3A3276296%7Cre%3A3276296%7Ccid%3A81741487%7Cgid%3A5104492492%7Caid%3A13258961460%7Cadp%3Ano%7Cpos%3Aother1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A11285%7C%25D0%259B%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA-%25D0%259A%25D1%2583%25D0%25B7%25D0%25BD%25D0%25B5%25D1%2586%25D0%25BA%25D0%25B8%25D0%25B9; advcake_click_id=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=8c5e3bfa-545d-4747-a0b9-a7591dd0dfd5; uxs_uid=a4e00090-be78-11ed-a227-45019dff26a7; flocktory-uuid=d777e599-eca1-4b20-a044-3d1ce7b3fcbb-6; adrdel=1; adrcid=Aif_ZOfJekZJzOSEr3yFjIA; afUserId=56211f06-c003-48b0-96f5-379630196453-p; AF_SYNC=1678366090006; cookie_ip_add=188.44.99.184; flacktory=no; BIGipServeratg-ps-prod_tcp80=1929698314.20480.0000; bIPs=2118529862; MVID_GUEST_ID=22364990686; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=false; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; HINTS_FIO_COOKIE_NAME=2; searchType2=2; COMPARISON_INDICATOR=false; CACHE_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1929698314.20480.0000; SMSError=; authError=; JSESSIONID=TtTqkJlJT18J7sMJ8byj1yVj54LsqQvpDLsnD4JPVrLBCfMtnvVb!2003107617; __hash_=e0fa6dc78c4b8476689d30a7939bd68f; _sp_ses.d61c=*; _ga=GA1.2.1952391252.1678366085; _sp_id.d61c=4b45d5fa-0463-446e-95b1-4e8105af8232.1678366085.3.1678374184.1678370314.5822e9a6-1ee4-4a7d-bd9b-7f7e81e4dc9b.b87d013d-a6f9-4c72-9f0d-4ca8700be612.f4081809-9cc8-4c11-90c7-e6962f244e1c.1678374128883.83; tmr_detect=0%7C1678374186208; _ga_CFMZTSS5FM=GS1.1.1678374129.3.1.1678374221.0.0.0; _ga_BNX5WPP3YK=GS1.1.1678374129.3.1.1678374222.60.0.0; MVID_ENVCLOUD=prod1; mindboxDeviceUUID=42142264-0aea-4b56-9772-6ba6139d89a6; directCrm-session=%7B%22deviceGuid%22%3A%2242142264-0aea-4b56-9772-6ba6139d89a6%22%7D',
        'origin': 'https://www.mvideo.ru',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.4.778 Yowser/2.5 Safari/537.36',
        'x-set-application-id': 'a9d503ae-45e4-4a73-abfa-cc9ecbe45f12',
    }

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': True,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
    return response["body"]["products"]

def main():
    count = 0
    result = {}
    for i in range(790//24):
        ids = get_ids('https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118', '118', i)
        products_data = get_data(ids)

        for p_data in products_data:
            result_one = {}
            
            params = ["name", "rating", "brandName"]
            
            # save data from keys in params array

            for param in params:
                result_one[param] = p_data[param]

            # save properties
            properties = {}

            for p in p_data["propertiesPortion"]:
                properties[p["name"]] = p["value"]

            result_one["properties"] = properties

            result[count] = result_one
            count += 1
            
            if count % 10 == 0:
                print("Обработано:", count)

    with open("data/products.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent = 4, ensure_ascii=False)
        file.close()
    
if __name__ == "__main__":
    main()