import vk_api
import requests
import random
import tokens

vk_session = vk_api.VkApi(token=tokens.access_token)
me = vk_session.get_api()


def sendReaction(params : dict):
        sent = me.messages.sendReaction(
                peer_id=params['peer_id'],
                cmid=params['cmid'],
                reaction_id=params['reaction_id']
                )
        
        return sent


def deleteReaction(params : dict):
      deleted = me.messages.deleteReaction(
            peer_id=params['peer_id'],
            cmid=params['cmid'] 
            )
      
      return deleted


def getChatParams(peer_id: int, last_cmid: int):
        if peer_id < 1_000:
            peer_id += 2_000_000_000

        chat_data = me.messages.getConversationsById(peer_ids=peer_id)

        if last_cmid == 0:
            last_cmid = chat_data['items'][0]['last_conversation_message_id']

        params = {
            'peer_id': peer_id, 
            'cmid': last_cmid, 
            'reaction_id': 2
            }
        
        return params

