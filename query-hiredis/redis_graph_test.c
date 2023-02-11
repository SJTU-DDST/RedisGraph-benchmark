#include <assert.h>
#include <errno.h>
#include <hiredis.h>
#include <limits.h>
#include <math.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <pthread.h>

#define REDIS_TEST_OK 0
#define REDIS_TEST_ERR 1

#define QUERY_NUM 6
#define PARAMS_NUM_PER_QUERY 10
#define BATCH_SIZE (QUERY_NUM * PARAMS_NUM_PER_QUERY)
#define BATCH_NUM 64

struct config
{
    struct timeval connect_timeout;

    struct
    {
        const char *host;
        int port;
    } tcp;
};

void *rgt_malloc(size_t size)
{
    void *ptr = malloc(size);
    if (ptr == NULL)
    {
        fprintf(stderr, "Error:  Out of memory\n");
        exit(-1);
    }

    return ptr;
}
long long usec(void)
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (((long long)tv.tv_sec) * 1000000) + tv.tv_usec;
}
/*
#define REDIS_REPLY_STRING 1
#define REDIS_REPLY_ARRAY 2
#define REDIS_REPLY_INTEGER 3
#define REDIS_REPLY_NIL 4
#define REDIS_REPLY_STATUS 5
#define REDIS_REPLY_ERROR 6
#define REDIS_REPLY_DOUBLE 7
#define REDIS_REPLY_BOOL 8
#define REDIS_REPLY_MAP 9
#define REDIS_REPLY_SET 10
#define REDIS_REPLY_ATTR 11
#define REDIS_REPLY_PUSH 12
#define REDIS_REPLY_BIGNUM 13
#define REDIS_REPLY_VERB 14
*/
int graph_build(struct config config)
{
    redisContext *c = redisConnectWithTimeout(config.tcp.host, config.tcp.port,
                                              config.connect_timeout);
    redisReply *reply;
    if (c == NULL || c->err)
    {
        if (c)
        {
            printf("Connection error: %s\n", c->errstr);
            redisFree(c);
        }
        else
        {
            printf("Connection error: can't allocate redis context\n");
        }
        return REDIS_TEST_ERR;
    }
    /* PING server */
    reply = redisCommand(c, "PING");
    printf("PING: %s\n", reply->str);
    freeReplyObject(reply);
    /* build graph */
    // printf("%s\n","GRAPH.QUERY MotoGP \"CREATE (:Rider {name:\'Valentino Rossi\'})-[:rides]->(:Team {name:\'Yamaha\'})\"");
    reply = redisCommand(c, "GRAPH.QUERY %s %s", "MotoGP", "CREATE (:Rider {name:'Valentino Rossi'})-[:rides]->(:Team {name:'Yamaha'}), (:Rider {name:'Dani Pedrosa'})-[:rides]->(:Team {name:'Honda'}), (:Rider {name:'Andrea Dovizioso'})-[:rides]->(:Team {name:'Ducati'})");
    // reply = redisCommand(c, "GRAPH.QUERY MotoGP \"%s\"","CREATE (:Rider {name:\'Valentino Rossi\'})-[:rides]->(:Team {name:\'Yamaha\'})");
    printf("BUILD GRAPH: %d\n", reply->type);
    freeReplyObject(reply);
    redisFree(c);
    return REDIS_TEST_OK;
}

char *query1_params[PARAMS_NUM_PER_QUERY] = {"933", "1129", "2199023256684", "4398046512167", "6597069767117",
                                             "10995116278700", "17592186045684", "21990232556027", "21990232556585", "24189255812290"};
char *query2_params[PARAMS_NUM_PER_QUERY] = {"933", "1129", "2199023256684", "4398046512167", "6597069767117",
                                             "10995116278700", "17592186045684", "21990232556027", "21990232556585", "24189255812290"};
char *query3_params[PARAMS_NUM_PER_QUERY] = {"933", "1129", "2199023256684", "4398046512167", "6597069767117",
                                             "10995116278700", "17592186045684", "21990232556027", "21990232556585", "24189255812290"};
char *query4_params[PARAMS_NUM_PER_QUERY] = {"618475290624", "3", "1030792151044", "412316860440", "481036337184",
                                             "481036337185", "481036337186", "481036337187", "481036337188", "481036337189"};
