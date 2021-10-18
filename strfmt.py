class format:
    def __init__(self, text, *values):
        self.text = iter(text)
        self.values = values
        self.advance()
        self.format()

    def __repr__(self):
        return self.text

    def advance(self):
        try: self.cur_char = next(self.text)
        except StopIteration: self.cur_char = None

    def format(self):
        cur_val = 0
        formatted_str = ""

        while self.cur_char != None:
            if self.cur_char not in "%{":
                formatted_str += self.cur_char
                self.advance()
            elif self.cur_char == "%":
                self.advance()
                
                if self.cur_char == "s":
                    if type(self.values[cur_val]) != str:
                        raise Exception(f"Invalid type.\nInfo: {self.values[cur_val]} is not of type \"string\"")
                    else:
                        formatted_str += self.values[cur_val]
                        cur_val += 1
                        self.advance()
                elif self.cur_char == "d":
                    if type(self.values[cur_val]) != int:
                        raise Exception(f"Invalid type.\nInfo: {self.values[cur_val]} is not of type \"int\"")
                    else:
                        formatted_str += str(self.values[cur_val])
                        cur_val += 1
                        self.advance()
                elif self.cur_char == "l":
                    self.advance()

                    if self.cur_char != "f":
                        raise Exception(f"Type \"l{self.cur_char}\" is not a valid type")
                    else:
                        if type(self.values[cur_val]) == int:
                            formatted_str += str(float(self.values[cur_val]))
                            cur_val += 1
                            self.advance()
                        elif type(self.values[cur_val]) != float:
                            raise Exception(f"Invalid type.\nInfo: {self.values[cur_val]} is not of type \"float\"")
                        else:
                            formatted_str += str(self.values[cur_val])
                            cur_val += 1
                            self.advance()
                else:
                    raise Exception("Unrecognized type")
            
            elif self.cur_char == "{":
                self.advance()

                if self.cur_char != "}":
                    raise Exception("Failed to format string")
                else:
                    formatted_str += self.values[cur_val]
                    cur_val += 1
                    self.advance()
    
        self.text = formatted_str