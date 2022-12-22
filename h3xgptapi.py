# import discord
# import json
# import requests
# import threading
# import uuid
# import settings as config
# import base64
# from requests_toolbelt.utils import dump
# import collections.abc
# #hyper needs the four following aliases to be done manually.
# collections.Iterable = collections.abc.Iterable
# collections.Mapping = collections.abc.Mapping
# collections.MutableSet = collections.abc.MutableSet
# collections.MutableMapping = collections.abc.MutableMapping
# import os

# import time
# from hyper import HTTP20Connection
# import shlex
# import subprocess
# import json

# def call_curl(curl):
#   args = shlex.split(curl)
#   process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#   stdout, stderr = process.communicate()
#   return json.loads(stdout.decode('utf-8'))


# # proxy = 'http://127.0.0.1:8080'

# # os.environ['http_proxy'] = proxy
# # os.environ['HTTP_PROXY'] = proxy
# # os.environ['https_proxy'] = proxy
# # os.environ['HTTPS_PROXY'] = proxy

# # # proxies = {
# # #   "http": "http://127.0.0.1:8080",
# # #   "https": "http://127.0.0.1:8080"
# # # }


# # # chat = ChatGPT(session_token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Neu5-zPvJyy8hEh0.xx3nu8D6sV1HCJ03feNVhTdiiB-HztyHXkROUweaZAz5WwbI86iTJtUWRr0d37Pp4k3UAGUx-M7ao6Nq3qM-fbTQ9Ze4IPJXoW3WYMzmFUhpRJ7TePZmuSfMb7Q_TC5IEOGcq8llrD-yYIXABrEztLfqLuaRbpy8LE6rJonf584L0LFhiBpiXvlNXlQVxjUPDaOHAIuCVj2st9xfyiZ97eP7wm-YlIp-LW2IruTNkAZHHiEah-h27uJRnxkETTkJEgIsjGl7VWDk8XHA1BpnLUH0N6wmD54g6GlT8b4c3puU1A3tV13LspOIgQzkLSflGioSyJK6pWGDjCPSevItXQRIO2rCEl0KjmWJv5ZfVBfDSFDukLthLdFtJPm5ShRB9ZyvicMVDVkQdiJCrlgKwR-FxeR_QpSDFpfE-L1JiOedNXTf8GrGgApVkaKXoslKvINeZlAm81zXygw6USJdaQ2YfXAIIpTp8Wya26doBDeJh2BC9mNf-bMrmXc8gecnN-aqhCYMoC1Rm4bDID5As904hMuXzfbWWoOVDmefoLtYdv1unj2peOpNZLs1uNgWigCcIsdyYmolfvSDkna_Z4-ZA6ETB3fSu7MAQMJqfGNvQ3BnagqG8nCuCjpb-Nu03jOnbxlVGF2aG7HEnwFFTUJmvfsRXRPxFl8D-3vuAoqHfCYUqnpxjxRasCHU37qMJUWfVBYFc_yxRK_lxfGf0uZav91tF38V6GqFbLHDiDmnBQNgPEuCzk9etyK274oeZxmm21zuLJYImcQPeZkTKuFnc2lBimSFRpom-21a0Sv5EjmbGsZO13wxTTUQOgo5YplNS3r5X6M8ZK9ZuW9m_lASwp8e6nh5gCpD5z6lTsn8XUd5qZSkoQGE9rvhw7MSmWdLNWebsx3sKPJFPsjj1Sz8VNm7F5babpW1Dm2zh_Lw4tma0_lVASYvymsOk-O7DLduSIQwtUfqRGGnFiP3OVSFilyJ1CwFe8Ez8MzZsaiC9fxiqSxCLh9VY2Z9LWDsvKh9Jo-lggr5dlEgc2h21JikqIBas-nPKI_nYZCRNGc5f5lFLQumqHhg4EBA0pizC1lt9h3O6OUC-kzTAEYznuqWYZAsfw5Dthb3e-Rqgdi5V6lAgG_wf1VNXSsMeAxZFEFQj9fGtBBGLwwpcRtTPQDYMU61aONnweSxJV6TRFpio-UYh6RfTxKVVcX9Ale43MfaLze8cx-MH3mbChDHeMAAaMuq-4mnEpzZazf5hh2-R3lzvlDf4kXVolce6kV8Pqi5-6N09_ZY3TpRljOe2v-cVwWSul54eBF-tkdPd_lur68E8X0VrloZQdUq-2VSAwv7Z68BQv_Si88mGfGa2qXWXw37OxWONr7DYy4e59egm4idC9GmcOHObDgV0GKaE-mSvMULuOfSwGWqLexGs5NdbTdH21OSRyqkrFrvivq-w2huxE13AeVftmEyvcc4nPOJ_3W76rLGFXANf6QnfXKqerM74tZQx8iCYUB3nHP-1GP3CRBPrA36SISkKqRfwnVI0MxPD0KehwsmL8WgJV-9pW4-h0JmH_wL3mTUH5cCki3EzAn_VnCPQYxs3iiCYwB-bUfwDi4NrxaZn6vthQ8V0Dv4VA_DEI4vJ6tEWp8JMMzAHnn6H2dbJOf93N0_-zL0JKPI3oV-LHkPzQMIrG0iK1hxCS3eZ0r-3tNV_2sNsjKLrHheoW9t8ZOrWQA7Fv9KJZf0hhK4O4Zrhb1J1ImmNjZwH6uj7PN-uXiou_zrrYzGuMiqxznVZgV3fFBq5Kaq4quxFpWEoMjigVDyHHjXwtlXhTEJee691DByJDHsBw5H1KHW2zTGL4Pc_AEwLCIKbBHbjuv17Q8Zjr0V1HNp6miarmTXoUbjR4A5huF0nibDWJ1dN-f4U_iiNauzyRsuQNenWDlgdxfItGVz69qRyLxhOneMcUVuzeeBGI-MCgvqqcNzd6U-hQcFcw3aV7IE1FrQRzcb-ACnsXqKe9xZygiut3jJLF2Hc5Ffdj8MJOj75UcVd0I8zO24ZKxIO4gQTwSpTFbop5Z7VZ3gSpeKEEoudNM2BIbnJ5ky4o7e6XROrOh1CsA_FLwSM7EHsbJ9qUwmkMK2KYXEzB0vxg3phm_tlMcqFV-AlaErE8NfD4JjnwWfflPpWCeTPeezf2v-jIPj_sst1jD1qA6v8_06HXbHIcfiQZcWZiLwKINyxKVt3-X35N6AM4W52CoEvpWFyx56TFILtsJir-1AepJXFpRezaXFO_-rGm32VzDxN4vmgIvq.cxe6o0a0B-sR9o0V9wbVcQ")
# # # chat.authenticate()

# # # chat.send_message("hello!")
# # # async def main():
# # #   client = aioquic.QuicConnection(
# # #           quic_logger=aioquic.QuicLogger(),
# # #   )

# # #   # send a GET request to the server
# # #   response = await client.request(b"GET", b"/", headers=[(b":method", b"GET")])

# # #   # print the response status code and body
# # #   print(f"Response status code: {response.status_code}")
# # #   print(f"Response body: {await response.read()}")

# # # main()

# # host_session = "http://chat.openai.com/api/auth/session"
import payloads
import requests
host_message = "https://chat.openai.com/backend-api/conversation"
# # user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"


# # # headers_session = {
# # #   "User-Agent": user_agent
# # # }

# # # client = httpx.Client(http2=True)
# # # client.cookies.set("cf_clearance", "KHYp0LRx6GwQp3ZZbgWznQ2Hl2AVdUXRZlg0Xyb1DH4-1671405154-0-1-ea1b3719.d8540aa0.bd1a68f9-160")
# # # client.cookies.set("__Secure-next-auth.session-token", "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..C2oD6FPeqi6ZSHOc.NaqJBeH_A4W-yz6MhcEtkTH8vDuTdbThWtUwylwwwmu96iTdmaGB04q6ujGp7dQo4-grbFtpYM15bMiQ8J4rAINjk3UG0kyw0P9pnefadsyTNd9exTwCaR_2kV5MKARBbQbaB2-sZBNGsMGclIJzh00Dibjo2lO9OYLCTUkD_PoFYr5mJ-NAKn5EuIan0oUaJg4KRBkrO544LGjSliDxMtNKw7x9D9aLrEW8Bknj5AXA6b06BZL7UIxJaCzJRPSHei1OGsQVPKsQ8-DsTaDdYDhKGy10lQGdNVILRjuClhhSCUea3UGOnK6LUYJxaWvV7U5fdNCfjWarRmmqA_HOZM-YpGdV05C7pNs7cvY8DSShB61NpnRQtM7Li9c9HNSNWC1cOcLLZdAb3G0b2ObQq4NVpPHQEtfxS-jJmB807ECoqZex5K1QASdOZzfuzJJYslBYz-ZvZirKb_K8i3K9_w0r7kP2zEJzyIdzM61feP2LtCh27a2jJ1Z_STKPK3cuTMUSWoMpD2iLpK0GslkMoklmMvN8pQ4NYSUvyx2pFLg-OGnAJanMRvZsyDJV8AWw_6FqQ3OFuxuwF7grxuMCETVX5wRCZ-iGM76-F45Im13UxMDdqsS_AjtYGQi_ZCVQmoJ-AHVXUPmBRoQqhRs5onK83aV4h_Fen191JoCsimlDMiyBx0LmudDNMgNWYkf-GEBUmxLPM5Sk5vBHkjQJAaiZuw7-0I2n-8pcTUFIQJakyEJEinfRuDbW7LXwSakhJEWaIXCYWxN172PMLbNPxb8Odu-m73KNEVAva_cG4_L29jH8GfPFps9vudNHpiIKm22T34fh-99ESsvr7a_zbRJxeHX7V696CP6EDoubG3tU-Qpio3vsOLjYRvMtD0B1MGeD6zY3q-NP63ZuPLc_TKYXcXuQAWATcILTdZE20_-rPn8xlNO8INmq92hTrkLpnGaKurWu3HGNx8bBchaWC9hVM7FdhMHbl1ZKolzHEndqicq7mNyhO5NZIGmOicUYb4WozDTYBlh6SUxJKJCzCwZWGmM1bKNjVQ7WrQ6qRX0Ko36trAnJOLfVolgxNO9tuEqLE59pu3TWjfDC7qLE7cq4CmX7WKGWBylUyU0gw7W-RvrGlsFANCWWr2XqtVZShlTrnNsyp2h0Z93LxotD8wiir_xEQZW0quLfGURR87A-J5q-P_iJKri2AS6cLSD_8Rf5MAqo5jy5VtaVdGwnEBgiXSL2Xv3akfHMSQKnLZ07TuyFl9LDHiPX8r8b6KlXlBJfI-joP57VnKgsbaZvvlB0Ehqor-r1DNoTRcotamRggpSUQ05YZoEwIPEGpgk1xqrOkvi183DhisY2zHoqj5mKem0oEDxgyxpA2Ifb_ltwwK-eTzGpTHsLaWmbfM8ZgYTu5B2H-0DV8xaSCxZKfwUljloHhQ-NucTHXg5EDZxi-00fBFp-RmnTK9ZFvZkFYwwjnlxFaMQUXGD1WjGMRdsSKCfMQC1v_kgEYcRBdsHinFXHPpcbNblRaQPG47pTmvWlFB_jbWVFn7611uOMzgArBNXqaNFHXZTrgxkPqIXqrt9hZRFRngTvLyY6l3AuhuwGHgFhpUUlU7iWcj_1ssvlH553FH8bTRFpKGVbH63vgb_2_-1URdSIAyZcUyBRJggfucT-oc_Xxzi0okfTCZBWHucPXV3I_vyDMPBqVVbMs2PgZ3IaJSRyliO_mgM7Yio-r75lwdgMPPoDa_vCtFD5OPFNyJf6y1M0NU3XqNo1q1XppfYsBUyv0b18bCRKSqwGxfJFnCXkx6MsGLhYeiITk2dHXdvF3GZAY7uiHAfaHiaKmhpz7ij25O9mVdqNOF5lk6hDPQg32UP4SrVbzJ44gWWz3GTzoXauUTNyz_ZQ2Vpy5y7CLI6bqSdSvJOvHytDM7amhxHkh0NQDHQvcp94Mo-qcvCSKREwnj-4S6IEsNEwh1rlgwJqHIOynW3uHsaNkN-o1CJdVJHzxNc25LNCHTFsd7MoCU7OvaFEWR3lOo7stieRPdvB-3UUd9T-TFO3zabhR09xQW29qwihhffhU7tylgqMpmh7wHS1TQxRQUlD3QDKyhKetPYuZKS7N12zbZ-HTg387btp3fZIuBTOF1kD4-PFJ49WmxXmUT9pEaT1Cf8zD4ASmunCUZmPr39_EPmSCmk1afG-ZEF5rcGGRrHIV2wGGKU4Bddo0O1DuMq33NseMfld7KbCuxD9J1mrr65ocfs8jXa10SZI4Qmd2Q7xeXQeRuEguERUlEnGfCjBI9BR.eP_fCTRCedqTNataUH387w")

