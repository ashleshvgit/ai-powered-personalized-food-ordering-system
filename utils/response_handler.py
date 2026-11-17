def add_message(history,role,message):
    history.append(
        {
            "role": role,
            "content": message
        })
    return history