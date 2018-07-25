import scrap
from Tokenise import tokenise
from time import sleep
from POSTagging import POStagger
from POSTagging import split_tagged
from Features import feature_extraction
from Extraction import predict
from Extraction import extraction


link = "https://www.mathrubhumi.com/print-edition/kerala/udayakumar-custodial-death-case-1.3000348"
ret = scrap.scrapper(link)
sleep(1)
while ret:
    wordcount = tokenise.tokenizer()
    sleep(1)
    POStagger.postagger()
    sleep(1)
    split_tagged.splitTagged()
    sleep(1)
    dic = feature_extraction.featureExtractor(wordcount)
    sleep(1)
    predict.predict()
    sleep(1)
    extraction.extraction(dic)
    ret = 0



