from functions import *

def main():
    you = getChatName()
    print(f"Logged in as: {you[0]} (id = {you[1]})")

    chat_list = getChatList()
    print("\nChoose one conversation to spam with reactions:")
    for i in range(len(chat_list)):
        print(f"[{i}] - {chat_list[i]['title'][0]} ({chat_list[i]['type']})")

    target_chat_pos = int(input("\nEnter chat position: "))
    target_chat = chat_list[target_chat_pos]
    target_chat_id = target_chat['id']
    printChatInfo(target_chat)

    action = int(input("Do you want (1) - to send or (0) - to delete reactions: "))
    if (action == 1):
        msg_count = int(input("Enter how many msgs to react for: "))
        start = input(("\nPress ENTER to begin, '0' to exit"))

        if (start == '0'): return
        
        print("\nReacting begins... (20 sec wait after every 20 requests)")
        Reactions(target_chat_id, msg_count, False)

    elif (action == 0):
        msg_count = int(input("Enter how many reactions to remove: "))
        start = input(("\nPress ENTER to begin, (0) - to exit"))

        if (start == '0'): return
        
        print("\nDeleting begins... (20 sec wait after every 20 requests)")
        Reactions(target_chat_id, msg_count, True)

    else:
        print("Deleting Windows...")
        while True: print(random.randint(10000000), end=' ')
    

if __name__ == "__main__":
    main()