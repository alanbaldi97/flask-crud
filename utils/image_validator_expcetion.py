

class ImageValidatorException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

        self.name_field = args[0]
        self.msg = args[1]
    

    def errors(self):
        return [
            {
                "loc" : [self.name_field],
                "msg" : self.msg,
                "type": "value_error.missing"
            }
        ]