import json

with open("spans-pred-bert.txt") as bert,open("spans-pred-electra.txt") as electra,open("spans-pred-roberta.txt") as roberta, open("ensemble_vote.txt","w") as output:
    i = 0
    while True:
        bert_in = bert.readline()
        electra_in = electra.readline()
        roberta_in = roberta.readline()
        if not bert_in:
            break
        bert_in = set(json.loads(bert_in.split("\t")[1]))
        electra_in = set(json.loads(electra_in.split("\t")[1]))
        roberta_in = set(json.loads(roberta_in.split("\t")[1]))
        result1 = bert_in.intersection(electra_in)
        result2 = bert_in.intersection(roberta_in)
        result3 = electra_in.intersection(roberta_in)
        result = result1.union(result2).union(result3)
        result = list(result)
        result.sort()
        output.write(str(i)+"\t"+str(result)+"\n")
        i += 1      
