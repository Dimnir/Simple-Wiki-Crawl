####  MANAGE SUBREDDITS DATA FILE  ##########
# list of subreddits in a text file
# loads data list from file, adds new
# items to list, saves the new data on file

###########  HOW TO USE  ####################
# ENTER FILE NAME TO SAVE DATA ON
# ENTER SUBS TO APPEND TO CURRENT SUBS LIST

file_name = 'sub_list.txt'
subs_to_add = []  # example = ['sub1', 'sub2', 'sub3', ...]


# DO NOT CHANGE FROM HERE
class subreddit:
    subreddits_list = []

    # saves new content to file
    def save_list(self, f_name):
        f = open(f_name, "w")
        for sub in self.subreddits_list:
            if len(sub) < 2: # if sub name empty dont save it
                pass
            else:
                f.write(sub.lower() + ", ")  # rewrite new list to file

        f.close()

    # loads data from file to self.subreddit_list
    def load_list(self, f_name):
        f = open(f_name, "r")
        self.subreddits_list = f.read()
        self.subreddits_list = self.subreddits_list.split(', ')
        f.close()

    # filters and adds new items to list and sorts the list
    def add_subs(self, subs):
        for sub in subs_to_add:
            if sub.lower() in self.subreddits_list:  # if sub already in subreddits list or empty
                pass
            else:
                self.subreddits_list.append(sub.lower())  # append new sub to file
        self.subreddits_list.sort()

    # print current subs list
    def print_list(self):
        print(self.subreddits_list)


s = subreddit()  # new obj
s.load_list(file_name)  # load data
s.add_subs(subs_to_add)  # add items
s.save_list(file_name)  # save data
print('total elements in list:', len(s.subreddits_list))  # print amount of items in list
s.print_list()  # outputs list