# # # response = client.get(url=host_session, headers=headers_session)
# # # access_token = response.json()["accessToken"]
# # # print(access_token)
# # # access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MTIyMzkyOSwiZXhwIjoxNjcxODI4NzI5LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ"

# # # headers_message = {
# # #   "Accept": "application/json",
# # #   "Accept-Language" : "en-US,en;q=0.5",
# # #   "Authorization": "Bearer {}".format(access_token),
# # #   "Content-Type": "application/json",
# # #   "Content-Length": "232",
# # #   "User-Agent": user_agent,
# # # }
data_payload = '{"action":"next","messages":[{"id":"c1049229-a54c-4388-b9ff-87eece40a9d0","role":"user","content":{"content_type":"text","parts":["sss"]}}],"parent_message_id":"8b47d50e-7511-4696-9c36-9f6f8c996ac3","model":"text-davinci-002-render"}'
headers_message = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept": "text/event-stream",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MTIyMzkyOSwiZXhwIjoxNjcxODI4NzI5LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.2.276779431.1670925280; cf_clearance=6BP.WNcvx_8u7.AybziVpxpdCaKhA3OGsumcJEEKoo0-1671659424-0-1-ea1b3719.7f8f7cfc.570e39dd-250; intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..p8PKQtDmmOHBepGK.jkcaofFIIDCycWOhebpPOVMKFthaokuiXKvI3d2e_iSfbX7_VmA67alz5EBGTu99jC4he-evcHEuounqHlpdVT1lbKIhJncfL5vPF8Y-G3x4847_GmnIh5yCjLe7JdC-c2nnVrVPBSsvGnEMcoj6kbHqa8Gw34Yn1NpBKXIjhkSFu-M1C9RZSejdAuJym_VLQJgm4fLibElP6sMzQlKArKhs2pwv9dd_aOCD22hFLtbyX5O4PJ2nLZJPpgIAsfaojKDO6m4bvLBMeJF_81hrDUmn5roACbP7x_NyHJ4-pvp8EUelmz8OZnLivIitA2HCX2M0zXkqSMWbjGu4Kraf5uHhPNhDX9e2uU5jRGji8EEAyNHUSRGf5_b2ViZt6NQs4cxD6nXWBxNq5ey_lKOeHfv04SMvq8fBIb2s_78hk70prL84HYKtMKdLKC2tFccN8tNspZfVO9_NeKHLeIhElx2BwmlIofrYaJgNed4WpoTyJXsnLUEXU5Mqli4KgVKnB5-GuM3LMj2HeVGEtH0RKRkRdAH0hwlAHIyv2Uksb2sIOu5nXT77tjaUo6Q6CVJmr2Rd3oVe3XW8WfxFJS4jGR45ccACtruWMm9aOY9B2UZ_UYVmxt2ruJ3UQq6mYQWHV_v53IbpgV2ulChPvBd6X3IEA3sbL6HJpQStp6ylIgJm2RR9pywVfvL3KpzMz8puZRuMCtzG7uCgoEyVe2dMh2n3dtM5P7ynJ4Iwp8Gw1X6ovTnMUMEnAJtioDdM4c4RIvE6Ox6dsOQ0yMTdWmwocXWd-XjcHhiF-KqqQlS92wgpb6WcnZo71uFHNZdgNVQxyuezHciDhE8bX_6VqTjySq1vBbnARURIKA8rQEdhlVVcp-uA9jnt1m5s2AVy-aq_3TphRqAAB7hkKKkHVC7WEMxOJdYYNMl8zqlgz8IrgDYjyKttvckYYi1GZ-ni2uFpu4UMAyEFBfIBaN9su_jKK-DLWbvTZ-nbXVMCyB6leeIuNGtxbbbqY7ntSbc7zcgzk2MB38YJN04dhdNbF_vKrMZTfxUTqUrqVvfzkWJQqZULglDynZHcItVMLqpKfZLMBqszsvn1_O5tr5qsf3lgON2uyP3hDqaUeITKUGKqZQaTOivHd_qTAk24p0RNxHY7mZJSFPLd-w7dJyfjS0zERvYIZQgWuasFEnWE8vGRPvuViZPRceeEbJrpcEkQXOUzdLWtKqsjZOnW78bWR8xftnsbRn17ubowSrRLr1sbruiIceuN1X1X1Wm8tX2lz2w-eQFBXq9kej11EJXkOwcdpnkf9Rm0Zs-S6L8sVCo3X3oDmdKlBpdyD7yG8OeRns_Ta4_OIbBO8XRxrtobMm5uXBpMbMyAk1bGh2y3_7H4bj49nq6OzZxWr1y3Wwl8_AwaKoIzufO0heLAcdv_s-wSWA0IXGG1cNFAf6OKrqhr4-8DRNxAhBBAKXav2_URwwBpx0eD7qNcXNWxLsz1qOz2BY9Wl9XHyhAX6zBRm_V9eCCNWn-AIWYvlblO7eCv2frz1yzScsQwQVXqSD5VEiI6ShIzfje89EdyapzbGG94Xv1Hmx-VdSb7kubiA_MJfH8xO8qbPJuVGc1T6Q6-MFRzqgtjHZQp_pxkyW-c9ccgmRUwXbWENP6DDv5Jno1p2EEazlwRh9_uCkdf0c_rIKJYeZhklVN9ThBmEH8l2sdu8ATuuDPexqfXk9CwztgQbjfDp2_Bh-3QSwDqho0HiaaqUghAm8dc3gb1uB863Px_tkm-yhjbiuBWqGHi0JlcVfZAjDKhZFq51pR5-eUcThsjsZQrjc2zAlwuTnqNMwp5pO5PudRH0SlwWI1g9GJolb0mBwnzmlJC0w_tTosa12TfyfmOW3Kh1WGAg2eg57fzC3o6dkrXYLQm1yJ1YRn1lkuntZnD6AYiVg9tt12GD4WBHG3ssh0slcMhUpWxZGkdssD9GaMs3Rm-IJkABBrlZzknpEoH3iJ1ObqXFz0ebhLbLRaLllDvxEZe-DF2_J735hTNUNGVAXPBF_bTOvqUamfDmt-ZKuYPBEbRwXj3xYFCGARduFP1ByHvnYGqeG9Vrql6qtbd6gHb6YIpreLfcqTxeiEewgObTF_7xwQvgSf6a3Gs2CC1xDevxrR2MErN5T8I6oxKmMjKwycE1kIRue22dKuCA3hNppcBvx-BZNlKXKTo9z2JCUqUlFoco1pixzu7YEsTVu6DYG6FhycwiY5RkWlj1Zzn6HDJKXiKXnoLm1XfO8pGdQB5LW7sTuFmErzKQUYH-n2s.kttDsf_NO7HWWXbYVVyQPg; __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; _gid=GA1.2.1218786756.1671659418; __cf_bm=xS3qzXjMhAZlw2I_U4iViJHo5JL9lsZqRXTaeGA8Nes-1671659425-0-AaUb1Zx4II5Y40Xr6grbI+uak1rb0uAlNqpB0JR6Dv4bO5ml2CfcYaXPkn/4JapGQCpwkwaXRAF5rnl0VCSvxnMPpkVo1fJYxnWvAbYjjvCDXiPtAPcOy2/Gs+VfdCG6f3Wo+0/ja7xhuL1NB3Hn5YuVzGETWRC0IF7FMHiCVKrH/YzI+Mcj29xGV0FRLsYSqA=="
}

# # conn = HTTP20Connection('chat.openai.com:443')
# # request = conn.request('POST', '/backend-api/conversation', headers=headers_message, body=data_payload.encode(encoding='utf-8'))

# # # time.sleep(5)

# # resp = conn.get_response()

# # f = open("cloud.html", 'w')
# # print(f.write(resp.read().decode('utf-8')))

# # # print(resp.read())


# # # response = client.post(host_message, headers=headers_message, data=data_payload)

# # # print(response)

# import requests


# # curl -L -X POST 'http://localhost:8191/v1' \
# # -H 'Content-Type: application/json' \
# # --data-raw '{
# #   "cmd": "request.get",
# #   "url":"http://www.google.com/",
# #   "maxTimeout": 60000
# # }'

# # ss  = requests.get()


