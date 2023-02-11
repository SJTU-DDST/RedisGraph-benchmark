import csv
import os
from redis.commands.graph import Graph
from redis.commands.graph.node import Node
from redis.commands.graph.edge import Edge

graph_name = "social_network"


def build_graph(redis_con, redis_graph):
    if redis_con.exists(graph_name):
        return

    # dictionary comment id to its node entity
    # id:ID(Comment)|creationDate:LONG|locationIP:STRING|browserUsed:STRING|content:STRING|length:INT
    comments = {}
    # dictionary forum id to its node entity
    # id:ID(Forum)|title:STRING|creationDate:LONG
    forums = {}

    # dictionary organisation id to its node entity
    # id:ID(Organisation)|:LABEL|name:STRING|url:STRING
    organisations = {}

    # dictionary person id to its node entity
    # id:ID(Person)|firstName:STRING|lastName:STRING|gender:STRING|birthday:LONG|creationDate:LONG|locationIP:STRING|browserUsed:STRING|speaks:STRING[]|email:STRING[]
    persons = {}

    # dictionary place id to its node entity
    # id:ID(Place)|name:STRING|url:STRING|:LABEL
    places = {}

    # dictionary post id to its node entity
    # id:ID(Post)|imageFile:STRING|creationDate:LONG|locationIP:STRING|browserUsed:STRING|language:STRING|content:STRING|length:INT
    posts = {}

    # dictionary tag id to its node entity
    # id:ID(Tag)|name:STRING|url:STRING
    tags = {}

    # dictionary tagclass id to its node entity
    # id:ID(TagClass)|name:STRING|url:STRING
    tagclasses = {}

    # Create comment entities
    # id:ID(Comment)|creationDate:LONG|locationIP:STRING|browserUsed:STRING|content:STRING|length:INT
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/comment_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            id = row[0]
            creationDate = row[1]
            locationIP = row[2]
            browserUsed = row[3]
            content = row[4]
            length = int(row[5])

            node = Node(label="Comment", properties={"id": id,
                                                     "creationDate": creationDate,
                                                     "locationIP": locationIP,
                                                     "browserUsed": browserUsed,
                                                     "content": content,
                                                     "length": length
                                                     })
            comments[id] = node
            redis_graph.add_node(node)
    print("Create comment entities succeed!")
    redis_graph.commit()
    res = redis_graph.query("CREATE INDEX ON :Comment(id)")
    print(res)
    
    # Create forum entities
    # id:ID(Forum)|title:STRING|creationDate:LONG
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/forum_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            id = row[0]
            title = row[1]
            creationDate = row[2]

            node = Node(label="Forum", properties={"id": id,
                                                   "title": title,
                                                   "creationDate": creationDate
                                                   })
            forums[id] = node
            redis_graph.add_node(node)
    print("Create forum entities succeed!")
    redis_graph.commit()
    res = redis_graph.query("CREATE INDEX ON :Forum(id)")
    print(res)

    # Create organisation entities
    # id:ID(Organisation)|:LABEL|name:STRING|url:STRING
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/organisation_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            id = row[0]
            LABEL = row[1]
            name = row[2]
            url = row[3]

            node = Node(label = ["Organisation",LABEL], properties={"id": id,
                                                   "name": name,
                                                   "url": url
                                                   })
            organisations[id] = node
            redis_graph.add_node(node)
    print("Create organisation entities succeed!")
    redis_graph.commit()
    res = redis_graph.query("CREATE INDEX ON :Organisation(id)")
    print(res)

    # Create person entities
    # id:ID(Person)|firstName:STRING|lastName:STRING|gender:STRING|birthday:LONG|creationDate:LONG|locationIP:STRING|browserUsed:STRING
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            id = row[0]
            firstName = row[1]
            lastName = row[2]
            gender = row[3]
            birthday = row[4]
            creationDate = row[5]
            locationIP = row[6]
            browserUsed = row[7]

            node = Node(label = "Person", properties={"id": id,
                                                   "firstName": firstName,
                                                   "lastName": lastName,
                                                   "gender": gender,
                                                   "birthday": birthday,
                                                   "creationDate": creationDate,
                                                   "locationIP": locationIP,
                                                   "browserUsed": browserUsed
                                                   })
            persons[id] = node
            redis_graph.add_node(node)
    print("Create person entities succeed!")
    redis_graph.commit()
    res = redis_graph.query("CREATE INDEX ON :Person(id)")
    print(res)

    # Create Place entities
    # id:ID(Place)|name:STRING|url:STRING|:LABEL
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/place_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            id = row[0]
            name = row[1]
            url = row[2]
            LABEL = row[3]

            node = Node(label = ["Place",LABEL], properties={"id": id,
                                                   "name": name,
                                                   "url": url
                                                   })
            places[id] = node
            redis_graph.add_node(node)
    print("Create Place entities succeed!")
    redis_graph.commit()
    res = redis_graph.query("CREATE INDEX ON :Place(id)")
    print(res)

    # Create post entities
    # id:ID(Post)|imageFile:STRING|creationDate:LONG|locationIP:STRING|browserUsed:STRING|language:STRING|content:STRING|length:INT
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/post_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            id = row[0]
            imageFile = row[1]
            creationDate = row[2]
            locationIP = row[3]
            browserUsed = row[4]
            language = row[5]
            content = row[6]
            length = int(row[7])

            node = Node(label = "Post", properties={"id": id,
                                                   "imageFile": imageFile,
                                                   "creationDate": creationDate,
                                                   "locationIP": locationIP,
                                                   "browserUsed": browserUsed,
                                                   "language": language,
                                                   "content": content,
                                                   "length": length
                                                   })
            posts[id] = node
            redis_graph.add_node(node)
    print("Create post entities succeed!")
    redis_graph.commit()
    res = redis_graph.query("CREATE INDEX ON :Post(id)")
    print(res)

    # Create tag entities
    # id:ID(Tag)|name:STRING|url:STRING
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/tag_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            id = row[0]
            name = row[1]
            url = row[2]

            node = Node(label = ["Tag",LABEL], properties={"id": id,
                                                   "name": name,
                                                   "url": url
                                                   })
            tags[id] = node
            redis_graph.add_node(node)
    print("Create tag entities succeed!")
    redis_graph.commit()
    res = redis_graph.query("CREATE INDEX ON :Tag(id)")
    print(res)
    
    # Create tagclass entities
    # id:ID(TagClass)|name:STRING|url:STRING
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/tagclass_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            id = row[0]
            name = row[1]
            url = row[2]

            node = Node(label = ["TagClass",LABEL], properties={"id": id,
                                                   "name": name,
                                                   "url": url
                                                   })
            tagclasses[id] = node
            redis_graph.add_node(node)
    print("Create tagclass entities succeed!")
    redis_graph.commit()
    res = redis_graph.query("CREATE INDEX ON :TagClass(id)")
    print(res)

    # Connect comment to person they've HAS_CREATOR.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/comment_hasCreator_person_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(Comment)|:END_ID(Person)
        for row in reader:
            comment = row[0]
            person = row[1]
            edge = Edge(comments[comment],
                        "HAS_CREATOR",
                        persons[person])
            redis_graph.add_edge(edge)
    print("Connect comment to person they've HAS_CREATOR succeed!")
    redis_graph.commit()

    # Connect comment to tag they've HAS_TAG.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/comment_hasTag_tag_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(Comment)|:END_ID(tag)
        for row in reader:
            comment = row[0]
            tag = row[1]
            edge = Edge(comments[comment],
                        "HAS_TAG",
                        tags[tag])
            redis_graph.add_edge(edge)
    print("Connect comment to tag they've HAS_TAG succeed!")
    redis_graph.commit()

    # Connect comment to place they've IS_LOCATED_IN.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/comment_isLocatedIn_place_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(Comment)|:END_ID(place)
        for row in reader:
            comment = row[0]
            place = row[1]
            edge = Edge(comments[comment],
                        "IS_LOCATED_IN",
                        places[place])
            redis_graph.add_edge(edge)
    print("Connect comment to place they've IS_LOCATED_IN succeed!")
    redis_graph.commit()

    # Connect comment to commit they've REPLY_OF.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/comment_replyOf_comment_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(Comment)|:END_ID(place)
        for row in reader:
            comment1 = row[0]
            comment2 = row[1]
            edge = Edge(comments[comment1],
                        "REPLY_OF",
                        comments[comment2])
            redis_graph.add_edge(edge)
    print("Connect comment to commit they've REPLY_OF succeed!")
    redis_graph.commit()

    # Connect comment to post they've REPLY_OF.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/comment_replyOf_post_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(Comment)|:END_ID(place)
        for row in reader:
            comment = row[0]
            post = row[1]
            edge = Edge(comments[comment],
                        "REPLY_OF",
                        posts[post])
            redis_graph.add_edge(edge)
    print("Connect comment to post they've REPLY_OF succeed!")
    redis_graph.commit()

    # Connect forum to post they've CONTAINER_OF.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/forum_containerOf_post_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            forum = row[0]
            post = row[1]
            edge = Edge(forums[forum],
                        "CONTAINER_OF",
                        posts[post])
            redis_graph.add_edge(edge)
    print("Connect forum to post they've CONTAINER_OF succeed!")
    redis_graph.commit()

    # Connect forum to person they've HAS_MEMBER.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/forum_hasMember_person_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            forum = row[0]
            person = row[1]
            edge = Edge(forums[forum],
                        "HAS_MEMBER",
                        persons[person])
            redis_graph.add_edge(edge)
    print("Connect forum to person they've HAS_MEMBER succeed!")
    redis_graph.commit()

    # Connect forum to person they've HAS_MODERATOR.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/forum_hasModerator_person_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            forum = row[0]
            person = row[1]
            edge = Edge(forums[forum],
                        "HAS_MODERATOR",
                        persons[person])
            redis_graph.add_edge(edge)
    print("Connect forum to person they've HAS_MODERATOR succeed!")
    redis_graph.commit()

    # Connect forum to tag they've HAS_TAG.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/forum_hasTag_tag_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            forum = row[0]
            tag = row[1]
            edge = Edge(forums[forum],
                        "HAS_TAG",
                        tags[tag])
            redis_graph.add_edge(edge)
    print("Connect forum to tag they've HAS_TAG succeed!")
    redis_graph.commit()

    # Connect organisation to place they've IS_LOCATED_IN.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/organisation_isLocatedIn_place_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            organisation = row[0]
            place = row[1]
            edge = Edge(organisations[organisation],
                        "IS_LOCATED_IN",
                        places[place])
            redis_graph.add_edge(edge)
    print("Connect organisation to place they've IS_LOCATED_IN succeed!")
    redis_graph.commit()

    # Connect person to tag they've HAS_INTEREST.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_hasInterest_tag_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            person = row[0]
            tag = row[1]
            edge = Edge(persons[person],
                        "HAS_INTEREST",
                        tags[tag])
            redis_graph.add_edge(edge)
    print("Connect person to tag they've HAS_INTEREST succeed!")
    redis_graph.commit()

    # Connect person to place they've IS_LOCATED_IN.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_isLocatedIn_place_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            person = row[0]
            place = row[1]
            edge = Edge(persons[person],
                        "IS_LOCATED_IN",
                        places[place])
            redis_graph.add_edge(edge)
    print("Connect person to place they've IS_LOCATED_IN succeed!")
    redis_graph.commit()

    # Connect person to place they've KNOWS.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_knows_person_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            person1 = row[0]
            person2 = row[1]
            creationDate = row[2]
            edge = Edge(persons[person1],
                        "KNOWS",
                        persons[person2],
                        properties={'creationDate': creationDate})
            redis_graph.add_edge(edge)
    print("Connect person to place they've KNOWS succeed!")
    redis_graph.commit()

    # Connect person to comment they've LIKES.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_likes_comment_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            person = row[0]
            comment = row[1]
            creationDate = row[2]
            edge = Edge(persons[person],
                        "LIKES",
                        comments[comment],
                        properties={'creationDate': creationDate})
            redis_graph.add_edge(edge)
    print("Connect person to comment they've LIKES succeed!")
    redis_graph.commit()

    # Connect person to post they've LIKES.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_likes_post_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            person = row[0]
            post = row[1]
            creationDate = row[2]
            edge = Edge(persons[person],
                        "LIKES",
                        posts[post],
                        properties={'creationDate': creationDate})
            redis_graph.add_edge(edge)
    print("Connect person to post they've LIKES succeed!")
    redis_graph.commit()

    # Connect person to organisation they've STUDY_AT.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_studyAt_organisation_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            person = row[0]
            organisation = row[1]
            classYear = int(row[2])
            edge = Edge(persons[person],
                        "STUDY_AT",
                        organisations[organisation],
                        properties={'classYear': classYear})
            redis_graph.add_edge(edge)
    print("Connect person to organisation they've STUDY_AT succeed!")
    redis_graph.commit()

    # Connect person to organisation they've WORK_AT.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_workAt_organisation_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            person = row[0]
            organisation = row[1]
            workFrom = int(row[2])
            edge = Edge(persons[person],
                        "WORK_AT",
                        organisations[organisation],
                        properties={'workFrom': classYear})
            redis_graph.add_edge(edge)
    print("Connect person to organisation they've WORK_AT succeed!")
    redis_graph.commit()

    # Connect place to place they've IS_PART_OF.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/place_isPartOf_place_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            place1 = row[0]
            place2 = row[1]
            edge = Edge(places[place1],
                        "IS_PART_OF",
                        places[place2])
            redis_graph.add_edge(edge)
    print("Connect place to place they've IS_PART_OF succeed!")
    redis_graph.commit()

    # Connect post to person they've HAS_CREATOR.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/post_hasCreator_person_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            post = row[0]
            person = row[1]
            edge = Edge(posts[post],
                        "HAS_CREATOR",
                        persons[person])
            redis_graph.add_edge(edge)
    print("Connect post to person they've HAS_CREATOR succeed!")
    redis_graph.commit()

    # Connect post to tag they've HAS_TAG.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/post_hasTag_tag_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            post = row[0]
            tag = row[1]
            edge = Edge(posts[post],
                        "HAS_TAG",
                        tags[tag])
            redis_graph.add_edge(edge)
    print("Connect post to tag they've HAS_TAG succeed!")
    redis_graph.commit()

    # Connect post to place they've IS_LOCATED_IN.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/post_isLocatedIn_place_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            post = row[0]
            place = row[1]
            edge = Edge(posts[post],
                        "IS_LOCATED_IN",
                        places[place])
            redis_graph.add_edge(edge)
    print("Connect post to place they've IS_LOCATED_IN succeed!")
    redis_graph.commit()

    # Connect tag to tagclass they've HAS_TYPE.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/tag_hasType_tagclass_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            tag = row[0]
            tagclass = row[1]
            edge = Edge(tags[tag],
                        "HAS_TYPE",
                        tagclasses[tagclass])
            redis_graph.add_edge(edge)
    print("Connect tag to tagclass they've HAS_TYPE succeed!")
    redis_graph.commit()

    # Connect tagclass to tagclass they've IS_SUBCLASS_OF.
    with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/tagclass_isSubclassOf_tagclass_0_0.csv', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        # :START_ID(forum)|:END_ID(post)
        for row in reader:
            tagclass1 = row[0]
            tagclass2 = row[1]
            edge = Edge(tagclasses[tagclass1],
                        "IS_SUBCLASS_OF",
                        tagclasses[tagclass2])
            redis_graph.add_edge(edge)
    print("Connect tagclass to tagclass they've IS_SUBCLASS_OF succeed!")
    # # Connect people to places they've IS_LOCATED_IN.
    # with open(os.path.dirname(os.path.abspath(__file__)) + '/social_network_0_1/person_isLocatedIn_place_0_0.csv', 'r') as f:
    #     reader = csv.reader(f, delimiter='|')
    #     next(reader)
    #     for row in reader:
    #         person = row[0]
    #         place = row[1]
    #         edge = Edge(persons[person],
    #                     "IS_LOCATED_IN",
    #                     places[place])
    #         redis_graph.add_edge(edge)

    redis_graph.commit()
