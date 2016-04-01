# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box
class WordTrigger(Trigger):
    def __init__(self,word):
        self.word = word.lower()
    def isWordIn(self,text):
        modifiedText = text.lower()
        for  punct in string.punctuation:
            if punct in text:
                modifiedText = modifiedText.replace(punct, ' ')
        textList = modifiedText.split(' ')
        if self.word in textList:
            return True
        else:
            return False

# """
#    This method of TitleTrigger works but in the question it was asked that
#    we can't use __init__ method for this class instead we have to use the 
#    init method of the parent class
# """
# class TitleTrigger(WordTrigger):
#     def __init__(self,word):
#         super(TitleTrigger,self).__init__(word)
#         #print a,a.word
#     def evaluate(self,story):
#         return super(TitleTrigger,self).isWordIn(story.getTitle())
class TitleTrigger(WordTrigger):
    '''
    No need to call __init__ method if not specified the parent class __init__ would be called.
    '''
    # def init(self,word): # this is simply a method that is use to call __init__ method of super class 
    #     super(TitleTrigger,self).__init__(word)
        #print a,a.word
    def evaluate(self,story):
        return super(TitleTrigger,self).isWordIn(story.getTitle())
class SubjectTrigger(WordTrigger):
    # def init(self,word):
    #     super(SubjectTrigger,self).__init__(word)
    def evaluate(self,story):
        return super(SubjectTrigger,self).isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    # def init(self,word):
    #     super(SummaryTrigger,self).__init__(word)
    def evaluate(self,story):
        return super(SummaryTrigger,self).isWordIn(story.getSummary())

        




# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self,trigger1):
        self.trigger1 = trigger1
    def evaluate(self,story):
        return not self.trigger1.evaluate(story)
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self,story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)
# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self,trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self,story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)
# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self,word):
        self.word = word
    def evaluate(self,story):
        if (self.word in story.getSummary() or self.word in story.getTitle() or self.word in story.getSubject()):
            return True
        else:
            return False



#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    #print stories
    #print triggerlist
    filterlist = []
    for trigger in triggerlist:
        for story in stories:
            if trigger.evaluate(story):
                if story not in filterlist:
                    filterlist.append(story)
    return filterlist
