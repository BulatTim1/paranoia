# BUILD
FROM node:lts AS build-stage

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY ./ ./
RUN npm run build

# DEVELOPMENT
# FROM build-stage AS development-stage

# RUN npm install -D vite

# EXPOSE 5173
# VOLUME /app
# ENTRYPOINT [ "npm", "run", "dev", "--", "--host" ]

# DEPLOY
FROM nginx:alpine AS deploy-stage

COPY nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=build-stage /app/dist .

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]