# payload = """{\\"action\\":\\"next\\",\\"messages\\":[{\\"id\\":\\"ede59e1f-ba84-4929-8210-48170a234b13\\",\\"role\\":\\"user\\",\\"content\\":{\\"content_type\\":\\"text\\",\\"parts\\":[\\"ss\\"]}}],\\"conversation_id\\":\\"2bd2d005-64e9-4e44-9d5e-4eee70e03721\\",\\"parent_message_id\\":\\"edfd6a8a-a2ff-42c1-902b-5563a266babe\\",\\"model\\":\\"text-davinci-002-render\\"}\\",\\"maxTimeout\\": 60000}"""

# data_raw = """{{\
#   "cmd": "request.post",\
#   "session" : "openaisession", \
#   "url":"https://chat.openai.com/backend-api/conversation",\
#   "postData":"{payload}"}}""".format(payload=payload)

# session_create_raw = """{\
#   "cmd": "sessions.create",\
#   "session":"openaisession"}"""


# curlss = "curl -L -X POST 'http://localhost:8191/v1' \
# -H 'Host: chat.openai.com' \
# -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0' \
# -H 'Accept: text/event-stream' \
# -H 'Accept-Language: en-US,en;q=0.5' \
# -H 'Accept-Encoding: gzip, deflate, br' \
# -H 'Referer: https://chat.openai.com/chat' \
# -H 'Content-Type: application/json' \
# -H 'X-OpenAI-Assistant-App-Id: ' \
# -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MTIyMzkyOSwiZXhwIjoxNjcxODI4NzI5LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ' \
# -H 'Origin: https://chat.openai.com' \
# -H 'Alt-Used: chat.openai.com' \
# -H 'Connection: keep-alive' \
# -H 'Cookie: _ga=GA1.2.276779431.1670925280; cf_clearance=6BP.WNcvx_8u7.AybziVpxpdCaKhA3OGsumcJEEKoo0-1671659424-0-1-ea1b3719.7f8f7cfc.570e39dd-250; intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..p8PKQtDmmOHBepGK.jkcaofFIIDCycWOhebpPOVMKFthaokuiXKvI3d2e_iSfbX7_VmA67alz5EBGTu99jC4he-evcHEuounqHlpdVT1lbKIhJncfL5vPF8Y-G3x4847_GmnIh5yCjLe7JdC-c2nnVrVPBSsvGnEMcoj6kbHqa8Gw34Yn1NpBKXIjhkSFu-M1C9RZSejdAuJym_VLQJgm4fLibElP6sMzQlKArKhs2pwv9dd_aOCD22hFLtbyX5O4PJ2nLZJPpgIAsfaojKDO6m4bvLBMeJF_81hrDUmn5roACbP7x_NyHJ4-pvp8EUelmz8OZnLivIitA2HCX2M0zXkqSMWbjGu4Kraf5uHhPNhDX9e2uU5jRGji8EEAyNHUSRGf5_b2ViZt6NQs4cxD6nXWBxNq5ey_lKOeHfv04SMvq8fBIb2s_78hk70prL84HYKtMKdLKC2tFccN8tNspZfVO9_NeKHLeIhElx2BwmlIofrYaJgNed4WpoTyJXsnLUEXU5Mqli4KgVKnB5-GuM3LMj2HeVGEtH0RKRkRdAH0hwlAHIyv2Uksb2sIOu5nXT77tjaUo6Q6CVJmr2Rd3oVe3XW8WfxFJS4jGR45ccACtruWMm9aOY9B2UZ_UYVmxt2ruJ3UQq6mYQWHV_v53IbpgV2ulChPvBd6X3IEA3sbL6HJpQStp6ylIgJm2RR9pywVfvL3KpzMz8puZRuMCtzG7uCgoEyVe2dMh2n3dtM5P7ynJ4Iwp8Gw1X6ovTnMUMEnAJtioDdM4c4RIvE6Ox6dsOQ0yMTdWmwocXWd-XjcHhiF-KqqQlS92wgpb6WcnZo71uFHNZdgNVQxyuezHciDhE8bX_6VqTjySq1vBbnARURIKA8rQEdhlVVcp-uA9jnt1m5s2AVy-aq_3TphRqAAB7hkKKkHVC7WEMxOJdYYNMl8zqlgz8IrgDYjyKttvckYYi1GZ-ni2uFpu4UMAyEFBfIBaN9su_jKK-DLWbvTZ-nbXVMCyB6leeIuNGtxbbbqY7ntSbc7zcgzk2MB38YJN04dhdNbF_vKrMZTfxUTqUrqVvfzkWJQqZULglDynZHcItVMLqpKfZLMBqszsvn1_O5tr5qsf3lgON2uyP3hDqaUeITKUGKqZQaTOivHd_qTAk24p0RNxHY7mZJSFPLd-w7dJyfjS0zERvYIZQgWuasFEnWE8vGRPvuViZPRceeEbJrpcEkQXOUzdLWtKqsjZOnW78bWR8xftnsbRn17ubowSrRLr1sbruiIceuN1X1X1Wm8tX2lz2w-eQFBXq9kej11EJXkOwcdpnkf9Rm0Zs-S6L8sVCo3X3oDmdKlBpdyD7yG8OeRns_Ta4_OIbBO8XRxrtobMm5uXBpMbMyAk1bGh2y3_7H4bj49nq6OzZxWr1y3Wwl8_AwaKoIzufO0heLAcdv_s-wSWA0IXGG1cNFAf6OKrqhr4-8DRNxAhBBAKXav2_URwwBpx0eD7qNcXNWxLsz1qOz2BY9Wl9XHyhAX6zBRm_V9eCCNWn-AIWYvlblO7eCv2frz1yzScsQwQVXqSD5VEiI6ShIzfje89EdyapzbGG94Xv1Hmx-VdSb7kubiA_MJfH8xO8qbPJuVGc1T6Q6-MFRzqgtjHZQp_pxkyW-c9ccgmRUwXbWENP6DDv5Jno1p2EEazlwRh9_uCkdf0c_rIKJYeZhklVN9ThBmEH8l2sdu8ATuuDPexqfXk9CwztgQbjfDp2_Bh-3QSwDqho0HiaaqUghAm8dc3gb1uB863Px_tkm-yhjbiuBWqGHi0JlcVfZAjDKhZFq51pR5-eUcThsjsZQrjc2zAlwuTnqNMwp5pO5PudRH0SlwWI1g9GJolb0mBwnzmlJC0w_tTosa12TfyfmOW3Kh1WGAg2eg57fzC3o6dkrXYLQm1yJ1YRn1lkuntZnD6AYiVg9tt12GD4WBHG3ssh0slcMhUpWxZGkdssD9GaMs3Rm-IJkABBrlZzknpEoH3iJ1ObqXFz0ebhLbLRaLllDvxEZe-DF2_J735hTNUNGVAXPBF_bTOvqUamfDmt-ZKuYPBEbRwXj3xYFCGARduFP1ByHvnYGqeG9Vrql6qtbd6gHb6YIpreLfcqTxeiEewgObTF_7xwQvgSf6a3Gs2CC1xDevxrR2MErN5T8I6oxKmMjKwycE1kIRue22dKuCA3hNppcBvx-BZNlKXKTo9z2JCUqUlFoco1pixzu7YEsTVu6DYG6FhycwiY5RkWlj1Zzn6HDJKXiKXnoLm1XfO8pGdQB5LW7sTuFmErzKQUYH-n2s.kttDsf_NO7HWWXbYVVyQPg; __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; _gid=GA1.2.1218786756.1671659418; __cf_bm=xS3qzXjMhAZlw2I_U4iViJHo5JL9lsZqRXTaeGA8Nes-1671659425-0-AaUb1Zx4II5Y40Xr6grbI+uak1rb0uAlNqpB0JR6Dv4bO5ml2CfcYaXPkn/4JapGQCpwkwaXRAF5rnl0VCSvxnMPpkVo1fJYxnWvAbYjjvCDXiPtAPcOy2/Gs+VfdCG6f3Wo+0/ja7xhuL1NB3Hn5YuVzGETWRC0IF7FMHiCVKrH/YzI+Mcj29xGV0FRLsYSqA==' \
# -H 'Sec-Fetch-Dest: empty' \
# -H 'Sec-Fetch-Mode: cors' \
# -H 'Sec-Fetch-Site: same-origin' \
# -H 'TE: trailers' \
# --data-raw '{}'".format(data_raw)


# session_create_curl = """curl -L -X POST 'http://localhost:8191/v1' \
# -H 'Content-Type: application/json' \
# --data-raw '{}' \
# """.format(session_create_raw)


# # response = requests.post(url="http://localhost:8191/v1", json=data, headers=headers_message)
# print(call_curl(session_create_curl))
# print(call_curl(curlss))


# import cfscrape

# scraper = cfscrape.create_scraper()  # create a scraper

# url = "https://chat.openai.com/backend-api/conversation"

# f = open("sss.html", 'w')
# response = scraper.post(url, json=data_payload, headers=headers_message)  # send the request

# print(response.status_code)  # prints the status code of the response (e.g. 200 for success)
# print(response.text)  # prints the content of the response
# f.write(response.text)


# openai.api_key = "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"

