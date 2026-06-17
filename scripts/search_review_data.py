#!/usr/bin/env python3
"""
Review Experience Miner - Search real submission/peer review experience data.

Provides structured templates and search queries for mining review experience
from LetPub, Xiaomuchong, ResearchGate, and other academic communities.

Usage:
    python search_review_data.py --journal "Remote Sensing of Environment"
    python search_review_data.py --journal "IEEE TGRS" --field "remote sensing"
"""

import argparse
import json
import sys


REVIEW_SOURCES = {
    "letpub": {
        "name": "LetPub (MedSci)",
        "url_base": "https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=",
        "description": "Chinese academic journal review platform with review time stats",
    },
    "xiaomuchong": {
        "name": "Xiaomuchong (Small Woodworm)",
        "url_base": "https://muchong.com/bbs/journal.php?action=search&keyword=",
        "description": "Large Chinese academic forum with real submission experience sharing",
    },
    "researchgate": {
        "name": "ResearchGate",
        "url_base": "https://www.researchgate.net/journal/",
        "description": "Global researcher network with journal ratings and discussions",
    },
    "scirev": {
        "name": "SciRev",
        "url_base": "https://scirev.org/journal/",
        "description": "International review speed and experience platform",
    },
}


JOURNAL_FIELDS = {
    "remote_sensing": {
        "name": "Remote Sensing & GIS",
        "keywords": ["remote sensing", "GIS", "LiDAR", "SAR", "hyperspectral", "land cover"],
        "queries": [
            "Remote Sensing of Environment review time",
            "IEEE TGRS review experience",
            "ISPRS JPRS acceptance rate",
            "MDPI Remote Sensing review speed",
        ],
    },
    "computer_science": {
        "name": "Computer Science & AI",
        "keywords": ["machine learning", "deep learning", "computer vision", "NLP"],
        "queries": [
            "CVPR acceptance rate 2025",
            "NeurIPS review experience",
            "Pattern Recognition journal review time",
        ],
    },
    "ecology": {
        "name": "Ecology & Environmental Science",
        "keywords": ["ecology", "biodiversity", "climate change", "conservation"],
        "queries": [
            "Ecology Letters review time",
            "STOTEN acceptance rate",
            "Ecological Indicators review experience",
        ],
    },
    "medical": {
        "name": "Medical & Biomedical",
        "keywords": ["clinical", "biomedical", "translational", "public health"],
        "queries": [
            "Nature Medicine review process time",
            "PLoS Medicine acceptance rate",
            "BMC Medicine review experience",
        ],
    },
}


def build_search_queries(journal_name, field=None):
    """Build web search queries for mining review experience data."""
    queries = []
    queries.append(f"{journal_name} review time experience 2024 2025")
    queries.append(f"{journal_name} acceptance rate")
    queries.append(f"{journal_name} desk reject rate")
    queries.append(f"{journal_name} submission experience")
    queries.append(f"{journal_name} ???? ??")
    queries.append(f"{journal_name} ???")

    if field and field in JOURNAL_FIELDS:
        for q in JOURNAL_FIELDS[field]["queries"]:
            queries.append(q)

    return queries


def format_review_data_report(journal_name, field=None):
    """Generate a structured report template for review experience data."""
    print("=" * 60)
    print(f"Review Experience Data Collection: {journal_name}")
    print("=" * 60)

    # Search queries
    queries = build_search_queries(journal_name, field)
    print("\nRecommended Search Queries:")
    print("-" * 40)
    for i, q in enumerate(queries, 1):
        print(f"  {i}. {q}")

    # Data collection template
    print("\nData Collection Template:")
    print("-" * 40)
    print("  Average Review Time (first decision): _____ months")
    print("  Average Total Time (submit to accept): _____ months")
    print("  Acceptance Rate: _____ %")
    print("  Desk Reject Rate: _____ %")
    print("  Major Revision Rate: _____ %")
    print("  Sample Size (number of reports): _____")
    print("  Common Reviewer Comments:")
    print("    1. _______________________________")
    print("    2. _______________________________")
    print("  Editor Friendliness: [Poor / Average / Good / Excellent]")
    print("  Overall Rating: [1-5 stars]")

    # Editor profile template
    print("\nEditor Profile Notes:")
    print("-" * 40)
    print("  Editor-in-Chief: _____")
    print("  Editorial Preferences:")
    print("    - Method novelty: [Low / Medium / High] importance")
    print("    - Application impact: [Low / Medium / High] importance")
    print("    - Theoretical contribution: [Low / Medium / High] importance")

    return queries


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mine review experience data")
    parser.add_argument("--journal", "-j", required=True, help="Journal name")
    parser.add_argument("--field", "-f", choices=list(JOURNAL_FIELDS.keys()),
                        help="Research field for tailored queries")
    args = parser.parse_args()
    format_review_data_report(args.journal, args.field)