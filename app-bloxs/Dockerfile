FROM ubuntu

WORKDIR /usr/src/app


COPY package.json ./

COPY . .

RUN apt update

RUN apt install npm -y

RUN npm install

EXPOSE 3000

CMD [ "npm" , "start" ]