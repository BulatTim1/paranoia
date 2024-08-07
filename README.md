# paranoia
Paranoia game for LetoCTF Hackathon

# services
 - bot - telegram bot for push notifications
   - aiogram
 - backend - telegram web app for players and admins
   - fastapi 
 - frontend - telegram web app for players and admins
   - react (так решил вебер)
 - db - postgres
   - sqlalchemy 

# how to start
1. write `.env` from template
2. `docker compose up -d --build`
3. profit

# detailed services
1. web (frontend + backend)
   - give tasks from pool to users
   - push notifications to bot for notifications (round start, round stop, GGWP) (TBD)
   - checkout leaderboard
   - survey in the end of round
   - admin panel (TBD)
     - create tasks (TBD)
     - TBD
2. bot
   - authorize by token
   - waiting for notifications and push them to specific group (probably)
