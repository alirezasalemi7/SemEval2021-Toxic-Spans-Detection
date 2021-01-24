import json

with open("spans-pred-bert.txt") as bert,open("spans-pred-electra.txt") as electra,open("spans-pred-roberta.txt") as roberta, open("ensamble-sentiment.txt","w") as output:
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
        result = bert_in.intersection(electra_in)
        result = result.intersection(roberta_in)
        result = list(result)
        result.sort()
        output.write(str(i)+"\t"+str(result)+"\n")
        i += 1      
