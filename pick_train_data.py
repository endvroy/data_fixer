import random
import argparse


def pick(intent_f, snippets_f, n):
    intents = intent_f.readlines()
    snippets = snippets_f.readlines()
    data = zip(intents, snippets)
    result = random.choices(data, n)
    return result


def main(intent_f_path,
         snippets_f_path,
         n,
         out_intent_path,
         out_snippets_path):
    with open(intent_f_path) as intent_f, open(snippets_f_path) as snippets_f:
        results = pick(intent_f, snippets_f, n)
    with open(out_intent_path, 'w') as out_intent_f, open(out_snippets_path, 'w') as out_snippets_f:
        for result in results:
            out_intent_f.write(result[0])
            out_snippets_f.write(result[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('intent_in')
    parser.add_argument('snippets_in')
    parser.add_argument('n')
    parser.add_argument('intent_out')
    parser.add_argument('snippets_out')
    args = parser.parse_args()
    main(args.intent_in,
         args.snippets_in,
         args.n,
         args.intent_out,
         args.snippets_out)
