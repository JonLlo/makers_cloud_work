def wrap_text(s, limit):
    """
    This function allows the user to wrap simple text s (no punctuation)
    according to a character limit, as you might seen in Google docs or MS Word.
    """
    if limit < 22:
        return "limit needs to be at least 22 for this exercise"
    if max([len(x) for x in s.split()]) > limit:
        return "can't wrap as at least one word is longer than the limit"
    lines = ["-"*limit] #### debug to help us know where the line starts and wrap happens (at the limit)
    words = s.split()
    count_so_far = 0
    line_so_far = ""
    while words:
        word = words.pop(0) #### pop words from the start, not the end
        if count_so_far == 0: #### need to handle the first word on a line
            line_so_far = word
            count_so_far = len(word)
        elif len(word)+1+count_so_far <= limit:
            line_so_far += " " + word
            count_so_far += len(word) + 1
        else:
            lines.append(line_so_far)
            line_so_far = ""
            count_so_far = 0
            words = [word]+words #### add the unused word back into the list
    if line_so_far != "":
        lines.append(line_so_far)
    for line in lines:
        print(line)