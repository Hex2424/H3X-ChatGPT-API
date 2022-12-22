
from collections import OrderedDict
import uuid

OPENAI_HOST = "chat.openai.com"

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"

SESSION_API = "https://{host}/api/auth/session".format(host=OPENAI_HOST)
MESSAGE_API = "https://{host}/backend-api/conversation".format(host=OPENAI_HOST)


def generateSessionHeadersPayload(clearance, session):
    headers = OrderedDict()

    headers["Host"] = OPENAI_HOST
    headers["User-Agent"] = USER_AGENT
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Referer"] = "https://{host}/chat".format(host=OPENAI_HOST)
    headers["Alt-Used"] = OPENAI_HOST
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = \
    "_ga=GA1.2.276779431.1670925280; \
    cf_clearance={clearance}; \
    intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; \
    intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; \
    __Secure-next-auth.session-token={session_token}; \
    __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; \
    _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; \
    _gid=GA1.2.1218786756.1671659418; \
    __cf_bm=fBOVua8ukB_lHb80mIGKmK0Cb9fW_VAVs9NwnFsFo.A-1671729164-0-AYzWjSoc9BflupwBw58hGnPgiAbwrj3P95o+eRWJczU5uWQC56ZJmOaKSs6jXG9oXtXvgOfQ/tz0lKTYdpt15kW5SZIF74APQsRx7WYtYRAvc7k4Sdzo8mPUtqZ1CtOcyOOGETgnLhRpHY9tj93eddSvYgqYl7171nYv31ooSFXWYO868lGeRfEDTAxxSQGTow==" \
    .format(clearance=clearance, session_token = session)

    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-origin"
    headers["If-None-Match"] = "W/\"13kj022q4ni16m\""
    headers["TE"] = "trailers"

    return headers

def generateConvoHeadersPayload():

    pass

def generateConvoBodyPayload():

    pass

def generateMessageHeadersPayload(bearer, clearance, session):
    headers = OrderedDict()

    headers["Host"] = OPENAI_HOST
    headers["User-Agent"] = USER_AGENT
    headers["Accept"] = "text/event-stream"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Referer"] = "https://{host}/chat".format(host=OPENAI_HOST)
    headers["Content-Type"] = "application/json"
    headers["X-OpenAI-Assistant-App-Id"] = ""
    headers["Authorization"] = "Bearer {bearer}".format(bearer=bearer)
    # headers["Content-Length"] = "233"
    headers["Origin"] = "https://chat.openai.com"
    headers["Alt-Used"] = OPENAI_HOST
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = "ga=GA1.2.276779431.1670925280; \
    cf_clearance={clearance}; \
    intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; \
    intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; \
    __Secure-next-auth.session-token={session_token}; \
    __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; \
    __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; \
    _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; \
    _gid=GA1.2.1218786756.1671659418; \
    __cf_bm=if03zIJqaBVFWS9hPSdCZIJol7skKQsivY2qds7oY1g-1671727780-0-AS0IMKd6Pi/pQfOXNtNz7BMpOW7TMpKZKe17EBfas4CLIUjXr9hlsRZTzSwMgC0QS/DjENNfNUM+JK+R3TryDKjlQVsbf5uemi+/gdviNLqJCUy24XG6YiGxR0l17EkxQLyDwmiuQdr5zQN2m/ZK4PmjIa0pvXUckxioEQkg9bk6K2W+YEzqdXqab4wDAOIjxA==XX".format(clearance=clearance, session_token=session)
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-origin"
    headers["TE"] = "trailers"

    return headers

def generateMessageBodyPayload(message):
    return {
        "action":"next",
        "messages":[{
            "id":str(uuid.uuid4()),
            "role":"user","content":{
                "content_type":"text",
                "parts":[message]}}],

        "parent_message_id": str(uuid.uuid4()),
        "model":"text-davinci-002-render"}

