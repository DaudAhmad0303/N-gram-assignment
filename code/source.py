
# -------------     Driver Program      ----------------
n_gram = []
sentences = ['John R ', ' Allen is a member of the Board of Advisors of Amida Technology and on the Board of Directors of Spark Cognition ', ' Both companies work in fields discussed in this piece ', ' ', 'We are grateful for the helpful comments of the reviewers of this paper ']
unigram = ['John', 'R', 'Allen', 'is', 'a', 'member', 'of', 'the', 'Board', 'of', 'Advisors', 'of', 'Amida', 'Technology', 'and', 'on', 'the', 'Board', 'of', 'Directors', 'of', 'Spark', 'Cognition', 'Both', 'companies', 'work', 'in', 'fields', 'discussed', 'in', 'this', 'piece', 'We', 'are', 'grateful', 'for', 'the', 'helpful', 'comments', 'of', 'the', 'reviewers', 'of', 
'this', 'paper']
# for i in range(len(sentences)):
#     temp = str(sentences[i])
#     n_gram += temp.strip().split()
# print(n_gram)
# probability = val.count(unigram)
count = 0
val = str(unigram[0])
for i in range(len(unigram)):
    if unigram[i] == val:
        count += 1
print(count)