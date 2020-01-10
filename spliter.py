
import jieba.posseg as pseg
pseg.lcut('你好大白兔')


def multilingual_sent_split(texts):
    print('\nOriginal texts: ', texts)
    lingual_split_sign = {'x', 'eng'}
    final_parts = []
    sub_part = []
    cuts = pseg.lcut(texts)
    for idx in range(len(cuts) - 1):
        # 如果当前位置的词语词性和下一个词词性相同，则把当前位置上的词添加进当前的sub_part中
        if (cuts[idx].flag in lingual_split_sign and cuts[idx + 1].flag in lingual_split_sign) or (
                cuts[idx].flag not in lingual_split_sign and cuts[idx + 1].flag not in lingual_split_sign):
            sub_part.append(cuts[idx].word)
        # 否则就应该把当前的sub_part添加进final_parts中，且要新建sub_part
        else:
            sub_part.append(cuts[idx].word)
            final_parts.append(sub_part)
            sub_part = []
    # 最后一个词如果和倒数第二个词词性相同，则把最后一个词添加进当前的sub_part中
    if (cuts[-1].flag in lingual_split_sign and cuts[-2].flag in lingual_split_sign) or (
            cuts[-1].flag not in lingual_split_sign and cuts[-2].flag not in lingual_split_sign):
        sub_part.append(cuts[-1].word)
    # 最后一个词如果和倒数第二个词词性不相同，则把最后一个词作为新的sub_part添加进final_parts中
    else:
        final_parts.append([cuts[-1].word])
    if sub_part:
        final_parts.append(sub_part)
    final_strs = [''.join(_l) for _l in final_parts]
    print('Cut texts: ', final_strs)
    return final_strs


multilingual_sent_split('接着开始舞动青春的翅膀')
# Original texts:  接着开始舞动青春的翅膀
# Cut texts:  ['接着开始舞动青春的翅膀']

multilingual_sent_split('continue flapping the wing of youth')
# Original texts:  continue flapping the wing of youth
# Cut texts:  ['continue flapping the wing of youth']

multilingual_sent_split('接着开始舞动hello青春的翅膀hello')
# Original texts:  接着开始舞动hello青春的翅膀hello
# Cut texts:  ['接着开始舞动', 'hello', '青春的翅膀', 'hello']

multilingual_sent_split('RÉLICL接着동일하며开始舞动hello青春的翅膀')
# Original texts:  RÉLICL接着동일하며开始舞动hello青春的翅膀
# Cut texts:  ['RÉLICL', '接着', '동일하며', '开始舞动', 'hello', '青春的翅膀']
