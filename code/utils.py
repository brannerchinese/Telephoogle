#! /usr/bin/env python
# utils.py
# David Prager Branner
# 20141025

import string
import difflib as D

all_punct = string.punctuation + (
        """　﹉﹊﹋﹌＿﹍﹎﹏︳︴－﹣︲﹘︱〜･，﹐︐、﹑︑､﹅﹆；﹔︔：﹕︓！﹗︕？﹖︖．﹒‥︰︙。︒｡＇＂〝〞〟（﹙︵）﹚︶［﹇］﹈｛﹛︷｝﹜︸｟｠〈︿〉﹀《︽》︾「﹁｢」﹂｣『﹃』﹄【︻】︼〔﹝︹〕﹞︺〖︗〗︘〘〙〚〛﹫＊﹡／＼﹨＆﹠＃﹟％﹪〃｀＾＋﹢＜﹤＝﹦>＞﹥￢｜￤～￨￮〄〒〓々＄﹩〇〆﹓﹧＀""")

def clean_for_edit_distance(s):
    """Convert to list and strip punctuation; if Chinese, use special rule."""
    cleaned = s.split()
    # Deal with Chinese case.
    if [s] == cleaned:
        cleaned = [i.strip(all_punct) for i in list(s)]
    # Downcase anything that can be downcased and delete empties.
    cleaned = [i.strip(string.punctuation).lower() for i in cleaned if i]
    return cleaned

def get_edit_distance(s1, s2):
    """Clean strings and return difflib.Sequencematcher ratio()."""
    sequence = D.SequenceMatcher(None,
            clean_for_edit_distance(s1),
            clean_for_edit_distance(s2))
    return sequence.ratio()
