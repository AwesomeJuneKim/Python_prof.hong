# msg = ["Hello","World","Bye"]
# def show_message(msg):
#     print(msg.pop())
    
# show_message(msg)
# show_message(msg)
# show_message(msg)



def show_messages(unsend_messages, sent_messages):
    
    while unsend_messages:
        current_message=unsend_messages.pop()
        print(f"현재 메세지:{current_message}")
        sent_messages.append(current_message)
        print("message sent\n")
    print(f"현재 메세지 리스트: {unsend_messages}\n")
def send_messages(sent_messages):
    for sent_message in sent_messages:
        print(f"보낸 메세지:{sent_message}")
    print(f"보낸 메세지 리스트: {sent_messages}\n")

unsend_messages = ["Hello","World","Bye"]
sent_messages = []

show_messages(unsend_messages, sent_messages)
send_messages(sent_messages)