# GET /api/auth/session HTTP/3
# Host: chat.openai.com
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
# Accept: */*
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate, br
# Referer: https://chat.openai.com/chat
# Alt-Used: chat.openai.com
# Connection: keep-alive
# Cookie: _ga=GA1.2.276779431.1670925280; cf_clearance=ChQ7Td.NxJlvhIv.3t.QRsO2zXwjy4EOg5kgQhOqYBo-1671727779-0-1-ea1b3719.7f8f7cfc.570e39dd-160; intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..hianWNk1SBPjr1q5.dzs-9zhFqchfNBDTunb8nhLMRS30WOxLxYQenlv6JAxQkejd8kMpdqJymvzl1ZiIBA3JA5QCBbmoWLRDqassYuxHbH2RGKRqiH8Vv7cjnkEd8mbN7uxLfuQoT9L6R0ZkDq9sZs8RWens4zEVjPEKjsceYPLtaN6QWHQrwdvGyEM9bL_Kk3mrQOwNLbQj7qO5LU4yXdsFBbpRSmeNuLaV9qeh73fwQNMrJy3Hit_9Kp6Y6dLNgGry2YWulX4CCpuIAFqTOd8edb_2obXtKyi4vniSPd7EHh3f6i9gTaabMbz7YNKqnEOt8slkrtD3ctt05MnH1li2TGaYWTRUBn68kHqBOrCodgwn5NnsZGcfiPUcCbOpta4ggnq3N9zlgmbuOrmVE3m_Si5JlQMHzI9eX6LyvMadzUbGMpT3r6P9vKXhFQAO9SHgaZZ8ILvwdmbhvuR4UxufwY0nrKsXcgLXVFfvV1fVVUSdY3XeGq2PpTHz5eoCd_TvwoIsOFXaJtABl1wOYEUkWNqnEJZ8B7Q7Y2L3VyXsu3iKsh0YrcVaDQozdZNhLK3pz1MAuIK029jH0ER26d-0KZeay73EOfqqgW1FBWwy6s8nSQZ_s6vwPT31k79PYam1fdatnanMiVqDO1GWOXQVGyNmLnl4Veo7DxFJzApgvY4NBj0j9R_LYETEDKDHzu0FEmbNhkebFUTrnlC-Hs3-KQro60_489NOK_wGEdfSibruhdaJq8hEu-YGZO_u4vFgyVYR3BOe-dTh7uBKDmTstM79NgOsYbPRnd9ORELD7xcGxoAxofaBdXT04B6recCD7AQq8tPsVAS3Q2lZfvPJA-pzFijD-tIMsXMAieTBztB_GlKDk97RunjD61DL6QH6gMXvn3XkFEhizXgmd-mShb3BgWyxieWGcf0pSAw1xDT69Qba1G0BWzQetGnTKpx6xrD2G_Ch1XkFir0s52o9DXCI6PQpg-uuRM0I_O8WQivEHGaW7tD0ybibLJrPD1SRpCD2zBV7y7tD2DV1pqQ1AFXGc8Yqg2rWK4XYo4KPM4IiEKQOMwqTIUEejUWMjGFRJVWbpvnlPNbL1TUds6XCHfsivf-aw9aPHaxuVV3istI8Q64r33Ndxk5DIZiwl9Fh_alPmQFGDZer1D_7sn83-mgsLkKIHNxKFSEEpulTnXmoOEDHc1jRAd_KHx0X6-xAogg4u7mw1OrtuY6dRpvrm93qBmsl8cUx6nhilZSTz8SlkxOP3I8XocTzrd03cs1BeA6TdPT6shyxDEgdzeUybCD0b-83o0BXk3foKEHayrUvqrFm-B6K4xGYrvUmg-VKdbn13cKQWcyiHbAdvX_dauiHTR3DTcg8vfUHUOUwPNFPGaUC2MW-msYGJN8vUoqUhZD7s4U58Nimkrets0ree0gKtYzlIEozBk58n8mokCAD8Ar6Wu1s9xR4tZbIluE3_qIp63-qfTMHBMXb18ZiVNm0aBt3tTse-qlnCNNEl7M4NvBfsUTWHNJtnaRqtbJizOY8RKdytHTKb-n8_Q80upYU6NnMKpz2QCTYZ4e41UKdkFrqh10L8S6AU48jXl1xHJ-uaXHCJnn2gVpisk-j6Eg7eyJZHVSd7cXCZ-Bdv9CYErYdyoGnq6c2EobZptaRfsf1oXcYcpl18si8Kk227--L5QZT2vsp1ZyBRU8pRJps2naKmMTo8w2NbXGRPjvKWdrmgLEOtWtoOqWzbWqOREzH1_GSUrCseQxOVTtIRkNOpmoCZ9fOUYi1UFjDnyClewmrgvrqVIwepnvK5jY28tDh6IboNGpSnlxqGhAg3ArytyO_QY8p8hsJvJg10A8-U0-W1wWqOYZAeF9jGXGVvaCc-aor-Hj6OjSe0oO1C-0DQeLAaYo_M9O5JZvHMqut7DnP-L9F_BVfYAxH2pvo3tTmUKZSCHlM4fdACOZvEg35L9CYbbTVIrlvgiNp6WhSexetGk8m_CAG7SFeyFLzKT83qi-gO3psuRNCiH4j5uSnLG_wE30F9ScHkIVcPQsJMfpyoC-b76bN3tNpq7JWOz4MLUuU6SsNAfBqJfHkllrwvvpw4vnmrsIUEJb1-YT1qyEf_BEGKNLTFD3kulozILg6Q4mkLfcySWm7DV3t1-m1Idlj88QKRixgF8HvRbgc3CB9y0cuTjqTDpgb2YnWL-Jv2aIA55oSMHqAcF4NHaN0qKRxZ88u_YnNiD3b7dnzbWwLDhBk4HJ7_iYKMOV7pp-N6QAgsed8gCHuyicwRmOIOJ1P3My9Kgv2rAhCWKCi.bM8Ry5F_UfJEd7wYKFfugg; __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; _gid=GA1.2.1218786756.1671659418; __cf_bm=fBOVua8ukB_lHb80mIGKmK0Cb9fW_VAVs9NwnFsFo.A-1671729164-0-AYzWjSoc9BflupwBw58hGnPgiAbwrj3P95o+eRWJczU5uWQC56ZJmOaKSs6jXG9oXtXvgOfQ/tz0lKTYdpt15kW5SZIF74APQsRx7WYtYRAvc7k4Sdzo8mPUtqZ1CtOcyOOGETgnLhRpHY9tj93eddSvYgqYl7171nYv31ooSFXWYO868lGeRfEDTAxxSQGTow==
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# If-None-Match: W/"13kj022q4ni16m"
# TE: trailers