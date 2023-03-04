class Error:

    type_of_errors = {
        1062: "Integrity"
    }
    
    def __init__(self, error):
        self.error = error
        self.code = self.error.orig.args[0]
        self.description = self.error.orig.args[1]

    def handle_sqlalchemy_errors(self) -> str:
        if self.code == 1062:
            index = self.description.index("for key '") 
            if index != -1:
                piece_of_error = self.description[index + 9:]
                final_index_attribute = piece_of_error.index("'")
                entity, attr = self.description[index + 9 : index + 9 + final_index_attribute].split('.')
                return f"{attr} já cadastrado!"
    