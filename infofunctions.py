import vk_api
import requests
import random
import tokens
import time

vk_session = vk_api.VkApi(token=tokens.access_token)
me = vk_session.get_api()

# получает название диалога
def getChatName(peer_id=0) -> tuple:
    if (peer_id > 2000000000):
            chat_data = me.messages.getChat(chat_id=peer_id - 2000000000)
            chat_name = (chat_data['title'], chat_data['id'])
    else:
        if (peer_id): chat_data = me.users.get(user_id=peer_id)
        else:         chat_data = me.users.get()

        chat_name = (f"{chat_data[0]['first_name']} {chat_data[0]['last_name']}", chat_data[0]['id'])
     
    return chat_name

def getChatList() -> list:
    chat_list = []
    chats = me.messages.getConversations(count=10)

    for i in range(10):
        chat = chats['items'][i]['conversation']

        chat_type = chat['peer']['type']

        if (chat_type == 'chat' or chat_type == 'user'):
            title = getChatName(chat['peer']['id'])
        else: continue

        id = chat['peer']['id']
        last_cmid = chat['last_conversation_message_id']

        chat_info = {
            "type": chat_type,
            "title" : title,
            "id": id,
            "last_cmid": last_cmid
        }

        chat_list.append(chat_info)

    return chat_list

def printChatInfo(target_chat : dict):
    chat_id = target_chat['id']
    chat_title = target_chat['title'][0]

    print(f"\nChat title = {chat_title}\nChat type = {target_chat['type']}\nChat id = {chat_id}\nLast message id = {target_chat['last_cmid']}\n")


def isMyMessage():
    pass