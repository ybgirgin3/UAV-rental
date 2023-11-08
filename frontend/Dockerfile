FROM node:16-alpine

WORKDIR /code/frontend/
COPY package*.json /code/frontend/
RUN npm install

COPY .  /code/frontend/
CMD [ "npm", "start" ]