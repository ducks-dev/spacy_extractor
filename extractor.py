import spacy
import sys
import csv
import patterns as pat

def pattern_extractor(text_extracted, pattern, nlp = spacy.blank("en"),
                      blacklist = []):
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(pattern)

    text = text_extracted[0]
    found_ents = text_extracted[1]
    doc = nlp(text)

    to_replace_ents = ["PERSON", "ADDRESS", "EMAIL", "PHONE_NUMBER"]

    for ent in doc.ents:
        if (ent.label_ in to_replace_ents and
            ent.text not in to_replace_ents and
            ent.text not in blacklist):
            text = text.replace(ent.text, ent.label_)
            found_ents += [ent.text]

    nlp.remove_pipe("entity_ruler")

    return (text, found_ents)

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
        output = pattern_extractor(output, p, nlp_no_ner)

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

def read_from_csv(infile):
    with open(infile, encoding="ISO-8859-1") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        data = []
        # assuming data starts on the first line
        for row in csvreader:
            data += [row]
    return data

def write_to_csv(outfile, data):
    # writes all redacted lines to named csv with no header
    with open(outfile, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        #csvwriter.writerow(header)
        for row in data:
            csvwriter.writerow(row)

def redact_data(data, nlp, nlp_no_ner):
    data = read_from_csv(sys.argv[1])
    split_data = []
    for line in data:
        text, redacted = extractor_wrapper(nlp, nlp_no_ner,
                                           preprocess_text(line[0]))
        split_data.append([text] + redacted)
    return split_data

def main():
    nlp_no_ner = spacy.load("en_core_web_lg", exclude=["ner"])
    nlp = spacy.load("en_core_web_lg")

    if len(sys.argv) >= 3:
        data = read_from_csv(sys.argv[1])
        redacted = redact_data(data, nlp, nlp_no_ner)
        write_to_csv(sys.argv[2], redacted)

    elif len(sys.argv) >= 2:
        data = read_from_csv(sys.argv[1])
        redacted = redact_data(data, nlp, nlp_no_ner)
        for row in redacted:
            print(row)
    else:
        print("You have entered interactive mode. Type exit to exit.")
        inline = input()
        while(inline != "exit"):
            text, redacted = extractor_wrapper(nlp, nlp_no_ner,
                                               preprocess_text(inline))
            print([text]  + redacted)
            inline = input()
if __name__ == "__main__":
    main()
