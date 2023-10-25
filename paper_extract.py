import os
import re
import nltk
import sys
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def is_quote_sentence(sentence):
    pattern1 = r"\d{4}"
    matches1 = re.findall(pattern1, sentence)
    for matches in matches1:
        if int(matches) > 1899 or int(matches) < 2024:
            return True
    return False
   
def is_quote_sentence_(sentence):
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

    pattern12 = r"\(e\.g\.,\s.*?\)"
    matches12 = re.findall(pattern12, sentence)

    pattern13 = r"\(see\s+e\.g\.,\s+[A-Za-z\s\-&]+,\s+\d+\)"
    matches13 = re.findall(pattern13, sentence)

    pattern14 = r"\(see\s+[A-Za-z\s,&]+\,\s+\d+[a-z]*;\s+\d+[a-z]*\)"
    matches14 = re.findall(pattern14, sentence)

    pattern15 = r"\(see\s+e\.g\.,\s+[A-Za-z\s,&-]+\,\s+\d+[a-z]*;?\s*(also see)?\s*[A-Za-z\s,&-]+\,\s+\d+\)"
    matches15 = re.findall(pattern15, sentence)

    pattern16 = r"\(see\s+[A-Za-z\s,&-]+\,\s.*?\)"
    matches16 = re.findall(pattern16, sentence)

    pattern17 = r"\(see,?\s.*?\)"
    matches17 = re.findall(pattern17, sentence)

    pattern18 = r"et al \(\d{4}\)"
    matches18 = re.findall(pattern18, sentence)

    pattern19 = r"\(i\.e\.,[^)]+\)"
    matches19 = re.findall(pattern19, sentence)

    pattern20 = r"\(\d{4}[a-z]?\)"
    matches20 = re.findall(pattern20, sentence)

    pattern21 = r"\([A-Za-z]+\,\s+\d{4}[a-z]?\)"
    matches21 = re.findall(pattern21, sentence)

    if len(matches1) != 0 or len(matches2) != 0 or len(matches3) != 0 or len(matches4) != 0 \
            or len(matches5) != 0 or len(matches6) != 0 or len(matches7) != 0 or len(matches8) != 0 \
                or len(matches9) != 0 or len(matches10) != 0 or len(matches11) != 0 or len(matches12) != 0 \
                    or len(matches13) != 0 or len(matches14) != 0 or len(matches15) != 0 or len(matches16) != 0\
                        or len(matches17) != 0 or len(matches18) != 0 or len(matches19) != 0 or len(matches20) != 0 or len(matches21) != 0:
        return True
    else:
        return False


# 输入文件夹路径
input_folder = 'input_txt'
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
# 输出文件夹路径
output_folder = 'output_txt'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# 遍历输入文件夹中的所有txt文件
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        # 打开输入文件
        with open(input_path, 'r', encoding='utf-8') as input_file:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                content = input_file.read()
                # 定义一个特殊标记，用于替换引用格式
                # special_marker = "SPECIAL_MARKER"
                # # 将引用格式替换为特殊标记
                # text_with_marker = re.sub(r'\(.*[\n]*.*\)', special_marker, content)
                chinese_instance_list = sent_tokenize(content)
                # # 还原引用格式
                # if len(text_with_marker) == len(chinese_instance_list):
                #     for i, sentence in enumerate(chinese_instance_list):
                #         for j, text in enumerate(text_with_marker):
                #             chinese_instance_list[i] = chinese_instance_list.replace(special_marker, text)
                # else:
                #     print("标记出错")
                num = 0
                i = 0
                j = 0
                for sentence in chinese_instance_list:                
                    if "Introduction\n" in sentence or "INTRODUCTION/n" in sentence:
                        num += 1
                        print("----------------Run from Introduction----------------")
                    if num > 0: 
                        print(num)
                        # if num >= 0:
                        #     print(sentence)
                        #     input()
                
                        flag = 0
                        for i in ['References\n', 'references\n', 'Reference\n', 'reference\n', 'REFERENCE\n', 'REFERENCES\n']:
                            if str(i) in sentence:
                                flag = 1
                                print('检查到reference,结束程序')
                        if flag == 1:
                            flag = 0
                            break
                                # sys.exit()
                        sentence = re.sub("[\n]", "", sentence)
                        print(sentence)

                        #修正第一句
                        if i==0 and sentence.endswith('(cf.') or sentence.endswith('et al.') or sentence.endswith('pp.') or sentence.endswith('e.g.'):
                            output_file.write(str(sentence) + ' ')
                            i = 1
                            continue
                        #修正中
                        elif i==1 and sentence.endswith('(cf.') or sentence.endswith('et al.') or sentence.endswith('pp.') or sentence.endswith('e.g.'):
                            output_file.write(str(sentence) + ' ')
                            i = 1
                            continue
                        #修正最后一句
                        if i == 1 and (sentence.endswith('(cf.') or sentence.endswith('et al.') or sentence.endswith('pp.') or sentence.endswith('e.g.'))==False:
                            output_file.write(str(sentence))
                            output_file.write("\n")
                            output_file.write("\n")
                            i = 0
                            print("修正完成")
                            continue

                        pattern1 = r"\d{4}"
                        matches1 = re.findall(pattern1, sentence)

                        pattern2 = r"http://[^\s]+"
                        matches2 = re.findall(pattern2, sentence)

                        pattern3 = r"\d+ \(\d+\)"
                        matches3 = re.findall(pattern3, sentence)
                        if len(matches2) != 0 or len(matches3) != 0:
                            continue

                        for matches in matches1:
                            if int(matches) > 1839 and int(matches) < 2024:
                                j += 1
                                output_file.write(str(j) + "-" + str(num) + ":" + str(sentence))
                                output_file.write("\n")
                                output_file.write("\n")
                                print(sentence)
                                # if num > 250:
                                #     print(matches1)
                                #     input()
                                break
                        num += 1                       
                        # input()
                        # if is_quote_sentence(sentence):
                        
                        #     output_file.write(str(sentence))
                        #     output_file.write("\n")
                        #     output_file.write("\n")
                        #     print(sentence)
                        #     # input()

# 完成任务
print('引用句子提取完成！')

