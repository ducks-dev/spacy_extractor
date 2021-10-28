import spacy
import csv
import patterns as pat

def pattern_extractor(text_extracted, pattern, nlp = spacy.blank("en"),
                      blacklist = []):
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(pattern)

    text = text_extracted[0]
    all_ents = text_extracted[1]
    doc = nlp(text)

    to_replace_ents = ["PERSON", "ADDRESS", "EMAIL", "PHONE_NUMBER"]

    for ent in doc.ents:
        if (ent.label_ in to_replace_ents and
            ent.text not in to_replace_ents and
            ent.text not in blacklist):
            text = text.replace(ent.text, ent.label_)
            all_ents += [ent.text]
    # for token in doc:
    #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #         token.shape_, token.is_alpha, token.is_stop)

    nlp.remove_pipe("entity_ruler")

    return (text, all_ents)

def extractor_wrapper(nlp, nlp_no_ner, text):
    # split rounds due to longer patterns not being detected
    # in favor of shorter ones
    round1 = pat.phone_r1 + pat.email_r1 + pat.street_r1
    round2 = pat.phone_r2 + pat.street_r2
    round3 = pat.phone_r3 + pat.street_r3
    round4 = pat.street_r4
    round5 = pat.person_r1

    pipeline_blank = [round1, round2, round3]
    pipeline_nlp = [round4]
    pipeline_nlp_ner = [round5]

    output = (text, [])
    for p in pipeline_blank:
        output = pattern_extractor(output, p)

    for p in pipeline_nlp:
       output = pattern_extractor(output, p, nlp)

    for p in pipeline_nlp_ner:
       output = pattern_extractor(output, p, nlp)

    return output

def preprocess_text(text):
    before = ["canal zone", "new hampshire", "new jersey", "new mexico",
              "north carolina",  "north dakota",  "puerto rico", "rhode island",
              "south carolina",  "south dakota",  "virgin islands",
              "west virginia", "new york"]

    after = ["canalzone", "newhampshire", "newjersey", "newmexico",
             "northcarolina",  "northdakota",  "puertorico", "rhodeisland",
             "southcarolina",  "southdakota",  "virginislands", "westvirginia",
             "newyork"]
    for x,y in zip(before, after):
        text = text.replace(x, y)
    return text

def main():
    nlp = spacy.load("en_core_web_lg", exclude=["ner"])
    nlp_no_ner = spacy.load("en_core_web_lg", exclude=["ner"])

    rows = []
    header = []
    with open("../texts.csv", encoding="ISO-8859-1") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)
        for row in csvreader:
            rows.append(row)

    for t in rows:
        print(extractor_wrapper(nlp, nlp_no_ner, preprocess_text(t[0])))
if __name__ == "__main__":
    main()
