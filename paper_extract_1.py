#目的：下载好的一篇pdf英文文献，获取全部参考文献，并提取pmid列表。

#输入一系列txt 然后把每个txt 文件中有引用的句子输出到对应名字的txt 文件中对吧

import importlib,sys
importlib.reload(sys)
# sys.setdefaultencoding('utf8') #注释
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
from pdfminer.converter import PDFPageAggregator
import os
import re
#句子分割模型
# import nltk
# print(nltk.data.path)
# # 下载nltk的句子分割模型
# nltk.download("punkt")
# # nltk.download()
# from nltk.tokenize import sent_tokenize

import nltk

# 下载nltk的句子分割模型
# nltk.download("punkt")

from nltk.tokenize import sent_tokenize


def is_complete_sentence(sentence):
    # 移除句子中的多余空格
    sentence = sentence.strip()
    
    # 判断句子是否以大写字母开头，以句号、问号或感叹号结尾
    if re.match(r'^[A-Z].*[.!?]$', sentence):
        return True
    
    # 判断句子是否以引号结尾（可能是引号内的一部分）
    if sentence.endswith('"') or sentence.endswith("'"):
        return False
    
    # 如果以上规则都不满足，可能是一个短语而不是完整句子
    return False

#打开pdf文件
path='Hyland_Jiang_2021_Delivering relevance.pdf'
fp = open(path, 'rb')
parser = PDFParser(fp)

# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
document = PDFDocument(parser)

#新建列表，读取的每行内容放进去，去除空行号
text_content = []
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            text_content.append(lt_obj.get_text())
        else:
            pass
# print(text_content)
# text_content 中每一个元素存储了一行文字
total_text = ''.join(text_content).replace("\n","")

#参考文献已写入文本中
file = open("reference.txt","w")
# p = re.compile('^[0-9]+\..*[0-9]+\.')
#[0-9]+\.\s[A-Z]+.*\.\s[0-9]{4};.*[0-9]+\.
# m = p.findall(total_text)    
# print(m) 
for i in text_content: 
    file.write(str(i))
    file.write("\n")
file.close()

num = 0   
for i in text_content:       
    #print i
    # if i.startswith("("):
    #     file.write(str(i))
    #     file.write("\n")
    # chinese_instance_list = i.split('.')
    # # 定义一个特殊标记，用于替换引用格式
    # special_marker = "SPECIAL_MARKER"
    # # 将引用格式替换为特殊标记
    # text_with_marker = re.sub(r'\(e\.g\.\s[\w\s&]+,\s\d{4}\)', special_marker, i)

    chinese_instance_list = sent_tokenize(i)
    # # 还原引用格式
    # for i, sentence in enumerate(chinese_instance_list):
    #     chinese_instance_list[i] = chinese_instance_list.replace(special_marker, "(e.g. Hutchinson & Waters, 1987)")
    j = 0
    # k = 0 
    # print(k)

        # print(matches4)
    for sentence in chinese_instance_list:
        matches = []
        
        # input()
        num += 1
        print(num)



        pattern1 = r"[A-Z][a-zA-Z]+\s\(\d{4}\)"
        matches1 = re.findall(pattern1, sentence)
        # print(matches1)
        pattern2 = r"\([\w\s&]+,\s\d{4}\)"
        matches2 = re.findall(pattern2, sentence)
        # print(matches2)
        # input()
        pattern3 = r"\([\w\s,;]+,\s\d{4}(?:;\s[\w\s,;]+,\s\d{4})*\)"
        matches3 = re.findall(pattern3, sentence)

        pattern4 = r"\w+’\s\(\d{4}\)"
        matches4 = re.findall(pattern4, sentence)

        pattern5 = r"\([\w\s,]+,\s\d{4}:\s\d+\)"
        matches5 = re.findall(pattern5, sentence)

        pattern6 = r"\([\w\s,&]+,\s\d{4}(?:;\s[\w\s,&]+,\s\d{4})*\)"
        matches6 = re.findall(pattern6, sentence)

        pattern7 = r"\w+’s\s\(\d{4}\)"
        matches7 = re.findall(pattern7, sentence)

        pattern8 = r"\(\s*e\.g\.\s*,\s*\w+\s*&\s*\w+\s*,\s*\d{4}\s*\)"
        matches8 = re.findall(pattern8, sentence)

        pattern9 = r"\(\s*e\.g\.\s*,\s*\w+\s*&\s*\w+\s*,\s*\d{4}\s*\)"
        matches9 = re.findall(pattern9, sentence)

        pattern10 = r"\(\s*[\w\s&-]+,\s*\d{4}(?:;\s*[\w\s&-]+,\s*\d{4})*\)"
        matches10 = re.findall(pattern10, sentence)

        pattern11 = r"\(see\s+e\.g\.,\s+[A-Za-z\s]+\,\s+\d+\)"
        matches11 = re.findall(pattern11, sentence)

        # if num == 193 or num == 194 or num == 195:
        #     print(sentence)
        #     input()

            
        
        # if not is_complete_sentence(sentence):
        #     k = k + 1
        #     # print(k)
        #     if k == 1:
        #         print("出现断句_开始融合")
        #         print("1.", sentence)
        #         sentences = sentence     
        #     elif k > 1:
        #         sentences = sentences + " " + sentence
        #         print(k,sentences)
        # else:
        #     if k != 0:
        #         sentences = sentences + " " + sentence
        #         print(k,". ",sentences)
        #         k = 0
            # input()


        

        if len(matches1) != 0 or len(matches2) != 0 or len(matches3) != 0 or len(matches4) != 0 \
            or len(matches5) != 0 or len(matches6) != 0 or len(matches7) != 0 or len(matches8) != 0 \
                or len(matches9) != 0 or len(matches10) != 0 or len(matches11) != 0:
        # if len(matches1) != 0:
            print(sentence)
            # if sentence.endswith("in."):
            #     file.write(str(sentence))
            #     j = 1
            # input()
            file.write(str(sentence))
            file.write("\n")
            file.write("\n")
            
        elif sentence.endswith("(e.g."):
            file.write(str(sentence))
            j = 1
        elif sentence.endswith("thrive in."):
            file.write(str(sentence))
            j = 1
        elif j == 1:
            file.write(str(sentence))
            file.write("\n")
            file.write("\n")
            j = 0
            
    
#     # chinese_dot_list = chinese_dot_list.split(' ')
#     for sentence in chinese_dot_list:
#         if 'see' in sentence:
#             print(chinese_dot_list)
#             file.write(str(i))
#             file.write("\n")
# file.close()

