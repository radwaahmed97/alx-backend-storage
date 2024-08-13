#!/usr/bin/env python3
"""
function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    name_query = {"name": name}
    updated_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, updated_values)
