#!/usr/bin/env python3
"""function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    documents = mongo_collection.find({"topics": topic})
    listed_documents = [d for d in documents]
    return listed_documents
