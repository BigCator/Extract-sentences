import re

text = "(Biber, aa\n,2006b)"

# 匹配"(Biber, 2006b)"格式的引用
references = re.findall(r'\(.*[\n]*.*\)', text)

# 输出匹配到的引用
for reference in references:
    print(reference)
