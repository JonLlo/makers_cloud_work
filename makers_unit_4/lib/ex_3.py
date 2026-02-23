class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.called = False
        self.current_words = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        str = self.contents
        str = (str.split())
        #print(str)
        return len(str)
        
        

    def reading_time(self, wpm):
        word_count = self.count_words()
        minutes = round(word_count / wpm)
        return minutes
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        if self.called == False:
            print("its false") 
            self.called = True
            str = self.contents
            str = (str.split())[0:(wpm*minutes)]
            str = " ".join(str)
            print(str)
            #print(f'lalal {self.contents[0:(wpm*minutes)]}')
            return str
        else:
            self.current_words = self.current_words + wpm*minutes

            print("its true") 
            str = self.contents
            str = (str.split())[self.current_words:self.current_words + wpm*minutes ]
            str = " ".join(str)
            self.contents = str
            print(str)
            return str




            
    



       



diaryEntry = DiaryEntry("Monday", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twentyone twentytwo twentythree twentyfour twentyfive twentysix twentyseven twentyeight twentynine thirty thirtyone thirtytwo thirtythree thirtyfour thirtyfive thirtysix thirtyseven thirtyeight thirtynine forty fortyone fortytwo fortythree fortyfour fortyfive fortysix fortyseven fortyeight fortynine fifty fiftyone fiftytwo fiftythree fiftyfour fiftyfive fiftysix fiftyseven fiftyeight fiftynine sixty sixtyone sixtytwo sixtythree sixtyfour sixtyfive sixtysix sixtyseven sixtyeight sixtynine seventy seventyone seventytwo seventythree seventyfour seventyfive seventysix seventyseven seventyeight seventynine eighty eightyone eightytwo eightythree eightyfour eightyfive eightysix eightyseven eightyeight eightynine ninety ninetyone ninetytwo ninetythree ninetyfour ninetyfive ninetysix ninetyseven ninetyeight ninetynine onehundred onehundredone onehundredtwo onehundredthree onehundredfour onehundredfive onehundredsix onehundredseven onehundredeight onehundrednine onehundredten onehundredeleven onehundredtwelve onehundredthirteen onehundredfourteen onehundredfifteen onehundredsixteen onehundredseventeen onehundredeighteen onehundrednineteen onehundredtwenty onehundredtwentyone onehundredtwentytwo onehundredtwentythree onehundredtwentyfour onehundredtwentyfive onehundredtwentysix onehundredtwentyseven onehundredtwentyeight onehundredtwentynine onehundredthirty onehundredthirtyone onehundredthirtytwo onehundredthirtythree onehundredthirtyfour onehundredthirtyfive onehundredthirtysix onehundredthirtyseven onehundredthirtyeight onehundredthirtynine onehundredforty onehundredfortyone onehundredfortytwo onehundredfortythree onehundredfortyfour onehundredfortyfive onehundredfortysix onehundredfortyseven onehundredfortyeight onehundredfortynine onehundredfifty onehundredfiftyone onehundredfiftytwo onehundredfiftythree onehundredfiftyfour onehundredfiftyfive onehundredfiftysix onehundredfiftyseven onehundredfiftyeight onehundredfiftynine onehundredsixty onehundredsixtyone onehundredsixtytwo onehundredsixtythree onehundredsixtyfour onehundredsixtyfive onehundredsixtysix onehundredsixtyseven onehundredsixtyeight onehundredsixtynine onehundredseventy onehundredseventyone onehundredseventytwo onehundredseventythree onehundredseventyfour onehundredseventyfive onehundredseventysix onehundredseventyseven onehundredseventyeight onehundredseventynine onehundredeighty onehundredeightyone onehundredeightytwo onehundredeightythree onehundredeightyfour onehundredeightyfive onehundredeightysix onehundredeightyseven onehundredeightyeight onehundredeightynine onehundredninety onehundredninetyone onehundredninetytwo onehundredninetythree onehundredninetyfour onehundredninetyfive onehundredninetysix onehundredninetyseven onehundredninetyeight onehundredninetynine twohundred")
diaryEntry.count_words()
diaryEntry.reading_time(6)
diaryEntry.reading_chunk(20, 2)