# access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2Fw…iOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ"
# # chat = ChatGPT(session_token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..MFQoCdj_x9T4CK3A.fQGYfZxWk9v1ERN0PX3ZfMuoGXNIGcrsKWiR0C6wG4vZQog2bQxuWnTqjJ5Ww4_-UNj3B4iJnwkPAV4njo1AD8l9wwnVfn6pG9ZvByOYEeHnfHo0AgLZlAfax6zr8Czs4DN1dorhaKBRn3aVkyo5d9h1V9WOazCVshO6UBqrpuyrwOzUf6mHmAzYsneOL4HD9D5x0uazC9ECh0blH9ll2YTriFpRiKI3Z8RoUs-uaeGYT79jFH-LJ6iGRbtDB1cW_dDoil96zf9cLToNPHxRkVin-lhqM4DZxfHouGIbO681tQG3Vs7GPSCg1vg4UlGyWSARchSjnVWh_51zRO6qsaQvVaPTkdsO4rloihPXPp8BDFNeJ_4C34sKrChBhKgejx0UKTCTTM0RqoqX7iHkmF17cXoRuu5L75FG66XDRPotBjw5jo88RyFP2J9S9X87hC0l1wYL-vCRRcr9UoezEKgknbJKDulP__GTc_d7W0ANzLZm2u58XJgcnltBaexOtjWH7nIj4RJZFj2UAdXR8cfmASoi_Dp_C_7U6vffIR6rehx44Id6s80PpHi9JSz4wjqcWP7cS6AZ6s5i67CYJoyb2kM7YVGx9gjPyCfvbY3LHQY3uZA2yE30NZFwgSbj_C831qxSSHgpkG22fSbYYYSJjGxMZ96vm-jke659ZT9PPRzHUis4M-Arb2GrP1c3R1rs-1lx_KZ5uhiuUk3jRdhc4udKrh8gwHl36uN7ttJ0DDduWCR-xf6KU_kEuThXyxvggq3dAmk-U9uU1QKxkxpCinf7XbuCritZOysyV0mZiFRiH0jjCdXBnBRPOFMZSBXr2qqxpdRuldWPqd9-IDRHzjAmb2NVNDlpqDoFxydm3oOXrgOt54MfysSDwjgMEqiv6y_Y6Ks16CTvjqu6ecE19lmuSRX5lfZhDY_Da1r8M1Mkn6GEB4iRYNt2kXu2jGeiMvlvGqcHKU7-aq2TrCi_90jKwUVaKERNlLSIUCvvy7vos7OssOTcAK03jkResyGFZRQClWHmvCKpMHzayc0JlLaqLdai-KoeaiPkm9tsabfTUwuta2zIo8YvZfqpdFVBDH2AMpDrzzPWekDi_WrNDM4olnu_Sz8FytWQm54BtyX8vb8IblsKReIv7mHnGCfm0A-kYpd_yLzRHsAMww9Pzxsv6LDbg8M0vwZMZmgVa9xN6BL2k6ZB49mpOZN407PspeHNKoT5vuctXjeNUu9F22YzB0F7MjSY8M93pB4lK00Us1CzSJUlQXNyg6I3QievwNCooxxNXQdBHG2fzmdy4jhYmphSBnisZmvMAYoc5V7M6H3NkAKW700SBQAjMAycQUhrzHOmCeVd4FbMKE3XvOGvVlddtUjPswO2-RgZE5Smnkp5ABrxfMv519MYHphgctf5mWCnvDcZhqMMlPIYo63Pf10L6gnd5qAt7C-HHo5D8P7-bbVsWR1NGJfrtgNFO8UOs91-QPr9cYj_6GyXuwC81JqrMiXm3Ms8ZsOnbYqXb_ULj_Nh1njBJhKLyS6o7DW0c0dukczkjSfP0yWJndVY7bzogfq1L-g2BKlBz92BBtECJLaogstR97qQbO9V7SLpNrLNJt9b350BxpKjVJV55QnTBiBtNE40NO1xIymsENVZdWB8qWhRPyo2IRpPPEW4t6Lsp3tvToYuxg872QCAdB6Ltaa7PBPtww8epE7DSNNZVJzt7ORig6pCjoWmJYO0GCoIQsBuW0jM2q3Cf9lGyxwvpX1p3ppuzQ3naM2RtXfRaM73x5vUMH-B48CZXI-TMR9KfVtO3Qq4sl4J5jWvFObxzG-toWuF7LEc-aGqJ1ofyv9qBWJ27PFkIrborlNTV8tSau8EGdisIjZG8nJp-XNWp8EIlhmYErL2lYaJXwGgpo3_dj31SV9V9aTsOuWrU84eZJIxYRZhjq4iWorkaFVYv-aUGncitiYlpWconye3CkV3BtZ3hvjg2CQZ5iEgjNYZjfUAsVUA7olde9NvcHzc7-_5WckpKF1G1dlSkDQ1q4n3cdsprSqzwt192mjD7_RVEvwZEpQPW-XdAnq2II7yAcLx-vZEeSJzpDKA_jC74L91KsmFsN0yQK-xhCzjCLts4JnGQ9Q6Dhw3Cw6JQjKFtxYjHBDLxrFnNbjF6eOCnivnwCpap2jozzSjYkwpY6aZY-hE8lr6G-1G1teHYDmYfysUePfZNnl_fT1lD8A7uVP3rQDGKE46DzDaZHkzxd-Amhx_RktPbj3vDtghmk1G3bC4uQygntIUsQtgQ_1H.RNAS1GWLHRbi9bozTXvVDQ")
# # chat.authenticate()
# data_json = {
# "action": "next",
# "messages": [
# {
#     "id": str(uuid.uuid4()),
#     "role": "user",
#     "content": {
#     "content_type": "text",
#     "parts": [
#         "nns"
#     ]
#     }
# }
# ],
# "parent_message_id": str(uuid.uuid4()),
# "model": "text-davinci-002-render"
# }


# headers_json = {
#     "Host": "chat.openai.com",
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
#     "Accept": "text/event-stream",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://chat.openai.com/chat",
#     "Content-Type": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MTIyMzkyOSwiZXhwIjoxNjcxODI4NzI5LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ",
#     "Cookie": "_ga=GA1.2.276779431.1670925280; cf_clearance=pBeikmtEypav5lydwU0azBU5uYwUvzYXgrUhEW6MvUA-1671389704-0-1-ea1b3719.7f8f7cfc.570e39dd-160; intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..BWyPAGB9Op8OPFT0.AAtfQsyfQBRM14TFUDBiGnn0A6-7Fa9t__TKvpxu8St00BB8hhd561V659lSjDv-3K4fkcfRKAmazJhPuWMqcVi2kUvd9a-IvJCsWhIsxhAHEj9VHiAkm_MDH7K0C-55XvLE0UiTeI8VUgNel5DfDVDDlsJghPQ-B8KGXLBZmtjN3nRtSdNU6n5BTp-Op8KwcqGGwJSgkw6Jl6aIYq3qPKz69CRqq-82I6Lv03fl4orDRiT6jJMPEWqOq3HGRoOgh9phYYOyUVftSIJ9z_9NJlqVAMUCDQEZVjmp1KopjgVrDi8WxKQofdyFupG2h_DL1KZB57xjQawKEum_AYqfXUm74YlY1V3XTqK18_XlIajOKdIuOUgY4v4Qp5D7yiWL3yr5hFQAORhclNZ6TF4YIGpcKmUtUhPTMQzvYUADRwM5E2iU4amAvlUaFYBhC6RFsD7_iv1QXd0pLzDy0p0gCM46hVPJy9zmNihZVNOH1VtxFjr5QRcvG0Q0EpYyyiW_tPKlrl44W9EpPZb5PsjL2_GH3IX9WGNCgftWBm0AFzaDnb8UBR96K767bersqlQkJoYoFWDca-7045LR4HmaFbvOve1KAfoqF_WYEZtL0eKSxaRKmZwEKdLS7YBSBIsTJ5tKo6iHSnDy4YXNQaR0VRLs4nOl3pOqPjs1178fOoCcpWMODmesjzEtwUOvHWRAMa36gGerbOqaJ9C2ZBH7_OeyVWKqDDWjtsBK10gwY7Ps6Wl5jw_qE60utaL8e8lOMmjNCINqvOtEWiuWPTtxK8VIpDfiuWq-zrtoO7GZEnB6Dg03L9C__ytGLZObfqU3yApcrfl68k2dpvFQ-RnNLZgYwA87904D9chnXPwOj38shDjpU6vjh4Tr7ytg5dZsF8uQRRbr1vKkaCx1PoJxgmx1ra1wB1JZeQ-WfB2rQ625s-rHpfO9WVMrHGP5e8zc9T0gVoIVU37tk0wPXRkXh215YEhTV85g9ejmO_XlfYWiKhO_KeFRvt4Vpm9Qhhlv4SjXyvr7JUvMYDj_KWpC_5Z0zTOdMxpdz-ueioO8So9yHIciRqWeU4IRB7SKxrJuCPltrbEXyGlZtcRE5pRyVIvuV9bJ-1vb3HZob0q5hF9u3tv0Ceh9dYbcwAiOepe3APwfjpK8q7cHLM29Ue6WeK3n65e1F46Ub1jDfwQ6sSWk7kPeUS86SySbe7EfVHbQLZoxsquWx_jUO9OkQvMqChg7sYKI1m2Sw9jAam57g6VF1uQF6KXmNNMaWoDAOjcq-V025b0bFz6FK4x4aWzkuvYN05E0JJzzDfHP37me81ZJf1feZC5fqt6GUq6zk98pF2RUp2XZvGlj2JhlbVWuvEFNYXYko_ysgKiAIoq8DtxuLQ81TPXHVlEJzg8QBsYBfBpwJXC9QASYo1-UgCxdvaQ9oQqJptDdsjJnoXku1ZuEgmN97KaUsJHpP2nJQepbdAzPhAvRUWutAT0R-tGEgzs5pwVUCE8zrI1ih0BonkHtF6tkgXrSkpta0ONCCc2juDmALxr-GChwFeMHArTP-aQyeyV-DgiX9NB28kKNfL90fz0RoS_kd9OtQUhNZoxFQnpY9M_QVC-8xakizFNQhuFIv8oT3cHs5HHkwJlrE9hbqd6mK9mJtbYyL-DbpDBMAds9pJWqOOpsdiN-6UU-5rHVAPj0RoOdga2wQNE5RCmOmhwYnPH8iOR0YzvykLVrE0nAKbokza_bbO01GG1mhg42FEPTVLbvMYQQhjTn67McVoQLHZsNg3_oVh_2W4yX75ghr30pXfdJa2vlgenuWx5X5gW5-JHxeZo3bgfdSd2d5Tferx1zeHWAvEbsGHmh6YDWcAQth9KU2UVfrzXcxMsrEXLaeKkW-hqxo7AtrE4fi1D-F_Hha37fLh3M64UI_lsc-fcCHldpYjhfmmWjOivfnfKESxYA7KDe0GvCdJvoJTgXg_ZUdGstQklvOYMh1Cbv_jLYx3X2Sv0daXoIBA98ATj2axC6H4l9tpMBDFq6FXSocnzGVaXISNtDvuugNpi2H7WHQD4rSwnAgHV1JLvLYRbqY6mrtCY0IZRLSipX8b3sNrMo8F2zp8nXo8KFqARaIeGwE61gHGlnGA9nfi-dz-ZxfAremOS9rfRNVoNe4tbjcDrAMDpjv19TFwsVQrfNVC1I4FObXtVlvtf0HZzWoa-2R_wfZxaPNZiEUyYqbcc44Ug2WCFQPyhlljOMU2xdYNb8LOCpJFrz8Ut0P7yR2XC8TU6Zrt-hSjwnb4314z1m8QsA.rRaVdFj--plYYv3OsC0IFg; _gid=GA1.2.553582256.1671223906; __cf_bm=3liSn92dgT_s_aqvAuNP_lSJWmDCbTwsfBNEpJ3_atg-1671392286-0-AUmPYTkLjKpoGp9Fw6LxU05IhNWbJqYewgST1ERNBvX4mh0/+M/u8qIVhyux0n6v8V1xu3+D5RFg43bdVqOuGnLK33SJKpywjBW1loOZGlU9tH01jlJCK1vRdlq2VvJr1NrJy1eEMmNFHX0ePaBVSD6oiKDFoiFeVHpeF6F7hv5cbtRvy2MEEFdS5Yr0oc5KDA==; __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; _cfuvid=mvlpWqIB_77JwbxdPgMG5C45t3Xq3g9TR5JQR8PmGlQ-1671223927506-0-604800000",
#     "Connection": "keep-alive",
# }