char *query5_params[PARAMS_NUM_PER_QUERY] = {"618475290625", "618475290626", "1030792151045", "1030792151046", "1030792151047",
                                             "1030792151048", "1030792151049", "1030792151050", "1030792151051", "1030792151052"};
char *query6_params[PARAMS_NUM_PER_QUERY] = {"618475290624", "3", "1030792151044", "412316860440", "481036337184",
                                             "481036337185", "481036337186", "481036337187", "481036337188", "481036337189"};

int graph_query(struct config config)
{
    redisContext *c = redisConnectWithTimeout(config.tcp.host, config.tcp.port,
                                              config.connect_timeout);
    // redisReply **replies;
    int i, j, num;
    long long t1, t2;
    if (c == NULL || c->err)
    {
        if (c)
        {
            printf("Connection error: %s\n", c->errstr);
            redisFree(c);
        }
        else
        {
            printf("Connection error: can't allocate redis context\n");
        }
        return REDIS_TEST_ERR;
    }
    num = BATCH_NUM*BATCH_SIZE;
    // replies = rgt_malloc(sizeof(redisReply*)*num);
    char str[1024];
    // sprintf(str,"MATCH (n:person_0_0 {id:'%s'})-[:person_isLocatedIn_place_0_0]->(p:place_0_0) RETURN p.url","933");
    // redisAppendCommand(c,"GRAPH.QUERY %s %s","social_network_0_1",str);
    // redisAppendCommand(c,"GRAPH.QUERY %s %s","MotoGP","MATCH (r:Rider)-[:rides]->(t:Team) WHERE t.name = 'Yamaha' RETURN r.name, t.name");
    // redisAppendCommand(c,"GRAPH.QUERY %s %s","MotoGP","MATCH (r:Rider)-[:rides]->(t:Team {name:'Ducati'}) RETURN count(r)");
    t1 = usec();
    for (j = 0; j < BATCH_NUM; j++)
    {
        for (i = 0; i < PARAMS_NUM_PER_QUERY; i++)
        {
            sprintf(str, "MATCH (n:person_0_0 {id:'%s'})-[:person_isLocatedIn_place_0_0]->(p:place_0_0) RETURN n.firstName AS firstName,n.lastName AS lastName,n.birthday AS birthday,n.locationIP AS locationIP,n.browserUsed AS browserUsed,p.id AS cityId,n.gender AS gender,n.creationDate AS creationDate",
                    query1_params[i]);
            redisCommand(c, "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (:person_0_0 {id:'%s'})<-[:comment_hasCreator_person_0_0]-(m:comment_0_0)-[:comment_replyOf_post_0_0*0..]->(p:post_0_0) MATCH (p)-[:post_hasCreator_person_0_0]->(c) RETURN m.id as messageId, CASE exists(m.content) WHEN true THEN m.content ELSE m.imageFile END AS messageContent, m.creationDate AS messageCreationDate, p.id AS originalPostId, c.id AS originalPostAuthorId, c.firstName as originalPostAuthorFirstName, c.lastName as originalPostAuthorLastName ORDER BY messageCreationDate DESC LIMIT 10",
                    query2_params[i]);
            redisCommand(c, "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (n:person_0_0 {id:'%s'})-[r:person_knows_person_0_0]-(friend) RETURN friend.id AS personId, friend.firstName AS firstName, friend.lastName AS lastName, r.creationDate AS friendshipCreationDate ORDER BY friendshipCreationDate DESC, toInteger(personId) ASC",
                    query3_params[i]);
            redisCommand(c, "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (m:post_0_0 {id:'%s'})-[:post_hasCreator_person_0_0]->(p:person_0_0) RETURN p.id AS personId, p.firstName AS firstName, p.lastName AS lastName",
                    query4_params[i]);
            redisCommand(c, "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (m:comment_0_0 {id:'%s'})-[:comment_replyOf_post_0_0*0..]->(p:post_0_0)<-[:forum_containerOf_post_0_0]-(f:forum_0_0)-[:forum_hasModerator_person_0_0]->(mod:person_0_0) RETURN f.id AS forumId, f.title AS forumTitle, mod.id AS moderatorId, mod.firstName AS moderatorFirstName,mod.lastName AS moderatorLastName",
                    query5_params[i]);
            redisCommand(c, "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (m:post_0_0 {id:'%s'})<-[:comment_replyOf_post_0_0]-(c:comment_0_0)-[:comment_hasCreator_person_0_0]->(p:person_0_0) OPTIONAL MATCH (m)-[:post_hasCreator_person_0_0]->(a:person_0_0)-[r:person_knows_person_0_0]-(p) RETURN c.id AS commentId, c.content AS commentContent, c.creationDate AS commentCreationDate, p.id AS replyAuthorId, p.firstName AS replyAuthorFirstName, p.lastName AS replyAuthorLastName, CASE r WHEN null THEN false ELSE true END AS replyAuthorKnowsOriginalMessageAuthor ORDER BY commentCreationDate DESC, replyAuthorId",
                    query6_params[i]);
            redisCommand(c, "GRAPH.QUERY %s %s", "social_network_0_1", str);
        }
    }

    t2 = usec();
    // for (i = 0; i < num; i++) freeReplyObject(replies[i]);
    // free(replies);
    printf("\t(%dx GRAPH.QUERY (no pipeline): %.3fs)\n", num, (t2 - t1) / 1000000.0);
    redisFree(c);
    return REDIS_TEST_OK;
}

