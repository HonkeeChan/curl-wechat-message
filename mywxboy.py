#!/usr/bin/env python
# encoding: utf-8

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        # print msg
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            """
            {
                'content': {
                    'data': u'aa', 
                    'desc': u'aa', 
                    'type': 0, 
                    'user': {
                        'id': u'@10ac71277ce6f3c76763a1302830361c2d8215d9a95441d3742cfc4391c82b8d',  //from user id
                        'name': u'\u81ea\u5df1\u597d\u53e5'
                    }, 
                    'detail': [{'type': 'str', 'value': u'aa'}]
                }, 
                'msg_id': u'2185443169392681243', 
                'msg_type_id': 3, 
                'to_user_id': u'@9f6b3f26463c348f0b10bf6cc61a031a',  //my id
                'user': {
                    'id': u'@@9f41ee170abc31fd5f17c1c0c4f2bde3adf49b81bfa19bbdfae900547242f627', //from group user id
                    'name': u'\u6d4b\u8bd5\u7528'
                }
            }
            """
            groupUsername = msg['user']['id']
            if(usernameMap.has_key(groupUsername)):
                if(usernameMap[groupUsername][1].get() == True):
                    fromUsername = msg["content"]["user"]["id"]
                    fromUserNickname = msg["content"]["user"]["name"]
                    fromGroupId = msg["user"]["id"]
                    fromGroupName = msg["user"]["name"]
                    sendMsg = "收到你在 " +fromGroupName.encode("utf8")+" 上发的消息 " + msg['content']['data'].encode("utf8") 
                    self.send_msg_by_uid(sendMsg, fromUsername)
                    self.send_msg_by_uid(sendMsg, fromGroupId)
        

    def get_contact(self):
        print 'MyWxBot get contact'
        WXBot.get_contact(self)
        for group in self.group_list:
            usernameMap[group['UserName']] = (group['NickName'], None)
  