# # #   print(data_json)
# # #   print()
# # #   print(headers_json)    "Origin": "https://chat.openai.com",
# # # #    {
# # #     "Host": "chat.openai.com",
# # #     "User-Agent":
# # #     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
# # #     "Accept": "text/event-stream",
# # #     "Accept-Language": "en-US,en;q=0.5",
# # #     "Accept-Encoding": "gzip, deflate, br",
# # #     "Referer": "https://chat.openai.com/chat",
# # #     "Content-Type": "application/json",
# # #     "Authorization": "Bearer " + access_token,
# # #     "Connection": "keep-alive"
# # #   }
# # #   print(headers_json, data_json, config.url_api)

# client = httpx.Client(http2=True)

# client.cookies.set("__Secure-next-auth.session-token", "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..BWyPAGB9Op8OPFT0.AAtfQsyfQBRM14TFUDBiGnn0A6-7Fa9t__TKvpxu8St00BB8hhd561V659lSjDv-3K4fkcfRKAmazJhPuWMqcVi2kUvd9a-IvJCsWhIsxhAHEj9VHiAkm_MDH7K0C-55XvLE0UiTeI8VUgNel5DfDVDDlsJghPQ-B8KGXLBZmtjN3nRtSdNU6n5BTp-Op8KwcqGGwJSgkw6Jl6aIYq3qPKz69CRqq-82I6Lv03fl4orDRiT6jJMPEWqOq3HGRoOgh9phYYOyUVftSIJ9z_9NJlqVAMUCDQEZVjmp1KopjgVrDi8WxKQofdyFupG2h_DL1KZB57xjQawKEum_AYqfXUm74YlY1V3XTqK18_XlIajOKdIuOUgY4v4Qp5D7yiWL3yr5hFQAORhclNZ6TF4YIGpcKmUtUhPTMQzvYUADRwM5E2iU4amAvlUaFYBhC6RFsD7_iv1QXd0pLzDy0p0gCM46hVPJy9zmNihZVNOH1VtxFjr5QRcvG0Q0EpYyyiW_tPKlrl44W9EpPZb5PsjL2_GH3IX9WGNCgftWBm0AFzaDnb8UBR96K767bersqlQkJoYoFWDca-7045LR4HmaFbvOve1KAfoqF_WYEZtL0eKSxaRKmZwEKdLS7YBSBIsTJ5tKo6iHSnDy4YXNQaR0VRLs4nOl3pOqPjs1178fOoCcpWMODmesjzEtwUOvHWRAMa36gGerbOqaJ9C2ZBH7_OeyVWKqDDWjtsBK10gwY7Ps6Wl5jw_qE60utaL8e8lOMmjNCINqvOtEWiuWPTtxK8VIpDfiuWq-zrtoO7GZEnB6Dg03L9C__ytGLZObfqU3yApcrfl68k2dpvFQ-RnNLZgYwA87904D9chnXPwOj38shDjpU6vjh4Tr7ytg5dZsF8uQRRbr1vKkaCx1PoJxgmx1ra1wB1JZeQ-WfB2rQ625s-rHpfO9WVMrHGP5e8zc9T0gVoIVU37tk0wPXRkXh215YEhTV85g9ejmO_XlfYWiKhO_KeFRvt4Vpm9Qhhlv4SjXyvr7JUvMYDj_KWpC_5Z0zTOdMxpdz-ueioO8So9yHIciRqWeU4IRB7SKxrJuCPltrbEXyGlZtcRE5pRyVIvuV9bJ-1vb3HZob0q5hF9u3tv0Ceh9dYbcwAiOepe3APwfjpK8q7cHLM29Ue6WeK3n65e1F46Ub1jDfwQ6sSWk7kPeUS86SySbe7EfVHbQLZoxsquWx_jUO9OkQvMqChg7sYKI1m2Sw9jAam57g6VF1uQF6KXmNNMaWoDAOjcq-V025b0bFz6FK4x4aWzkuvYN05E0JJzzDfHP37me81ZJf1feZC5fqt6GUq6zk98pF2RUp2XZvGlj2JhlbVWuvEFNYXYko_ysgKiAIoq8DtxuLQ81TPXHVlEJzg8QBsYBfBpwJXC9QASYo1-UgCxdvaQ9oQqJptDdsjJnoXku1ZuEgmN97KaUsJHpP2nJQepbdAzPhAvRUWutAT0R-tGEgzs5pwVUCE8zrI1ih0BonkHtF6tkgXrSkpta0ONCCc2juDmALxr-GChwFeMHArTP-aQyeyV-DgiX9NB28kKNfL90fz0RoS_kd9OtQUhNZoxFQnpY9M_QVC-8xakizFNQhuFIv8oT3cHs5HHkwJlrE9hbqd6mK9mJtbYyL-DbpDBMAds9pJWqOOpsdiN-6UU-5rHVAPj0RoOdga2wQNE5RCmOmhwYnPH8iOR0YzvykLVrE0nAKbokza_bbO01GG1mhg42FEPTVLbvMYQQhjTn67McVoQLHZsNg3_oVh_2W4yX75ghr30pXfdJa2vlgenuWx5X5gW5-JHxeZo3bgfdSd2d5Tferx1zeHWAvEbsGHmh6YDWcAQth9KU2UVfrzXcxMsrEXLaeKkW-hqxo7AtrE4fi1D-F_Hha37fLh3M64UI_lsc-fcCHldpYjhfmmWjOivfnfKESxYA7KDe0GvCdJvoJTgXg_ZUdGstQklvOYMh1Cbv_jLYx3X2Sv0daXoIBA98ATj2axC6H4l9tpMBDFq6FXSocnzGVaXISNtDvuugNpi2H7WHQD4rSwnAgHV1JLvLYRbqY6mrtCY0IZRLSipX8b3sNrMo8F2zp8nXo8KFqARaIeGwE61gHGlnGA9nfi-dz-ZxfAremOS9rfRNVoNe4tbjcDrAMDpjv19TFwsVQrfNVC1I4FObXtVlvtf0HZzWoa-2R_wfZxaPNZiEUyYqbcc44Ug2WCFQPyhlljOMU2xdYNb8LOCpJFrz8Ut0P7yR2XC8TU6Zrt-hSjwnb4314z1m8QsA.rRaVdFj--plYYv3OsC0IFg")

# data = client.post(url=config.url_api,
#                     data=data_json,
#                     headers=headers_json)

# print(data)

# lock = False
# # print(access_token[505])
# # print(access_token.decode(encoding="latin-1"))

# def getAnswerByQuestion(prompt):
#     # response = chat.send_message("Hello!")
#     # print(response.content)
#     # chat.close()
# #   # return openai.Completion.create(engine=model,
# #   #                                 prompt=prompt,
# #   #                                 max_tokens=2048,
# #   #                                 n=1,
# #   #                                 stop=None,
# #   #                                 temperature=0.4)["choices"][0]["text"]
#     # data_json = {
#     #     "action":
#     #     "next",
#     #     "messages": [{
#     #     "id": str(uuid.uuid4()),
#     #     "role": config.role,
#     #     "content": {
#     #         "content_type": config.content_type,
#     #         "parts": [prompt]
#     #     }
#     #     }],
#     #     "parent_message_id":
#     #     str(uuid.uuid4()),
#     #     "model":
#     #     config.model
#     # }


#     return stringy

# client = discord.Client(intents=discord.Intents.all())


# @client.event
# async def on_ready():
#   print('We have logged in as {0.user}'.format(client))


# @client.event
# async def on_message(message):

#   if message.author == client.user:
#     return

#   if message.content.startswith('?'):
#     global lock
#     if not lock:
#       await message.channel.send("...")
#       lock = True
#       msg = message.content[1:]
#       print(msg)
#     #   try:
#       await message.channel.send("```" + getAnswerByQuestion(msg) + "```")
#     #   except Exception as e:
#     #     print(e)
#     #     await message.channel.send("Internal ERROR Occured")

#       lock = False
#     else:
#       await message.channel.send(
#         "Iam not done with previous question answering")


# client.run(
#   'MTA1MjM5NzM5MjU2MzAxNTY5MA.GGFVNp.udJmmdCZSxplYwwVAv7yFkKD5L0oJLChpguXJM')


