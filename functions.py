from infofunctions import *

from progress.bar import IncrementalBar

def sendReaction_(params : dict) -> int:
        try:
            sent = me.messages.sendReaction(
                    peer_id=params['peer_id'],
                    cmid=params['cmid'],
                    reaction_id=params['reaction_id']
                    )
            return sent
        except Exception as e:
             return -1


def deleteReaction_(params : dict) -> int:
    try:
        deleted = me.messages.deleteReaction(
                peer_id=params['peer_id'],
                cmid=params['cmid'] 
                )
        return deleted
    except Exception as e:
             return -1


def Reactions(peer_id : int, msg_count : int, remove : bool):
    bar = IncrementalBar("Messages", max = msg_count)

    params = getChatParams(peer_id)
    sent_total = 0
    while msg_count:
        sent_of_20 = 0
        if (sent_total % 20 == 0 and sent_total != 0):
            time.sleep(20)

        if (remove): sent = deleteReaction_(params)
        else:        sent = sendReaction_(params)

        if (sent):
            bar.next()
            sent_total += 1
            sent_of_20 += 1

        msg_count -= 1
        params['cmid'] -= 1
        params['reaction_id'] = random.randint(1, 12)

    bar.finish()
    print(f"\nDONE - Total {sent_total} reactions sent")
            
        
def getChatParams(peer_id : int, last_cmid = 0) -> dict:
        if (peer_id < 1_000):
            peer_id += 2_000_000_000

        chat_data = me.messages.getConversationsById(peer_ids=peer_id)

        if (last_cmid == 0):
            last_cmid = chat_data['items'][0]['last_conversation_message_id']

        params = {
            'peer_id': peer_id, 
            'cmid': last_cmid, 
            'reaction_id': 1
            }
        
        return params

