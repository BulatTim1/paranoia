# paranoia
Paranoia game for LetoCTF Hackathon

# services
 - bot - telegram bot for push notifications
 - web - telegram web app for players
 - admin - telegram web app for admins
 - db - postgres

# how to start
1. write `.env` from template
2. `docker compose up -d --build`
3. profit

# detailed services
1. web
   - give tasks from pool to users
   - push notifications to bot for notifications (round start, round stop, GGWP)
   - checkout leaderboard
   - survey in the end of round
2. admin
   - create tasks
   - TBD
3. bot
   - waiting for notifications and push them to specific group (probably)
