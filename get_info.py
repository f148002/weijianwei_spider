import pandas as pd
import re


def get_date(text):
    date = re.search(r'\d{1,2}月\d{1,2}日', text).group(0)
    return date


if __name__ == '__main__':
    df = pd.read_excel('/Users/jarod/Downloads/yiqing_yiqing_结果.xlsx', dtype='str')

    result = {'日期': ''}

    for i, r in df.iterrows():

        all_text = r['text']
        date = r['整理日期']
        result.update({'日期': date})

        all_text = all_text.replace(' ', '')
        all_text = all_text.replace('\n', '')



        if '均为境外' not in all_text:
            if '均为本土' in all_text:
                zongshu = re.search(r'新增确诊病例(\d{1,99999})例', all_text).group(0)
                jieguo = re.search(r'本土病例(（|\()(.*?.[^残])(）|\))', all_text)
                sub_jieguo = jieguo.group(2)
            else:
                temp = re.search(r'本土病例(\d{1,99999})例.[^（]*?(均在.*?)；', all_text)
                if temp:
                    zongshu = jieguo.group(1)
                    sub_jieguo = jieguo.group(2)
                else:
                    jieguo = re.search(r'本土病例(\d{1,99999})例(（|\()(.*?.[^残])(）|\))', all_text)
                    zongshu = jieguo.group(1)
                    sub_jieguo = jieguo.group(3)

            result.update({'总数': zongshu})


            if '；' in sub_jieguo:
                xxxx = re.split('；', sub_jieguo)
                for each_text in xxxx:
                    try:
                        temp_re = re.search('(.[^\d]{1,3})(\d{1,4})例', each_text)
                    except:
                        pass
                    province = temp_re.group(1)
                    number = temp_re.group(2)
                    result.update({province: number})
            else:
                if '均在' in sub_jieguo:
                    try:
                        temp_re = re.search(r'均在(.[^\d]{1,3})，?', all_text)
                    except:
                        pass
                    province = temp_re.group(1)
                    number = zongshu
                    result.update({province: number})
                else:
                    if '，' in sub_jieguo:
                        xxxx = re.split('，', sub_jieguo)
                        for each_text in xxxx:
                            temp_re = re.search('(.[^\d]{1,3})(\d{1,4})例', each_text)
                            province = temp_re.group(1)
                            number = temp_re.group(2)
                            result.update({province: number})
        else:
            zongshu = 0
            result.update({'总数': zongshu})

    print('okay')
    print(result)

    # df['日期'] = df['text'].map(get_date)
    # df['完整日期'] = df['年份'] + "年" + df['日期']
    #
    # df['整理日期'] = pd.to_datetime(df['完整日期'], format='%Y年%m月%d日')
    #
    # df.sort_values(by=['整理日期'])
    #
    # df.to_excel('/Users/jarod/Downloads/yiqing_yiqing_结果.xlsx', index=False)