class GrammarStats:
    def __init__(self):
        self.pass_count = 0

    def check(self, text):
        if text[0].isupper():
            self.pass_count = self.pass_count + 1
            return True
        else:
            return False
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
   

    def percentage_good(self):
        return self.pass_count

        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
