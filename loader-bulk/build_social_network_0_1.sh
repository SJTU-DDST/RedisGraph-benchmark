rg_host=$1
rg_port=$2

redisgraph-bulk-insert social_network_0_1 --host ${rg_host} --port ${rg_port} \
--enforce-schema --skip-invalid-nodes --skip-invalid-edges --separator \| \
--nodes ./social_network_0_1/comment_0_0.csv --nodes ./social_network_0_1/forum_0_0.csv --nodes ./social_network_0_1/organisation_0_0.csv \
--nodes ./social_network_0_1/person_0_0.csv --nodes ./social_network_0_1/place_0_0.csv --nodes ./social_network_0_1/post_0_0.csv \
--nodes ./social_network_0_1/tag_0_0.csv --nodes ./social_network_0_1/tagclass_0_0.csv \
--relations ./social_network_0_1/comment_hasCreator_person_0_0.csv --relations ./social_network_0_1/comment_hasTag_tag_0_0.csv \
--relations ./social_network_0_1/comment_isLocatedIn_place_0_0.csv --relations ./social_network_0_1/comment_replyOf_comment_0_0.csv \
--relations ./social_network_0_1/comment_replyOf_post_0_0.csv --relations ./social_network_0_1/forum_containerOf_post_0_0.csv \
--relations ./social_network_0_1/forum_hasMember_person_0_0.csv --relations ./social_network_0_1/forum_hasModerator_person_0_0.csv \
--relations ./social_network_0_1/forum_hasTag_tag_0_0.csv --relations ./social_network_0_1/organisation_isLocatedIn_place_0_0.csv \
--relations ./social_network_0_1/person_hasInterest_tag_0_0.csv --relations ./social_network_0_1/person_isLocatedIn_place_0_0.csv \
--relations ./social_network_0_1/person_knows_person_0_0.csv --relations ./social_network_0_1/person_likes_comment_0_0.csv \
--relations ./social_network_0_1/person_likes_post_0_0.csv --relations ./social_network_0_1/person_studyAt_organisation_0_0.csv \
--relations ./social_network_0_1/person_workAt_organisation_0_0.csv --relations ./social_network_0_1/place_isPartOf_place_0_0.csv \
--relations ./social_network_0_1/post_hasCreator_person_0_0.csv --relations ./social_network_0_1/post_hasTag_tag_0_0.csv \
--relations ./social_network_0_1/post_isLocatedIn_place_0_0.csv --relations ./social_network_0_1/tagclass_isSubclassOf_tagclass_0_0.csv \
--relations ./social_network_0_1/tag_hasType_tagclass_0_0.csv \
--index comment_0_0:id --index forum_0_0:id --index organisation_0_0:id \
--index person_0_0:id --index place_0_0:id --index post_0_0:id \
--index tag_0_0:id --index tagclass_0_0:id