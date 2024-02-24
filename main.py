from functions import *
import time

def main():
    klan_snus_id = 226  #5539 - reaction sent to: 81491 <Response [200]>
    memnie_id = 138

    params = getChatParams(klan_snus_id, 0)
    print('\nlast message id = ', params['cmid'], '\n')
    
    counter = 0
    while True:
        sent_counter = 0
        for _ in range(20):
            sent = deleteReaction(params)

            if sent:
                sent_counter += 1
            
            counter += 1
            params['cmid'] -= 1  
            params['reaction_id'] = random.randint(1, 16) 

        print(f'({counter}) {sent_counter}/{20} reactions sent | last cmid = {params['cmid']}')
        time.sleep(20)  
          

if __name__ == "__main__":
    main()