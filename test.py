        button_details_list = [
            # text, color, command, row, column
            # put your buttons features in list.
            ["results", "#aaaeff", lambda:self.question_answer(), "1"],
            ["finish", "#ffe600", lambda:self.buttonswitch_right("default"), "1"],
        ]
        self.button_ref_list = []