void graph_query_batch(void* arg){
    redisReply *replies[BATCH_SIZE];
    int i;
    for (i = 0; i < BATCH_SIZE; i++)
    {
        redisGetReply((redisContext *)arg, (void *)&replies[i]);
        // printf("GRAPH.QUERY: %d\n", replies[i]->type);
    }
    // free replies
}

int graph_query_pipeline(struct config config)
{
    redisContext *c[BATCH_NUM];
    // redisReply **replies;
    int i, j, num;
    long long t1, t2;
    pthread_t pid[BATCH_NUM];
    num = BATCH_NUM*BATCH_SIZE;

    for(i=0;i<BATCH_NUM;i++){
        c[i]= redisConnectWithTimeout(config.tcp.host, config.tcp.port,
                                              config.connect_timeout);
        if (c[i] == NULL || c[i]->err)
        {
            if (c[i])
            {
                printf("Connection error: %s\n", c[i]->errstr);
                redisFree(c[i]);
            }
            else
            {
                printf("Connection error: can't allocate redis context\n");
            }
            return REDIS_TEST_ERR;
        }
    }
    // replies = rgt_malloc(sizeof(redisReply *) * num);
    char str[1024];
    for (j = 0; j < BATCH_NUM; j++)
    {
        for (i = 0; i < PARAMS_NUM_PER_QUERY; i++)
        {
            sprintf(str, "MATCH (n:person_0_0 {id:'%s'})-[:person_isLocatedIn_place_0_0]->(p:place_0_0) RETURN n.firstName AS firstName,n.lastName AS lastName,n.birthday AS birthday,n.locationIP AS locationIP,n.browserUsed AS browserUsed,p.id AS cityId,n.gender AS gender,n.creationDate AS creationDate",
                    query1_params[i]);
            redisAppendCommand(c[j], "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (:person_0_0 {id:'%s'})<-[:comment_hasCreator_person_0_0]-(m:comment_0_0)-[:comment_replyOf_post_0_0*0..]->(p:post_0_0) MATCH (p)-[:post_hasCreator_person_0_0]->(c) RETURN m.id as messageId, CASE exists(m.content) WHEN true THEN m.content ELSE m.imageFile END AS messageContent, m.creationDate AS messageCreationDate, p.id AS originalPostId, c.id AS originalPostAuthorId, c.firstName as originalPostAuthorFirstName, c.lastName as originalPostAuthorLastName ORDER BY messageCreationDate DESC LIMIT 10",
                    query2_params[i]);
            redisAppendCommand(c[j], "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (n:person_0_0 {id:'%s'})-[r:person_knows_person_0_0]-(friend) RETURN friend.id AS personId, friend.firstName AS firstName, friend.lastName AS lastName, r.creationDate AS friendshipCreationDate ORDER BY friendshipCreationDate DESC, toInteger(personId) ASC",
                    query3_params[i]);
            redisAppendCommand(c[j], "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (m:post_0_0 {id:'%s'})-[:post_hasCreator_person_0_0]->(p:person_0_0) RETURN p.id AS personId, p.firstName AS firstName, p.lastName AS lastName",
                    query4_params[i]);
            redisAppendCommand(c[j], "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (m:comment_0_0 {id:'%s'})-[:comment_replyOf_post_0_0*0..]->(p:post_0_0)<-[:forum_containerOf_post_0_0]-(f:forum_0_0)-[:forum_hasModerator_person_0_0]->(mod:person_0_0) RETURN f.id AS forumId, f.title AS forumTitle, mod.id AS moderatorId, mod.firstName AS moderatorFirstName,mod.lastName AS moderatorLastName",
                    query5_params[i]);
            redisAppendCommand(c[j], "GRAPH.QUERY %s %s", "social_network_0_1", str);

            sprintf(str, "MATCH (m:post_0_0 {id:'%s'})<-[:comment_replyOf_post_0_0]-(c:comment_0_0)-[:comment_hasCreator_person_0_0]->(p:person_0_0) OPTIONAL MATCH (m)-[:post_hasCreator_person_0_0]->(a:person_0_0)-[r:person_knows_person_0_0]-(p) RETURN c.id AS commentId, c.content AS commentContent, c.creationDate AS commentCreationDate, p.id AS replyAuthorId, p.firstName AS replyAuthorFirstName, p.lastName AS replyAuthorLastName, CASE r WHEN null THEN false ELSE true END AS replyAuthorKnowsOriginalMessageAuthor ORDER BY commentCreationDate DESC, replyAuthorId",
                    query6_params[i]);
            redisAppendCommand(c[j], "GRAPH.QUERY %s %s", "social_network_0_1", str);
        }
    }
    // sprintf(str, "MATCH (n:person_0_0 {id:'%s'})-[:person_isLocatedIn_place_0_0]->(p:place_0_0) RETURN p.url", "933");
    // redisAppendCommand(c, "GRAPH.QUERY %s %s", "social_network_0_1", str);
    // redisAppendCommand(c,"GRAPH.QUERY %s %s","MotoGP","MATCH (r:Rider)-[:rides]->(t:Team) WHERE t.name = 'Yamaha' RETURN r.name, t.name");
    // redisAppendCommand(c,"GRAPH.QUERY %s %s","MotoGP","MATCH (r:Rider)-[:rides]->(t:Team {name:'Ducati'}) RETURN count(r)");
    t1 = usec();
    for (i = 0; i < BATCH_NUM; i++)
    {
        pthread_create(&pid[i], NULL, graph_query_batch, c[i]);
        // redisGetReply(c, (void *)&replies[i]);
        // printf("GRAPH.QUERY: %d\n", replies[i]->type);
    }
    for (i = 0; i < BATCH_NUM; i++)
    {
        pthread_join(pid[i], NULL);
        // redisGetReply(c, (void *)&replies[i]);
        // printf("GRAPH.QUERY: %d\n", replies[i]->type);
    }
    t2 = usec();
    // for (i = 0; i < num; i++)
    //     freeReplyObject(replies[i]);
    // free(replies);
    printf("\t(%dx GRAPH.QUERY (pipelined): %.3fs)\n", num, (t2 - t1) / 1000000.0);
    for (i = 0; i < BATCH_NUM; i++)
    {
        redisFree(c[i]);
    }

    return REDIS_TEST_OK;
}
int main(int argc, char **argv)
{
    struct config cfg = {.connect_timeout = {1, 500000},
                         .tcp = {.host = "127.0.0.1", .port = 6379}};
    /* Parse command line options. */
    argv++;
    argc--;
    while (argc)
    {
        if (argc >= 2 && !strcmp(argv[0], "-h"))
        {
            argv++;
            argc--;
            cfg.tcp.host = argv[0];
        }
        else if (argc >= 2 && !strcmp(argv[0], "-p"))
        {
            argv++;
            argc--;
            cfg.tcp.port = atoi(argv[0]);
        }
        else
        {
            fprintf(stderr, "Invalid argument: %s\n", argv[0]);
            exit(1);
        }
        argv++;
        argc--;
    }
    // graph_build(cfg);
    graph_query(cfg);
    graph_query_pipeline(cfg);
    return 0;
}
