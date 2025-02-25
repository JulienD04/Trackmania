import sys
sys.path.append("class_TMStyleParam.py")
from class_TMStyleParam import TMStyleParam


class TMCharacter:

    def __init__(self, p_rep: str = "", p_color: str = "$g", p_reset_all: bool = False, p_reset_color: bool = False,
                 p_reset_width: bool = False, p_bold: bool = False, p_italic: bool = False, p_wide: bool = False,
                 p_narrow: bool = False, p_uppercase: bool = False, p_shadow: bool = False, p_link: bool = False):
        self.reset_all: TMStyleParam = TMStyleParam(p_reset_all, "$z")
        self.reset_color: TMStyleParam = TMStyleParam(p_reset_color, "$g")
        self.reset_width: TMStyleParam = TMStyleParam(p_reset_width, "$m")
        self.bold: TMStyleParam = TMStyleParam(p_bold, "$o")
        self.italic: TMStyleParam = TMStyleParam(p_italic, "$i")
        self.wide: TMStyleParam = TMStyleParam(p_wide, "$w")
        self.narrow: TMStyleParam = TMStyleParam(p_narrow, "$n")
        self.uppercase: TMStyleParam = TMStyleParam(p_uppercase, "$t")
        self.shadow: TMStyleParam = TMStyleParam(p_shadow, "$s")
        self.link: TMStyleParam = TMStyleParam(p_link, "$l")

        self.color = p_color
        self.rep = p_rep if p_rep != "$" else "$$"
        self.output = self.character_output()

    def character_output(self):
        """
        Function to create the output of a single character's styling
        :return: The string output of the character with the styling implemented
        """
        output_string = ""
        output_string += self.reset_all.result_bool_param()
        output_string += self.reset_color.result_bool_param()
        output_string += self.reset_width.result_bool_param()
        output_string += self.bold.result_bool_param()
        output_string += self.italic.result_bool_param()
        output_string += self.wide.result_bool_param()
        output_string += self.narrow.result_bool_param()
        output_string += self.uppercase.result_bool_param()
        output_string += self.shadow.result_bool_param()
        output_string += self.link.result_bool_param()

        output_string += self.color + self.rep

        return output_string

    def copy_styling(self, other_tmcharacter):
        self.reset_all = other_tmcharacter.reset_all
        self.reset_color = other_tmcharacter.reset_color
        self.reset_width = other_tmcharacter.reset_width
        self.bold = other_tmcharacter.bold
        self.italic = other_tmcharacter.italic
        self.wide = other_tmcharacter.wide
        self.narrow = other_tmcharacter.narrow
        self.uppercase = other_tmcharacter.uppercase
        self.shadow = other_tmcharacter.shadow
        self.link = other_tmcharacter.link
        self.color = other_tmcharacter.color

    def __eq__(self, other):
        if isinstance(other, TMCharacter):
            return self.rep == other.rep
        elif isinstance(other, str):
            return self.rep == other