# POST /backend-api/conversation HTTP/3
# Host: chat.openai.com
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
# Accept: text/event-stream
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate, br
# Referer: https://chat.openai.com/chat
# Content-Type: application/json
# X-OpenAI-Assistant-App-Id:
# Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MTIyMzkyOSwiZXhwIjoxNjcxODI4NzI5LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ
# Content-Length: 289
# Origin: https://chat.openai.com
# Alt-Used: chat.openai.com
# Connection: keep-alive
# Cookie: _ga=GA1.2.276779431.1670925280; cf_clearance=6BP.WNcvx_8u7.AybziVpxpdCaKhA3OGsumcJEEKoo0-1671659424-0-1-ea1b3719.7f8f7cfc.570e39dd-250; intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..p8PKQtDmmOHBepGK.jkcaofFIIDCycWOhebpPOVMKFthaokuiXKvI3d2e_iSfbX7_VmA67alz5EBGTu99jC4he-evcHEuounqHlpdVT1lbKIhJncfL5vPF8Y-G3x4847_GmnIh5yCjLe7JdC-c2nnVrVPBSsvGnEMcoj6kbHqa8Gw34Yn1NpBKXIjhkSFu-M1C9RZSejdAuJym_VLQJgm4fLibElP6sMzQlKArKhs2pwv9dd_aOCD22hFLtbyX5O4PJ2nLZJPpgIAsfaojKDO6m4bvLBMeJF_81hrDUmn5roACbP7x_NyHJ4-pvp8EUelmz8OZnLivIitA2HCX2M0zXkqSMWbjGu4Kraf5uHhPNhDX9e2uU5jRGji8EEAyNHUSRGf5_b2ViZt6NQs4cxD6nXWBxNq5ey_lKOeHfv04SMvq8fBIb2s_78hk70prL84HYKtMKdLKC2tFccN8tNspZfVO9_NeKHLeIhElx2BwmlIofrYaJgNed4WpoTyJXsnLUEXU5Mqli4KgVKnB5-GuM3LMj2HeVGEtH0RKRkRdAH0hwlAHIyv2Uksb2sIOu5nXT77tjaUo6Q6CVJmr2Rd3oVe3XW8WfxFJS4jGR45ccACtruWMm9aOY9B2UZ_UYVmxt2ruJ3UQq6mYQWHV_v53IbpgV2ulChPvBd6X3IEA3sbL6HJpQStp6ylIgJm2RR9pywVfvL3KpzMz8puZRuMCtzG7uCgoEyVe2dMh2n3dtM5P7ynJ4Iwp8Gw1X6ovTnMUMEnAJtioDdM4c4RIvE6Ox6dsOQ0yMTdWmwocXWd-XjcHhiF-KqqQlS92wgpb6WcnZo71uFHNZdgNVQxyuezHciDhE8bX_6VqTjySq1vBbnARURIKA8rQEdhlVVcp-uA9jnt1m5s2AVy-aq_3TphRqAAB7hkKKkHVC7WEMxOJdYYNMl8zqlgz8IrgDYjyKttvckYYi1GZ-ni2uFpu4UMAyEFBfIBaN9su_jKK-DLWbvTZ-nbXVMCyB6leeIuNGtxbbbqY7ntSbc7zcgzk2MB38YJN04dhdNbF_vKrMZTfxUTqUrqVvfzkWJQqZULglDynZHcItVMLqpKfZLMBqszsvn1_O5tr5qsf3lgON2uyP3hDqaUeITKUGKqZQaTOivHd_qTAk24p0RNxHY7mZJSFPLd-w7dJyfjS0zERvYIZQgWuasFEnWE8vGRPvuViZPRceeEbJrpcEkQXOUzdLWtKqsjZOnW78bWR8xftnsbRn17ubowSrRLr1sbruiIceuN1X1X1Wm8tX2lz2w-eQFBXq9kej11EJXkOwcdpnkf9Rm0Zs-S6L8sVCo3X3oDmdKlBpdyD7yG8OeRns_Ta4_OIbBO8XRxrtobMm5uXBpMbMyAk1bGh2y3_7H4bj49nq6OzZxWr1y3Wwl8_AwaKoIzufO0heLAcdv_s-wSWA0IXGG1cNFAf6OKrqhr4-8DRNxAhBBAKXav2_URwwBpx0eD7qNcXNWxLsz1qOz2BY9Wl9XHyhAX6zBRm_V9eCCNWn-AIWYvlblO7eCv2frz1yzScsQwQVXqSD5VEiI6ShIzfje89EdyapzbGG94Xv1Hmx-VdSb7kubiA_MJfH8xO8qbPJuVGc1T6Q6-MFRzqgtjHZQp_pxkyW-c9ccgmRUwXbWENP6DDv5Jno1p2EEazlwRh9_uCkdf0c_rIKJYeZhklVN9ThBmEH8l2sdu8ATuuDPexqfXk9CwztgQbjfDp2_Bh-3QSwDqho0HiaaqUghAm8dc3gb1uB863Px_tkm-yhjbiuBWqGHi0JlcVfZAjDKhZFq51pR5-eUcThsjsZQrjc2zAlwuTnqNMwp5pO5PudRH0SlwWI1g9GJolb0mBwnzmlJC0w_tTosa12TfyfmOW3Kh1WGAg2eg57fzC3o6dkrXYLQm1yJ1YRn1lkuntZnD6AYiVg9tt12GD4WBHG3ssh0slcMhUpWxZGkdssD9GaMs3Rm-IJkABBrlZzknpEoH3iJ1ObqXFz0ebhLbLRaLllDvxEZe-DF2_J735hTNUNGVAXPBF_bTOvqUamfDmt-ZKuYPBEbRwXj3xYFCGARduFP1ByHvnYGqeG9Vrql6qtbd6gHb6YIpreLfcqTxeiEewgObTF_7xwQvgSf6a3Gs2CC1xDevxrR2MErN5T8I6oxKmMjKwycE1kIRue22dKuCA3hNppcBvx-BZNlKXKTo9z2JCUqUlFoco1pixzu7YEsTVu6DYG6FhycwiY5RkWlj1Zzn6HDJKXiKXnoLm1XfO8pGdQB5LW7sTuFmErzKQUYH-n2s.kttDsf_NO7HWWXbYVVyQPg; __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; _gid=GA1.2.1218786756.1671659418; __cf_bm=xS3qzXjMhAZlw2I_U4iViJHo5JL9lsZqRXTaeGA8Nes-1671659425-0-AaUb1Zx4II5Y40Xr6grbI+uak1rb0uAlNqpB0JR6Dv4bO5ml2CfcYaXPkn/4JapGQCpwkwaXRAF5rnl0VCSvxnMPpkVo1fJYxnWvAbYjjvCDXiPtAPcOy2/Gs+VfdCG6f3Wo+0/ja7xhuL1NB3Hn5YuVzGETWRC0IF7FMHiCVKrH/YzI+Mcj29xGV0FRLsYSqA==
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# TE: trailers


# curl -L -X POST 'http://localhost:8191/v1' \
# -H 'Host: chat.openai.com' \
# -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0' \
# -H 'Accept: text/event-stream' \
# -H 'Accept-Language: en-US,en;q=0.5' \
# -H 'Accept-Encoding: gzip, deflate, br' \
# -H 'Referer: https://chat.openai.com/chat' \
# -H 'Content-Type: application/json' \
# -H 'X-OpenAI-Assistant-App-Id: ' \
# -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MTIyMzkyOSwiZXhwIjoxNjcxODI4NzI5LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ' \
# -H 'Content-Length: 289' \
# -H 'Origin: https://chat.openai.com' \
# -H 'Alt-Used: chat.openai.com' \
# -H 'Connection: keep-alive' \
# -H 'Cookie: _ga=GA1.2.276779431.1670925280; cf_clearance=6BP.WNcvx_8u7.AybziVpxpdCaKhA3OGsumcJEEKoo0-1671659424-0-1-ea1b3719.7f8f7cfc.570e39dd-250; intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..p8PKQtDmmOHBepGK.jkcaofFIIDCycWOhebpPOVMKFthaokuiXKvI3d2e_iSfbX7_VmA67alz5EBGTu99jC4he-evcHEuounqHlpdVT1lbKIhJncfL5vPF8Y-G3x4847_GmnIh5yCjLe7JdC-c2nnVrVPBSsvGnEMcoj6kbHqa8Gw34Yn1NpBKXIjhkSFu-M1C9RZSejdAuJym_VLQJgm4fLibElP6sMzQlKArKhs2pwv9dd_aOCD22hFLtbyX5O4PJ2nLZJPpgIAsfaojKDO6m4bvLBMeJF_81hrDUmn5roACbP7x_NyHJ4-pvp8EUelmz8OZnLivIitA2HCX2M0zXkqSMWbjGu4Kraf5uHhPNhDX9e2uU5jRGji8EEAyNHUSRGf5_b2ViZt6NQs4cxD6nXWBxNq5ey_lKOeHfv04SMvq8fBIb2s_78hk70prL84HYKtMKdLKC2tFccN8tNspZfVO9_NeKHLeIhElx2BwmlIofrYaJgNed4WpoTyJXsnLUEXU5Mqli4KgVKnB5-GuM3LMj2HeVGEtH0RKRkRdAH0hwlAHIyv2Uksb2sIOu5nXT77tjaUo6Q6CVJmr2Rd3oVe3XW8WfxFJS4jGR45ccACtruWMm9aOY9B2UZ_UYVmxt2ruJ3UQq6mYQWHV_v53IbpgV2ulChPvBd6X3IEA3sbL6HJpQStp6ylIgJm2RR9pywVfvL3KpzMz8puZRuMCtzG7uCgoEyVe2dMh2n3dtM5P7ynJ4Iwp8Gw1X6ovTnMUMEnAJtioDdM4c4RIvE6Ox6dsOQ0yMTdWmwocXWd-XjcHhiF-KqqQlS92wgpb6WcnZo71uFHNZdgNVQxyuezHciDhE8bX_6VqTjySq1vBbnARURIKA8rQEdhlVVcp-uA9jnt1m5s2AVy-aq_3TphRqAAB7hkKKkHVC7WEMxOJdYYNMl8zqlgz8IrgDYjyKttvckYYi1GZ-ni2uFpu4UMAyEFBfIBaN9su_jKK-DLWbvTZ-nbXVMCyB6leeIuNGtxbbbqY7ntSbc7zcgzk2MB38YJN04dhdNbF_vKrMZTfxUTqUrqVvfzkWJQqZULglDynZHcItVMLqpKfZLMBqszsvn1_O5tr5qsf3lgON2uyP3hDqaUeITKUGKqZQaTOivHd_qTAk24p0RNxHY7mZJSFPLd-w7dJyfjS0zERvYIZQgWuasFEnWE8vGRPvuViZPRceeEbJrpcEkQXOUzdLWtKqsjZOnW78bWR8xftnsbRn17ubowSrRLr1sbruiIceuN1X1X1Wm8tX2lz2w-eQFBXq9kej11EJXkOwcdpnkf9Rm0Zs-S6L8sVCo3X3oDmdKlBpdyD7yG8OeRns_Ta4_OIbBO8XRxrtobMm5uXBpMbMyAk1bGh2y3_7H4bj49nq6OzZxWr1y3Wwl8_AwaKoIzufO0heLAcdv_s-wSWA0IXGG1cNFAf6OKrqhr4-8DRNxAhBBAKXav2_URwwBpx0eD7qNcXNWxLsz1qOz2BY9Wl9XHyhAX6zBRm_V9eCCNWn-AIWYvlblO7eCv2frz1yzScsQwQVXqSD5VEiI6ShIzfje89EdyapzbGG94Xv1Hmx-VdSb7kubiA_MJfH8xO8qbPJuVGc1T6Q6-MFRzqgtjHZQp_pxkyW-c9ccgmRUwXbWENP6DDv5Jno1p2EEazlwRh9_uCkdf0c_rIKJYeZhklVN9ThBmEH8l2sdu8ATuuDPexqfXk9CwztgQbjfDp2_Bh-3QSwDqho0HiaaqUghAm8dc3gb1uB863Px_tkm-yhjbiuBWqGHi0JlcVfZAjDKhZFq51pR5-eUcThsjsZQrjc2zAlwuTnqNMwp5pO5PudRH0SlwWI1g9GJolb0mBwnzmlJC0w_tTosa12TfyfmOW3Kh1WGAg2eg57fzC3o6dkrXYLQm1yJ1YRn1lkuntZnD6AYiVg9tt12GD4WBHG3ssh0slcMhUpWxZGkdssD9GaMs3Rm-IJkABBrlZzknpEoH3iJ1ObqXFz0ebhLbLRaLllDvxEZe-DF2_J735hTNUNGVAXPBF_bTOvqUamfDmt-ZKuYPBEbRwXj3xYFCGARduFP1ByHvnYGqeG9Vrql6qtbd6gHb6YIpreLfcqTxeiEewgObTF_7xwQvgSf6a3Gs2CC1xDevxrR2MErN5T8I6oxKmMjKwycE1kIRue22dKuCA3hNppcBvx-BZNlKXKTo9z2JCUqUlFoco1pixzu7YEsTVu6DYG6FhycwiY5RkWlj1Zzn6HDJKXiKXnoLm1XfO8pGdQB5LW7sTuFmErzKQUYH-n2s.kttDsf_NO7HWWXbYVVyQPg; __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; _gid=GA1.2.1218786756.1671659418; __cf_bm=xS3qzXjMhAZlw2I_U4iViJHo5JL9lsZqRXTaeGA8Nes-1671659425-0-AaUb1Zx4II5Y40Xr6grbI+uak1rb0uAlNqpB0JR6Dv4bO5ml2CfcYaXPkn/4JapGQCpwkwaXRAF5rnl0VCSvxnMPpkVo1fJYxnWvAbYjjvCDXiPtAPcOy2/Gs+VfdCG6f3Wo+0/ja7xhuL1NB3Hn5YuVzGETWRC0IF7FMHiCVKrH/YzI+Mcj29xGV0FRLsYSqA==' \
# -H 'Sec-Fetch-Dest: empty' \
# -H 'Sec-Fetch-Mode: cors' \
# -H 'Sec-Fetch-Site: same-origin' \
# -H 'TE: trailers \
# --data-raw '{
#   "cmd": "request.post",
#   "url":"https://chat.openai.com/backend-api/conversation",
#   "postData": "{\"action\":\"next\",\"messages\":[{\"id\":\"ede59e1f-ba84-4929-8210-48170a234b13\",\"role\":\"user\",\"content\":{\"content_type\":\"text\",\"parts\":[\"ss\"]}}],\"conversation_id\":\"2bd2d005-64e9-4e44-9d5e-4eee70e03721\",\"parent_message_id\":\"edfd6a8a-a2ff-42c1-902b-5563a266babe\",\"model\":\"text-davinci-002-render\"}",
#   "maxTimeout": 60000
# }'


