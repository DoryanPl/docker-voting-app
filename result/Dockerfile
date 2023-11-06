FROM node:20.8-alpine
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY package*.json .
RUN npm install
RUN npm ci --omit=dev
USER node
COPY --chown=node:node . .
EXPOSE 8081
CMD ["npm", "start"]
