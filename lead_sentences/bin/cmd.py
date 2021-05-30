#!/usr/bin/env python
import lead_sentences
import argparse


def main():
    parser = argparse.ArgumentParser("lead_sentences")

    parser.add_argument("path")
    parser.add_argument("-out_path", "-o", required=True)
    parser.add_argument("-n", default=3, type=int,
                        help="Number of sentences to select")
    parser.add_argument("-lead_reference", default=None,
                        help="Use a reference to match the number of "
                             "sentences")

    args = parser.parse_args()
    
    lead_sentences.path_lead_n(
        args.path, args.out_path, args.n, lead_reference_path=args.lead_reference
    )
