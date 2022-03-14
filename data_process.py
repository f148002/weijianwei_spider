import pandas as pd
import re


def get_date(text):
    date = re.search(r'\d{1,2}月\d{1,2}日', text).group(0)
    return date

if __name__ == '__main__':
    df = pd.read_excel('/Users/jarod/Downloads/yiqing_yiqing.xlsx', dtype='str')

    df['日期'] = df['text'].map(get_date)
    df['完整日期'] = df['年份'] + "年" + df['日期']

    df['整理日期'] = pd.to_datetime(df['完整日期'], format='%Y年%m月%d日')

    df.sort_values(by=['整理日期'])

    df.to_excel('/Users/jarod/Downloads/yiqing_yiqing_结果.xlsx', index=False)
