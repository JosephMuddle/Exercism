def commands(binary_str):
    command_dict = {1: "jump",2: "close your eyes",3: "double blink",4: "wink"}
    handshake = [command_dict[i] for i in range(1,5) if binary_str[i] == "1"]
    return handshake[::-1] if binary_str[0] == "0" else handshake

commands("00001")