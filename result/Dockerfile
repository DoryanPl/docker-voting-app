FROM node:20.8-alpine
ENV NODE_ENV production
WORKDIR /app
COPY package*.json .
RUN npm ci --omit=dev
USER node
COPY --chown=node:node . .
EXPOSE 8081
CMD ["npm", "start"]
