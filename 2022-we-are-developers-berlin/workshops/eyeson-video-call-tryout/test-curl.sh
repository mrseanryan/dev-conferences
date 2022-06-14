curl -X POST \
-H "Authorization: $API_KEY" \
-d "id=eyeson-sean-test-project-1" \
-d "name=Marketing Team" \
-d "user[name]=Alice" \
"https://api.eyeson.team/rooms" | jq ".links.gui"

# curl -X POST \
# -H "Authorizao=tion: $API_KEY" \
# -d "id=workspace-one" \
# -d "name=Marketing Team" \
# "https://api.eyeson.team/rooms" | jq ".links.gui"