# curl -L -X POST 'http://localhost:8191/v1' \
# -H 'Host: chat.openai.com' \
# -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0' \
# -H 'Accept: text/event-stream' \
# -H 'Accept-Language: en-US,en;q=0.5' \
# -H 'Accept-Encoding: gzip, deflate, br' \
# -H 'Referer: https://chat.openai.com/chat' \
# -H 'Content-Type: application/json' \
# -H 'X-OpenAI-Assistant-App-Id: ' \
# -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MTIyMzkyOSwiZXhwIjoxNjcxODI4NzI5LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ' \
# -H 'Origin: https://chat.openai.com' \
# -H 'Alt-Used: chat.openai.com' \
# -H 'Connection: keep-alive' \
# -H 'Cookie: _ga=GA1.2.276779431.1670925280; cf_clearance=6BP.WNcvx_8u7.AybziVpxpdCaKhA3OGsumcJEEKoo0-1671659424-0-1-ea1b3719.7f8f7cfc.570e39dd-250; intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..p8PKQtDmmOHBepGK.jkcaofFIIDCycWOhebpPOVMKFthaokuiXKvI3d2e_iSfbX7_VmA67alz5EBGTu99jC4he-evcHEuounqHlpdVT1lbKIhJncfL5vPF8Y-G3x4847_GmnIh5yCjLe7JdC-c2nnVrVPBSsvGnEMcoj6kbHqa8Gw34Yn1NpBKXIjhkSFu-M1C9RZSejdAuJym_VLQJgm4fLibElP6sMzQlKArKhs2pwv9dd_aOCD22hFLtbyX5O4PJ2nLZJPpgIAsfaojKDO6m4bvLBMeJF_81hrDUmn5roACbP7x_NyHJ4-pvp8EUelmz8OZnLivIitA2HCX2M0zXkqSMWbjGu4Kraf5uHhPNhDX9e2uU5jRGji8EEAyNHUSRGf5_b2ViZt6NQs4cxD6nXWBxNq5ey_lKOeHfv04SMvq8fBIb2s_78hk70prL84HYKtMKdLKC2tFccN8tNspZfVO9_NeKHLeIhElx2BwmlIofrYaJgNed4WpoTyJXsnLUEXU5Mqli4KgVKnB5-GuM3LMj2HeVGEtH0RKRkRdAH0hwlAHIyv2Uksb2sIOu5nXT77tjaUo6Q6CVJmr2Rd3oVe3XW8WfxFJS4jGR45ccACtruWMm9aOY9B2UZ_UYVmxt2ruJ3UQq6mYQWHV_v53IbpgV2ulChPvBd6X3IEA3sbL6HJpQStp6ylIgJm2RR9pywVfvL3KpzMz8puZRuMCtzG7uCgoEyVe2dMh2n3dtM5P7ynJ4Iwp8Gw1X6ovTnMUMEnAJtioDdM4c4RIvE6Ox6dsOQ0yMTdWmwocXWd-XjcHhiF-KqqQlS92wgpb6WcnZo71uFHNZdgNVQxyuezHciDhE8bX_6VqTjySq1vBbnARURIKA8rQEdhlVVcp-uA9jnt1m5s2AVy-aq_3TphRqAAB7hkKKkHVC7WEMxOJdYYNMl8zqlgz8IrgDYjyKttvckYYi1GZ-ni2uFpu4UMAyEFBfIBaN9su_jKK-DLWbvTZ-nbXVMCyB6leeIuNGtxbbbqY7ntSbc7zcgzk2MB38YJN04dhdNbF_vKrMZTfxUTqUrqVvfzkWJQqZULglDynZHcItVMLqpKfZLMBqszsvn1_O5tr5qsf3lgON2uyP3hDqaUeITKUGKqZQaTOivHd_qTAk24p0RNxHY7mZJSFPLd-w7dJyfjS0zERvYIZQgWuasFEnWE8vGRPvuViZPRceeEbJrpcEkQXOUzdLWtKqsjZOnW78bWR8xftnsbRn17ubowSrRLr1sbruiIceuN1X1X1Wm8tX2lz2w-eQFBXq9kej11EJXkOwcdpnkf9Rm0Zs-S6L8sVCo3X3oDmdKlBpdyD7yG8OeRns_Ta4_OIbBO8XRxrtobMm5uXBpMbMyAk1bGh2y3_7H4bj49nq6OzZxWr1y3Wwl8_AwaKoIzufO0heLAcdv_s-wSWA0IXGG1cNFAf6OKrqhr4-8DRNxAhBBAKXav2_URwwBpx0eD7qNcXNWxLsz1qOz2BY9Wl9XHyhAX6zBRm_V9eCCNWn-AIWYvlblO7eCv2frz1yzScsQwQVXqSD5VEiI6ShIzfje89EdyapzbGG94Xv1Hmx-VdSb7kubiA_MJfH8xO8qbPJuVGc1T6Q6-MFRzqgtjHZQp_pxkyW-c9ccgmRUwXbWENP6DDv5Jno1p2EEazlwRh9_uCkdf0c_rIKJYeZhklVN9ThBmEH8l2sdu8ATuuDPexqfXk9CwztgQbjfDp2_Bh-3QSwDqho0HiaaqUghAm8dc3gb1uB863Px_tkm-yhjbiuBWqGHi0JlcVfZAjDKhZFq51pR5-eUcThsjsZQrjc2zAlwuTnqNMwp5pO5PudRH0SlwWI1g9GJolb0mBwnzmlJC0w_tTosa12TfyfmOW3Kh1WGAg2eg57fzC3o6dkrXYLQm1yJ1YRn1lkuntZnD6AYiVg9tt12GD4WBHG3ssh0slcMhUpWxZGkdssD9GaMs3Rm-IJkABBrlZzknpEoH3iJ1ObqXFz0ebhLbLRaLllDvxEZe-DF2_J735hTNUNGVAXPBF_bTOvqUamfDmt-ZKuYPBEbRwXj3xYFCGARduFP1ByHvnYGqeG9Vrql6qtbd6gHb6YIpreLfcqTxeiEewgObTF_7xwQvgSf6a3Gs2CC1xDevxrR2MErN5T8I6oxKmMjKwycE1kIRue22dKuCA3hNppcBvx-BZNlKXKTo9z2JCUqUlFoco1pixzu7YEsTVu6DYG6FhycwiY5RkWlj1Zzn6HDJKXiKXnoLm1XfO8pGdQB5LW7sTuFmErzKQUYH-n2s.kttDsf_NO7HWWXbYVVyQPg; __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; _gid=GA1.2.1218786756.1671659418; __cf_bm=xS3qzXjMhAZlw2I_U4iViJHo5JL9lsZqRXTaeGA8Nes-1671659425-0-AaUb1Zx4II5Y40Xr6grbI+uak1rb0uAlNqpB0JR6Dv4bO5ml2CfcYaXPkn/4JapGQCpwkwaXRAF5rnl0VCSvxnMPpkVo1fJYxnWvAbYjjvCDXiPtAPcOy2/Gs+VfdCG6f3Wo+0/ja7xhuL1NB3Hn5YuVzGETWRC0IF7FMHiCVKrH/YzI+Mcj29xGV0FRLsYSqA==' \
# -H 'Sec-Fetch-Dest: empty' \
# -H 'Sec-Fetch-Mode: cors' \
# -H 'Sec-Fetch-Site: same-origin' \
# -H 'TE: trailers' \
# --data-raw '{
#   "cmd": "request.post",
#   "url":"https://chat.openai.com/backend-api/conversation",
#   "postData": "{\"action\":\"next\",\"messages\":[{\"id\":\"ede59e1f-ba84-4929-8210-48170a234b13\",\"role\":\"user\",\"content\":{\"content_type\":\"text\",\"parts\":[\"ss\"]}}],\"conversation_id\":\"2bd2d005-64e9-4e44-9d5e-4eee70e03721\",\"parent_message_id\":\"edfd6a8a-a2ff-42c1-902b-5563a266babe\",\"model\":\"text-davinci-002-render\"}",
#   "maxTimeout": 60000
# }'


# import selenium
from cipherAdapters import CipherAdapter
import payloads

# s = requests.session()
# s.mount('https://chat.openai.com/', CipherAdapter())
# s.headers = OrderedDict()

