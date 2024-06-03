# 定义一个发送消息的函数
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# 创建一个包含简短文本消息的列表
messages = ["Hello there!", "How are you doing?", "Python is fun!", "Have a great day!"]
# 创建一个空列表，用于存储已发送的消息
sent_messages = []

# 调用展示消息的函数来展示初始列表的消息
print("The original messages:")
show_messages(messages)

# 调用发送消息的函数
print("\nSending messages...")
send_messages(messages[:], sent_messages)  # 发送messages的副本以保留原始列表

# 打印验证消息是否正确移动
print("\nFinal lists:")
print("Original messages:")
print(messages)  # 原列表应该保持不变，因为我们传递了它的副本
print("Sent messages:")
print(sent_messages)  # 新列表应该包括所有被发送的消息
