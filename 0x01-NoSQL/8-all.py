#!/usr/bin/env python3
"""Operations with Python using pymongo"""


def list_all(mongo_collection):
    """ List all documents in a collection """
    collection_documents = mongo_collection.find()

    if collection_documents.count() == 0:
        return []

    return collection_documents