# s.headers["Host"] = "chat.openai.com"
# s.headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
# s.headers["Accept"] = "text/event-stream"
# s.headers["Accept-Language"] = "en-US,en;q=0.5"
# s.headers["Accept-Encoding"] = "gzip, deflate, br"
# s.headers["Referer"] = "https://chat.openai.com/chat"
# s.headers["Content-Type"] = "application/json"
# s.headers["X-OpenAI-Assistant-App-Id"] = ""
# s.headers["Authorization"] = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtYXJrYXMudmllbGF2aWNpdXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJMVCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItZnVra2hrZWpXVG9lb1F5MUJub1B6b3JUIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjYyMzI1MjUxNjU2NjYzNTU1NCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MTIyMzkyOSwiZXhwIjoxNjcxODI4NzI5LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.kNAVnuQ6R73Nqg3oUZ_6WmUtCLwV8bf2gAxTzesJZv4aIdMESZvC6bEm9PJeoYb4tCR_MBxWMZThtzhu3673Mf6czmSw_T49wPjz-TOLPTiOBUbIvL1FjO8v86MTC3B_jXZgUi-0Pn2YPS6QBrH4YYP-obEovEKiDhI3Mm_hNG_A7RTqm7dI2BKWpqKXbySxCOjSqqjdDr7tsVDSWKXvhQUfO_Oie_gYUhvNsAIdSYNDOOhM7aTuc7dYZAHmfPZlIoX4_y3M6eFj3ef6tkXf5NMRD32oq-wrl127RwQpPSZXY7Jh62-xSquWZZVbWFc1z8d2sFESeAr8DC4UfDu8jQ"
# s.headers["Content-Length"] = "233"
# s.headers["Origin"] = "https://chat.openai.com"
# s.headers["Alt-Used"] = "chat.openai.com"
# s.headers["Connection"] = "keep-alive"
# s.headers["Cookie"] = "ga=GA1.2.276779431.1670925280; cf_clearance=ChQ7Td.NxJlvhIv.3t.QRsO2zXwjy4EOg5kgQhOqYBo-1671727779-0-1-ea1b3719.7f8f7cfc.570e39dd-160; intercom-session-dgkjq2bp=WFJudkNJODdIWFExTkFZb0oxekxVM25kNmFFcXh3TUREV2oxNS82bU1naGlxS3JHUWI4a29iRGpueUVXSlpMVS0teEt0b3V4OHprUUJpKzk2K3E2TUoydz09--f298ba6b7fe13393a442fbda77610b361451a72a; intercom-device-id-dgkjq2bp=5c42ddb6-551b-4733-b2fc-479cff7e58d8; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..O72y6lRHg9nTQbgK.rsPzyz6PKslYMAfPWF8bu1cl6F6O3BtM4po9gnGvfMh10klaSPvkwZ7e8KMRfWW-dnUt8cZaV6fTqgBym5fyEIkKEwihHy_xLbUEcsFHi4ZYYY2B3DmGM5zdkl0mtdmSKtjNqhbgZvPqTJawRNuiRk1t94RCHsmyrDgIc7fS9XLcHIlxIQsDPdyHC7qwIOu2yRFhQyFbC0R5KgYyw7-zwQ41EkXK-jUDzr7klsGMKei6WQjs2XLYzn37MpUdMKHdJJmp14U-31x-bNZRdLkGN5fL9GnH3LP0nMsBmsf2qqU7xVDWw5XYjOLL9kGKYghNVi_pjn_BP6K2kjkLFcEfOnYjqA2WWXqaCVY1pmWDEJgDyZcdem-nXWoorr6-xPXUYcFmdNsL6QJdvPWUkpq-KDst5_CP8Y5VwODtViXEVVg5ZdRX7695idt0AGbwMFvX8ziyJJJV2q_Sdna_7USHiVzqubn1299lpyzSdsbCX1YCk59RV30yeGR2q7Ip3V3zYKiVE7Mh35uUKw4yS2abAcEfFufjTfczUEDFXEPImH6ueIm07IYoOms7c4NeqQcnGrgjIjNcf2s3-LLJR721xFPIzv5uuEZpf27IBPqkaxJXQ_9hFnmyJRVf6xRbrZi7sTILSGalQZULsslZbhb1U2KDjC-OtBztfvqU_zRdCoPMutftN-_nRXXPwwXV2982hXtAiVkx3UnEp4GGpNtgFwwg5xsBOLl6IlR9as-3spqUjOqJJv5D7Qm2WGMZsl7FRE27D8Fd6KM9Cu0KK099QkJyR_9G_TdVGyJ-1H8S4rJDvyWbT27GBUrIu2nH4nIXPnUTXDQei0nd5tSWkcnqpzG1htYALzNCfOXy_luyAvJmgYQDt6VDnY99EYPxQwYZXOcubnRl1Su1pZ9Ef2L3zI_lqNtWz5k_YtG0Ajg4wOM6Z4r37kEFaOGuc8xg3Y8JHSiD-5jcc2wCfIosNEwYTF24B15q7uF4cmFH7Zl0hetu_rjmIgSncJH0HMvQbPIM_pjKLxZkI-9IruzqeFnkxrSHX-Mm4bbbkPt1boaa0VGfq0r_LpDSgRZXI7CIIp6_pps5VQhHy3nrq1TBezFEakdLKkmT51E_ao50BuD_NGhGynVwM1bROipQIINeJUL7VGDLxx240W2VDbisXpd90FRd9NlEdzXjmB3wK5Cy_mkyxTfmTdSadu04_i3w8ILeKUCjTNztMePF_rdXG5xQqAYznpb9t1H9Xvf-ibvGZkx-8eLke0fcApo-Azc061Z0Q2B_oJ1qkSgdUN1lTQDe5Y2IE604UrMT4lAXQZPLYDk4Xy19eJ8j6nXVImNSYfdi4EK0GKNDh8qrWkXgpNCk1o8Hg9llN2jDk5ofFzF7cKxo447tSCJFYsRy6ujja7eUmn9mT7Ml7UCAtdCbZnEOtSGWgGoNAxTqYSNCjjUPe9v0hx7LTqRrjo5Wte6E2QTti1FTFmH3un3CKCaZxc7o9VGS00rAcpe7fWIXXP10lfVuonx_tlcH80ZFenzdmgMpqSHR7-Ay9Z6dcagSaK_i0tKYdOAd3bQFXjzuf7nFjDNBGs0suEW33FotRk4exD5lw8o6LXYcdpknG1g-fTnf9KxQcdPNh7ulqqmQ9USvGmDo8gpBvEnYmlkJn74J79aD5JU6Z-osFbTYeOTWxXnXzvJNotmKwNyLtFxMqBo3HO6_iR_vv-JRtK9fFqGqznv2rqwKKH167T-eXwRPIHxGVH_QjHGI_5LVCAKBvlr18bsVJTbJoyfV44BK4s1jOj08BAQFw7L1aAa3hTUA1SsZnB98js3lUTaDhvNusVzPvR4wI3LMsw6qg42d9DRNYQGtskFFAV9GQPdLIar3d75b3PGClx5J5pqoZ9bbYshbDkFR1bVo4uocOvVRRHfpxl_H9s47JFqlSN2xKGCYbih1dk1qwungNogHz6f-jgz01oREW4j5_jpICKAzMOjWEf-xt3p5b0DNNM-BOrLtsGEuRotTFM4AoY-nktezB9ulK68FMmSA9UBQwgQnTSf3EQckP_-g5GywGlxTxfkLaG0p_Cvlx5IPaO5os9_AjmcC7g7tLaISzg_nwxqC9lOCgwopNC29vIyENCYLRf-z1BtKZHybFHWFhVe7JRlJexxfSLLd3WytCaPNfjJ1TwioBdpAk6NImRhp48XGVN77l1whhrKTAuu2-jhiDu3lAtDDzb7yaFNT3KrnSXEHAUphcq8pz8XHcGuKA8BiTaGZPQBQuLMJpHSms-KY76HMeHK4HAwLvHPEJMt4.MiYkkn-TvXPC8sxP7EeBBg; __Host-next-auth.csrf-token=ae2da62f2c18cc56ae3774e8e6d3941cba92dee2b9c6f636e1378e6a60b2f172%7Ca3facbcc0fa98177e9eaa9921b7e3c4618a8fe8a50d989b3c0f1d1f02a619a1f; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; _cfuvid=kZCoZC2zxGLpu4OZFhqgS.pJjG63PFV0bJLTsWR3UBw-1671527691263-0-604800000; _gid=GA1.2.1218786756.1671659418; __cf_bm=if03zIJqaBVFWS9hPSdCZIJol7skKQsivY2qds7oY1g-1671727780-0-AS0IMKd6Pi/pQfOXNtNz7BMpOW7TMpKZKe17EBfas4CLIUjXr9hlsRZTzSwMgC0QS/DjENNfNUM+JK+R3TryDKjlQVsbf5uemi+/gdviNLqJCUy24XG6YiGxR0l17EkxQLyDwmiuQdr5zQN2m/ZK4PmjIa0pvXUckxioEQkg9bk6K2W+YEzqdXqab4wDAOIjxA==XX"
# s.headers["Sec-Fetch-Dest"] = "empty"
# s.headers["Sec-Fetch-Mode"] = "cors"
# s.headers["Sec-Fetch-Site"] = "same-origin"
# s.headers["TE"] = "trailers"

# print(s.post(host_message, data=data_payload).content)


class ChatGPTSession():

    def __initializeSession(self):
        self.session = requests.session()
        self.session.mount("https://{host}/".format(host=payloads.OPENAI_HOST), CipherAdapter())

    def __getAuthToken(self):
        self.session.headers = payloads.generateSessionHeadersPayload(self.clearance_token, self.session_token)
        response = self.session.get(payloads.SESSION_API)

        if response.status_code == 200:
            # everything worked out, continue
            print(response.json())
            return response.content
        elif response.status_code == 403:

            # cloudflare finger print worked out
            return None

        else:
            raise Exception("Unknown status code on session creation: {status}".format(response.status_code))

    def __init__(self, session_token, clearance_token):

        # Initialization steps:
        self.session_token = session_token
        self.clearance_token = clearance_token
        self.__initializeSession()

        # Safety checks steps:

        if self.session == None:
            raise Exception("Failed to initialize Requests session with custom ciphers")

        if self.session_token == None:
            raise Exception("Session token is not provided")

        if self.clearance_token == None:
            raise Exception("Clearance token is not provided")

        self.bearerToken = self.__getAuthToken()

        if self.bearerToken == None:
            raise Exception(
                "Session / clearance token is incorrect (something may changed in their api)")

    def create_convo(self):
        return ChatConversation(self)


class ChatConversation():
    def __init__(self, chatgptsession):
        pass



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
