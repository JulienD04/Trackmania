import sys
sys.path.append("class_TMCharacter.py")
from class_TMCharacter import TMCharacter


class TMString:

    def __init__(self, p_string: str):
        self.string: str = p_string
        self.string_info: list[TMCharacter] = [TMCharacter(character) for character in p_string]
        self.output_unclean = self.reset_output_unclean()

    def insert_character(self, index: int, character: str):
        if 0 <= index <= len(self) and len(character) == 1:
            if index == 0:
                self.string_info.insert(index, TMCharacter(character))
            else:
                parent = self.string_info[index - 1]
                tm_character: TMCharacter = TMCharacter(character)
                tm_character.copy_styling(parent)
                self.string_info.insert(index, tm_character)

        self.reset_output()

    def append_character(self, character: str):
        if len(self.string_info) == 0:
            self.string_info.append(TMCharacter(character))
        else:
            parent = self.string_info[-1]
            tm_character: TMCharacter = TMCharacter(character)
            tm_character.copy_styling(parent)
            self.string_info.append(tm_character)

        self.reset_output()

    def reset_all(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].reset_all.value = True

            self.reset_output()

    def reset_color(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].reset_color.value = True

            self.reset_output()

    def reset_width(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].reset_width.value = True

            self.reset_output()

    def bold(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].bold.value = True

            self.reset_output()

    def italic(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].italic.value = True

            self.reset_output()

    def wide(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].wide.value = True

            self.reset_output()

    def narrow(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].narrow.value = True

            self.reset_output()

    def uppercase(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].uppercase.value = True

            self.reset_output()

    def shadow(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].shadow.value = True

            self.reset_output()

    def link(self, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].link.value = True

            self.reset_output()

    def color(self, value: str, start_index: int = 0, end_index: int | None = None):
        self_len = len(self)
        if end_index is None:
            end_index = self_len
        if 0 <= start_index <= end_index <= self_len:
            for index in range(start_index, end_index):
                self.string_info[index].color = value

            self.reset_output()

    def reset_output(self):
        string = ""
        for index in range(len(self.string_info)):
            string += self.string_info[index].rep
            self.string_info[index].output = self.string_info[index].character_output()

        self.string = string
        self.output_unclean = self.reset_output_unclean()

    def reset_output_unclean(self) -> str:
        return "".join([character.output for character in self.string_info])

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    @staticmethod
    def _main():
        string = "te$op oupsi"
        tm_string = TMString(string)
        tm_string.bold()
        tm_string.shadow(6, 9)
        print(tm_string.output_unclean)


if __name__ == '__main__':
    TMString._main()
