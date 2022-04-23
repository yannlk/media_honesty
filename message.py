import wiki
import rating

listen = "( (listen)) "
empty = ""


def msg(row):
    po = f"Hi! Thanks for calling me. \n\n This post is sourced from [{row[1]}](http://{row[0]}) which is known for {rating.bias_score(float(row[2]))} bias** and is " + f"{rating.reliability_score(float(row[3]))}"
    pt = f"\n\n For questions, concerns, and recommendations please visit r/media_honesty."
    if wiki.wiki(row[1])[1]:
        pf = f"\n\n {wiki.wiki(row[1])[0].replace(listen, empty)} ([Wikipedia]({wiki.wiki_unk(row[1])[2]}))"
    else:
        pf = ""

    return po + pf + pt


def n_db(domain):
    po = f"Hi! Thanks for calling me. \n\n Unfortunately, this post's source ({domain}) is not in my database. If you think it should be added, please make a post on r/media_honesty requesting this."
    pt = f"\n\n For questions, concerns, and recommendations please visit r/media_honesty."
    if wiki.wiki_unk(domain)[1]:
        pf = f"\n\n {wiki.wiki_unk(domain)[0].replace(listen, empty)} ([Wikipedia]({wiki.wiki_unk(domain)[2]}))"
    else:
        pf = ""
    return po + pf + pt



