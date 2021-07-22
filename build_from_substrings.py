# Task 1

class Node:
    """
    This class creates a node that stores a list of size 27 (1-27 that would correspond with the index value of alphabets
    and index 0 would be used to store the data of the trie), stores the level of the trie, index of the character being inserted
    and the parent index.

    Complexity:
    Time-Complexity = O(1) as the Node is generated instantly as it is instantiated.
    Space-Complexity = 0(n) where n is the size of the link plus other related constants.
    """
    def __init__(self,level=None,size=27,data=None,char_index=None,parent_index=None):
        self.data = data
        self.level = level
        self.link = [None] * size
        self.char_index = char_index
        self.parent_index = parent_index


class Trie:
    """
    This class instantiates a Trie that has the class Node as it's root.
    """
    def __init__(self):
        self.root = Node()

    def insert(self,key,data,char_index,parent):
        """
        This method inserts a stringo of N characters into the Trie and it's associated data at it's lowest level.
        :param key: the string value
        :param data: the data associated with the key
        :param char_index: the index of the character being inserted
        :param parent: the index of the parent node

        Complexity:
        This method has a time-complexity of O(n) where n is the length of the key.

        """
        # current is initialised to self.root
        current = self.root

        # the level of current is 0
        current_level = 0

        # this block of code, if the index in current.link is occupied, it would then go deeper else it would create a new Node
        # to be stored at the index and the level is incremented by 1
        for char in key:
            index = ord(char) - 97 + 1
            if current.link[index] is not None:
                current = current.link[index]
            else:
                current.link[index] = Node(level=current_level,char_index=char_index,parent_index=parent)
                current = current.link[index]
            current_level += 1
            char_index += 1

        # this block of code would return the data associated with the key.
        index = 0
        if current.link[index] is not None:
            current = current.link[index]
        else:
            current.link[index] = Node(level=current_level)
            current = current.link[index]
        current.data = data


    def search(self,key):
        """
        This method searches for the key and returns the data associated with the key. In this scenario, the method would
        return the index values of the substring (key) and if the substring is not present, returns a False statement
        :param key: The string being searched
        :return: The indexes of the substrings


        Complexity:
        This method has a time-complexity of O(m) where m is the length of the key.

        """
        # this variable stores the substrings that were formed to create the key
        substring = []
        # this variable stores the tuple containing the indexes to form the key
        indexes = []
        # current = self.root
        current = self.root

        counter = 0
        for char in key:
            # this variable gets the ASCII value of the string
            index = ord(char) - 97 + 1
            # if the index in current.link is not none, it means that the index matches the char value and the tuple value
            # is stored in the indexes variable
            if current.link[index] is not None:
                current = current.link[index]
                indexes.append((current.parent_index,current.char_index))
                counter += 1
            # this block is executed when the key value is not present as a suffix trie in current.link and it then traverses from self.root again
            elif self.root.link[index] is not None:
                # the latest value in indexes would be added to substring
                substring.append(indexes[-1])
                # indexes would be reset to empty
                indexes = []
                # the index values of the substring would be added
                indexes.append((self.root.link[index].parent_index,self.root.link[index].char_index))
                # current is then reset to self.root.link[index]
                current = self.root.link[index]
            else:
                # if char is not present in the Trie, then a False statement is returned
                return False
        # the last value in indexes is appended to substring
        substring.append(indexes[-1])
        return substring

def build_from_substrings(S,T):
    """
    This function creates a suffix Trie that is populated by the String S and the key T is used to build a substring from the
    suffixes present in trie.
    :param S: String populating suffix trie
    :param T: built from the suffixes of S
    :return: returns the indexes of S that were used to build T or False if a character from T is not present in S

    Complexity:
    This function has a complexity of O(N^2 + M) where N is the length of S since a nested loop is used to create the Suffix trie
    and M is the length of T where one traversal of T would result in the indexes used to create T from S.
    """
    trie = Trie()
    n = len(S)
    for i in range(n):
        substring = ""
        for j in range(i,n):
            substring += S[j]
        trie.insert(substring,(i,n-1),i,i)
    return trie.search(T)


# print(build_from_substrings("banana","naanb"))
#

