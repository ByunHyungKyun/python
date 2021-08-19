import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

if __name__ == "__main__":
    
    # coolsms 媛쒕컻 / �뿰�룞 �럹�씠吏��뿉�꽌 諛쒓툒 諛쏆� api_key, api_secret �엯�젰
    
    api_key = "NCSIBZM5LQKKGFN9" 
    api_secret = "UK35DIQZ3TKFQBQLASEAOWGGFQHZK8N7"
    
    # # 4 params(to, from, type, text) are mandatory. must be filled
    
    params = dict() # 蹂대궡�뒗 �뙆�씪誘명꽣�뱾�쓣 dict�뿉 �떞�븘 �쟾�넚�븿 // python dict() �븿�닔
    
    params['type'] = 'sms'  # 硫붿꽭吏� ���엯 (sms, lms, mms, ata )
    params['to'] = '01033600299'  # �닔�떊�옄 踰덊샇 �엯�젰, �떎以묒쑝濡� 蹂대궡�젮硫� '01012341234, 01043214321' �쑝濡� �엯�젰
    params['from'] = '01033600299'  # 諛쒖떊�옄 踰덊샇 �엯�젰, api_key�뿉 �븷�떦�맂 �냼�쑀�옄�쓽 踰덊샇濡� �엯�젰�빐�빞 �꽦怨듭쟻�쑝濡� 吏꾪뻾�맖
    params['text'] = 'Test Message'  # 蹂대궪 �뀓�뒪�듃
    
    cool = Message(api_key, api_secret)  # apikey, secret �씤利앹쓣 嫄곗묠
    
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        
        # 蹂대궡�뒗�뜲 �꽦怨듯븯硫� 蹂대궦 媛쒖닔留뚰겮 Success Count : n
        # 蹂대궡�뒗�뜲 �떎�뙣�븯硫� 蹂대궦 媛쒖닔留뚰겮 Error Count : n
        
        if "error_list" in response:
            print("Error List : %s" % response['error_list'])
            
    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)
        sys.exit()
