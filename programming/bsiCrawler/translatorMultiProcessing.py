import json
from googletrans import Translator
import os
from multiprocessing import Pool
import re
import io
import time
import progressbar
from threading import Thread

def content_from_list(content):
    mdFilePart = ''
    for den in content:
        if (not isinstance(den, list)):
            mdFilePart += den + '\n\n'
        else:
            for li in den:
                mdFilePart += '* ' + li + '\n'
            mdFilePart += '\n\n'
    return mdFilePart + '\n\n'
urls = [
        'translate.google.com',
        'translate.google.co.kr',
        'translate.google.de',
        'translate.google.at',
        'translate.google.pl',
        'translate.google.am',
        'translate.google.ba',
        'translate.google.ae',
        'translate.google.ad',
        'translate.google.be',
        'translate.google.bf',
        'translate.google.bg',
        'translate.google.ba',
        'translate.google.bi',
        'translate.google.bj',
        'translate.google.bs',
        'translate.google.by',
        'translate.google.cm',
        'translate.google.cn',
        'translate.google.ca',
        'translate.google.cv',
        'translate.google.fr',
        'translate.google.fm',
        'translate.google.ga',
        'translate.google.ge',
        'translate.google.gg',
        'translate.google.gl',
        'translate.google.es',
        'translate.google.gy',
        'translate.google.gr',
        'translate.google.gp',
        'translate.google.gp',
        'translate.google.hr',
        'translate.google.ht',
        'translate.google.hu',
      ]

directoryContentEN = './contentEn/'
directoryContent = './content/'
directory = './content'
directoryEN = './contentEn'
fertig = False

def checkStatus(filesLenght):
    bar = progressbar.ProgressBar(maxval=filesLenght).start()
    files = os.listdir(directoryEN)
    lastFile = len(files)
    while (fertig != True):
        files = os.listdir(directoryEN)
        if(lastFile != len(files)):
            bar.update(len(files))
            lastFile = len(files)
        else:
            pass
        time.sleep(0.1)

    bar.finish()
    return


def check15k(list):
    size = 0
    for li in list:
        size += len(li)

    if size < 14999:
        return True
    else:
        False

def generateText(object):
    text = []
    for ob in object:
        if(isinstance(ob,list)):
            liList = []
            for li in ob:
                liList.append(li.text)
            text.append(liList)
        else:
            text.append(ob.text)
    return text


def translate(fileJSON):
    translator = Translator(service_urls=urls)
    filename = os.fsdecode(fileJSON)
    first = " ".join(filename.split(" ", 1)[:1])
    mdFile = ''
    if filename.endswith('.json'):
        #translate all components
        if(first == 'B'):
            test = directoryContent + fileJSON
            with io.open(test, 'r', encoding='utf-8') as f:
                jsonFile = json.load(f)

            h1DE = jsonFile['h1']
            #print(h1DE)
            descriptionDE = jsonFile['description']['content']
            recomContentDE = jsonFile['recommendations']['content']
            subHeadersDEList = jsonFile['recommendations']['subheaders']
            subheaderDEList1 = []
            for subHeader in subHeadersDEList:
                subheaderDEList1.append((subHeader['h3'],subHeader['content']))

            h1EN = translator.translate(h1DE, dest='en', src='de').text

            if(check15k(descriptionDE)):
                descriptionENObject = translator.translate(descriptionDE, dest='en', src='de')
                descriptionEn = generateText(descriptionENObject)
            else:
                descriptionEn = descriptionDE


            if (check15k(recomContentDE)):
                recomContentENObject = translator.translate(recomContentDE, dest='en', src='de')
                recomContentEN = generateText(recomContentENObject)
            else:
                recomContentEN = recomContentDE

            subheaderEN = []
            for el in subheaderDEList1:
                translateObject = []
                translateObject.append(el[0])
                translateObject.append(el[1])
                translateObjectResponse = translator.translate(translateObject, dest='en', src='de')
                subheaderEN.append((translateObjectResponse[0].text,generateText(translateObjectResponse[1])))


            mdFile += '#' + h1EN + '\n'
            mdFile += '## Description \n'
            mdFile += content_from_list(descriptionEn)

            mdFile += '## Countermeasures \n'
            mdFile += content_from_list(recomContentEN)

            for sub in subheaderEN:
                mdFile += '###' + sub[0] + '\n'
                mdFile += content_from_list(sub[1])

            #jsonFile['h1'] = h1EN
            #jsonFile['description']['content'] = descriptionEn
            #jsonFile['recommendations']['content'] = recomContentEN


            #for i in range(0,len(jsonFile ['recommendations']['subheaders'])):
             #   jsonFile['recommendations']['subheaders'][i]['h3'] = subheaderEN[i][0]
              #  jsonFile['recommendations']['subheaders'][i]['content'] = subheaderEN[i][1]

            f = open(directoryContentEN + re.sub('/','-',h1EN) + '.md', 'w')
            f.write(mdFile)
            f.close()

        #transalte all thread and counter measures
        else:
            try:
                test = directoryContent + fileJSON
                with io.open(test, 'r', encoding='utf-8') as f:
                    jsonFile = json.load(f)

                h1DE = jsonFile['h1']
                descriptionDE = jsonFile['content']

                #Workaround: maybe google translate bug --> 'G 5.24 Wiederherstellung von Nachrichten'
                first = " ".join(h1DE.split(" ", 2)[:2])
                secound = h1DE.split(" ", 2)[2]
                firstEN = translator.translate(first, dest='en', src='de').text
                secoundEN =  translator.translate(secound, dest='en', src='de').text
                h1EN = firstEN.replace(",",".") + " " + secoundEN


                if (check15k(descriptionDE)):
                    descriptionENObject = translator.translate(descriptionDE, dest='en', src='de')
                    descriptionEn = generateText(descriptionENObject)
                else:
                    descriptionEn = descriptionDE

                mdFile += '#' + h1EN + '\n'
                # mdFile += '## Description \n'
                mdFile += content_from_list(descriptionEn)
                try:
                    subHeaderDE = jsonFile['subheaders']
                    if (check15k(subHeaderDE)):
                        subHeaderENObject = translator.translate(subHeaderDE, dest='en', src='de')
                        subHeaderEN = generateText(subHeaderENObject)
                    else:
                        subHeaderEN = subHeaderDE


                    mdFile += "## Examples \n"
                    array = []
                    array.append(subHeaderEN)
                    mdFile += content_from_list(array)

                except:
                     pass
                #jsonFile['h1'] = h1EN
                #jsonFile['content'] = descriptionEn

                f = open(directoryContentEN + re.sub('/', '-', h1EN) + '.md', 'w')
                f.write(mdFile)
                f.close()
            except :
                pass
                print(fileJSON)


if __name__ == '__main__':
    files = os.listdir(directory)

    #add progressbar
    t = Thread(target=checkStatus, args=(len(files),))
    t.start()

    #start Multiprocessing
    start = time.time()
    pool = Pool()
    pool.map(translate, files)
    fertig = True
    t.join()
    print("MultiProcessing: ", time.time() - start)
    print('Finished')
