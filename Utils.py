def freqs(ids):
    counts={}
    for pair in zip(ids, ids[1:]): #each adjacent pair
        counts[pair] = counts.get(pair, 0) + 1 #If Pair is not in counts, it will be added with value 0, then incremented by 1
    return counts

def merge(ids,pair,new_id): #merges the tokens of the highest pair count with a new id
    new_ids=[]
    i=0
    while i < len(ids):
        if i < len(ids)-1 and ids[i]==pair[0] and ids[i+1]==pair[1]:
            new_ids.append(new_id)
            i+=2
        else:
            new_ids.append(ids[i])
            i+=1
    return new_ids   

def create_vocab(ids,vocab_size): 
  num_merges= vocab_size - 256
  merges={}
  for i in range(num_merges):
    frequencies=freqs(ids)
    top_pair=max(frequencies, key=frequencies.get)
    merges[top_pair]=256 + i
    #print(f'Merging pair {top_pair} into new token id {256 + i}')
    ids=merge(ids, top_pair, 256 + i)
  return ids, merges