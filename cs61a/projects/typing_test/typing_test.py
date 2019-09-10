""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"

# BEGIN Q1

def lines_from_file(path):
    text=readlines(open(path))
    return [strip(text[i]) for i in range(len(text))]

def new_sample(path,i):
    return lines_from_file(path)[i]

def analyze(sample_paragraph,typed_string,start_time,end_time):
    def helper_minute(sample_paragraph,start_time,end_time):
        length=len(typed_string)
        words=length/5
        per_minute=words/((end_time-start_time)/60)
        return per_minute
    def helper_accuracy(sample_paragraph,typed_string):
        sample_str=split(sample_paragraph)
        typed_str=split(typed_string)
        length=len(sample_str)
        #print(length)
        total=0
        counter=0
        while length!=0:
            if len(typed_str)-1<len(sample_str)-length:
                break
            if sample_str[len(sample_str)-length]==typed_str[len(sample_str)-length]:
                #print(sample_str[len(sample_paragraph)-length])
                #print(typed_str[len(sample_paragraph)-length])
                total+=1
            length=length-1
        #print(total)
        if len(typed_str)==0:
            return 0.0
        if len(typed_str)<len(sample_str):
            return (total/len(typed_str))*100
        accuracy=(total/len(sample_str))*100
        return accuracy
    return [helper_minute(sample_paragraph,start_time,end_time),helper_accuracy(sample_paragraph,typed_string)]

def pig_latin(s):
    length=len(s)
    i=0
    judge=True
    judgenum=0
    if s[0] =='a' or s[0] =='e' or s[0] =='i' or s[0] =='o' or s[0] =='u':
        judge=True
    else:
        judge=False
    if judge:
        s=s+'way'
    else:
        while length!=0:
            if s[i] =='a' or s[i] =='e' or s[i] =='i' or s[i] =='o' or s[i] =='u':
                s=s[i:]+s[:i]+'ay'
                judgenum=999
                break
            length-=1
            i+=1
    if length==0 and judgenum!=999:
        s=s+'ay'
    return s

def autocorrect(user_input,words_list,score_function):
    if user_input in words_list:
        return user_input
    else:
        return min(words_list,key=lambda x: score_function(x,user_input))

def swap_score(w1,w2):
    if not w1:
        return 0
    if not w2:
        return 0
    if w1[0]==w2[0]:
        return swap_score(w1[1:],w2[1:])
    else:
        return swap_score(w1[1:],w2[1:])+1
        


# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)
    elif word1[0]==word2[0]:
        return score_function(word1[1:],word2[1:])
    else:
        add_char = score_function(word1[0:],word2[1:])+1
        remove_char = score_function(word1[1:],word2[0:])+1
        substitute_char = score_function(word1[1:], word2[1:])+1
        return min(add_char,remove_char,substitute_char)

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(word1, word2):
	if not word1:
		return len(word2)
	if not word2:
		return len(word1)
	elif word1[0]==word2[0]:
		return score_function_accurate(word1[1:],word2[1:])
	else:
		add_char = score_function_accurate(word1[0:],word2[1:])+1
		remove_char = score_function_accurate(word1[1:],word2[0:])+1
		substitute_char = score_function_accurate(word1[1:], word2[1:])+KEY_DISTANCES[word1[0],word2[0]]
		#print(abs(KEY_DISTANCES[word1[0]]-KEY_DISTANCES[word2[0]]))
		return min(add_char,remove_char,substitute_char)
		#return substitute_char
dic = {}
#Mword1 = ''
#Mword2 = ''
#memoization = 0
lst=[]

def score_function_final(word1, word2):
	global lst, dic
	lst.append(word1)
	lst.append(word2)
	#global Mword1, Mword2, memoization
	if word1 in dic.keys():
		if dic[word1][0]==word2:
			return dic[word1][1]
	elif word2 in dic.keys():
		if dic[word2][0]==word1:
			return dic[word2][1]
	if not word1:
		#nonlocal Mword1, Mword2
		#nonlocal memoization
		#if len(lst)<2:
			#lst=['',word2]
		dic[lst[0]]=[lst[1],len(word2)]
		dic[lst[1]]=[lst[0],len(word2)]
		lst=[]
		return len(word2)
	if not word2:
		#if len(lst)<2:
			#lst=['',word1]
		#nonlocal Mword1, Mword2
		#Mword1=word1
		#Mword2=word2
		#nonlocal memoization
		#memoization = len(word1)python3
		dic[lst[0]]=[lst[1],len(word1)]
		dic[lst[1]]=[lst[0],len(word1)]
		lst=[]
		return len(word1)
	elif word1[0]==word2[0]:
		#memoization = score_function_final(word1[1:],word2[1:])
		return score_function_final(word1[1:],word2[1:])
	else:
		#Mword1=word1
		#Mword2=word2
		add_char = score_function_final(word1[0:],word2[1:])+1
		remove_char = score_function_final(word1[1:],word2[0:])+1
		substitute_char = score_function_final(word1[1:], word2[1:])+KEY_DISTANCES[word1[0],word2[0]]
		#print(abs(KEY_DISTANCES[word1[0]]-KEY_DISTANCES[word2[0]]))
		#nonlocal memoization
		#memoization = min(add_char,remove_char,substitute_char)
		#nonlocal Mword1, Mword2
		a=min(add_char,remove_char,substitute_char)
		if len(lst)<2:
			lst.append(word1)
			lst.append(word2)
		dic[lst[1]]=[lst[0],a]
		dic[lst[0]]=[lst[1],a]
		lst=[]
		return a

# END Q7-8
