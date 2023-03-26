# A Dedicated Kik Api For Beginners.

Use this library to develop bots for Kik Messenger that are essentially automated humans.

It basically lets you do the same things as the offical Kik app by pretending to be a real Iphone or Android client, It communicates with Kik's servers over a modified version of the XMPP protocol.

This is the easiest Way to Learn.

# Installation / SetUp / Independencies
I have Provided a BAT / BATCH Script. just run the script to install the Python Packages Needed.

just incase if it fails. i have provided the Package Installations Below.

(python installation)
- pip install beautifulsoup4
- pip3 install ./kik-bot-api-unofficial
- git clone -b new https://github.com/tomer8007/kik-bot-api-unofficial

(javascript installation)
- npm i kik-node-api

This API uses The Tomer API https://github.com/tomer8007/kik-bot-api-unofficial

and https://github.com/YassienW/kik-node-api

# What can i do With This API?
You can do a lot with it. Below is some Examples.

- Log in with kik username and password, retrieve user information (such as email, name, etc).
- Fetch chat partners information
- Log Messages,Groupchat,PMs
- Send text messages to users/groups and listen for incoming messages
- Send and receive 'is-typing' status
- Send and receive read receipts
- Fetch group information (name, participants, etc.)
- Admin groups (add, remove or ban members, etc)
- Fetch past message history
- Search for groups and join them [Experimental]
- Receive media content: camera, gallery, stickers
- Add a kik user as a friend
- Send images (including GIFs, using a tendor.com API key)
- Troll


You can Pretty much Make Anything With This.




# BreakDown / Documentation (Python)
- chat_message 
-a chat_message is just a normal message.

- from_jid
-from_jid is identifying where the message or so on is from (usually used for PM Commands)

-  self.client.send_chat_message
-This just tells the self client (the client) to send a chat message(text message)

-  username
-This is the @ of the bot / account

-  check_captchas
-This is self Explantory. it checks for captchas

-   clear_captchas
-Clears Captchas

# BreakDown / Documentation (JavaScript)

Send Image
- Kik.sendImage(jid, imgPath, allowForwarding, allowSaving)

Add Friend
- Kik.addFriend(jid)

Remove Friend
- Kik.removeFriend(jid)

Search Groups
- Kik.searchGroups(searchQuery, (groups) => {
    
})

Join Group
- Kik.joinGroup(groupJid, groupCode, joinToken)

Leave Group
- Kik.leaveGroup(groupJid)

Kick / Add
- Kik.setGroupMember(groupJid, userJid, bool)

Promote / Demote
- Kik.setAdmin(groupJid, userJid, bool)

Ban/UnBan
- Kik.setBanned(groupJid, userJid, bool)

Change Group Name
- Kik.setGroupName(groupJid, name)

Set Profile Name
- Kik.setProfileName(firstName, lastName)

Set Email
- Kik.setEmail(newEmail, password)

Set Password
- Kik.setPassword(newPassword, oldPassword)

Send Message
- Kik.sendMessage(jid, msg, (delivered, read) => {
    if(delivered){
        console.log("Delivered")
    }else if(read){
        console.log("Read")
    }
})

# Contact For Help

https://t.me/Rediselitev1

https://kik.me/Rediselitev2

# Please Note!

i will not update this Repository that much.

# Useful Links

https://github.com/QLG1/ichi-source
